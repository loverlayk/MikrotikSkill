# profile

> Configure MACsec profiles with an ordered cipher-suite list and a key-server election priority, then assign a profile to a MACsec interface. See MACsec for key provisioning, cipher selection, and election behavior.

-----------

## interface/macsec/profile 
**Conditions:** !smips
**Type:** Directory

Configure MACsec profiles with an ordered cipher-suite list and a key-server election priority, then assign a profile to a MACsec interface. See [MACsec](../../../bridging-and-switching/macsec) for key provisioning, cipher selection, and election behavior.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Marks the built-in default MACsec profile.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the MACsec profile.</ArgTableRow>
<ArgTableRow arg="ciphers" typ="multi { cipher: enum (aes-gcm-128 | aes-gcm-xpn-128)
 }" mandatory="1">
Ordered list of cipher suites permitted for MACsec negotiation. Custom profiles must specify this list; the built-in default profile uses `aes-gcm-128`. The key server selects the first common suite in its own profile order. If the peers have no common suite, forwarding does not start; inspect both peers because their status values can differ.

- `aes-gcm-128` - AES-GCM with a 128-bit key.
- `aes-gcm-xpn-128` - AES-GCM with a 128-bit key and extended packet numbering (XPN). XPN extends the packet-number space before Secure Association replacement is required; it does not provide an unlimited Secure Association lifetime.

</ArgTableRow>
<ArgTableRow arg="server-priority" typ="num">Priority used to elect the key server in a point-to-point connection. A lower numeric value takes precedence. If both peers have equal priority, the peer with the lower MAC address becomes key server. Accepted range: `0..255`. Default: `10`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string">Name of the default MACsec profile used when an interface does not explicitly select another profile.</ArgTableRow>
</ArgTable>
