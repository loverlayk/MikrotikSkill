# profile

> RouterOS directory reference for /ppp/profile.

-----------

## ppp/profile 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { pool: enum
, address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { pool: enum
, address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-pool" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-prefix-reuse" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-pd-pool" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dhcpv6-use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="bridge-port-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-learning" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }"></ArgTableRow>
<ArgTableRow arg="bridge-port-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-port-trusted" typ="bool"></ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="use-ipv6" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }"></ArgTableRow>
<ArgTableRow arg="use-mpls" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }"></ArgTableRow>
<ArgTableRow arg="use-compression" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }"></ArgTableRow>
<ArgTableRow arg="use-encryption" typ="enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 }"></ArgTableRow>
<ArgTableRow arg="only-one" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }"></ArgTableRow>
<ArgTableRow arg="change-tcp-mss" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }"></ArgTableRow>
<ArgTableRow arg="use-upnp" typ="enum (default | no | yes) { default:0xffffffff, no:0, yes:1 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first) { bottom:0xffffffff, first:0 }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="composite { upload-queue: enum
, download-queue: enum
 }"></ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { address-list: enum
 }"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="on-up" typ="alt { script: string
 }"></ArgTableRow>
<ArgTableRow arg="on-down" typ="alt { script: string
 }"></ArgTableRow>
</ArgTable>
