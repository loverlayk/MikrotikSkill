# requests

> RouterOS directory reference for /certificate/scep-server/requests.

-----------

## certificate/scep-server/requests 
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="authority" typ="alt { ca: enum
, ra: enum
 }"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (pending | granted | denied | authorized | waiting | failed | issued | invalid) { pending:1, granted:2, denied:3, authorized:4, waiting:10, failed:11, issued:12, invalid:13 }"></ArgTableRow>
<ArgTableRow arg="created" typ="date"></ArgTableRow>
<ArgTableRow arg="transaction-id" typ="string"></ArgTableRow>
<ArgTableRow arg="req-fingerprint" typ="string"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="locality" typ="string"></ArgTableRow>
<ArgTableRow arg="organization" typ="string"></ArgTableRow>
<ArgTableRow arg="unit" typ="string"></ArgTableRow>
<ArgTableRow arg="common-name" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="subject-alt-name" typ="object { alt-name: composite { type: enum (IP | DNS | email)
, value: alt { ip: alt { ipv6: ip6Addr
, ip: ipAddr
 }
, string: string
 }
 }
 }"></ArgTableRow>
</ArgTable>
