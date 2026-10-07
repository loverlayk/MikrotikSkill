# calea

> RouterOS directory reference for /tool/calea.

-----------

## tool/calea 
**Package:** calea
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="case-id" typ="num"></ArgTableRow>
<ArgTableRow arg="case-name" typ="string"></ArgTableRow>
<ArgTableRow arg="intercept-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="intercept-port" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (pcap | limited) { pcap:0, limited:1 }"></ArgTableRow>
<ArgTableRow arg="file-root" typ="string"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-size" typ="num"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-count" typ="num"></ArgTableRow>
<ArgTableRow arg="pcap-file-hash-method" typ="enum (none | md5 | sha1 | sha256) { none:0, md5:1, sha1:2, sha256:3 }"></ArgTableRow>
<ArgTableRow arg="limited-file-stop-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="limited-file-hash-method" typ="enum (none | md5 | sha1 | sha256) { none:0, md5:1, sha1:2, sha256:3 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="access-session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
</ArgTable>
