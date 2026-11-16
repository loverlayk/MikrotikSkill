# HotSpot - Captive portal

> Set up a HotSpot (captive portal) in RouterOS: run the setup, add users and user profiles with rate and time limits, select the login methods, let selected traffic through without login, and authenticate against a...

# HotSpot - Captive portal

A HotSpot asks the users of a network to log in before they get network access. A device that connects to the HotSpot network gets an IP address and can resolve DNS names, but every web page that it opens over HTTP is replaced by the login page of the router, and all other traffic is rejected. After the user logs in, the device has network access until the user logs out or a limit is reached.

The HotSpot can:

- authenticate users from a list on the router or on a RADIUS server;
- limit each user by time, by traffic amount, and by data rate;
- log in known devices without a login page, by their MAC address;
- give time-limited trial access without an account;
- let selected sites, services, and devices through without login (walled garden and IP bindings);
- show your own login page, see [HotSpot customisation](./hotspot-customisation).

## Before you start

- HotSpot works with IPv4 only.
- [Device-mode](../../system-information-and-utilities/device-mode) can block HotSpot. Check that `hotspot` is `yes` in `/system/device-mode/print`.
- One HotSpot server runs on one interface. To serve several ports, put them in a bridge and run the HotSpot on the bridge interface, not on a bridge port. Do not put the interface that leads to the Internet into this bridge.
- A user rate limit creates a simple queue. Simple queues do not limit FastTracked connections, see [Simple queue](../../firewall-and-quality-of-service/queues/simple-queue).
- If you set up the HotSpot on the interface through which you manage the router, you lose access until you log in on the login page. Manage the router through another interface, or add an IP binding for your computer first, as described in the IP bindings section of this page.

## Set up a HotSpot

The `/ip/hotspot/setup` command asks a few questions and creates the HotSpot server together with everything that it needs.

| Question | What to answer |
| :-- | :-- |
| `hotspot interface` | The interface with the clients. On a router with the default configuration this is `bridge`. |
| `local address of network` | The address of the router on this interface. The address that the interface already has is offered. |
| `masquerade network` | `yes` adds a source NAT rule for the HotSpot network. |
| `address pool of network` | The addresses for the clients. If the interface has a DHCP server, its pool is offered. |
| `select certificate` | Answer `none`, unless you use the `https` login method. |
| `ip address of smtp server` | Keep `0.0.0.0`. |
| `dns servers` | The DNS servers that the router itself uses. The answer is written to `/ip/dns`, so do not enter the address of the router here. |
| `dns name` | A name for the login page, for example `hotspot.lan`. The router resolves this name to its own address for the clients. Leave it empty to use the IP address. |
| `name of local hotspot user`, `password for the user` | The first user account. These two questions are asked only when the router has no HotSpot user yet. |

On a router with the default configuration, with `bridge` as the HotSpot interface and `hotspot.lan` as the DNS name, the setup creates this configuration:

```ros
/ip/hotspot/profile
add dns-name=hotspot.lan hotspot-address=192.168.88.1 name=hsprof1
/ip/hotspot
add address-pool=default-dhcp disabled=no interface=bridge \
    name=hotspot1 profile=hsprof1
/ip/hotspot/user
add name=user1
/ip/firewall/nat
add action=masquerade chain=srcnat \
    comment="masquerade hotspot network" src-address=192.168.88.0/24
```

If the interface has no DHCP server, the setup also creates an IP pool and a DHCP server for it. The existing firewall rules of the router are not changed; the HotSpot adds its own dynamic rules, which are listed at the end of this page.

Check that the server runs:

```ros
/ip/hotspot/print
```

```ros
Columns: NAME, INTERFACE, ADDRESS-POOL, PROFILE, IDLE-TIMEOUT
# NAME      INTERFACE  ADDRESS-POOL  PROFILE  IDLE-TIMEOUT
0 hotspot1  bridge     default-dhcp  hsprof1  5m
```

Connect a device to the HotSpot network and open an HTTP page, for example `http://example.com`. The login page of the router opens instead. The device is now in the host list:

```ros
/ip/hotspot/host/print
```

```ros
Flags: H - DHCP
Columns: MAC-ADDRESS, ADDRESS, TO-ADDRESS, SERVER, IDLE-TIMEOUT
#   MAC-ADDRESS        ADDRESS         TO-ADDRESS      SERVER    IDLE-TIMEOUT
0 H 52:54:09:80:02:01  192.168.88.254  192.168.88.254  hotspot1  5m
1 H 52:54:09:81:02:01  192.168.88.253  192.168.88.253  hotspot1  5m
```

Log in with the user that you created. The host gets the `A` (authorized) flag, and the session is in the active list:

```ros
/ip/hotspot/active/print
```

```ros
Columns: USER, ADDRESS, UPTIME
# USER   ADDRESS         UPTIME
0 user1  192.168.88.254  2s
```

To log a user out, remove the session from `/ip/hotspot/active`. The user can also open the status page, `http://hotspot.lan/status`, and log out there.

## Add users and limits

Users are in `/ip/hotspot/user`. A user profile in `/ip/hotspot/user/profile` holds the settings that several users share.

Add a user:

```ros
/ip/hotspot/user/add name=anna password=ChangeMe-1
```

### Limit the data rate and the session time

Create a profile for guests and a user with this profile:

```ros
/ip/hotspot/user/profile/add name=guest rate-limit=512k/2M \
    session-timeout=1h shared-users=1 address-list=hotspot-guests
/ip/hotspot/user/add name=guest1 password=ChangeMe-2 profile=guest
```

- `rate-limit` is the upload/download limit of each user of the profile. The first value limits what the user sends, the second what the user receives.
- `session-timeout` logs the user out after this time.
- `shared-users` is the number of devices that can be logged in with the same user name at the same time. A login from one more device fails with the message "no more sessions are allowed for user".
- `address-list` adds the address of each logged-in user to a firewall address list. Use the list in your own firewall, mangle, or queue rules.

While `guest1` is logged in, the router has a dynamic simple queue and an address list entry for the user. Both are removed when the user logs out:

```ros
/queue/simple/print where dynamic
/ip/firewall/address-list/print where list=hotspot-guests
```

```ros
Flags: D - DYNAMIC
0 D name="<hotspot-guest1>" target=192.168.88.253/32 parent=none
    packet-marks="" priority=8/8 queue=default-small/default-small
    limit-at=512k/2M max-limit=512k/2M burst-limit=0/0 burst-threshold=0/0
    burst-time=0s/0s bucket-size=0.1/0.1

Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST            ADDRESS         CREATION-TIME
0 D hotspot-guests  192.168.88.253  2026-11-13 20:45:06
```

### Limit the total time and traffic of a user

`session-timeout` in the profile limits one session, and the user can log in again. The limits of the user itself count over all sessions:

```ros
/ip/hotspot/user/add name=daypass password=ChangeMe-3 limit-uptime=1d \
    limit-bytes-total=2G
```

When a limit is reached, the user is logged out. A new login fails with the message "user daypass has reached uptime limit" or "user daypass has reached traffic limit". The counters of the user are in `/ip/hotspot/user/print detail`. To let the user in again, reset them:

```ros
/ip/hotspot/user/reset-counters daypass
```

### Run a script at login and logout

The `on-login` and `on-logout` scripts of a user profile run for every user of the profile. This example writes a line to the log:

```ros
/ip/hotspot/user/profile/set guest \
    on-login=":log info \"HotSpot login: \$user \$address\"" \
    on-logout=":log info \"HotSpot logout: \$user \$cause\""
```

```ros
/log/print where message~"^HotSpot log"
```

```ros
 2026-11-13 20:45:47 script,info HotSpot login: guest1 192.168.88.253
 2026-11-13 20:45:49 script,info HotSpot logout: guest1 admin reset
 2026-11-13 20:51:40 script,info HotSpot login: guest1 192.168.88.254
 2026-11-13 20:51:45 script,info HotSpot logout: guest1 user request
 2026-11-13 20:51:50 script,info HotSpot login: guest1 192.168.88.254
 2026-11-13 20:51:54 script,info HotSpot logout: guest1 admin reset
```

The scripts can use these variables:

| Variable | Value |
| :-- | :-- |
| `$user`, `$username` | The user name. |
| `$address` | The IP address of the device. |
| `$"mac-address"` | The MAC address of the device. |
| `$interface` | The HotSpot interface. |
| `$cause` | Only in `on-logout`: why the session ended, for example `user request`, `session timeout`, or `traffic limit reached`. |
| `$"uptime-secs"` | Only in `on-logout`: the session time in seconds. |
| `$"bytes-in"`, `$"bytes-out"`, `$"bytes-total"` | Only in `on-logout`: the bytes that the user sent and received. |
| `$"packets-in"`, `$"packets-out"`, `$"packets-total"` | Only in `on-logout`: the packets that the user sent and received. |

## Select the login methods

The `login-by` setting of the server profile in `/ip/hotspot/profile` selects how users can log in. Several methods can be enabled at the same time. The default is `cookie,http-chap`.

| Method | How the user logs in |
| :-- | :-- |
| `http-chap` | With a user name and password on the login page. The page does not send the password itself: JavaScript on the page hashes it together with a challenge from the router. |
| `http-pap` | With a user name and password on the login page. The password is sent as plain text. A login link or an external page that sends the password directly needs this method. |
| `https` | As `http-pap`, but the login page is opened over HTTPS. Set `ssl-certificate` in the server profile. The server then has the `S` flag in `/ip/hotspot/print`. |
| `cookie` | Automatically, with a browser cookie from an earlier login. The cookie is valid for `http-cookie-lifetime`. |
| `mac-cookie` | Automatically, by the MAC address of a device that has logged in before. |
| `mac` | Automatically, when a user with the MAC address of the device as its name exists. |
| `trial` | With a link on the login page, without an account, for a limited time. |

Without `http-pap`, a login that sends the plain password fails with the message "web browser did not send challenge response (try again, enable JavaScript)".

### Remember devices with a MAC cookie

With `mac-cookie`, the user logs in once. After that, the router logs the device in by itself each time it comes back, until the cookie expires. This suits phones, which leave and join the network often.

```ros
/ip/hotspot/profile/set hsprof1 login-by=cookie,http-chap,mac-cookie
```

The user profile must have `add-mac-cookie=yes`, which is the default, and `mac-cookie-timeout` sets how long the cookie is valid. The cookies are in `/ip/hotspot/cookie`; a MAC cookie has the `M` flag:

```ros
/ip/hotspot/cookie/print
```

```ros
Flags: M - MAC-COOKIE
Columns: USER, MAC-ADDRESS, EXPIRES-IN
#   USER  MAC-ADDRESS        EXPIRES-IN
0 M anna  52:54:09:80:02:01  2d23h59m58s
1   anna  52:54:09:80:02:01  2d23h59m58s
```

The cookie is removed when the user logs out on the status page. To make a device log in again, remove its cookie from this list.

### Log in devices by MAC address

With `mac`, a device needs no login page at all. Add a user whose name is the MAC address of the device:

```ros
/ip/hotspot/profile/set hsprof1 login-by=cookie,http-chap,mac
/ip/hotspot/user/add name=00:00:5E:00:53:10 comment="reception TV"
```

A MAC address is easy to copy, so use this method only for devices that cannot show a login page.

### Give trial access

With `trial`, the login page shows a "Free trial available" link. A user who follows it gets access for `trial-uptime-limit` and can use the trial again after `trial-uptime-reset`:

```ros
/ip/hotspot/profile/set hsprof1 login-by=cookie,http-chap,trial \
    trial-uptime-limit=30m trial-uptime-reset=1d
```

The router creates a dynamic user named `T-` and the MAC address of the device for each trial, with the profile set in `trial-user-profile`. When the time is used up, a new trial login fails with the message "has reached uptime limit" until the reset time passes.

## Let traffic through without login

### Sites: walled garden

The walled garden lists the web sites that a device can open before login, for example your own site or a payment page. Rules in `/ip/hotspot/walled-garden` match HTTP and HTTPS requests by the host name of the site:

```ros
/ip/hotspot/walled-garden/add dst-host=example.com
/ip/hotspot/walled-garden/add dst-host=*.example.com
```

`dst-host` and `path` must match the whole value. Use `*` for any number of characters and `?` for one character. A value that starts with `:` is a regular expression.

Rules in `/ip/hotspot/walled-garden/ip` match packets by address, protocol, and port, so they also work for services other than the web:

```ros
/ip/hotspot/walled-garden/ip/add action=accept \
    dst-host=pay.example.com
/ip/hotspot/walled-garden/ip/add action=accept protocol=tcp \
    dst-port=443 dst-address=192.0.2.10
```

With `dst-host`, the router adds a dynamic rule with the address that the name resolves to.

The `hits` counter of a walled garden rule shows that it is used:

```ros
/ip/hotspot/walled-garden/print
```

```ros
Flags: X - DISABLED, D - DYNAMIC
Columns: DST-HOST, DST-PORT, ACTION, HITS
#    DST-HOST       DST-PORT  ACTION  HITS
0 D                      443  allow      0
;;; place hotspot rules here
1 X                           allow      0
2    example.com              allow      2
3    *.example.com            allow      1
```

### Devices: IP bindings

An IP binding in `/ip/hotspot/ip-binding` sets how the HotSpot treats one device, selected by its MAC address or IP address:

```ros
/ip/hotspot/ip-binding/add mac-address=00:00:5E:00:53:20 type=bypassed \
    comment="office printer"
/ip/hotspot/ip-binding/add mac-address=00:00:5E:00:53:21 type=blocked
```

- `bypassed` - the device has network access without login. It is in the host list with the `P` flag and is not in the active list.
- `blocked` - the device has no access at all, also not to the login page.
- `regular` - the device logs in as usual; with `to-address`, the HotSpot translates its address to this address.

To create a binding for a device that is already connected, use `/ip/hotspot/host/make-binding` on its entry in the host list.

## Authenticate users with RADIUS

To keep the users on a RADIUS server, add the server for the `hotspot` service and enable RADIUS in the server profile:

```ros
/radius/add service=hotspot address=192.0.2.5 secret=ChangeMe-4
/ip/hotspot/profile/set hsprof1 use-radius=yes
```

Users that exist in `/ip/hotspot/user` still log in from the local list. A session that RADIUS authenticated has the `R` flag in `/ip/hotspot/active`. The reply of the server can set the limits of the session, for example `Session-Timeout` for the session time and `Mikrotik-Rate-Limit` for the rate limit. With `radius-accounting=yes`, which is the default, the router also sends accounting records for each session.

The attributes are listed on the [RADIUS](../radius) page. [User Manager](../user-manager) is a RADIUS server that runs on RouterOS.

## How HotSpot behaves

### Hosts and sessions

- Every device that sends traffic to the HotSpot interface gets an entry in `/ip/hotspot/host`. `found-by` shows the packet that created the entry.
- A logged-in user has an entry in `/ip/hotspot/active`. The session ends when the user logs out, when a limit or `session-timeout` is reached, when the device does not answer for the `keepalive-timeout` of the user profile, or when you remove the entry.
- `/ip/hotspot/active/login` logs a connected device in from the console, without the login page.

### What a device can do before login

- Its DNS requests are answered by the router.
- HTTP requests to a site in the walled garden pass. All other HTTP requests show the login page.
- Everything else is rejected, including ping to the router: TCP with a reset, other protocols with an ICMP "prohibited" message.

### Routing marks

The login page is served by the router itself. A mangle rule that puts a routing mark on all traffic from the HotSpot network, for example for load balancing between two uplinks, also marks the requests to the login page, and the page no longer opens. Exclude the traffic to the router from such a rule with `dst-address-type=!local`.

### Firewall rules that HotSpot adds

A running HotSpot server adds dynamic rules to the NAT and filter tables. They are placed before your own rules.

In `/ip/firewall/nat`, the `dstnat` chain sends the packets of HotSpot clients to the `hotspot` chain:

```ros
/ip/firewall/nat/print dynamic
```

```ros
Flags: D - DYNAMIC
 0 D chain=dstnat action=jump jump-target=hotspot hotspot=from-client

 1 D chain=hotspot action=jump jump-target=pre-hotspot

 2 D chain=hotspot action=redirect to-ports=64872 protocol=udp dst-port=53

 3 D chain=hotspot action=redirect to-ports=64872 protocol=tcp dst-port=53

 4 D chain=hotspot action=redirect to-ports=64873 protocol=tcp
     hotspot=local-dst dst-port=80

 5 D chain=hotspot action=redirect to-ports=64875 protocol=tcp
     hotspot=local-dst dst-port=443

 6 D chain=hotspot action=jump jump-target=hs-unauth protocol=tcp hotspot=!auth

 7 D chain=hotspot action=jump jump-target=hs-auth protocol=tcp hotspot=auth

 8 D chain=hs-unauth action=redirect to-ports=64874 protocol=tcp dst-port=80

 9 D chain=hs-unauth action=redirect to-ports=64874 protocol=tcp dst-port=3128

10 D chain=hs-unauth action=redirect to-ports=64874 protocol=tcp dst-port=8080

11 D chain=hs-unauth action=redirect to-ports=64875 protocol=tcp dst-port=443

12 D chain=hs-unauth action=jump jump-target=hs-smtp protocol=tcp dst-port=25

13 D chain=hs-auth action=redirect to-ports=64874 protocol=tcp hotspot=http

14 D chain=hs-auth action=jump jump-target=hs-smtp protocol=tcp dst-port=25
```

- `hotspot` redirects DNS requests and the requests to the login page to the HotSpot service, and sends the other TCP packets to `hs-unauth` (not logged in) or `hs-auth` (logged in).
- `hs-unauth` redirects HTTP, the proxy ports 3128 and 8080, and HTTPS to the HotSpot service, which checks the walled garden and shows the login page.
- `pre-hotspot` is for your own rules: add rules to this chain to handle packets of HotSpot clients before the HotSpot rules.

In `/ip/firewall/filter`, the packets of clients that are not logged in go to their own chains:

```ros
/ip/firewall/filter/print dynamic where chain~"hs-" or hotspot
```

```ros
Flags: D - DYNAMIC
 0 D chain=forward action=jump jump-target=hs-unauth hotspot=from-client,!auth

 1 D chain=forward action=jump jump-target=hs-unauth-to hotspot=to-client,!auth

 2 D chain=input action=jump jump-target=hs-input hotspot=from-client

 3 D chain=input action=drop protocol=tcp hotspot=!from-client
     dst-port=64872-64875

 4 D chain=hs-input action=jump jump-target=pre-hs-input

 5 D chain=hs-input action=accept protocol=udp dst-port=64872

 6 D chain=hs-input action=accept protocol=tcp dst-port=64872-64875

 7 D chain=hs-input action=jump jump-target=hs-unauth hotspot=!auth

 8 D chain=hs-unauth action=reject reject-with=tcp-reset protocol=tcp

 9 D chain=hs-unauth action=reject reject-with=icmp-net-prohibited

10 D chain=hs-unauth-to action=reject reject-with=icmp-host-prohibited
```

- `hs-unauth` handles the packets from clients that are not logged in, and `hs-unauth-to` the packets to them. Both reject everything that a walled garden IP rule does not allow.
- `hs-input` accepts the connections of clients to the HotSpot service on the router.
- `pre-hs-input` is for your own rules for packets from HotSpot clients to the router.

Each rule in `/ip/hotspot/walled-garden/ip` appears as dynamic rules in these chains.

## Read more

- [HotSpot customisation](./hotspot-customisation) - your own login page.
- CLI reference: [`/ip/hotspot`](../../cli-reference/ip/hotspot), [`/ip/hotspot/profile`](../../cli-reference/ip/hotspot/profile), [`/ip/hotspot/user`](../../cli-reference/ip/hotspot/user), [`/ip/hotspot/user/profile`](../../cli-reference/ip/hotspot/user/profile), [`/ip/hotspot/active`](../../cli-reference/ip/hotspot/active), [`/ip/hotspot/host`](../../cli-reference/ip/hotspot/host), [`/ip/hotspot/walled-garden`](../../cli-reference/ip/hotspot/walled-garden), [`/ip/hotspot/walled-garden/ip`](../../cli-reference/ip/hotspot/walled-garden/ip), [`/ip/hotspot/ip-binding`](../../cli-reference/ip/hotspot/ip-binding), [`/ip/hotspot/cookie`](../../cli-reference/ip/hotspot/cookie), [`/ip/hotspot/setup`](../../cli-reference/ip/hotspot/setup).
