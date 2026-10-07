# interworking-profiles

> RouterOS directory reference for /interface/wireless/interworking-profiles.

-----------

## interface/wireless/interworking-profiles 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard) { private:0, private-with-guest:1, public-chargeable:2, public-free:3, personal-device:4, emergency-only:5, test:14, wildcard:15 }"></ArgTableRow>
<ArgTableRow arg="internet" typ="bool"></ArgTableRow>
<ArgTableRow arg="asra" typ="bool"></ArgTableRow>
<ArgTableRow arg="esr" typ="bool"></ArgTableRow>
<ArgTableRow arg="uesa" typ="bool"></ArgTableRow>
<ArgTableRow arg="venue" typ="enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="hessid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hotspot20" typ="bool"></ArgTableRow>
<ArgTableRow arg="hotspot20-dgaf" typ="bool"></ArgTableRow>
<ArgTableRow arg="roaming-ois" typ="multi { array-id, roaming-oi: string
 }"></ArgTableRow>
<ArgTableRow arg="venue-names" typ="object { venue-name: composite { venue-name-name: string
, venue-name-lang: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) { terms-and-conditions:0, online-enrollment:1, https-redirection:2, dns-redirection:3 }
, authentication-type-url: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown) { not-available:0, public:1, port-restricted:2, single-nated:3, double-nated:4, port-restricted-single-nated:5, port-restricted-double-nated:6, unknown:7 }"></ArgTableRow>
<ArgTableRow arg="ipv6-availability" typ="enum (not-available | available | unknown) { not-available:0, available:1, unknown:2 }"></ArgTableRow>
<ArgTableRow arg="realms" typ="object { realm: composite { realm-name: string
, realm-authentication: enum (not-specified | eap-sim | eap-tls | eap-aka)
 }
 }"></ArgTableRow>
<ArgTableRow arg="realms-raw" typ="multi { array-id, realm-raw: string
 }"></ArgTableRow>
<ArgTableRow arg="3gpp-raw" typ="string"></ArgTableRow>
<ArgTableRow arg="3gpp-info" typ="object { 3gpp: composite { 3gpp-mcc: string
, 3gpp-mnc: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="multi { array-id, domain-name: string
 }"></ArgTableRow>
<ArgTableRow arg="operator-names" typ="object { operator-name: composite { operator-name-name: string
, operator-name-lang: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="wan-status" typ="enum (reserved | up | down | test) { reserved:0, up:1, down:2, test:3 }"></ArgTableRow>
<ArgTableRow arg="wan-symmetric" typ="bool"></ArgTableRow>
<ArgTableRow arg="wan-at-capacity" typ="bool"></ArgTableRow>
<ArgTableRow arg="wan-downlink" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-uplink" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-downlink-load" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-uplink-load" typ="num"></ArgTableRow>
<ArgTableRow arg="wan-measurement-duration" typ="num"></ArgTableRow>
<ArgTableRow arg="connection-capabilities" typ="object { connection-cap: composite { protocol: num
, connection-cap2: composite { port: num
, status: enum (closed | open | unknown) { closed:0, open:1, unknown:2 }
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="operational-classes" typ="multi { array-id, operational-class: num
 }"></ArgTableRow>
</ArgTable>
