# hotspot

> The /ip/hotspot menu lists the HotSpot servers of the router. One server runs on one interface. Use /ip/hotspot/setup to create a server together with the configuration that it needs. See the HotSpot guide.

-----------

## ip/hotspot 
**Type:** Directory

The `/ip/hotspot` menu lists the HotSpot servers of the router. One server runs on one interface. Use [`/ip/hotspot/setup`](./setup) to create a server together with the configuration that it needs. See the [HotSpot](../../../authentication-authorization-accounting/hotspot-captive-portal) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The server is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The server is invalid, for example its interface does not exist.</ArgTableRow>
<ArgTableRow arg="S" typ="HTTPS">The server profile uses the `https` login method.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the HotSpot server.</ArgTableRow>
<ArgTableRow arg="interface" typ="alt { interface: iface_enum
, interface: iface_enum
 }" mandatory="1">Interface on which the server runs. To serve several ports, use a bridge interface, not a bridge port.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:0 }">IP pool for the addresses of the clients. The server uses it to give a valid address to a client whose own address does not fit the network. `none` - the addresses of the clients are not changed.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Server profile from `/ip/hotspot/profile` with the login methods, the HTML directory, and the RADIUS settings.</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">Time without traffic after which a host that is not logged in is removed from `/ip/hotspot/host`. Default: `5m`.</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">Time for which a host that is not logged in can be unreachable before it is removed from `/ip/hotspot/host`. Default: `none`.</ArgTableRow>
<ArgTableRow arg="login-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">Time after which a host that has not logged in is removed from `/ip/hotspot/host`. Default: `none`.</ArgTableRow>
<ArgTableRow arg="addresses-per-mac" typ="enum (unlimited) { unlimited:0 }">Number of IP addresses that one MAC address can use on this server. Default: `2`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="ip-of-dns-name" typ="ipAddr">IP address to which the `dns-name` of the server profile resolves for the clients.</ArgTableRow>
<ArgTableRow arg="proxy-status" typ="string">State of the HotSpot service of this server, for example `running`.</ArgTableRow>
</ArgTable>
