# target

> RouterOS directory reference for /ip/traffic-flow/target.

-----------

## ip/traffic-flow/target 
**Type:** Directory
Export targets: the collector hosts (for example a NetFlow analyzer host) that receive traffic-flow data over UDP.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">Source address of the export packets. 0.0.0.0 means auto-detect: the router uses the source of the outgoing interface</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }" mandatory="1">IP address of the host that receives the flow data</ArgTableRow>
<ArgTableRow arg="port" typ="num">UDP port to send flows to. Default: 2055</ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 5 | 9 | ipfix) { 1:1, 5:5, 9:9, ipfix:10 }">NetFlow format of the export packets: `1`, `5`, `9` or `ipfix`</ArgTableRow>
<ArgTableRow arg="v9-template-refresh" typ="num">Number of export packets after which the FlowSet template is resent (version 9 and IPFIX only). Default: 20</ArgTableRow>
<ArgTableRow arg="v9-template-timeout" typ="time">Send the FlowSet template after this interval if it has not been sent by then (version 9 and IPFIX only)</ArgTableRow>
</ArgTable>
