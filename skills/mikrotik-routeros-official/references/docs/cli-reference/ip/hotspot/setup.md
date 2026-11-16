# setup

> The /ip/hotspot/setup command asks the questions below and creates a HotSpot server, its server profile, the first user, and, where they are missing, the IP address, the IP pool, the DHCP server, and the masquerade...

-----------

## ip/hotspot/setup 
**Type:** Command

The `/ip/hotspot/setup` command asks the questions below and creates a HotSpot server, its server profile, the first user, and, where they are missing, the IP address, the IP pool, the DHCP server, and the masquerade rule. See the [HotSpot](../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="alt { interface1: iface_enum
, interface2: iface_enum
 }">Question `hotspot interface`: the interface with the clients.</ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: num
 }">Question `local address of network`: the address of the router on the HotSpot interface, with the mask. The address that the interface already has is offered.</ArgTableRow>
<ArgTableRow arg="masq" typ="bool">Question `masquerade network`: `yes` adds a source NAT rule with `action=masquerade` for the HotSpot network.</ArgTableRow>
<ArgTableRow arg="pool" typ="multi { range: composite { min: ipAddr
, max: ipAddr
 }
 }">Question `address pool of network`: the address range for the clients.</ArgTableRow>
<ArgTableRow arg="ssl-cert" typ="enum (import-other-certificate | none) { import-other-certificate:0, none:0xffffffff }">Question `select certificate`: the certificate for the `https` login method. `none` - HTTPS login is not used.</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">Passphrase of the private key, when a certificate is imported.</ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr">Question `ip address of smtp server`: the server to which the SMTP connections of the clients are redirected. `0.0.0.0` - no redirect.</ArgTableRow>
<ArgTableRow arg="use-dnscache" typ="bool">Whether to use the DNS cache of the router.</ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { address: ipAddr
 }">Question `dns servers`: the DNS servers of the router. The value is written to `/ip/dns`.</ArgTableRow>
<ArgTableRow arg="dns-name" typ="string">Question `dns name`: the DNS name of the login page. Empty - the IP address is used.</ArgTableRow>
<ArgTableRow arg="username" typ="string">Question `name of local hotspot user`: the name of the first user.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Question `password for the user`: the password of the first user.</ArgTableRow>
</ArgTable>
