# option

> Additional options the DHCP server can send. Assign them with dhcp-option to a network, a server or a lease, or group them in option sets. When the same option is set on several levels, the lease takes precedence...

-----------

## ip/dhcp-server/option 
**Type:** Directory

Additional options the DHCP server can send. Assign them with `dhcp-option` to a network, a server or a lease, or group them in option sets. When the same option is set on several levels, the lease takes precedence over the server, and the server over the network. For examples, see [DHCP Server](../../../../network-management/dhcp/server).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the option, used where options are assigned.</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1">DHCP option code (1-254).</ArgTableRow>
<ArgTableRow arg="value" typ="string">
Value of the option. The value is converted according to how it is written:
- `'test'` - Text in quotes is sent as text (`74657374`).
- `'10.10.10.10'` - An IP address in quotes is sent as four bytes (`0a0a0a0a`).
- `s'10.10.10.10'` - With the `s` prefix, the value is always sent as text (`31302e31302e31302e3130`).
- `'10'` - A number in quotes is sent as one byte (`0a`).
- `0x0a0a` - A hex value is sent as it is.

Parts can be combined, for example `0x01'vards'$(HOSTNAME)`. These variables can be used:
- `$(HOSTNAME)` - The router's identity.
- `$(NETWORK_GATEWAY)` - The first gateway of the matching network (`/ip/dhcp-server/network`), filled in when the option is sent.
- `$(RADIUS_MT_STR1)`, `$(RADIUS_MT_STR2)` - MikroTik RADIUS attributes 24 and 25.
- `$(REMOTE_ID)` - Remote ID of the relay agent information (option 82).
</ArgTableRow>
<ArgTableRow arg="force" typ="bool">Whether to send the option even when the client did not ask for it in its parameter request list (option 55). Without it, the option is sent only to clients that ask for it. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string">The option value as it is sent, in hex. Variables that depend on the client or network are filled in only when the option is sent.</ArgTableRow>
</ArgTable>
