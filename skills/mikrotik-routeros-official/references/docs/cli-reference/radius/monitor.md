# monitor

> Shows the request counters of one entry. See RADIUS for the full guide.

-----------

## radius/monitor 
**Type:** Command

Shows the request counters of one entry. See [RADIUS](../../authentication-authorization-accounting/radius) for the full guide.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pending" typ="num">Requests that wait for an answer.</ArgTableRow>
<ArgTableRow arg="requests" typ="num">Requests sent to the server, without the resent ones.</ArgTableRow>
<ArgTableRow arg="accepts" typ="num">Access-Accept answers received.</ArgTableRow>
<ArgTableRow arg="rejects" typ="num">Access-Reject answers received.</ArgTableRow>
<ArgTableRow arg="challenges" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-responses" typ="num">Answers to accounting requests received.</ArgTableRow>
<ArgTableRow arg="other-replies" typ="num"></ArgTableRow>
<ArgTableRow arg="resends" typ="num">Requests sent again after `timeout`.</ArgTableRow>
<ArgTableRow arg="timeouts" typ="num">Requests that got no answer after all tries.</ArgTableRow>
<ArgTableRow arg="bad-replies" typ="num">Answers that were dropped: a wrong signature, or no Message-Authenticator while `require-message-auth` asks for it.</ArgTableRow>
<ArgTableRow arg="last-request-rtt" typ="time">Time between the last request and its answer.</ArgTableRow>
</ArgTable>
