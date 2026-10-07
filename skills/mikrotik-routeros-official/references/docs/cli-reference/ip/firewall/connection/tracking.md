# tracking

> RouterOS settings reference for /ip/firewall/connection/tracking.

-----------

## ip/firewall/connection/tracking 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (auto | yes | no) { auto:0, yes:1, no:2 }"></ArgTableRow>
<ArgTableRow arg="tcp-syn-sent-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-syn-received-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-established-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-fin-wait-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-close-wait-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-last-ack-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-time-wait-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-close-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-max-retrans-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="tcp-unacked-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="loose-tcp-tracking" typ="bool"></ArgTableRow>
<ArgTableRow arg="liberal-tcp-tracking" typ="bool"></ArgTableRow>
<ArgTableRow arg="udp-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="udp-stream-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="icmp-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="generic-timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-ipv4" typ="bool"></ArgTableRow>
<ArgTableRow arg="active-ipv6" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-entries" typ="num"></ArgTableRow>
<ArgTableRow arg="total-entries" typ="num"></ArgTableRow>
<ArgTableRow arg="total-ip4-entries" typ="num"></ArgTableRow>
<ArgTableRow arg="total-ip6-entries" typ="num"></ArgTableRow>
</ArgTable>
