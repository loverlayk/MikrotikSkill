# select-rule

> RouterOS directory reference for /routing/filter/select-rule.

-----------

## routing/filter/select-rule 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" unset="1" mandatory="1"></ArgTableRow>
<ArgTableRow arg="do-where" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-num" typ="super { prop: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, [chain] >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-prfx" typ="super { prop: enum (dst | gw | pref-src | ospf-fwd | ospf-fwd | bgp-input-local-addr | bgp-input-remote-addr | bgp-output-local-addr | bgp-output-remote-addr)
, [chain] >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-num" typ="super { prop: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag)
, [compare] >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-prfx" typ="super { prop: enum (dst | gw | pref-src | ospf-fwd | ospf-fwd | bgp-input-local-addr | bgp-input-remote-addr | bgp-output-local-addr | bgp-output-remote-addr)
, [compare] >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-take" typ="num"></ArgTableRow>
<ArgTableRow arg="do-jump" typ="enum"></ArgTableRow>
</ArgTable>
