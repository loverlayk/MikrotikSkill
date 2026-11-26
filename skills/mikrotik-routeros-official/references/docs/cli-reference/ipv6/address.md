# address

> RouterOS directory reference for /ipv6/address.

-----------

## ipv6/address 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="G" typ="global">global</ArgTableRow>
<ArgTableRow arg="L" typ="link-local">link-local</ArgTableRow>
<ArgTableRow arg="S" typ="slave">Whether address belongs to an interface which is a slave port to some other master interface.</ArgTableRow>
<ArgTableRow arg="d" typ="deprecated">deprecated</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="composite { address: ip6Addr
, netmask: [ num [ .. 128]]
 }">
IPv6 address.  Address can also be constructed from the pool if `from-pool` parameter is specified.
For example if address is set to `::1/64` then address will be constructed as follows `<prefix_from_pool>::1/64`
</ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address from address property.</ArgTableRow>
<ArgTableRow arg="from-pool-policy" typ="enum (recommended | strict | without-acquire)">
Specify how to acquire prefix from pool, if `from-pool` parameter is set.

- `recommended` option will use `address` as a postfix and **subnet-id**, if subnet-id is provided.
- `strict` will use **address** as a strict postfix.
- `without-acquire` will not allocate a prefix from a pool and will allow other services to use the exact same prefix. The `without-acquire` option should be mainly used to create SLAAC address on a router which at the same time will be a DHCPv6 server providing addresses to client from the same subnet.
</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Specifies the interface on which the IPv6 address is configured. You can select it from the pool of interfaces available on the router.</ArgTableRow>
<ArgTableRow arg="eui-64" typ="bool">Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">Whether to enable stateless address configuration. The prefix of that address is automatically advertised three times to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64. If address is removed or changed, then old prefix will be deprecated by automatically advertising the old prefix with lifetime set to `0s` three times to hosts using ICMPv6 protocol.</ArgTableRow>
<ArgTableRow arg="no-dad" typ="bool">If enabled (yes) - disables Duplicate Address Detection (DAD) for IPv6 addresses on an interface. This can be useful in scenarios where you want to assign static IPv6 addresses to devices and avoid the delay caused by DAD.</ArgTableRow>
<ArgTableRow arg="auto-link-local" typ="bool">
Controls whether the automatically generated link-local address remains on the interface when a manual link-local address is added. Default: `yes`.

- `yes` - Add the manual link-local address in addition to the automatically generated one.
- `no` - Use the manual link-local address instead of the automatically generated one. Removing the manual address restores the automatic one.

The property is shown on every IPv6 address, but only manual link-local (`fe80::/64`) addresses use it. Setting `no` on a global or unique local address fails with "selected address is not link local".
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-interface" typ="iface_enum">Actual interface on which address is set up. For example, if address was configured on ethernet interface and ethernet interface was added to bridge, then actual interface is bridge not ethernet.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Indicates which VRF this IP address is associated with.</ArgTableRow>
<ArgTableRow arg="valid" typ="alt { valid: enum (forever) { forever:-1 }
, valid: time
 }"></ArgTableRow>
<ArgTableRow arg="preferred" typ="alt { preferred: enum (forever) { forever:-1 }
, preferred: time
 }"></ArgTableRow>
</ArgTable>
