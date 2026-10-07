# list

> Interface lists allow defining a set of interfaces for easier interface management in different interface-based configuration sections such as Neighbour Discovery, Firewall, Bridge, and Internet Detect.

-----------

## interface/list 
**Type:** Directory

Interface lists allow defining a set of interfaces for easier interface management in different interface-based configuration sections such as Neighbour Discovery, Firewall, Bridge, and Internet Detect.

There are four predefined lists: `all` (contains all interfaces), `none` (contains no interfaces), `dynamic` (contains dynamic interfaces), and `static` (contains static interfaces). You can also create additional interface lists.

:::info
Dynamic interfaces are interfaces that have a "dynamic" flag. Any interface that does not have a dynamic flag will be part of the `static` interface list.
:::

Members are added to an interface list in the following order:

1. Include members are added to the interface list.
2. Exclude members are removed from the list.
3. Statically configured members are added to the list.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="builtin">Built-in system list.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Dynamically created list.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the interface list. Predefined lists include "all", "none", "dynamic", and "static".</ArgTableRow>
<ArgTableRow arg="include" typ="multi { include-list: enum
 }">Interface list whose members are included in this list. Multiple lists can be specified, separated by commas.</ArgTableRow>
<ArgTableRow arg="exclude" typ="multi { exclude-list: enum
 }">Interface list whose members are excluded from this list. Multiple lists can be specified, separated by commas.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dynamic" typ="bool">Whether the interface list was created dynamically.</ArgTableRow>
</ArgTable>
