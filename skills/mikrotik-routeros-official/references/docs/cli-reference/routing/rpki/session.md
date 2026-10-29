# session

> RouterOS directory reference for /routing/rpki/session.

-----------

## routing/rpki/session 
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (idle | connecting | prepare | loading | sync | error)"></ArgTableRow>
<ArgTableRow arg="version" typ="num">Negotiated RTR protocol version. RouterOS starts with version 2 and falls back to version 1 when the validator does not support version 2. ASPA data is available only over version 2. The field is shown after the session has synchronized.</ArgTableRow>
<ArgTableRow arg="session" typ="num"></ArgTableRow>
<ArgTableRow arg="serial" typ="num"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
</ArgTable>
