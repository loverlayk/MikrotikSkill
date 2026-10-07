# cloud

> Settings of the MikroTik cloud services: the DDNS name, the time update at startup and Back To Home. The router sends its requests to cloud2.mikrotik.com on UDP port 15252. For an overview and examples, see Cloud and...

-----------

## ip/cloud 
**Type:** Settings Directory

Settings of the MikroTik cloud services: the DDNS name, the time update at startup and Back To Home. The router sends its requests to `cloud2.mikrotik.com` on UDP port 15252. For an overview and examples, see [Cloud](../../../network-management/cloud/) and [Back To Home](../../../network-management/cloud/back-to-home).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ddns-enabled" typ="enum (auto | yes)">
Whether the router registers a DNS name (`dns-name`) with the cloud server and keeps it pointing to the router's public address.
- `auto` (default) - DDNS is on only while Back To Home is enabled (`back-to-home-vpn=enabled`). When DDNS turns off, the router asks the cloud server to delete the name, and the name stops resolving within a few minutes.
- `yes` - DDNS is always on. Behind NAT, the router sends an update every minute.
</ArgTableRow>
<ArgTableRow arg="ddns-update-interval" typ="alt { ddns-update-interval: enum (none) { none:0 }
, ddns-update-interval: time [1m .. ]
 }">Interval at which the router sends DDNS updates to the cloud server, in addition to the updates it decides to send by itself. With `none`, the router only sends its own updates; behind NAT, that is one every minute. Minimum: 1 minute. Default: none.</ArgTableRow>
<ArgTableRow arg="update-time" typ="bool">Whether the router sets its clock from the cloud server when it starts. It does so only while the NTP client (`/system/ntp/client`) is disabled, also with `ddns-enabled=auto`, and logs `cloud change time <old> => <new>`. DDNS updates and `force-update` do not set the clock. The time zone is set separately by `time-zone-autodetect` in `/system/clock`. Default: yes.</ArgTableRow>
<ArgTableRow arg="back-to-home-vpn" typ="enum (revoked-and-disabled | enabled)" syscap="cloud-vpn">
Whether Back To Home runs.
- `revoked-and-disabled` (default) - Back To Home is off. Setting it removes the `back-to-home-vpn` interface with its peers, addresses and dynamic firewall rules, and all users in [`back-to-home-user`](back-to-home-user/), and asks the cloud server to delete `vpn-dns-name`. Enabling Back To Home again creates new keys and a new port, so every client needs a new configuration.
- `enabled` - Create the WireGuard interface `back-to-home-vpn` with the addresses 192.168.216.1/24 and fc00:0:0:216::1/64, add dynamic firewall and NAT rules, register `vpn-dns-name`, and connect to a relay when the router cannot be reached directly. With `ddns-enabled=auto`, DDNS turns on too.
</ArgTableRow>
<ArgTableRow arg="vpn-prefer-relay-code" typ="string" syscap="cloud-vpn">Code of the relay region to use, from `vpn-relay-regions`, for example `EUR1`. When it is empty, the router uses the relay with the lowest round-trip time (`vpn-relay-rtts`). Default: empty.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="public-address" typ="ipAddr">Public IPv4 address of the router as the cloud server sees it, that is, the source address of the router's requests. Behind NAT, this is the address of the NAT device. Shown after the first reply from the cloud server, also when only the time update runs.</ArgTableRow>
<ArgTableRow arg="public-address-ipv6" typ="ip6Addr">Public IPv6 address of the router as the cloud server sees it. Shown when the router reaches the cloud server over IPv6.</ArgTableRow>
<ArgTableRow arg="dns-name" typ="string">DNS name of the router: its serial number in lower case followed by `.sn.mynetname.net`. Shown after the name is registered. It resolves to `public-address`, or to the router's local address with `use-local-address=yes` in [`advanced`](advanced), with a time to live of 60 seconds.</ArgTableRow>
<ArgTableRow arg="status" typ="string">
State of the last request to the cloud server, for example:
- `updating...` - The router sent a request and is waiting for the reply. Without a reply, it keeps retrying with growing intervals.
- `updated` - The cloud server confirmed the last request.
- `failed to connect` - The cloud server did not answer.
</ArgTableRow>
<ArgTableRow arg="vpn-dns-name" typ="string" syscap="cloud-vpn">DNS name of the Back To Home endpoint: the serial number in lower case followed by `.vpn.mynetname.net`. It resolves to the router's public address, or to the relay the router uses when it cannot be reached directly. Client configurations use it as the endpoint.</ArgTableRow>
<ArgTableRow arg="vpn-port" typ="num" syscap="cloud-vpn">UDP port of the `back-to-home-vpn` WireGuard interface. The router picks it when Back To Home is enabled.</ArgTableRow>
<ArgTableRow arg="vpn-status" typ="string" syscap="cloud-vpn">State of Back To Home, for example `running`.</ArgTableRow>
<ArgTableRow arg="vpn-relay-rtts" typ="multi { code: string
 }" syscap="cloud-vpn">Round-trip time to each relay region over IPv4 and IPv6, for example `EUR1(ip4: 0.976ms, ip6: timeout)`.</ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv4-status" typ="string" syscap="cloud-vpn">How clients reach the router over IPv4: `reachable directly (region: EUR1 ip: <relay address> rtt: 0.761ms)` when they can connect to the router's public address, or `reachable via relay (region: EUR1 ...)` when they connect through the relay.</ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv6-status" typ="string" syscap="cloud-vpn">How clients reach the router over IPv6, in the same format as `vpn-relay-ipv4-status`, for example `connecting (...)` while the router has no IPv6 internet access.</ArgTableRow>
<ArgTableRow arg="vpn-relay-regions" typ="multi { code: string
 }" syscap="cloud-vpn">Relay regions the router can use, for example `EUR1` and `USA1`. Use a code from this list in `vpn-prefer-relay-code`.</ArgTableRow>
<ArgTableRow arg="vpn-relay-addresses" typ="multi { address: ipAddr
 }" syscap="cloud-vpn">IPv4 addresses of the relay servers, one per region.</ArgTableRow>
<ArgTableRow arg="vpn-relay-addresses-ipv6" typ="multi { address: ip6Addr
 }" syscap="cloud-vpn">IPv6 addresses of the relay servers, one per region.</ArgTableRow>
<ArgTableRow arg="vpn-private-key" typ="string" syscap="cloud-vpn">Private key of the `back-to-home-vpn` WireGuard interface.</ArgTableRow>
<ArgTableRow arg="vpn-public-key" typ="string" syscap="cloud-vpn">Public key of the `back-to-home-vpn` WireGuard interface. Client configurations use it as the key of the router's peer.</ArgTableRow>
<ArgTableRow arg="vpn-peer-private-key" typ="string" syscap="cloud-vpn">Private key of the built-in client configuration in `vpn-wireguard-client-config`.</ArgTableRow>
<ArgTableRow arg="vpn-peer-public-key" typ="string" syscap="cloud-vpn">Public key of the built-in client configuration. The router has a dynamic peer with this key on `back-to-home-vpn`.</ArgTableRow>
<ArgTableRow arg="vpn-interface" typ="iface_enum" syscap="cloud-vpn">WireGuard interface of Back To Home, `back-to-home-vpn`.</ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config" typ="string" syscap="cloud-vpn">WireGuard configuration of the built-in client, with the addresses 192.168.216.2 and fc00:0:0:216::2 and the DNS server the router uses. Import it in a WireGuard app on one device. For more devices, add users in [`back-to-home-user`](back-to-home-user/).</ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config-qrcode" typ="pic" syscap="cloud-vpn">`vpn-wireguard-client-config` as a QR code, for a WireGuard app on a phone.</ArgTableRow>
<ArgTableRow arg="warning" typ="string">Warning about the router's setup, for example `Router is behind a NAT. Remote connection might not work.` Shown only when there is a warning.</ArgTableRow>
</ArgTable>
