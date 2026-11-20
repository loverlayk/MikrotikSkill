# monitor

> Shows the counters of the Disconnect and CoA requests. See RADIUS for the full guide.

-----------

## radius/incoming/monitor 
**Type:** Command

Shows the counters of the Disconnect and CoA requests. See [RADIUS](../../../authentication-authorization-accounting/radius) for the full guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requests" typ="num">Valid requests received.</ArgTableRow>
<ArgTableRow arg="bad-requests" typ="num">Requests dropped because of a wrong signature.</ArgTableRow>
<ArgTableRow arg="acks" typ="num">Requests answered with Disconnect-ACK or CoA-ACK.</ArgTableRow>
<ArgTableRow arg="naks" typ="num">Requests answered with Disconnect-NAK or CoA-NAK, for example when no session matches.</ArgTableRow>
</ArgTable>
