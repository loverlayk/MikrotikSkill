# RADIUS

> RouterOS RADIUS client: add RADIUS servers, authenticate PPP, router login, DHCP and HotSpot users, send accounting, accept Disconnect and CoA requests, use RadSec, and look up the supported RADIUS attributes.

# RADIUS

RADIUS (Remote Authentication Dial-In User Service) keeps user accounts on a central server. The RouterOS RADIUS client asks the server whether a user is allowed to connect, applies the settings that the server returns for the user (an address, a rate limit, a session time), and reports the session to the server for accounting. One server can manage the users of many routers.

The `/radius` menu holds the list of servers. Each entry names the router services that use it: `ppp`, `login` ([router users](user)), `hotspot` ([HotSpot](hotspot-captive-portal/)), `dhcp` ([DHCP server](../network-management/dhcp/server)), `dot1x` ([Dot1X](dot1x)), `ipsec` ([IPsec](../virtual-private-networks/ipsec/)) and `wireless`. The `ppp` service covers all PPP servers: PPPoE, L2TP, SSTP and the others. Each service also has its own setting that turns RADIUS on.

A PPP secret or a router user that exists on the router is checked on the router. The router does not ask the server about that name.

On the server, add the router as a client with the same shared secret, and load the MikroTik attribute dictionary (see RADIUS attributes at the end of this page). [User Manager](user-manager) is a RADIUS server that runs on RouterOS. The server examples on this page use the `users` file format of FreeRADIUS.

## Authenticate PPP users

This example sends the logins of a PPP server, for example a [PPPoE server](../virtual-private-networks/pppoe/), to the RADIUS server at 192.0.2.10. Add the server and turn RADIUS on for PPP:

```ros
/radius/add service=ppp address=192.0.2.10 secret=Example-secret-1
/ppp/aaa/set use-radius=yes
```

On the server, the user gets a fixed address and a rate limit:

```text
alice Cleartext-Password := "Example-pass-1"
	Framed-IP-Address = 10.0.0.10,
	Mikrotik-Rate-Limit = "10M/50M"
```

When the user connects, the session has the `R` flag and the address from the server:

```ros
[admin@MikroTik] > /ppp/active/print
Flags: R - RADIUS
Columns: NAME, SERVICE, CALLER-ID, ADDRESS, UPTIME
#   NAME   SERVICE  CALLER-ID          ADDRESS    UPTIME
0 R alice  pppoe    00:00:5E:00:53:0B  10.0.0.10  9s
```

The rate limit is a dynamic simple queue on the interface of the user. The first value limits the upload of the user and the second the download:

```ros
[admin@MikroTik] > /queue/simple/print where dynamic
Flags: D - DYNAMIC
0 D name="<pppoe-alice>" target=<pppoe-alice> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=10M/50M
    max-limit=10M/50M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

The default configuration has a FastTrack rule, and simple queues do not limit FastTracked connections. See [Simple queue](../firewall-and-quality-of-service/queues/simple-queue) before you rely on these queues.

Framed-IP-Address or Framed-Pool from the server replaces `remote-address` of the PPP profile. Settings that the server does not send come from the default profile of the PPP server (`default-profile` in the settings of the server). `Mikrotik-Group` in the reply selects another PPP profile for the user.

## Log in to the router with RADIUS accounts

This example lets administrators log in to the router with accounts from the same server. Add `login` to the services of the entry and turn RADIUS on for router users:

```ros
/radius/set [find address=192.0.2.10] service=ppp,login
/user/aaa/set use-radius=yes
```

On the server, `Mikrotik-Group` names the [user group](user) of the account:

```text
netadmin Cleartext-Password := "Example-pass-2"
	Mikrotik-Group = "full"
```

Log in with the account and list the sessions that RADIUS authenticated:

```ros
[netadmin@MikroTik] > /user/active/print where radius
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                 NAME      ADDRESS     VIA
0 R 2026-11-20 08:57:50  netadmin  192.0.2.20  ssh
```

`ADDRESS` is the address that the administrator logged in from.

:::warning
Every account that the server accepts for a login request can log in to the router. An account without `Mikrotik-Group`, or with a group that does not exist on the router, gets the group set in `default-group` of `/user/aaa`, which is `read` by default. The `read` group can do more than look: see [User](user) for its policies. When the same server also holds PPP or HotSpot users, configure it to accept requests with Service-Type `Login` only for administrator accounts.
:::

The router does not ask the server about names that exist in `/user`, so keep a local administrator account for the time when the server cannot be reached.

## Authorize DHCP clients

With RADIUS, the [DHCP server](../network-management/dhcp/server) asks the RADIUS server before it gives a lease. The server can set the address, the lease time and a rate limit for each device. The example uses the DHCP server of the default configuration, `defconf`:

```ros
/radius/set [find address=192.0.2.10] service=ppp,login,dhcp
/ip/dhcp-server/set defconf use-radius=yes
```

With the default settings, the router sends the MAC address of the device as the user name, with an empty password. On the server, accept the device by its MAC address:

```text
00:00:5E:00:53:0A Auth-Type := Accept
	Framed-IP-Address = 192.168.88.50,
	Session-Timeout = 3600,
	Mikrotik-Rate-Limit = "5M/20M"
```

`Session-Timeout` is the lease time in seconds. The lease has the `R` flag:

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/print
Flags: R - RADIUS, D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS, HOST-NAME, SERVER, RATE-LIMIT, STATUS,
         LAST-SEEN
#   ADDRESS        MAC-ADDRESS        HOST-NAME  SERVER   RATE-L  STATUS  LAS
0 R 192.168.88.50  00:00:5E:00:53:0A  laptop     defconf  5M/20M  bound   12s
```

A device that the server rejects gets no address. Add all devices of the network to the server before you turn RADIUS on for a DHCP server that is in use.

## Authenticate HotSpot users

Add `hotspot` to the services of the entry and set `use-radius=yes` in the HotSpot server profile. The [HotSpot](hotspot-captive-portal/) page describes the HotSpot server and its profiles.

## Authenticate IPsec users

An IKEv2 server can pass the EAP authentication of its clients to RADIUS. [IPsec](../virtual-private-networks/ipsec/) has the complete server setup; this example shows the RADIUS part. The server certificate is `ike-server`. Add `ipsec` to the services of the entry and set `auth-method=eap-radius` in the identity:

```ros
/radius/set [find address=192.0.2.10] \
    service=ppp,login,dhcp,ipsec
/ip/pool/add name=ike-pool ranges=10.10.10.10-10.10.10.100
/ip/ipsec/mode-config/add name=ike-conf address-pool=ike-pool
/ip/ipsec/peer/add name=ike-clients passive=yes exchange-mode=ike2
/ip/ipsec/identity/add peer=ike-clients auth-method=eap-radius \
    certificate=ike-server generate-policy=port-strict \
    mode-config=ike-conf
```

On the server, Framed-IP-Address gives the client a fixed address in place of one from the pool:

```text
mario Cleartext-Password := "Example-pass-3"
	Framed-IP-Address = 10.10.10.50
```

A client that logs in with EAP-MSCHAPv2 is listed with its user name and the address from the server:

```ros
[admin@MikroTik] > /ip/ipsec/active-peers/print
Flags: R - RESPONDER
Columns: ID, STATE, UPTIME, PH2-TOTAL, REMOTE-ADDRESS, DYNAMIC-ADDRESS
#   ID     STATE        UPTIME  PH2-TOTAL  REMOTE-ADDRESS  DYNAMIC-ADDRESS
0 R mario  established  9s              1  192.0.2.50      10.10.10.50
```

## Authenticate Dot1X clients

The [Dot1X](dot1x) server passes the EAP authentication of the devices on an Ethernet port to RADIUS. Add `dot1x` to the services of the entry and add the port to the Dot1X server:

```ros
/radius/set [find address=192.0.2.10] \
    service=ppp,login,dhcp,ipsec,dot1x
/interface/dot1x/server/add interface=ether2 auth-types=dot1x
```

```text
carol Cleartext-Password := "Example-pass-4"
```

When the device has logged in, the port is authorized:

```ros
[admin@MikroTik] > /interface/dot1x/server/state/print
Columns: INTERFACE, STATUS
#  INTERFACE  STATUS
0  ether2     authorized
```

With `auth-types=mac-auth`, the router sends the MAC address of the device as the user name, by default with an empty password, as the DHCP server does. `mac-auth-mode` and `radius-mac-format` of the [Dot1X](dot1x) server change the password and the format of the address.

## Send accounting

The router reports the start and the end of each session to the server, and the traffic counters in between when an interim interval is set. Accounting is on by default in `/ppp/aaa`, `/user/aaa` and the Dot1X server (`accounting=yes`); `interim-update` in the same menus sets the interval. For DHCP, both settings are in `/ip/dhcp-server/config`. In a HotSpot server profile the settings are `radius-accounting` and `radius-interim-update`. The server can set the interval for one session with Acct-Interim-Interval.

## Add a second server

The router uses the entries in the order of the list. This example adds a second server for the time when the first one does not answer, and a third one that keeps a copy of the accounting records:

```ros
/radius/add service=ppp,login,dhcp address=192.0.2.11 \
    secret=Example-secret-2
/radius/add service=ppp,dhcp address=192.0.2.12 \
    secret=Example-secret-3 accounting-backup=yes
```

```ros
[admin@MikroTik] > /radius/print detail
0  service=ppp,login,dhcp,ipsec,dot1x called-id="" domain="" address=192.0.2.10
   authentication-port=1812 accounting-port=1813 timeout=1s100ms
   radsec-timeout=3s300ms accounting-backup=no realm="" protocol=udp
   certificate=none require-message-auth=yes-for-request-resp status=""

1  service=ppp,login,dhcp called-id="" domain="" address=192.0.2.11
   authentication-port=1812 accounting-port=1813 timeout=1s100ms
   radsec-timeout=3s300ms accounting-backup=no realm="" protocol=udp
   certificate=none require-message-auth=yes-for-request-resp status=""

2  service=ppp,dhcp called-id="" domain="" address=192.0.2.12
   authentication-port=1812 accounting-port=1813 timeout=1s100ms
   radsec-timeout=3s300ms accounting-backup=yes realm="" protocol=udp
   certificate=none require-message-auth=yes-for-request-resp status=""
```

- The router sends a request to the first enabled entry that matches the service. It sends the request three times. When no answer arrives, it sends the request to the next matching entry.
- Each new request starts at the first entry again.
- An entry with `accounting-backup=yes` gets a copy of every accounting request, in addition to the entry that answers. The router does not send authentication requests to it.
- `place-before` in `/radius/add` puts a new entry before an existing one.

## Change or disconnect a session from the server

The server can end a session with a Disconnect-Request and change a running session with a Change of Authorization (CoA) request (RFC 5176, earlier RFC 3576). The router ignores these requests until you allow them:

```ros
/radius/incoming/set accept=yes
```

The router listens on UDP port 3799; `port` changes it, and `vrf` selects the VRF in which the router listens. The router checks a request with the shared secret of the first `/radius` entry whose address is the source address of the request. It does not answer requests from other addresses. A server with an entry can change and disconnect every session of the router, also the sessions of users that another server authenticated.

The default firewall drops these requests when the server is on the WAN side. Accept the port from the address of the server, before the default drop rule:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    dst-port=3799 src-address=192.0.2.10 comment="RADIUS CoA" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

This command, run on the server, changes the rate limit of a connected PPP user. `radclient` is part of FreeRADIUS:

```bash
echo 'User-Name=alice,Mikrotik-Rate-Limit="20M/100M"' | \
    radclient -x 192.0.2.1:3799 coa Example-secret-1
```

```text
Sent CoA-Request Id 179 from 0.0.0.0:52783 to 192.0.2.1:3799 length 43
	User-Name = "alice"
	Mikrotik-Rate-Limit = "20M/100M"
Received CoA-ACK Id 179 from 192.0.2.1:3799 to 192.0.2.10:52783 length 38
	Message-Authenticator = 0x3e08daec066d6cdd8aab7b9d6f3b98c7
```

The queue of the user has the new limit, and the session stays connected:

```ros
[admin@MikroTik] > /queue/simple/print where name~"alice"
Flags: D - DYNAMIC
1 D name="<pppoe-alice>" target=<pppoe-alice> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=20M/100M
    max-limit=20M/100M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

This command disconnects the user:

```bash
echo 'User-Name=alice' | \
    radclient -x 192.0.2.1:3799 disconnect Example-secret-1
```

```text
Sent Disconnect-Request Id 18 from 0.0.0.0:34758 to 192.0.2.1:3799 length 27
	User-Name = "alice"
Received Disconnect-ACK Id 18 from 192.0.2.1:3799 to 192.0.2.10:34758 length 38
	Message-Authenticator = 0x15c3ee3b3b79a6f8b4fd44b83b46bb1a
```

- A PPP session is found by `User-Name` or by `Acct-Session-Id`. When the user has several sessions, a request with only `User-Name` changes or disconnects one of them. Send `Acct-Session-Id` to select the session.
- A HotSpot session is found by `Framed-IP-Address`, the address of the device.
- A DHCP lease is found by `Acct-Session-Id`.
- The router login (`/user/aaa`) does not support these requests. The router answers with CoA-NAK or Disconnect-NAK.
- When no session matches, the router answers with CoA-NAK or Disconnect-NAK.
- The router does not answer a request with a wrong secret. `/radius/incoming/monitor` counts it in `bad-requests`.

Some vendors call the Disconnect-Request a Packet of Disconnect (PoD).

With RadSec, the requests come inside the TLS connection to the server, not to `port` of `/radius/incoming`.

[User Manager](user-manager) sends these requests itself, for example when the plan of a connected user changes.

### Send the requests from FreeRADIUS

FreeRADIUS can send these requests itself when it processes the accounting of the router. This example slows down a PPP user who downloads more than 3 GB in a session, and disconnects the session of a PPP user whose account is blocked. The requests find the session by User-Name and Acct-Session-Id, as PPP sessions are found. The router must send interim updates: the users get `Acct-Interim-Interval` from the server, or set `interim-update` on the router. The router entry uses `protocol=udp`.

The users of the example:

```text
mario Cleartext-Password := "Example-pass-4"
	Mikrotik-Rate-Limit = "10M/20M",
	Acct-Interim-Interval = 60

luigi Auth-Type := Reject
	Reply-Message = "Account blocked"
```

Put these entries at the top of the `users` file (`mods-config/files/authorize`), before the `DEFAULT` entries.

Add the router as a CoA server, for example in the file `sites-enabled/coa-routers`. `ipaddr` is the address of the router that sends the accounting, and FreeRADIUS sends the requests to this server. The secret is the secret of the `/radius` entry on the router:

```text
home_server router1-coa {
	type = coa
	ipaddr = 192.0.2.1
	port = 3799
	secret = Example-secret-1
	coa {
		irt = 2
		mrt = 16
		mrc = 5
		mrd = 30
	}
}
```

The router answers only requests that come from the address of its `/radius` entry. When the server has several addresses, add `src_ipaddr = 192.0.2.10` to the `home_server`.

Add the policies in `policy.d/mikrotik-coa`:

```text
mikrotik_fair_use {
	if (&Acct-Status-Type == Interim-Update && &Acct-Output-Octets > 3000000000) {
		update coa {
			&User-Name := &User-Name
			&Acct-Session-Id := &Acct-Session-Id
			&Mikrotik-Rate-Limit := "1M/2M"
		}
	}
}
mikrotik_blocked {
	if (&Acct-Status-Type == Interim-Update && &User-Name == "luigi") {
		update disconnect {
			&User-Name := &User-Name
			&Acct-Session-Id := &Acct-Session-Id
		}
	}
}
```

Call them at the start of the `accounting` section in `sites-enabled/default`, and restart FreeRADIUS:

```text
accounting {
	mikrotik_fair_use
	mikrotik_blocked
	...
```

At the first interim update over the limit, the router gets the CoA and changes the queue of the user. The user stays connected:

```ros
[admin@MikroTik] > /queue/simple/print where name="<pppoe-mario>"
Flags: D - DYNAMIC
0 D name="<pppoe-mario>" target=<pppoe-mario> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=1M/2M
    max-limit=1M/2M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

The counters of the router, reset with `/radius/incoming/reset-counters` before the test:

```ros
[admin@MikroTik] > /radius/incoming/monitor once
      requests: 1
  bad-requests: 0
          acks: 1
          naks: 0
```

- `freeradius -X` shows each request and the answer of the router, for example `Received CoA-ACK`.
- The fair use policy sends the CoA again at every interim update over the limit, and the router applies the same speed again.
- Acct-Output-Octets restarts after 4 GiB. For higher limits, also check Acct-Output-Gigawords.
- Block an account by adding its `Auth-Type := Reject` entry and its name in `mikrotik_blocked`. A session that is open at that time is disconnected at its next interim update, and the entry refuses the next logins. Without the entry, the client logs in again at once.

## Encrypt the connection with RadSec

RadSec carries RADIUS over TLS on TCP port 2083. Use it when the path between the router and the server is not trusted. The router needs:

- A client certificate with its private key.
- The certificate authority that signed the certificate of the server, as a trusted certificate.
- A server certificate that contains the address set in `address` of the entry.

[Certificates](certificates) explains how to create, sign, export and import certificates. In this example the client certificate is imported with the name `radius-client`. Change the entry to RadSec:

```ros
/radius/set [find address=192.0.2.10] protocol=radsec \
    certificate=radius-client
```

After the first request, `status` shows the state of the TLS connection:

```ros
[admin@MikroTik] > /radius/print detail where address=192.0.2.10
0  service=ppp,login,dhcp,ipsec,dot1x called-id="" domain="" address=192.0.2.10
   authentication-port=1812 accounting-port=1813 timeout=1s100ms
   radsec-timeout=3s300ms accounting-backup=no realm="" protocol=radsec
   certificate=radius-client require-message-auth=yes-for-request-resp
   status="TLS connected"
```

- With RadSec, the router connects to TCP port 2083. `authentication-port` and `accounting-port` are not used.
- `secret` is not used. RFC 6614 sets the shared secret of RadSec to `radsec`: configure this secret on a server that asks for one.

When the server is [User Manager](user-manager) on another router, set the server certificate and mark the router entry as a RadSec client:

```ros
/user-manager/set enabled=yes radsec-certificate=radius-server
/user-manager/router/add name=router1 address=192.0.2.1 \
    protocol=radsec
```

User Manager accepts the connection only when the client certificate of the router has the address of the router entry, for example `subject-alt-name=IP:192.0.2.1`. With another name, the log of User Manager has `ssl: name verification failed`, and the router shows `status="ssl: bad certificate (6)"`.

## Check and troubleshoot

`/radius/monitor` counts the requests and answers of one entry:

```ros
[admin@MikroTik] > /radius/monitor [find address=192.0.2.10] once
               pending: 0
              requests: 3
               accepts: 1
               rejects: 0
            challenges: 0
  accounting-responses: 2
         other-replies: 0
               resends: 0
              timeouts: 0
           bad-replies: 0
      last-request-rtt: 10ms
```

- `accepts` counts the accepted logins, and `accounting-responses` counts the answers to accounting requests.
- `rejects` counts the logins that the server refused.
- `resends` and `timeouts` count requests without an answer.
- `bad-replies` counts answers that failed the check of the shared secret or of the Message-Authenticator.

`/radius/reset-counters` sets the counters of all entries to zero. The read-only `status` of an entry shows the last connection error, or the state of the RadSec connection.

To see each request and answer in the log, add the `radius` topic:

```ros
/system/logging/add topics=radius,debug,!packet
```

Without `!packet`, the log also has every attribute of every packet.

| Symptom | Cause |
| :-- | :-- |
| `timeouts` grows. A PPP login fails with `authentication failed - radius timeout` in the log. | The server is not reachable, the router is not a client on the server, or the shared secret is wrong and the server drops the request. |
| `bad-replies` grows. | The answer is signed with another secret, or it has no Message-Authenticator. |
| `rejects` grows. | The server refused the user: a wrong password or an unknown name. |
| No requests are counted. | RADIUS is not turned on in the service, no entry matches the service, `called-id` or `domain`, or the name exists on the router. |
| `status` is `connect:Connection refused`. | The server does not listen on TCP port 2083. On User Manager, the router entry needs `protocol=radsec`. |
| `status` is `client certificate required`. | The RadSec entry has `certificate=none`. |
| `status` is `ssl: name verification failed`. | The certificate of the server does not contain the value of `address`. |
| `status` is `ssl: no trusted CA certificate found`. | The certificate authority of the server is not a trusted certificate on the router. |

## How the router selects an entry

An entry is used for a request when all of these match:

- `service` contains the service that makes the request.
- `called-id` is empty or equals the Called-Station-Id of the request. For PPPoE, this is the service name of the PPPoE server.
- `domain` is empty or equals the domain of the user name. The domain is the part before `\` or after `@`.

A user who logs in as `EXAMPLE\alice` is sent to the server as `alice`, with `EXAMPLE` in the MS-CHAP-Domain attribute. A user who logs in as `alice@example.org` is sent with the complete name, and `example.org` in MS-CHAP-Domain.

Put the entries with a `domain` before the entries with an empty `domain`. When the server of the first matching entry refuses the user, the router does not ask the next entry. [User Manager](user-manager) has an example that sends the users of a partner realm to the server of the partner.

A HotSpot server profile with `radius-default-domain` sends all logins of the profile to the entry with the same `domain`, also names that have another domain. The name is sent as the user typed it, and the default domain is in MS-CHAP-Domain and Mikrotik-Realm.

`realm` sets the Mikrotik-Realm attribute in the Access-Requests of the entry. Without `realm`, the attribute has the domain of the user name, or the `radius-default-domain` of a HotSpot profile. It is not sent when there is no domain.

`src-address` sets the source address of the packets. The same address is sent as NAS-IP-Address.

`address` can be an IPv6 address; the router then sends NAS-IPv6-Address in place of NAS-IP-Address. To reach a server in a VRF, add the VRF name to the address: `address=192.0.2.10@vrf1`.

## Message-Authenticator

The router adds the Message-Authenticator attribute to every Access-Request. With `require-message-auth=yes-for-request-resp`, the default, the router also drops an answer to an Access-Request that has no Message-Authenticator and counts it in `bad-replies`. Accounting requests and their answers do not have the attribute. Set `require-message-auth=no` only for a server that cannot send the attribute. The router drops an answer with a wrong Message-Authenticator with either value.

## RADIUS attributes

Two dictionary files list the attributes that RouterOS supports:

- [RADIUS reference dictionary](pathname:///assets/319783010_RADIUS_reference_dictionary.txt) is a complete dictionary in the FreeRADIUS format. It can conflict with the default dictionary of your RADIUS server. Correct the configuration of the server, not the dictionary: RouterOS supports no other attributes.
- [MikroTik vendor attributes](pathname:///assets/319783011_MikroTik_Vendor_attributes.txt) has only the MikroTik vendor-specific attributes, to include in an existing dictionary.

On a router with User Manager, `/user-manager/attribute/print` lists the attributes that User Manager can send.

The attributes that the server sends override the settings of the service: the PPP profile, the HotSpot user profile or the DHCP server. A setting that the server does not send comes from the service.

### Access-Request

- **Service-Type** - `Framed` for PPP, DHCP, Dot1X and IPsec; `Login` for router login and HotSpot.
- **Framed-Protocol** - `PPP` (PPP only).
- **NAS-Identifier** - Identity of the router.
- **NAS-IP-Address** - Address of the router: the source address of the request. With an IPv6 server, NAS-IPv6-Address is sent.
- **NAS-Port** - Port number of the session on the router.
- **Acct-Session-Id** - Session ID, eight hexadecimal digits. The first two digits depend on the service. The next digit is incremented on each reboot, and the last digits on each new session, so an ID is not repeated for 1 million connections of one service after a boot. If the server gets a Start message for a new session while it still keeps an older session open, the Stop message of the older session was lost: the server must close the old session and start the new one.
- **NAS-Port-Type** - Async PPP and SSTP - `Async`; PPTP, L2TP and IPsec - `Virtual`; PPPoE, DHCP and Dot1X - `Ethernet`; ISDN - `ISDN Sync`; HotSpot - `Ethernet`, `Cable` or `Wireless-802.11`, as set in `nas-port-type` of the HotSpot server profile.
- **Calling-Station-Id** - PPPoE and HotSpot - MAC address of the client in capital letters; PPTP, L2TP, SSTP and IPsec - public IP address of the client; router login - IP address of the client; DHCP - client ID of the device; Dot1X - MAC address of the device, written with dashes.
- **Called-Station-Id** - PPPoE - service name; PPTP, L2TP, SSTP and IPsec - IP address of the server; HotSpot - name of the HotSpot server; DHCP - name of the DHCP server; Dot1X - MAC address of the port of the router, written with dashes.
- **NAS-Port-Id** - Async PPP - serial port name; PPPoE, DHCP and Dot1X - name of the interface on which the server runs; HotSpot - name of the physical HotSpot interface (if bridged, the bridge port name); not present for ISDN, PPTP, L2TP and SSTP.
- **Framed-IP-Address** - IP address of the HotSpot client after Universal Client translation.
- **Mikrotik-Host-IP** - IP address of the HotSpot client before Universal Client translation (the original IP address of the client).
- **User-Name** - Login name of the client. For DHCP and Dot1X MAC authentication, the MAC address of the device, by default in capital letters.
- **Framed-MTU** - 1400 (Dot1X and IPsec).
- **EAP-Message** - EAP packet of the client (Dot1X and IPsec).
- **MS-CHAP-Domain** - Domain of the user name, if present.
- **Mikrotik-Realm** - Value of `realm` of the entry. Without `realm`, the same value as MS-CHAP-Domain.
- **WISPr-Location-ID** - Value of `radius-location-id` of the HotSpot server profile.
- **WISPr-Location-Name** - Value of `radius-location-name` of the HotSpot server profile.
- **WISPr-Logoff-URL** - Full link to the HotSpot logout page.
- **Message-Authenticator** - Signature of the request.

The password attributes depend on the authentication method. Router login uses MS-CHAPv2. HotSpot uses CHAP by default, PAP if unencrypted passwords are enabled, and cannot use MS-CHAP. DHCP and Dot1X MAC authentication send an empty User-Password by default. Dot1X and IPsec carry the EAP method of the client in EAP-Message.

- **User-Password** - Encrypted password (PAP).
- **CHAP-Password**, **CHAP-Challenge** - Encrypted password and challenge (CHAP).
- **MS-CHAP-Response**, **MS-CHAP-Challenge** - Encrypted password and challenge (MS-CHAPv1).
- **MS-CHAP2-Response**, **MS-CHAP-Challenge** - Encrypted password and challenge (MS-CHAPv2).

### Access-Accept

- **Framed-IP-Address** - IP address of the client. For PPP, if the address belongs to the 127.0.0.0/8 or 224.0.0.0/3 networks, the address comes from the pool of the profile. If Framed-IP-Address is sent, Framed-Pool is ignored. For IPsec, the address given to the client by mode config.
- **Framed-IP-Netmask** - Netmask of the client. PPP - together with Framed-IP-Address, adds a route to the network of the address through the client; HotSpot - ignored.
- **Framed-Pool** - Name of the IP pool on the router that gives the address of the client.
- **Framed-IPv6-Prefix** - IPv6 prefix that the router advertises to the PPP client.
- **Framed-IPv6-Pool** - Name of the IPv6 pool on the router that gives the prefix advertised to the PPP client.
- **Delegated-IPv6-Prefix** - IPv6 prefix that the router delegates to the PPP client with DHCPv6.
- **Mikrotik-Delegated-IPv6-Pool** - Name of the IPv6 pool on the router that gives the delegated prefix.
- **Idle-Timeout** - Overrides `idle-timeout` of the service.
- **Session-Timeout** - Overrides `session-timeout` of the service. For DHCP, the lease time.
- **Port-Limit** - Maximal number of simultaneous connections with the same user name (overrides `shared-users` of the HotSpot user profile).
- **Class** - Cookie. The router includes it unchanged in the accounting requests of the session.
- **Framed-Route** - Route to add on the router. The format is specified in RFC 2865 (chapter 5.22). Can be sent several times.
- **Filter-Id** - Name of a firewall filter chain. For PPP, the router adds dynamic rules to the `ppp` chain that jump to this chain for the packets from and to the client. For HotSpot, the rules are added to the `hotspot` chain. Jump rules from the `forward` chain to the `ppp` or `hotspot` chain must exist. The suffix `.in` or `.out` after the name adds the rule only for incoming or only for outgoing traffic. If Filter-Id is sent several times, only the last ones for incoming and outgoing are used.
- **Mikrotik-Mark-Id** - Packet mark (HotSpot only). The router adds dynamic rules to the `hotspot` chain of the firewall mangle that mark the packets from and to the client. The suffix `.in` or `.out` adds the rule only for incoming or only for outgoing traffic. If the attribute is sent several times, only the last ones for incoming and outgoing are used.
- **Mikrotik-Address-List** - Name of a firewall address list. The router adds the address of the client to the list while the session or the lease is active.
- **Mikrotik-DHCP-Option-Set** - Name of a DHCP option set on the router that is sent to the device (DHCP only).
- **Acct-Interim-Interval** - Interval of the Interim-Update accounting requests in seconds. PPP - if 0, the interval of `/ppp/aaa` is used. HotSpot - only respected if `radius-interim-update=received` in the HotSpot server profile.
- **MS-MPPE-Encryption-Policy** - `require-encryption` property (PPP only).
- **MS-MPPE-Encryption-Types** - `use-encryption` property. A non-zero value means to use encryption (PPP only).
- **Ascend-Data-Rate** - Data rate limit. If the attribute is sent two times, the first limits the transmit rate and the second the receive rate. If it is sent together with Ascend-Xmit-Rate, it sets the receive rate. 0 means unlimited. Ignored if Mikrotik-Rate-Limit is present.
- **Ascend-Xmit-Rate** - Transmit rate limit. 0 means unlimited. Ignored if Mikrotik-Rate-Limit is present.
- **MS-CHAP2-Success** - Authentication response if MS-CHAPv2 was used.
- **MS-MPPE-Send-Key**, **MS-MPPE-Recv-Key** - Encryption keys for encrypted PPP, sent by the server only if MS-CHAPv2 was used (PPP only).
- **Ascend-Client-Gateway** - Client gateway for the DHCP-pool HotSpot login method (HotSpot only).
- **Mikrotik-Recv-Limit** - Total receive limit in bytes for the client.
- **Mikrotik-Recv-Limit-Gigawords** - Upper 32 bits of the receive limit (bits 32..63, when bits 0..31 are sent in Mikrotik-Recv-Limit).
- **Mikrotik-Xmit-Limit** - Total transmit limit in bytes for the client.
- **Mikrotik-Xmit-Limit-Gigawords** - Upper 32 bits of the transmit limit (bits 32..63, when bits 0..31 are sent in Mikrotik-Xmit-Limit).
- **Mikrotik-Total-Limit** - Limit in bytes for the received and transmitted traffic together (HotSpot).
- **Mikrotik-Wireless-Forward** - Does not forward the frames of the client back to the wireless infrastructure if this attribute is set to "0" (wireless only).
- **Mikrotik-Wireless-Skip-Dot1x** - Disables 802.1x authentication for the wireless client if set to a non-zero value (wireless only).
- **Mikrotik-Wireless-Enc-Algo** - WEP encryption algorithm: 0 - no encryption, 1 - 40-bit WEP, 2 - 104-bit WEP (wireless only).
- **Mikrotik-Wireless-Enc-Key** - WEP encryption key for the client (wireless only).
- **Mikrotik-Wireless-VLANID** - VLAN ID for the client (wireless only).
- **Mikrotik-Wireless-VLANIDtype** - VLAN ID type for the client: 0 - 802.1q tag, 1 - 802.1ad tag (wireless only).
- **Mikrotik-Switching-Filter** - Dynamic switch rules for a client that the [Dot1X](dot1x) server authenticates.
- **Tunnel-Type**, **Tunnel-Medium-Type**, **Tunnel-Private-Group-ID** - VLAN of a client that the [Dot1X](dot1x) server authenticates.
- **Mikrotik-Rate-Limit** - Data rate limit for the client. See Rate limit format.
- **Mikrotik-Group** - Router login - name of the user group; HotSpot - name of the HotSpot user profile; PPP - name of the PPP profile.
- **Mikrotik-Advertise-URL** - URL of the page with advertisements that is displayed to HotSpot clients. If this attribute is sent, advertisements are enabled, including the transparent proxy, even if they are disabled in the user profile. The server can send the attribute several times; the URLs are used in turn.
- **Mikrotik-Advertise-Interval** - Time between two advertisements. The server can send the attribute several times. The values are used one by one for each successful advertisement, and the last value is used when the end of the list is reached.
- **WISPr-Redirection-URL** - URL to which HotSpot clients are redirected after a successful login.
- **WISPr-Bandwidth-Min-Up** - Minimal data rate (CIR) for the upload of the HotSpot client.
- **WISPr-Bandwidth-Min-Down** - Minimal data rate (CIR) for the download of the HotSpot client.
- **WISPr-Bandwidth-Max-Up** - Maximal data rate (MIR) for the upload of the HotSpot client.
- **WISPr-Bandwidth-Max-Down** - Maximal data rate (MIR) for the download of the HotSpot client.
- **WISPr-Session-Terminate-Time** - Time when the user is disconnected, in the form "YYYY-MM-DDThh:mm:ssTZD": Y - year; M - month; D - day; T - separator between date and time; h - hour (24-hour format); m - minute; s - second; TZD - time zone as "+hh:mm", "+hhmm", "-hh:mm" or "-hhmm".

Mikrotik-Rate-Limit takes precedence over the other ways to set the data rate. The Ascend attributes come second and the WISPr attributes last.

### Rate limit format

The format of Mikrotik-Rate-Limit is:

```text
rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate]
[rx-burst-threshold[/tx-burst-threshold]
[rx-burst-time[/tx-burst-time] [priority [rx-rate-min[/tx-rate-min]]]]]]
```

The value is one line with spaces between the fields. The rates are from the point of view of the router: `rx` is the upload of the client and `tx` the download. All rates are numbers with an optional `k` (1 000) or `M` (1 000 000).

- If `tx-rate` is not set, it is the same as `rx-rate`. The same applies to the burst rate, the burst threshold and the burst time.
- If the burst thresholds are not set but a burst rate is, `rx-rate` and `tx-rate` are the burst thresholds.
- If the burst times are not set, they are 1 second.
- `priority` is 1 to 8, where 1 is the highest priority.
- If `rx-rate-min` and `tx-rate-min` are not set, they are the same as `rx-rate` and `tx-rate`. They cannot be higher than `rx-rate` and `tx-rate`.

Examples:

- **128k** - rx-rate=128000, tx-rate=128000 (no bursts).
- **64k/128M** - rx-rate=64000, tx-rate=128000000.
- **64k 256k** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=64000, rx/tx-burst-time=1s.
- **64k/64k 256k/256k 128k/128k 10/10** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=128000, rx/tx-burst-time=10s.

### Accounting-Request

An accounting request has the attributes of the Access-Request, without the password attributes and the Message-Authenticator, and these:

- **Acct-Status-Type** - Start, Stop, or Interim-Update.
- **Acct-Authentic** - Whether RADIUS or the router authenticated the session.
- **Class** - Cookie of the server, as received in the Access-Accept.
- **Acct-Delay-Time** - How long the router has tried to send this request.
- **Event-Timestamp** - Time of the event.
- **Framed-IP-Address** - Address of the client.

Stop and Interim-Update requests also have:

- **Acct-Session-Time** - Connection uptime in seconds.
- **Acct-Input-Octets** - Bytes received from the client: the upload of the client.
- **Acct-Input-Gigawords** - Upper 32 bits of the bytes received from the client (bits 32..63, when bits 0..31 are sent in Acct-Input-Octets).
- **Acct-Input-Packets** - Number of packets received from the client.
- **Acct-Output-Octets** - Bytes sent to the client: the download of the client.
- **Acct-Output-Gigawords** - Upper 32 bits of the bytes sent to the client (bits 32..63, when bits 0..31 are sent in Acct-Output-Octets).
- **Acct-Output-Packets** - Number of packets sent to the client.

Stop requests also have:

- **Acct-Terminate-Cause** - Cause of the session end (see RFC 2866, chapter 5.10).

### Change of Authorization

A CoA request can change these attributes of a running session:

- **Mikrotik-Group**
- **Mikrotik-Recv-Limit**
- **Mikrotik-Xmit-Limit**
- **Mikrotik-Rate-Limit**
- **Ascend-Data-Rate** (only if Mikrotik-Rate-Limit is not present)
- **Ascend-Xmit-Rate** (only if Mikrotik-Rate-Limit is not present)
- **Mikrotik-Mark-Id**
- **Filter-Id**
- **Mikrotik-Address-List**
- **Mikrotik-Advertise-URL**
- **Mikrotik-Advertise-Interval**
- **Session-Timeout**
- **Idle-Timeout**
- **Port-Limit**

A CoA request cannot change the IP address, the pool or the routes of a session. Disconnect the user to change them.

### MikroTik attribute numbers

The vendor ID of MikroTik is 14988.

| Name | Vendor ID | Number |
| :-- | --: | --: |
| **Mikrotik-Recv-Limit** | 14988 | 1 |
| **Mikrotik-Xmit-Limit** | 14988 | 2 |
| **Mikrotik-Group** | 14988 | 3 |
| **Mikrotik-Wireless-Forward** | 14988 | 4 |
| **Mikrotik-Wireless-Skip-Dot1x** | 14988 | 5 |
| **Mikrotik-Wireless-Enc-Algo** | 14988 | 6 |
| **Mikrotik-Wireless-Enc-Key** | 14988 | 7 |
| **Mikrotik-Rate-Limit** | 14988 | 8 |
| **Mikrotik-Realm** | 14988 | 9 |
| **Mikrotik-Host-IP** | 14988 | 10 |
| **Mikrotik-Mark-Id** | 14988 | 11 |
| **Mikrotik-Advertise-URL** | 14988 | 12 |
| **Mikrotik-Advertise-Interval** | 14988 | 13 |
| **Mikrotik-Recv-Limit-Gigawords** | 14988 | 14 |
| **Mikrotik-Xmit-Limit-Gigawords** | 14988 | 15 |
| **Mikrotik-Wireless-PSK** | 14988 | 16 |
| **Mikrotik-Total-Limit** | 14988 | 17 |
| **Mikrotik-Total-Limit-Gigawords** | 14988 | 18 |
| **Mikrotik-Address-List** | 14988 | 19 |
| **Mikrotik-Wireless-MPKey** | 14988 | 20 |
| **Mikrotik-Wireless-Comment** | 14988 | 21 |
| **Mikrotik-Delegated-IPv6-Pool** | 14988 | 22 |
| **Mikrotik-DHCP-Option-Set** | 14988 | 23 |
| **Mikrotik-DHCP-Option-Param-STR1** | 14988 | 24 |
| **Mikrotik-DHCP-Option-Param-STR2** | 14988 | 25 |
| **Mikrotik-Wireless-VLANID** | 14988 | 26 |
| **Mikrotik-Wireless-VLANIDtype** | 14988 | 27 |
| **Mikrotik-Wireless-Minsignal** | 14988 | 28 |
| **Mikrotik-Wireless-Maxsignal** | 14988 | 29 |
| **Mikrotik-Switching-Filter** | 14988 | 30 |

### Standard and other vendor attribute numbers

| Name | Vendor ID | Number | Defined in |
| :-- | --: | --: | :-- |
| **Acct-Authentic** |  | 45 | RFC 2866 |
| **Acct-Delay-Time** |  | 41 | RFC 2866 |
| **Acct-Input-Gigawords** |  | 52 | RFC 2869 |
| **Acct-Input-Octets** |  | 42 | RFC 2866 |
| **Acct-Input-Packets** |  | 47 | RFC 2866 |
| **Acct-Interim-Interval** |  | 85 | RFC 2869 |
| **Acct-Output-Gigawords** |  | 53 | RFC 2869 |
| **Acct-Output-Octets** |  | 43 | RFC 2866 |
| **Acct-Output-Packets** |  | 48 | RFC 2866 |
| **Acct-Session-Id** |  | 44 | RFC 2866 |
| **Acct-Session-Time** |  | 46 | RFC 2866 |
| **Acct-Status-Type** |  | 40 | RFC 2866 |
| **Acct-Terminate-Cause** |  | 49 | RFC 2866 |
| **Ascend-Client-Gateway** | 529 | 132 |  |
| **Ascend-Data-Rate** | 529 | 197 |  |
| **Ascend-Xmit-Rate** | 529 | 255 |  |
| **Called-Station-Id** |  | 30 | RFC 2865 |
| **Calling-Station-Id** |  | 31 | RFC 2865 |
| **CHAP-Challenge** |  | 60 | RFC 2865 |
| **CHAP-Password** |  | 3 | RFC 2865 |
| **Class** |  | 25 | RFC 2865 |
| **Delegated-IPv6-Prefix** |  | 123 | RFC 4818 |
| **EAP-Message** |  | 79 | RFC 2869 |
| **Error-Cause** |  | 101 | RFC 5176 |
| **Event-Timestamp** |  | 55 | RFC 2869 |
| **Filter-Id** |  | 11 | RFC 2865 |
| **Framed-Compression** |  | 13 | RFC 2865 |
| **Framed-IP-Address** |  | 8 | RFC 2865 |
| **Framed-IP-Netmask** |  | 9 | RFC 2865 |
| **Framed-IPv6-Pool** |  | 100 | RFC 3162 |
| **Framed-IPv6-Prefix** |  | 97 | RFC 3162 |
| **Framed-Mtu** |  | 12 | RFC 2865 |
| **Framed-Pool** |  | 88 | RFC 2869 |
| **Framed-Protocol** |  | 7 | RFC 2865 |
| **Framed-Route** |  | 22 | RFC 2865 |
| **Framed-Routing** |  | 10 | RFC 2865 |
| **Idle-Timeout** |  | 28 | RFC 2865 |
| **Message-Authenticator** |  | 80 | RFC 2869 |
| **MS-CHAP-Challenge** | 311 | 11 | RFC 2548 |
| **MS-CHAP-Domain** | 311 | 10 | RFC 2548 |
| **MS-CHAP-Response** | 311 | 1 | RFC 2548 |
| **MS-CHAP2-Response** | 311 | 25 | RFC 2548 |
| **MS-CHAP2-Success** | 311 | 26 | RFC 2548 |
| **MS-MPPE-Encryption-Policy** | 311 | 7 | RFC 2548 |
| **MS-MPPE-Encryption-Types** | 311 | 8 | RFC 2548 |
| **MS-MPPE-Recv-Key** | 311 | 17 | RFC 2548 |
| **MS-MPPE-Send-Key** | 311 | 16 | RFC 2548 |
| **NAS-Identifier** |  | 32 | RFC 2865 |
| **NAS-IP-Address** |  | 4 | RFC 2865 |
| **NAS-IPv6-Address** |  | 95 | RFC 3162 |
| **NAS-Port** |  | 5 | RFC 2865 |
| **NAS-Port-Id** |  | 87 | RFC 2869 |
| **NAS-Port-Type** |  | 61 | RFC 2865 |
| **Port-Limit** |  | 62 | RFC 2865 |
| **Redback-Agent-Remote-Id** | 2352 | 96 |  |
| **Redback-Agent-Circuit-Id** | 2352 | 97 |  |
| **Service-Type** |  | 6 | RFC 2865 |
| **Session-Timeout** |  | 27 | RFC 2865 |
| **Tunnel-Medium-Type** |  | 65 | RFC 2868 |
| **Tunnel-Private-Group-ID** |  | 81 | RFC 2868 |
| **Tunnel-Type** |  | 64 | RFC 2868 |
| **User-Name** |  | 1 | RFC 2865 |
| **User-Password** |  | 2 | RFC 2865 |
| **WISPr-Bandwidth-Max-Down** | 14122 | 8 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Max-Up** | 14122 | 7 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Down** | 14122 | 6 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Up** | 14122 | 5 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Id** | 14122 | 1 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Name** | 14122 | 2 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Logoff-URL** | 14122 | 3 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Redirection-URL** | 14122 | 4 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-Time** | 14122 | 9 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-End-Of-Day** | 14122 | 10 | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Billing-Class-Of-Service** | 14122 | 11 | [wi-fi.org](https://www.wi-fi.org/) |

## Read more

- [`/radius`](../cli-reference/radius/), [`/radius/monitor`](../cli-reference/radius/monitor), [`/radius/incoming`](../cli-reference/radius/incoming/), [`/radius/incoming/monitor`](../cli-reference/radius/incoming/monitor)
- [User](user)
- [PPP AAA](ppp-aaa)
- [HotSpot](hotspot-captive-portal/)
- [Dot1X](dot1x)
- [IPsec](../virtual-private-networks/ipsec/)
- [User Manager](user-manager)
- [Certificates](certificates)
