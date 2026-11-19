# connection

> List of the IPv4 connections that connection tracking holds. All properties are read-only. See Connection tracking.

-----------

## ip/firewall/connection 
**Type:** Directory

List of the IPv4 connections that connection tracking holds. All properties are read-only. See [Connection tracking](../../../../firewall-and-quality-of-service/connection-tracking).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expected">The connection was expected by a connection helper (`/ip/firewall/service-port`), for example the data connection of an FTP session.</ArgTableRow>
<ArgTableRow arg="S" typ="seen-reply">The destination has replied: the connection has seen packets in both directions.</ArgTableRow>
<ArgTableRow arg="A" typ="assured">The connection is assured: it is not removed early when the connection list is full.</ArgTableRow>
<ArgTableRow arg="C" typ="confirmed">The connection is confirmed: its first packet has left the router.</ArgTableRow>
<ArgTableRow arg="D" typ="dying">The connection is being removed because its timeout has ended.</ArgTableRow>
<ArgTableRow arg="F" typ="fasttrack">The connection is FastTracked.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offload">The connection is offloaded to hardware.</ArgTableRow>
<ArgTableRow arg="s" typ="srcnat">Source NAT is applied to the connection, including masquerade.</ArgTableRow>
<ArgTableRow arg="d" typ="dstnat">Destination NAT is applied to the connection, for example a port forward.</ArgTableRow>
<ArgTableRow arg="h" typ="uses-helper">A connection helper of `/ip/firewall/service-port` handles the connection.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="enum ()">Connection protocol.</ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr">Source IP address of the connection.</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">Source port of the connection.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="ipAddr">Destination IP address of the connection.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">Destination port of the connection.</ArgTableRow>
<ArgTableRow arg="reply-src-address" typ="ipAddr">Source IP address that the reply packets have. With destination NAT, it differs from `dst-address`.</ArgTableRow>
<ArgTableRow arg="reply-src-port" typ="num">Source port that the reply packets have.</ArgTableRow>
<ArgTableRow arg="reply-dst-address" typ="ipAddr">Destination IP address that the reply packets have. With source NAT, it differs from `src-address`.</ArgTableRow>
<ArgTableRow arg="reply-dst-port" typ="num">Destination port that the reply packets have.</ArgTableRow>
<ArgTableRow arg="tcp-state" typ="enum (none | syn-sent | syn-recv | established | fin-wait | close-wait | last-ack | time-wait | close | listen) { none:0, syn-sent:1, syn-recv:2, established:3, fin-wait:4, close-wait:5, last-ack:6, time-wait:7, close:8, listen:9 }">State of the TCP connection, for example `syn-sent`, `established` or `time-wait`. The state selects the timeout of the entry.</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="num">ICMP type.</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="num">ICMP code.</ArgTableRow>
<ArgTableRow arg="icmp-id" typ="num">ICMP ID.</ArgTableRow>
<ArgTableRow arg="gre-protocol" typ="num">Protocol of the payload that GRE carries.</ArgTableRow>
<ArgTableRow arg="gre-version" typ="num">Version of the GRE protocol.</ArgTableRow>
<ArgTableRow arg="gre-key" typ="num">Contents of the GRE key field.</ArgTableRow>
<ArgTableRow arg="connection-type" typ="string">Type that a connection helper has set, for example `ftp`, `tftp` or `pptp`. Empty when connection tracking cannot determine the type, for example on a related connection that a helper created.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Time after which the router removes the connection from the list if it sees no more packets of it.</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="string">Connection mark that a mangle rule has set.</ArgTableRow>
<ArgTableRow arg="orig-packets" typ="num">Number of packets sent from the source address of the connection.</ArgTableRow>
<ArgTableRow arg="orig-bytes" typ="num">Number of bytes sent from the source address of the connection.</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-packets" typ="num">Number of FastTracked packets sent from the source address of the connection.</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-bytes" typ="num">Number of FastTracked bytes sent from the source address of the connection.</ArgTableRow>
<ArgTableRow arg="repl-packets" typ="num">Number of packets sent from the destination address of the connection.</ArgTableRow>
<ArgTableRow arg="repl-bytes" typ="num">Number of bytes sent from the destination address of the connection.</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-packets" typ="num">Number of FastTracked packets sent from the destination address of the connection.</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-bytes" typ="num">Number of FastTracked bytes sent from the destination address of the connection.</ArgTableRow>
<ArgTableRow arg="orig-rate" typ="num">Current data rate from the source address of the connection.</ArgTableRow>
<ArgTableRow arg="repl-rate" typ="num">Current data rate from the destination address of the connection.</ArgTableRow>
</ArgTable>
