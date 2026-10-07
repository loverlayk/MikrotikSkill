# settings

> RouterOS settings reference for /interface/bridge/settings.

-----------

## interface/bridge/settings 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="use-ip-firewall" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-ip-firewall-for-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-ip-firewall-for-pppoe" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bridge-fast-path-active" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-path-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-forward-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge-fast-forward-bytes" typ="num"></ArgTableRow>
</ArgTable>
