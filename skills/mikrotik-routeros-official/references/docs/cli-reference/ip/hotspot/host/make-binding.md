# make-binding

> The /ip/hotspot/host/make-binding command creates an entry in /ip/hotspot/ip-binding from a host.

-----------

## ip/hotspot/host/make-binding 
**Type:** Command

The `/ip/hotspot/host/make-binding` command creates an entry in `/ip/hotspot/ip-binding` from a host.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="comment" typ="string">Comment of the new binding.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (regular | bypassed | blocked) { regular:0, bypassed:1, blocked:2 }">Type of the new binding, see `/ip/hotspot/ip-binding`.</ArgTableRow>
</ArgTable>
