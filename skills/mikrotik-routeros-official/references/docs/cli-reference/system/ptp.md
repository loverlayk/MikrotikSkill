# ptp

> RouterOS directory reference for /system/ptp.

-----------

## system/ptp 
**Conditions:** !smips
**Syscap:** ptp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="priority1" typ="enum (auto) { auto:0 }"></ArgTableRow>
<ArgTableRow arg="priority2" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="delay-mode" typ="enum (auto | e2e | p2p)"></ArgTableRow>
<ArgTableRow arg="transport" typ="enum (auto | ipv4 | l2-non-forwardable | l2-forwardable)"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum (default | 802.1as | g8275.1 | aes67 | smpte-2059)"></ArgTableRow>
<ArgTableRow arg="domain" typ="enum (auto)"></ArgTableRow>
<ArgTableRow arg="ptp-mode" typ="enum (ordinary-clock | transparent-clock)"></ArgTableRow>
</ArgTable>
