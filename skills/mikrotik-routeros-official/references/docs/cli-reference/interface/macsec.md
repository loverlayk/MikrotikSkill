# macsec

> Create MACsec interfaces on Ethernet links and inspect their Secure Channel (SC) and Secure Association (SA) statistics. Interfaces can carry a comment, and new interfaces are enabled by default. RouterOS uses...

-----------

## interface/macsec 
**Conditions:** !smips
**Type:** Directory

Create MACsec interfaces on Ethernet links and inspect their Secure Channel (SC) and Secure Association (SA) statistics. Interfaces can carry a `comment`, and new interfaces are enabled by default. RouterOS uses matching static CAK and CKN values on both peers; automatic dot1x key provisioning is not available. The `tx-sc-*` and `rx-sc-*` rows are aggregate counters for each SC, while the `tx-sa-*` and `rx-sa-*` rows are arrays for individual SA slots. See [MACsec](../../../bridging-and-switching/macsec) for configuration, MTU, negotiation, and troubleshooting.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">The MACsec interface is inactive.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The MACsec interface is disabled by configuration.</ArgTableRow>
<ArgTableRow arg="R" typ="running">The MACsec interface is running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">MACsec processing is actively offloaded to supported hardware for this interface. The flag does not merely indicate hardware capability.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the MACsec interface. Default: `macsec1`.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Maximum transmission unit in bytes for traffic on the MACsec interface. The MACsec L2MTU is automatically set to the parent interface L2MTU minus the 32-byte MACsec overhead and cannot be changed directly. Default: `1468`.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Parent Ethernet interface on which to create MACsec. Only one MACsec interface can use a parent. A parent that already belongs to a bridge produces an invalid MACsec interface with the detail `Interface is already a slave`; add the MACsec interface to the bridge instead.</ArgTableRow>
<ArgTableRow arg="cak" typ="string">Sixteen-byte pre-shared Connectivity Association Key (CAK), entered as 32 hexadecimal characters. Both ends of the link must use matching CAK and CKN values. Use `print show-sensitive` to display the value for provisioning on the peer. Default: a randomly generated 16-byte value.</ArgTableRow>
<ArgTableRow arg="ckn" typ="string">Thirty-two-byte Connectivity Association Name (CKN), entered as 64 hexadecimal characters. Both ends of the link must use matching CAK and CKN values. Default: a randomly generated 32-byte value.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">MACsec profile that supplies the ordered cipher-suite list and key-server priority. Default: `default`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">
Current MACsec interface state.

- `disabled` - The interface is disabled.
- `initializing` - MACsec initialization is in progress.
- `invalid` - The configuration cannot be used. For example, the parent interface already belongs to a bridge.
- `negotiating` - MACsec Key Agreement has not established an operational secure channel. Check that both peers have matching CAK and CKN values and a common cipher suite.
- `open-encrypted` - The local interface reports an encrypted channel open. This alone does not prove peer negotiation or end-to-end forwarding.
</ArgTableRow>
<ArgTableRow arg="tx-untagged" typ="num">Transmitted frames sent without a SecTAG because MACsec protection was not applied.</ArgTableRow>
<ArgTableRow arg="rx-untagged" typ="num">Received frames without a SecTAG that were accepted when frame validation was not Strict.</ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="num">Transmitted frames discarded because MACsec overhead would make the secured frame too long.</ArgTableRow>
<ArgTableRow arg="rx-no-tag" typ="num">Received frames discarded because the SecTAG was absent while Strict validation required it.</ArgTableRow>
<ArgTableRow arg="rx-bad-tag" typ="num">Received frames discarded because their SecTAG was malformed or otherwise invalid.</ArgTableRow>
<ArgTableRow arg="rx-unknown-sci" typ="num">Received frames discarded because their Secure Channel Identifier (SCI) did not identify a known receive SC.</ArgTableRow>
<ArgTableRow arg="rx-no-sci" typ="num">Received frames discarded because the SCI was absent and no receive SC could be identified.</ArgTableRow>
<ArgTableRow arg="rx-overrun" typ="num">Received frames discarded because SecY receive or validation resources were overrun.</ArgTableRow>
<ArgTableRow arg="tx-sc-protected-byte" typ="multi { counter: num
 }">Aggregate number of plaintext octets transmitted with integrity protection but without encryption on this TX SC.</ArgTableRow>
<ArgTableRow arg="tx-sc-protected-packet" typ="multi { counter: num
 }">Aggregate number of packets transmitted with integrity protection but without encryption on this TX SC.</ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-byte" typ="multi { counter: num
 }">Aggregate number of plaintext octets transmitted with encryption and integrity protection on this TX SC.</ArgTableRow>
<ArgTableRow arg="tx-sc-encrypted-packet" typ="multi { counter: num
 }">Aggregate number of packets transmitted with encryption and integrity protection on this TX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-validated-byte" typ="multi { counter: num
 }">Aggregate number of plaintext octets successfully integrity-validated without decryption on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-decrypted-byte" typ="multi { counter: num
 }">Aggregate number of plaintext octets successfully decrypted and integrity-validated on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-unchecked" typ="multi { counter: num
 }">Aggregate number of packets received while frame validation was Disabled and accepted without integrity validation on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-delayed" typ="multi { counter: num
 }">Aggregate number of valid packets received out of order but inside the replay window when replay protection is enabled on this RX SC. The counter definition does not indicate that replay protection is enabled in RouterOS.</ArgTableRow>
<ArgTableRow arg="rx-sc-ok" typ="multi { counter: num
 }">Aggregate number of secured packets successfully validated on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-invalid" typ="multi { counter: num
 }">Aggregate number of packets that failed Integrity Check Value (ICV) validation on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-late" typ="multi { counter: num
 }">Aggregate number of valid packets received with a packet number lower than the next expected packet number while replay protection is disabled on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-not-valid" typ="multi { counter: num
 }">Aggregate number of packets rejected because their packet number failed the applicable validity or replay-window checks on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-not-using-sa" typ="multi { counter: num
 }">Aggregate number of packets rejected because they referred to an SA that was not in use on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sc-unused-sa" typ="multi { counter: num
 }">Aggregate number of SecTAGged, integrity-only frames (C=0) received on an SA not in use and accepted because validation was not Strict on this RX SC.</ArgTableRow>
<ArgTableRow arg="rx-sa-ok" typ="multi { counter: num
 }">Per-SA slot count of packets successfully validated with this individual RX SA.</ArgTableRow>
<ArgTableRow arg="rx-sa-invalid" typ="multi { counter: num
 }">Per-SA slot count of packets that failed ICV validation for this individual RX SA.</ArgTableRow>
<ArgTableRow arg="rx-sa-not-valid" typ="multi { counter: num
 }">Per-SA slot count of packets that failed packet-number validity checks for this individual RX SA.</ArgTableRow>
<ArgTableRow arg="rx-sa-not-using-sa" typ="multi { counter: num
 }">Per-SA slot count of rejected packets associated with this RX SA while it was not in use.</ArgTableRow>
<ArgTableRow arg="rx-sa-unused-sa" typ="multi { counter: num
 }">Per-SA slot count of SecTAGged, integrity-only frames (C=0) received while this SA was not in use and accepted because validation was not Strict.</ArgTableRow>
<ArgTableRow arg="tx-sa-protected" typ="multi { counter: num
 }">Per-SA slot count of integrity-protected, unencrypted packets transmitted with this individual TX SA.</ArgTableRow>
<ArgTableRow arg="tx-sa-encrypted" typ="multi { counter: num
 }">Per-SA slot count of encrypted, integrity-protected packets transmitted with this individual TX SA.</ArgTableRow>
</ArgTable>
