# crl

> RouterOS directory reference for /certificate/crl.

-----------

## certificate/crl 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="E" typ="expired">expired</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="url" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cert" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="trust-store" typ="alt { all: enum (all)
, component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging)
 }"></ArgTableRow>
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="revoked" typ="num"></ArgTableRow>
<ArgTableRow arg="next-update" typ="date"></ArgTableRow>
<ArgTableRow arg="last-update" typ="date"></ArgTableRow>
<ArgTableRow arg="akid" typ="string"></ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="signature" typ="string"></ArgTableRow>
</ArgTable>
