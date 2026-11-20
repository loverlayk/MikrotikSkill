# aaa

> RADIUS authentication and accounting for PPP users. See PPP AAA and RADIUS for the full guides.

-----------

## ppp/aaa 
**Type:** Settings Directory

RADIUS authentication and accounting for PPP users. See [PPP AAA](../../authentication-authorization-accounting/ppp-aaa) and [RADIUS](../../authentication-authorization-accounting/radius) for the full guides.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="use-radius" typ="bool">Whether the router asks a RADIUS server about users that have no secret on the router. A [`/radius`](../radius/) entry with `service=ppp` must exist. Default: no.</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">Whether the router sends RADIUS accounting requests for PPP sessions. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-circuit-id-in-nas-port-id" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">Interval of the Interim-Update accounting requests. Default: 0s, none are sent unless the server sets an interval for the session.</ArgTableRow>
<ArgTableRow arg="enable-ipv6-accounting" typ="bool">Whether IPv6 traffic is reported separately in the accounting requests. By default the counters have layer 2, IPv4 and IPv6 traffic together. The user needs a prefix from the PPP service and a rate limit, because the counters of the dynamic queue are used. It does not work for prefixes that the dynamic DHCPv6 server delegates (`dhcpv6-pd-pool`), because DHCP assigns them, not PPP. Default: no.</ArgTableRow>
</ArgTable>
