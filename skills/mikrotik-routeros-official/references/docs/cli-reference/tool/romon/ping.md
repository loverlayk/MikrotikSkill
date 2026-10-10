# ping

> Ping a router over the RoMON overlay by its RoMON ID, without any IP connectivity.

-----------

## tool/romon/ping 
**Type:** Command

Ping a router over the [RoMON](../../../management-tools/romon) overlay by its RoMON ID, without any IP connectivity.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="id" typ="macAddr">RoMON ID (MAC address) of the router to ping</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of the ping packet payload (default value: **32**)</ArgTableRow>
<ArgTableRow arg="interval" typ="time">Interval between pings (default value: **1s**)</ArgTableRow>
<ArgTableRow arg="count" typ="num">Number of pings to send (default value: **100**)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="num">Ping sequence number</ArgTableRow>
<ArgTableRow arg="host" typ="macAddr">RoMON ID (MAC address) of the router that answered</ArgTableRow>
<ArgTableRow arg="time" typ="time">Round-trip time of the reply</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of the reply</ArgTableRow>
<ArgTableRow arg="status" typ="string">Failure reason (for example `timeout`); empty on success</ArgTableRow>
<ArgTableRow arg="sent" typ="num">Pings sent</ArgTableRow>
<ArgTableRow arg="received" typ="num">Replies received</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">Percentage of lost pings</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">Smallest round-trip time</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">Average round-trip time</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">Largest round-trip time</ArgTableRow>
</ArgTable>
