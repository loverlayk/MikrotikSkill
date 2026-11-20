# monitor

> Counters of the requests of a router.

-----------

## user-manager/router/monitor 
**Package:** userman-5
**Type:** Command

Counters of the requests of a router.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="broken-requests" typ="num">Requests that could not be read.</ArgTableRow>
<ArgTableRow arg="unknown-requests" typ="num">Requests of an unknown type.</ArgTableRow>
<ArgTableRow arg="access-requests" typ="num">Access-Request messages received.</ArgTableRow>
<ArgTableRow arg="access-failures" typ="num">Access-Request messages that were refused.</ArgTableRow>
<ArgTableRow arg="accounting-requests" typ="num">Accounting-Request messages received.</ArgTableRow>
<ArgTableRow arg="accounting-failures" typ="num">Accounting-Request messages that failed.</ArgTableRow>
<ArgTableRow arg="disconnect-ack" typ="num">Disconnect requests that the router confirmed.</ArgTableRow>
<ArgTableRow arg="disconnect-nak" typ="num">Disconnect requests that the router refused.</ArgTableRow>
<ArgTableRow arg="coa-ack" typ="num">Change of Authorization requests that the router confirmed.</ArgTableRow>
<ArgTableRow arg="coa-nak" typ="num">Change of Authorization requests that the router refused.</ArgTableRow>
<ArgTableRow arg="sent-from-cache" typ="num">Replies that were sent again for a repeated request.</ArgTableRow>
</ArgTable>
