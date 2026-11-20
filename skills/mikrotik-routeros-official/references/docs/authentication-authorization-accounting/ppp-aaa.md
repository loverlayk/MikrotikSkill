# PPP AAA

> PPP users and profiles in RouterOS: create profiles and secrets for PPPoE, L2TP, SSTP and other PPP servers, assign addresses, routes and IPv6 prefixes, limit speed and traffic, filter user traffic, run scripts on...

# PPP AAA

All PPP servers of RouterOS ([PPPoE](../virtual-private-networks/pppoe/), [L2TP](../virtual-private-networks/l2tp/), [SSTP](../virtual-private-networks/sstp), [OpenVPN](../virtual-private-networks/openvpn), [PPTP](../virtual-private-networks/pptp)) share one user database:

- `/ppp/secret` has the users: a name, a password and the settings of one user.
- `/ppp/profile` has the profiles: settings that many users share, such as the addresses, the DNS server, a rate limit and firewall chains.
- `/ppp/active` lists the users that are connected.
- `/ppp/aaa` hands the authentication over to a [RADIUS](radius) server for users that have no secret on the router.

The examples use an L2TP server. Profiles and secrets are used in the same way with the other PPP servers; the CLI reference names the few settings that do not apply to every server.

## Create a profile and a user

This example gives the router the address 10.0.0.1 inside the tunnels and the users addresses from a pool:

```ros
/ip/pool/add name=vpn-pool ranges=10.0.0.10-10.0.0.100
/ppp/profile/add name=vpn local-address=10.0.0.1 \
    remote-address=vpn-pool
/ppp/secret/add name=alice password=Example-pass-1 profile=vpn \
    service=l2tp
```

`service` limits the user to one kind of PPP server. Without it, the user can log in to any of them.

The users connect to a PPP server, which must be enabled. For L2TP:

```ros
/interface/l2tp-server/server/set enabled=yes default-profile=vpn
```

The default firewall drops connections that come from the internet, so the users cannot connect until the firewall accepts the port of the server. For L2TP without IPsec this is UDP port 1701:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    dst-port=1701 in-interface-list=WAN comment="accept L2TP" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

[L2TP](../virtual-private-networks/l2tp/) describes the server and IPsec for it.

`dns-server` in the profile gives the clients one or two DNS servers when the link comes up (the IPCP DNS options of RFC 1877). A client uses them only if it asks for them: a RouterOS PPP client does with `use-peer-dns=yes`. When the address is the router itself, the router must answer DNS requests (`allow-remote-requests=yes` in `/ip/dns`) and its firewall must accept them from the PPP users.

When the user connects, `/ppp/active` shows the session, the address the user connected from and the address from the pool:

```ros
[admin@MikroTik] > /ppp/active/print
Columns: NAME, SERVICE, CALLER-ID, ADDRESS, UPTIME, ENCODING
# NAME   SERVICE  CALLER-ID      ADDRESS    UPTIME  ENCODING
0 alice  l2tp     172.31.30.195  10.0.0.99  8s      MPPE128 stateless
```

## Give a user a fixed address and a route

A remote office needs the same address every time, and the router needs a route to the network behind it. Set both in the secret:

```ros
/ppp/secret/set alice remote-address=10.0.0.5 \
    routes="192.168.50.0/24 10.0.0.5 1"
```

The format of a route is `dst-address gateway metric`. Several routes are separated with commas. The route exists while the user is connected:

```ros
[admin@MikroTik] > /ip/route/print where dst-address=192.168.50.0/24
Flags: D - DYNAMIC; A - ACTIVE; v - VPN
Columns: DST-ADDRESS, GATEWAY, ROUTING-TABLE, DISTANCE
    DST-ADDRESS      GATEWAY   ROUTING-TABLE  DISTANCE
DAv 192.168.50.0/24  10.0.0.5  main                  1
```

An address in the secret takes precedence over the address or the pool of the profile. `ipv6-routes` does the same for IPv6 networks.

## Limit the speed

`rate-limit` in a profile limits each user of the profile. The first value is the upload of the user and the second the download:

```ros
/ppp/profile/set vpn rate-limit=5M/10M
```

The limit applies when the user connects again. The router then adds a dynamic simple queue for the interface of the user:

```ros
[admin@MikroTik] > /queue/simple/print where dynamic
Flags: D - DYNAMIC
0 D name="<l2tp-alice>" target=<l2tp-alice> parent=none packet-marks=""
    priority=8/8 queue=default-small/default-small limit-at=5M/10M
    max-limit=5M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
    bucket-size=0.1/0.1
```

While the user sends and receives as much as the link allows, `rate` of the queue stays at the limits, and `dropped` counts the packets over the limit:

```ros
[admin@MikroTik] > /queue/simple/print stats where dynamic
Flags: D - DYNAMIC
0 D name="<l2tp-alice>" target=<l2tp-alice> rate=5.0Mbps/9.9Mbps
    total-rate=0bps packet-rate=791/1063 total-packet-rate=0 queued-bytes=0/0
    total-queued-bytes=0 queued-packets=0/0 total-queued-packets=0
    bytes=8368364/56349507 total-bytes=0 packets=17379/42613 total-packets=0
    dropped=3219/2273 total-dropped=0
```

The default configuration has a FastTrack rule, and simple queues do not limit FastTracked connections. See [Simple queue](../firewall-and-quality-of-service/queues/simple-queue) for how to make the queues work with it.

The value can also set bursts, a priority and a guaranteed rate; the [RADIUS](radius) page describes the format. `parent-queue` makes the queues of the users children of an existing simple queue, `queue-type` sets the queue types for upload and download, and `insert-queue-before` sets the place of the queue in the list.

## Allow one session for each user

By default, a user can connect several times with the same name. To refuse a second connection while the first one is active:

```ros
/ppp/profile/set vpn only-one=yes
```

The second connection fails, and the log of the router has the message `user alice is already active`.

The setting counts all PPP servers together: a user who is connected to the L2TP server cannot log in to the SSTP server at the same time. It also applies to users that a RADIUS server authenticates.

## Limit the traffic of a session

`limit-bytes-in` is the number of bytes the user can upload in one session, and `limit-bytes-out` the number the user can download:

```ros
/ppp/secret/set alice limit-bytes-in=1000000000 \
    limit-bytes-out=10000000000
```

```ros
[admin@MikroTik] > /ppp/active/print detail
0  name="alice" service=l2tp caller-id="172.31.30.195" address=10.0.0.5
   uptime=9s encoding="MPPE128 stateless" session-id=0x81100056
   limit-bytes-in=1000000000 limit-bytes-out=10000000000
```

When a limit is reached, the router disconnects the user. The limits count each session separately: a user who connects again gets the full amount again.

## Put the addresses of users in an address list

With `address-list`, the router adds the address of each connected user of the profile to a firewall [address list](../firewall-and-quality-of-service/firewall/address-lists). Firewall rules can then match all users of the profile:

```ros
/ppp/profile/set vpn address-list=vpn-users
```

```ros
[admin@MikroTik] > /ip/firewall/address-list/print where list=vpn-users
Flags: D - DYNAMIC
Columns: LIST, ADDRESS, CREATION-TIME
#   LIST       ADDRESS   CREATION-TIME
0 D vpn-users  10.0.0.5  2026-11-19 10:13:38
```

`interface-list` does the same with the interfaces of the users and an interface list.

## Filter the traffic of users

`incoming-filter` and `outgoing-filter` name firewall filter chains for the packets from and to the users of a profile. The router adds a dynamic jump rule to the chain `ppp` for each connected user. The firewall reaches the chain `ppp` only when a rule jumps to it: add a jump rule to each chain that applies the user rules, `forward` for the traffic through the router and `input` for the traffic to the router itself. This example stops the users from sending mail directly:

```ros
/ip/firewall/filter/add chain=forward action=jump jump-target=ppp \
    comment="PPP user rules"
/ip/firewall/filter/add chain=vpn-in action=drop protocol=tcp \
    dst-port=25 comment="VPN users: no direct SMTP"
/ppp/profile/set vpn incoming-filter=vpn-in
```

The example adds the jump rule at the end of the `forward` chain. With the default firewall this place works: the rules before it accept the packets of established connections, and the chain `ppp` gets the first packet of each new connection of a user. In a firewall with more rules, put the jump rule before any rule that accepts or drops the new connections of the users.

With the default firewall, a connected user can reach all devices of the LAN. Of the router itself, the user can only ping the address. To let the users reach one device only, here the file server 192.168.88.10, accept this address and drop the rest:

```ros
/ip/firewall/filter/add chain=vpn-in action=accept \
    dst-address=192.168.88.10
/ip/firewall/filter/add chain=vpn-in action=drop
```

A change of `incoming-filter` in the profile applies when the user connects again.

After the user connects again, the chain `ppp` has the rule for the interface of the user:

```ros
[admin@MikroTik] > /ip/firewall/filter/print where chain=ppp
Flags: D - DYNAMIC
0 D chain=ppp action=jump jump-target=vpn-in in-interface=<l2tp-alice>
```

The counters of the drop rule show the blocked packets:

```ros
[admin@MikroTik] > /ip/firewall/filter/print stats where chain=vpn-in
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN   ACTION  BYTES  PACKETS
;;; VPN users: no direct SMTP
1 vpn-in  drop      240        4
```

## Run a script when a user connects

`on-up` and `on-down` run a script when a user of the profile connects and disconnects. The script can read the variables `user`, `local-address`, `remote-address`, `caller-id`, `called-id` and `interface`:

```ros
/ppp/profile/set vpn \
    on-up=":log info \"PPP user \$user is up\"" \
    on-down=":log info \"PPP user \$user is down\""
```

The log then has the lines `PPP user alice is up` and `PPP user alice is down` under the topic `script`.

## Give users IPv6 prefixes

`remote-ipv6-prefix-pool` gives each user a prefix that the router advertises on the interface of the user. `dhcpv6-pd-pool` adds a DHCPv6 server on the interface that delegates a prefix to the router of the user:

```ros
/ipv6/pool/add name=vpn-v6 prefix=2001:db8:10::/48 prefix-length=64
/ipv6/pool/add name=vpn-pd prefix=2001:db8:20::/48 prefix-length=56
/ppp/profile/set vpn remote-ipv6-prefix-pool=vpn-v6 \
    dhcpv6-pd-pool=vpn-pd
```

```ros
[admin@MikroTik] > /ipv6/nd/prefix/print where dynamic
Flags: D - DYNAMIC
0 D prefix=2001:db8:10::/64 6to4-interface=none interface=<l2tp-alice>
    on-link=yes autonomous=yes dhcp6-pd-preferred=no valid-lifetime=4w2d
    preferred-lifetime=1w
```

A user router that runs a DHCPv6 client on the PPP interface gets the delegated prefix:

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: D - DYNAMIC
Columns: ADDRESS, DUID, SERVER, STATUS
#   ADDRESS           DUID                    SERVER        STATUS
0 D 2001:db8:20::/56  0x0003000102ffe1f54851  <l2tp-alice>  bound
```

`remote-ipv6-prefix` in a secret gives one user a fixed prefix. [IPv6 PD over PPP](../virtual-private-networks/pppoe/ipv6-pd-over-ppp) has a complete example.

## Restrict where a user connects from

`caller-id` in a secret accepts the user only from one address: an IP address for L2TP and PPTP, a MAC address in capital letters for PPPoE. A login from another address is refused, and the log has `user alice called from ..., but was expected from ...`.

## See and disconnect users

`/ppp/active/print` lists the connected users. The `R` flag marks a user that RADIUS authenticated. To disconnect a user:

```ros
/ppp/active/remove [find name=alice]
```

The client can connect again immediately. The secret keeps the time, the address and the reason of the last disconnect:

```ros
[admin@MikroTik] > /ppp/secret/print detail
0  name="alice" service=l2tp caller-id="" profile=vpn remote-address=10.0.0.5
   routes="192.168.50.0/24 10.0.0.5 1" ipv6-routes="" limit-bytes-in=1000000000
   limit-bytes-out=10000000000 last-logged-out=2026-11-19 10:15:03
   last-caller-id="172.31.30.195" last-disconnect-reason=nas-request
```

## Authenticate users with RADIUS

With `use-radius=yes` in `/ppp/aaa`, the router asks a RADIUS server about each user that has no secret on the router. The server can send the address, the rate limit and most other settings of the profile for each user, and the router reports the sessions to it (`accounting` and `interim-update` in `/ppp/aaa`). A RADIUS user gets the settings that the server does not send from the default profile of the PPP server (`default-profile` in the settings of the server), or from the profile that the server names in the Mikrotik-Group attribute. See [RADIUS](radius) for the setup and the attributes.

The Framed-MTU attribute of a RADIUS server is not applied: PPP negotiates the MTU with LCP before the authentication.

## How the settings are combined

- The settings of a user come from three places. The secret has the highest priority, then the profile of the secret, then the default profile of the PPP server that the user connects to.
- A profile setting with the value `default` takes the value from the default profile of the PPP server.
- A user without `profile` uses the profile `default`.
- In a profile, `local-address` and `remote-address` accept an address or the name of an IP pool. A secret takes an address only, and that address takes precedence over a pool.
- The two built-in profiles, `default` and `default-encryption`, cannot be removed. Both have `change-tcp-mss=yes`, and `default-encryption` has `use-encryption=yes`.

## L2TP tunnel secrets

`/ppp/l2tp-secret` sets a secret for the L2TP tunnel itself, for clients that connect from the given address or network. A client that does not use this secret cannot connect.

## Read more

- [`/ppp/profile`](../cli-reference/ppp/profile), [`/ppp/secret`](../cli-reference/ppp/secret), [`/ppp/active`](../cli-reference/ppp/active), [`/ppp/aaa`](../cli-reference/ppp/aaa), [`/ppp/l2tp-secret`](../cli-reference/ppp/l2tp-secret)
- [RADIUS](radius)
- [Simple queue](../firewall-and-quality-of-service/queues/simple-queue)
- [PPPoE](../virtual-private-networks/pppoe/)
- [L2TP](../virtual-private-networks/l2tp/)
