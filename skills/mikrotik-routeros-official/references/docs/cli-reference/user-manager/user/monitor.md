# monitor

> RouterOS command reference for /user-manager/user/monitor.

-----------

## user-manager/user/monitor 
**Package:** userman-5
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="total-download" typ="num"></ArgTableRow>
<ArgTableRow arg="total-upload" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="active-sub-sessions" typ="num"></ArgTableRow>
<ArgTableRow arg="actual-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="attributes-details" typ="object { attribute-value: super { attribute: enum
, [value] :string
, [value-type] :enum (ip-address | string | uint32 | hex | ip6-prefix | macro)
, [raw-value] :0xstring
 }
 }"></ArgTableRow>
</ArgTable>
