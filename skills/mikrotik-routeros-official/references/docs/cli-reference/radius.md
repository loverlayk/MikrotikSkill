# radius

> RADIUS servers that the router services use for authentication and accounting. The entries are used in the order of the list. See RADIUS for the full guide.

-----------

## radius 
**Type:** Directory

RADIUS servers that the router services use for authentication and accounting. The entries are used in the order of the list. See [RADIUS](../../authentication-authorization-accounting/radius) for the full guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The entry is disabled and is not used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="service" typ="ubit (ppp, login, hotspot, wireless, dhcp, ipsec, dot1x)">
Router services that use this server. Each service also has its own setting that turns RADIUS on.
- `ppp` - PPP servers.
- `login` - Router users.
- `hotspot` - HotSpot.
- `wireless` - Wireless client authentication.
- `dhcp` - DHCP server. The MAC address of the device is sent as User-Name.
- `ipsec` - IPsec client authentication.
- `dot1x` - Dot1X.
</ArgTableRow>
<ArgTableRow arg="called-id" typ="string">The entry is used only for requests with this Called-Station-Id. For PPPoE it is the service name, for PPTP and L2TP the IP address of the server. An empty value matches every request. Default: empty.</ArgTableRow>
<ArgTableRow arg="domain" typ="string">The entry is used only for users with this domain in the login name (`DOMAIN\name` or `name@domain`). An empty value matches every user. Default: empty.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46v)" mandatory="1">IPv4 or IPv6 address of the RADIUS server. With an IPv6 address the router sends NAS-IPv6-Address in place of NAS-IP-Address. To reach the server in a VRF, add the VRF name: `address@vrf`.</ArgTableRow>
<ArgTableRow arg="secret" typ="string">Shared secret of the router and the server. Not used with `protocol=radsec`. This is a [sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters) parameter.</ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num">UDP port of the server for authentication requests. Not used with `protocol=radsec`. Range: 1..65535. Default: 1812.</ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num">UDP port of the server for accounting requests. Not used with `protocol=radsec`. Range: 1..65535. Default: 1813.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Time to wait for an answer before the request is sent again. Default: 1100ms.</ArgTableRow>
<ArgTableRow arg="radsec-timeout" typ="time">Time to wait for an answer before the request is sent again over RadSec. Default: 3300ms.</ArgTableRow>
<ArgTableRow arg="accounting-backup" typ="bool">
Whether the server gets a copy of the accounting requests.
- `no` (default) - The entry is used for authentication and accounting in the order of the list.
- `yes` - The entry gets a copy of every accounting request of its services, in addition to the entry that answers. It gets no authentication requests.
</ArgTableRow>
<ArgTableRow arg="realm" typ="string">Value of the Mikrotik-Realm attribute in the Access-Requests of the entry. Without it, the attribute has the domain of the user name, and it is not sent when the name has no domain. Default: empty.</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-address: ipAddr
, ipv6-address: ip6Addr
 }">Source IPv4 or IPv6 address of the packets sent to the server. The same address is sent as NAS-IP-Address. Default: not set, the router selects the address.</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)">
Transport of the requests.
- `udp` (default) - RADIUS over UDP, to `authentication-port` and `accounting-port`.
- `radsec` - RADIUS over TLS, to TCP port 2083. Needs `certificate`.
</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">Client certificate, with its private key, for `protocol=radsec`. The certificate authority of the server must be a trusted certificate on the router, and the certificate of the server must contain the value of `address`. Default: none.</ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-for-request-resp)">
Whether an answer to an Access-Request must have the Message-Authenticator attribute. The router adds the attribute to every Access-Request with either value.
- `yes-for-request-resp` (default) - An answer without the attribute is dropped and counted in `bad-replies`.
- `no` - An answer without the attribute is accepted.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Last connection error of the entry, for example `error: Connection refused`. With `protocol=radsec`, the state of the TLS connection: `connecting`, `performing TLS handshake`, `TLS connected`, or an error such as `connect:Connection refused` or `client certificate required`.</ArgTableRow>
</ArgTable>
