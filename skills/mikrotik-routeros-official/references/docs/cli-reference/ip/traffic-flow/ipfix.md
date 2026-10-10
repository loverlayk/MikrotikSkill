# ipfix

> RouterOS settings reference for /ip/traffic-flow/ipfix.

-----------

## ip/traffic-flow/ipfix 
**Type:** Settings Directory
Select the fields included in IPFIX flow records. A row set to `yes` exports that field per flow.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="nat-events" typ="bool">Include the NAT bitmask of the flow (event flags)</ArgTableRow>
<ArgTableRow arg="first-forwarded" typ="bool">Include the timestamp of the first forwarded packet of the flow</ArgTableRow>
<ArgTableRow arg="last-forwarded" typ="bool">Include the timestamp of the last forwarded packet of the flow</ArgTableRow>
<ArgTableRow arg="sys-init-time" typ="bool">Include the system boot time reference of the flow</ArgTableRow>
<ArgTableRow arg="packets" typ="bool">Include the number of packets in the flow</ArgTableRow>
<ArgTableRow arg="bytes" typ="bool">Include the total byte count of the flow</ArgTableRow>
<ArgTableRow arg="src-port" typ="bool">Include the source port number of the flow</ArgTableRow>
<ArgTableRow arg="dst-port" typ="bool">Include the destination port number of the flow</ArgTableRow>
<ArgTableRow arg="in-interface" typ="bool">Include the interface the flow was received on</ArgTableRow>
<ArgTableRow arg="out-interface" typ="bool">Include the interface the flow was sent out on</ArgTableRow>
<ArgTableRow arg="protocol" typ="bool">Include the IP protocol number (TCP, UDP, ICMP, ...)</ArgTableRow>
<ArgTableRow arg="tos" typ="bool">Include the IP header TOS (Type of Service) field</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="bool">Include the cumulative TCP flags of the flow (SYN, ACK, ...)</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="bool">Include the destination MAC address of the flow</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="bool">Include the source MAC address of the flow</ArgTableRow>
<ArgTableRow arg="src-address" typ="bool">Include the source IP address of the flow</ArgTableRow>
<ArgTableRow arg="dst-address" typ="bool">Include the destination IP address of the flow</ArgTableRow>
<ArgTableRow arg="src-address-mask" typ="bool">Include the source netmask length (summarization)</ArgTableRow>
<ArgTableRow arg="dst-address-mask" typ="bool">Include the destination netmask length</ArgTableRow>
<ArgTableRow arg="gateway" typ="bool">Include the gateway IP address the flow was routed to</ArgTableRow>
<ArgTableRow arg="ttl" typ="bool">Include the TTL of the packets</ArgTableRow>
<ArgTableRow arg="ip-header-length" typ="bool">Include the IP header length</ArgTableRow>
<ArgTableRow arg="is-multicast" typ="bool">Mark the multicast flows</ArgTableRow>
<ArgTableRow arg="ip-total-length" typ="bool">Include the total IP packet length in bytes</ArgTableRow>
<ArgTableRow arg="nat-src-address" typ="bool">Include the NATed source address of the flow</ArgTableRow>
<ArgTableRow arg="nat-dst-address" typ="bool">Include the NATed destination address of the flow</ArgTableRow>
<ArgTableRow arg="nat-src-port" typ="bool">Include the NATed source port of the flow</ArgTableRow>
<ArgTableRow arg="nat-dst-port" typ="bool">Include the NATed destination port of the flow</ArgTableRow>
<ArgTableRow arg="ipv6-flow-label" typ="bool">Include the IPv6 flow label field</ArgTableRow>
<ArgTableRow arg="udp-length" typ="bool">Include the UDP payload length</ArgTableRow>
<ArgTableRow arg="tcp-seq-num" typ="bool">Include the TCP sequence number</ArgTableRow>
<ArgTableRow arg="tcp-ack-num" typ="bool">Include the TCP acknowledgment number</ArgTableRow>
<ArgTableRow arg="tcp-window-size" typ="bool">Include the TCP window size</ArgTableRow>
<ArgTableRow arg="igmp-type" typ="bool">Include the IGMP message type</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="bool">Include the ICMP type</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="bool">Include the ICMP code</ArgTableRow>
</ArgTable>
