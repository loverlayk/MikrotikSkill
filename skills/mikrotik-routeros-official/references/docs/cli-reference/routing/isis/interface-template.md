# interface-template

> RouterOS directory reference for /routing/isis/interface-template.

-----------

## routing/isis/interface-template 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="levels" typ="ubit (l1, l2)"></ArgTableRow>
<ArgTableRow arg="ptp" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="passive" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.hello-3way" typ="switch" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ptp.l2.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l1.metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-interval-dr" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.hello-multiplier" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.csnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.psnp-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bcast.l2.metric" typ="num" unset="1"></ArgTableRow>
</ArgTable>
