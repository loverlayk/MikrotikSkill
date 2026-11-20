# monitor

> Totals of a user.

-----------

## user-manager/user/monitor 
**Package:** userman-5
**Type:** Command

Totals of a user.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total-uptime" typ="time">Time of all sessions of the user together.</ArgTableRow>
<ArgTableRow arg="total-download" typ="num">Bytes sent to the user in all sessions.</ArgTableRow>
<ArgTableRow arg="total-upload" typ="num">Bytes received from the user in all sessions.</ArgTableRow>
<ArgTableRow arg="active-sessions" typ="num">Number of active sessions.</ArgTableRow>
<ArgTableRow arg="active-sub-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="actual-profile" typ="enum">Profile that the user has now.</ArgTableRow>
<ArgTableRow arg="attributes-details" typ="object { attribute-value: super { attribute: enum
, [value] :string
, [value-type] :enum (ip-address | string | uint32 | hex | ip6-prefix | macro)
, [raw-value] :0xstring
 }
 }">Attributes that the user gets, each as name, value, type and the encoded value.</ArgTableRow>
</ArgTable>
