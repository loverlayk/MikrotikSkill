# connect-list

> RouterOS directory reference for /interface/wireless/connect-list.

-----------

## interface/wireless/connect-list 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="connect" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="signal-range" typ="composite { min: num [-120 .. 120]
, max: num [-120 .. 120]
 }"></ArgTableRow>
<ArgTableRow arg="allow-signal-out-of-range" typ="alt { signal-out-of-range-always: enum (always) { always:0 }
, signal-out-of-range-time: time
 }"></ArgTableRow>
<ArgTableRow arg="area-prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="security-profile" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (any | 802.11 | nstreme | tdma) { any:0, 802.11:1, nstreme:2, tdma:3 }"></ArgTableRow>
<ArgTableRow arg="interworking" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard)"></ArgTableRow>
<ArgTableRow arg="iw-venue" typ="enum (any | assembly | business | educational | industrial | institutional | mercantile | residential | storage | utility | vehicular | outdoor) { any:0xffffffff, assembly:0x0001ffff, business:0x0002ffff, educational:0x0003ffff, industrial:0x0004ffff, institutional:0x0005ffff, mercantile:0x0006ffff, residential:0x0007ffff, storage:0x0008ffff, utility:0x0009ffff, vehicular:0x000affff, outdoor:0x000bffff }"></ArgTableRow>
<ArgTableRow arg="iw-hessid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="iw-internet" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-asra" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-esr" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-uesa" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-hotspot20" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-hotspot20-dgaf" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="iw-roaming-ois" typ="multi { array-id, iw-roaming-oi: string
 }"></ArgTableRow>
<ArgTableRow arg="iw-authentication-types" typ="object { iw-authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) { terms-and-conditions:0, online-enrollment:1, https-redirection:2, dns-redirection:3 }
 }"></ArgTableRow>
<ArgTableRow arg="iw-ipv4-availability" typ="enum (any | not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown) { any:0xffffffff, not-available:0, public:1, port-restricted:2, single-nated:3, double-nated:4, port-restricted-single-nated:5, port-restricted-double-nated:6, unknown:7 }"></ArgTableRow>
<ArgTableRow arg="iw-ipv6-availability" typ="enum (any | not-available | available | unknown) { any:0xffffffff, not-available:0, available:1, unknown:2 }"></ArgTableRow>
<ArgTableRow arg="iw-realms" typ="object { realm: composite { iw-realm-name: string
, iw-realm-authentication: enum (not-specified | eap-sim | eap-tls | eap-aka)
 }
 }"></ArgTableRow>
<ArgTableRow arg="3gpp" typ="string"></ArgTableRow>
<ArgTableRow arg="iw-connection-capabilities" typ="object { iw-connection-cap: composite { protocol: num
, port: num
 }
 }"></ArgTableRow>
</ArgTable>
