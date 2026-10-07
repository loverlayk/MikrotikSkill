# instance

> RouterOS directory reference for /routing/isis/instance.

-----------

## routing/isis/instance 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="system-id" typ="string"></ArgTableRow>
<ArgTableRow arg="areas" typ="multi { area: string
 }"></ArgTableRow>
<ArgTableRow arg="areas-max" typ="num"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="metric-type" typ="enum (old | wide | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.redistribute" typ="ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.originate-default" typ="enum (never | always | if-installed)" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l1.lsp-refresh-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.redistribute" typ="ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.originate-default" typ="enum (never | always | if-installed)" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-size" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-max-age" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-update-interval" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="l2.lsp-refresh-interval" typ="num" unset="1"></ArgTableRow>
</ArgTable>
