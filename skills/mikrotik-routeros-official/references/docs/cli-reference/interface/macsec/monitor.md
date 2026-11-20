# monitor

> Display the key-server role and active cipher suite for a MACsec interface. See MACsec for negotiation and troubleshooting.

-----------

## interface/macsec/monitor 
**Conditions:** !smips
**Type:** Command

Display the key-server role and active cipher suite for a MACsec interface. See [MACsec](../../../bridging-and-switching/macsec) for negotiation and troubleshooting.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-server" typ="bool">Whether this interface is the key server that generates and distributes Secure Association Keys for the point-to-point link.</ArgTableRow>
<ArgTableRow arg="cipher-suite" typ="enum (aes-gcm-128 | aes-gcm-xpn-128)">
Cipher suite selected for the active MACsec session. The key server selects the first common suite in its own profile order.

- `aes-gcm-128` - AES-GCM with a 128-bit key.
- `aes-gcm-xpn-128` - AES-GCM with a 128-bit key and extended packet numbering (XPN).

</ArgTableRow>
</ArgTable>
