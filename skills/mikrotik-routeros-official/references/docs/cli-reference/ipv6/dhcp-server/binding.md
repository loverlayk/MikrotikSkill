# binding

> Bindings of the DHCPv6 servers: the prefixes and addresses given to clients. Dynamic bindings are created from the server's pools; static bindings give a client, identified by its DUID and IAID, a fixed prefix or...

-----------

## ipv6/dhcp-server/binding 
**Type:** Directory

Bindings of the DHCPv6 servers: the prefixes and addresses given to clients. Dynamic bindings are created from the server's pools; static bindings give a client, identified by its DUID and IAID, a fixed prefix or address. For details, see [DHCPv6 Server](../../../../network-management/dhcp/dhcpv6-server).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid">The binding is invalid.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The binding is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="radius">The binding was assigned by a RADIUS server.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">The binding is dynamic. Use `make-static` to turn it into a static binding.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { prefix: ip6Prefix
 }">Prefix or address assigned to the client.</ArgTableRow>
<ArgTableRow arg="duid" typ="string" mandatory="1">DUID of the client, in hex, for example `0x00030001dc2c6ee7106a`. Together with `iaid`, it identifies the client request the binding answers.</ArgTableRow>
<ArgTableRow arg="iaid" typ="num" mandatory="1">Identity association identifier (IAID) of the client request. Together with `duid`, it identifies the binding.</ArgTableRow>
<ArgTableRow arg="ia-type" typ="enum (na | pd)">
Type of the binding:
- `na` - An address binding (IA_NA).
- `pd` - A prefix delegation binding (IA_PD).
</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)">Name of the DHCPv6 server that can offer this binding, or `all` for every server.</ArgTableRow>
<ArgTableRow arg="life-time" typ="time">Lifetime of a static binding. Dynamic bindings use the `lease-time` of the server. Default: 1w.</ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="enum">IPv6 pool the prefix or address of the binding comes from. For addresses, the pool prefix length is 128.</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }">Options (`/ipv6/dhcp-server/option`) to send to this client.</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Bandwidth limit for the client, in the same format as the `rate-limit` of a DHCP server lease. The server creates a dynamic simple queue for the prefix or address of the binding.</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">Whether this binding and a DHCP lease of the same client share one dynamic simple queue. Default: yes.</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">IPv6 firewall address lists to which the prefix or address of the binding is added. Overrides the `address-lists` setting of the server.</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">Where to place the dynamic simple queue created for this binding: `first` (default), `bottom`, or before the named queue.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">Parent of the dynamic simple queue created for this binding. Default: none.</ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum">Queue type of the dynamic simple queue created for this binding.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-server" typ="enum (none)">DHCPv6 server that serves the binding.</ArgTableRow>
<ArgTableRow arg="status" typ="enum (waiting | offered | bound)">
State of the binding:
- `waiting` - A static binding that is not in use, or a dynamic binding that was used before. The server keeps a dynamic binding for 10 minutes so the old client can get it back; after that the prefix can be given to other clients.
- `offered` - The server answered a Solicit with an Advertise, but has not received the Request. The client has 2 minutes to request the binding.
- `bound` - The client uses the binding.
</ArgTableRow>
<ArgTableRow arg="expires-after" typ="time">Time until the binding expires.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time: time
 }">Time since the server last received a message from the client, or `never`.</ArgTableRow>
<ArgTableRow arg="client-address" typ="ip6Addr">IPv6 address the client sends from, usually its link-local address. The routes to the binding use it as the gateway.</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">Key the server gave the client for authenticating Reconfigure messages (`use-reconfigure`).</ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string">Replay-detection counter of the last Reconfigure message sent to the client. It increases with every Reconfigure message.</ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
<ArgTableRow arg="fqdn" typ="string">FQDN the client sent (option 39).</ArgTableRow>
</ArgTable>
