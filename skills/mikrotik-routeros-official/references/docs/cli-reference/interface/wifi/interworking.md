# interworking

> RouterOS directory reference for /interface/wifi/interworking.

-----------

## interface/wifi/interworking 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard) { private:0, private-with-guest:1, public-chargeable:2, public-free:3, personal-device:4, emergency-only:5, test:14, wildcard:15 }" unset="1"></ArgTableRow>
<ArgTableRow arg="internet" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="esr" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="uesa" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="venue" typ="enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="hessid" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="hotspot20" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="hotspot20-dgaf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="roaming-ois" typ="multi { array-id, roaming-oi: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="venue-names" typ="object { venue-name: composite { venue-name-name: string
, venue-name-lang: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) { terms-and-conditions:0, online-enrollment:1, https-redirection:2, dns-redirection:3 }
, authentication-type-url: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown) { not-available:0, public:1, port-restricted:2, single-nated:3, double-nated:4, port-restricted-single-nated:5, port-restricted-double-nated:6, unknown:7 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ipv6-availability" typ="enum (not-available | available | unknown) { not-available:0, available:1, unknown:2 }" unset="1"></ArgTableRow>
<ArgTableRow arg="realms" typ="object { realm: composite { realm-name: string
, realm-auth: enum (not-specified | eap-sim | eap-tls | eap-aka)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="realms-raw" typ="multi { array-id, realm-raw: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="3gpp-info" typ="object { 3gpp: composite { 3gpp-mcc: string
, 3gpp-mnc: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="3gpp-info-raw" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="domain-names" typ="multi { array-id, domain-name: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="operator-names" typ="object { operator-name: composite { operator-name-name: string
, operator-name-lang: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-status" typ="enum (reserved | up | down | test) { reserved:0, up:1, down:2, test:3 }" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-symmetric" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-at-capacity" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-downlink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-uplink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-downlink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-uplink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="wan-measurement-duration" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="connection-capabilities" typ="object { connection-cap: composite { protocol: num
, connection-cap2: composite { port: num
, status: enum (closed | open | unknown) { closed:0, open:1, unknown:2 }
 }
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="operational-classes" typ="multi { array-id, operational-class: num
 }" unset="1"></ArgTableRow>
</ArgTable>
