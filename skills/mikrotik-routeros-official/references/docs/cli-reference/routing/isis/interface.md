# interface

> RouterOS directory reference for /routing/isis/interface.

-----------

## routing/isis/interface 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="ptp" typ="switch"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.usage" typ="ubit (l1, l2)" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.3way-state" typ="enum (down | init | up)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-dr-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.passive" typ="switch"></ArgTableRow>
<ArgTableRow arg="l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-dr-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.passive" typ="switch"></ArgTableRow>
</ArgTable>
