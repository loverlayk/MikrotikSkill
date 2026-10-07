# alert

> Detects unknown (rogue) DHCP servers on an interface. The alert sends its own DHCPDISCOVER about once a minute, and checks the source of every DHCP reply it sees against valid-server. An unknown server is logged with...

-----------

## ip/dhcp-server/alert 
**Type:** Directory

Detects unknown (rogue) DHCP servers on an interface. The alert sends its own DHCPDISCOVER about once a minute, and checks the source of every DHCP reply it sees against `valid-server`. An unknown server is logged with the `dhcp,critical` topics, listed in `unknown-server`, and triggers `on-alert`. Because the alert sends DHCP requests itself, do not use it on an interface where the router runs a DHCP client. For details, see [DHCP Server](../../../../network-management/dhcp/server).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The alert is disabled. New alerts are created disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The alert configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface to watch for DHCP servers.</ArgTableRow>
<ArgTableRow arg="valid-server" typ="multi { mac-address: macAddr
 }">MAC addresses of the DHCP servers that are allowed on the interface. Replies from other servers raise an alert.</ArgTableRow>
<ArgTableRow arg="on-alert" typ="alt { script: string
 }">Script to run when an unknown DHCP server is detected.</ArgTableRow>
<ArgTableRow arg="alert-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">Time after which a detected server is forgotten. If the server is still present afterwards, a new alert is raised. With `none`, detected servers are never forgotten. Default: 1h.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="unknown-server" typ="multi { mac-address: macAddr
 }">MAC addresses of the unknown DHCP servers that were detected.</ArgTableRow>
</ArgTable>
