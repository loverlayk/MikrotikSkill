# connection

> RouterOS directory reference for /ip/firewall/connection.

-----------

## ip/firewall/connection 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expected">expected</ArgTableRow>
<ArgTableRow arg="S" typ="seen-reply">seen-reply</ArgTableRow>
<ArgTableRow arg="A" typ="assured">assured</ArgTableRow>
<ArgTableRow arg="C" typ="confirmed">confirmed</ArgTableRow>
<ArgTableRow arg="D" typ="dying">dying</ArgTableRow>
<ArgTableRow arg="F" typ="fasttrack">fasttrack</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offload">hw-offload</ArgTableRow>
<ArgTableRow arg="s" typ="srcnat">srcnat</ArgTableRow>
<ArgTableRow arg="d" typ="dstnat">dstnat</ArgTableRow>
<ArgTableRow arg="h" typ="uses-helper">uses-helper</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="enum ()">Connection protocol.</ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr">Source IP address of the connection.</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">Source port of the connection.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="ipAddr">Destination IP address of the connection.</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">Destination port of the connection.</ArgTableRow>
<ArgTableRow arg="reply-src-address" typ="ipAddr">Reply source IP address.</ArgTableRow>
<ArgTableRow arg="reply-src-port" typ="num">Reply source port.</ArgTableRow>
<ArgTableRow arg="reply-dst-address" typ="ipAddr">Reply destination IP address.</ArgTableRow>
<ArgTableRow arg="reply-dst-port" typ="num">Reply destination port.</ArgTableRow>
<ArgTableRow arg="tcp-state" typ="enum (none | syn-sent | syn-recv | established | fin-wait | close-wait | last-ack | time-wait | close | listen) { none:0, syn-sent:1, syn-recv:2, established:3, fin-wait:4, close-wait:5, last-ack:6, time-wait:7, close:8, listen:9 }">TCP connection state.</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="num">ICMP type.</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="num">ICMP code.</ArgTableRow>
<ArgTableRow arg="icmp-id" typ="num">ICMP ID.</ArgTableRow>
<ArgTableRow arg="gre-protocol" typ="num">GRE protocol.</ArgTableRow>
<ArgTableRow arg="gre-version" typ="num">GRE version.</ArgTableRow>
<ArgTableRow arg="gre-key" typ="num">GRE key.</ArgTableRow>
<ArgTableRow arg="connection-type" typ="string">Connection type.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Connection timeout.</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="string">Connection mark.</ArgTableRow>
<ArgTableRow arg="orig-packets" typ="num">Number of original direction packets.</ArgTableRow>
<ArgTableRow arg="orig-bytes" typ="num">Number of original direction bytes.</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-packets" typ="num">Number of original direction fasttrack packets.</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-bytes" typ="num">Number of original direction fasttrack bytes.</ArgTableRow>
<ArgTableRow arg="repl-packets" typ="num">Number of reply direction packets.</ArgTableRow>
<ArgTableRow arg="repl-bytes" typ="num">Number of reply direction bytes.</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-packets" typ="num">Number of reply direction fasttrack packets.</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-bytes" typ="num">Number of reply direction fasttrack bytes.</ArgTableRow>
<ArgTableRow arg="orig-rate" typ="num">Original direction rate.</ArgTableRow>
<ArgTableRow arg="repl-rate" typ="num">Reply direction rate.</ArgTableRow>
</ArgTable>
