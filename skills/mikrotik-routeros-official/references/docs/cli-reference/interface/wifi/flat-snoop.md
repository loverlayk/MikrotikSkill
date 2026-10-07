# flat-snoop

> RouterOS command reference for /interface/wifi/flat-snoop.

-----------

## interface/wifi/flat-snoop 
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="M" typ="mikrotik-oui"></ArgTableRow>
<ArgTableRow arg="L" typ="locally-administered-address"></ArgTableRow>
<ArgTableRow arg="B" typ="multicast-address"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="filter-type" typ="ubit (frequency, bsss, stas)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (freq | bss | sta)"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="bss-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="basic-rates-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="supported-rates-mbps" typ="string"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="snr" typ="num"></ArgTableRow>
<ArgTableRow arg="noise" typ="num"></ArgTableRow>
<ArgTableRow arg="seen-frame-count" typ="num"></ArgTableRow>
<ArgTableRow arg="beacon-size" typ="num"></ArgTableRow>
<ArgTableRow arg="first-beacon" typ="date"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
<ArgTableRow arg="country" typ="string"></ArgTableRow>
<ArgTableRow arg="erp-info" typ="ubit (non-erp-present, use-protection, barker-preamble-mode)"></ArgTableRow>
<ArgTableRow arg="rsn-capab" typ="ubit (preauth, no-pairwise, ptksa-rcntr-0, ptksa-rcntr-1, gtksa-rcntr-0, gtksa-rcntr-1, mfpr, mfpc, joint-multiband-assoc, peerkey, spp-amsdu-c, spp-amsdu-req, pbac, ext-keyid-unicast-frames, ocvc)"></ArgTableRow>
<ArgTableRow arg="group-data-cipher" typ="enum (use-gcs | group-traffic-disallowed | wep40 | tkip | ccmp | wep104 | aes-cmac | gcmp | gcmp-256 | ccmp-256 | bip-gmac_128 | bip-gmac_256 | bip-cmac_256)"></ArgTableRow>
<ArgTableRow arg="group-mgmt-cipher" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="pairwise-ciphers" typ="multi { array-id, cipher: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="rsn-akms" typ="multi { array-id, akm: enum (802.1x | psk | ft-802.1x | ft-psk | 802.1x-256 | psk-sha256 | tdls | sae | sae | ft-sae | ft-sae | ap-peerkey | 802.1x-b-256 | 802.1x-b-192 | ft-802.1x-sha384 | fils-sha256 | fils-sha384 | ft-fils-sha256 | ft-fils-sha384 | owe | ft-psk-sha384 | psk-sha384) { 802.1x:0xfac01, psk:0xfac02, ft-802.1x:0xfac03, ft-psk:0xfac04, 802.1x-256:0xfac05, psk-sha256:0xfac06, tdls:0xfac07, sae:0xfac08, sae:0xfac18, ft-sae:0xfac09, ft-sae:0xfac19, ap-peerkey:0xfac0a, 802.1x-b-256:0xfac0b, 802.1x-b-192:0xfac0c, ft-802.1x-sha384:0xfac0d, fils-sha256:0xfac0e, fils-sha384:0xfac0f, ft-fils-sha256:0xfac10, ft-fils-sha384:0xfac11, owe:0xfac12, ft-psk-sha384:0xfac13, psk-sha384:0xfac14 }
 }"></ArgTableRow>
<ArgTableRow arg="pmkids" typ="multi { array-id, pmkid: string
 }"></ArgTableRow>
<ArgTableRow arg="rsn" typ="string"></ArgTableRow>
<ArgTableRow arg="bss-on-time" typ="time"></ArgTableRow>
<ArgTableRow arg="sta-count" typ="num"></ArgTableRow>
<ArgTableRow arg="bss-count" typ="num"></ArgTableRow>
</ArgTable>
