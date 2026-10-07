# security-profiles

> RouterOS directory reference for /interface/wireless/security-profiles.

-----------

## interface/wireless/security-profiles 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (none | static-keys-optional | static-keys-required | dynamic-keys) { none:0, static-keys-optional:1, static-keys-required:2, dynamic-keys:3 }"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)"></ArgTableRow>
<ArgTableRow arg="unicast-ciphers" typ="ubit (tkip, aes-ccm)"></ArgTableRow>
<ArgTableRow arg="group-ciphers" typ="ubit (tkip, aes-ccm)"></ArgTableRow>
<ArgTableRow arg="wpa-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="wpa2-pre-shared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="supplicant-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, method: enum (eap-tls | eap-ttls-mschapv2 | peap | passthrough) { eap-tls:13, eap-ttls-mschapv2:21, peap:25, passthrough:0xffffffff }
 }"></ArgTableRow>
<ArgTableRow arg="tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl) { verify-certificate:0, dont-verify-certificate:1, no-certificates:2 }"></ArgTableRow>
<ArgTableRow arg="tls-certificate" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="mschapv2-username" typ="string"></ArgTableRow>
<ArgTableRow arg="mschapv2-password" typ="string"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool"></ArgTableRow>
<ArgTableRow arg="static-algo-0" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-0" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-1" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-1" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-2" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-2" typ="string"></ArgTableRow>
<ArgTableRow arg="static-algo-3" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-key-3" typ="string"></ArgTableRow>
<ArgTableRow arg="static-transmit-key" typ="enum (key-0 | key-1 | key-2 | key-3) { key-0:0, key-1:1, key-2:2, key-3:3 }"></ArgTableRow>
<ArgTableRow arg="static-sta-private-algo" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="static-sta-private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="radius-mac-authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-mac-accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-eap-accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX | xx:xx:xx:xx:xx:xx | xxxx:xxxx:xxxx | xxxxxx:xxxxxx | xx-xx-xx-xx-xx-xx | xxxxxx-xxxxxx | xxxxxxxxxxxx | xx xx xx xx xx xx) { XX:XX:XX:XX:XX:XX:0, XXXX:XXXX:XXXX:1, XXXXXX:XXXXXX:2, XX-XX-XX-XX-XX-XX:3, XXXXXX-XXXXXX:4, XXXXXXXXXXXX:5, XX XX XX XX XX XX:6, xx:xx:xx:xx:xx:xx:7, xxxx:xxxx:xxxx:8, xxxxxx:xxxxxx:9, xx-xx-xx-xx-xx-xx:10, xxxxxx-xxxxxx:11, xxxxxxxxxxxx:12, xx xx xx xx xx xx:13 }"></ArgTableRow>
<ArgTableRow arg="radius-mac-mode" typ="enum (as-username | as-username-and-password) { as-username:0, as-username-and-password:1 }"></ArgTableRow>
<ArgTableRow arg="radius-called-format" typ="enum (mac:ssid | mac | ssid)"></ArgTableRow>
<ArgTableRow arg="radius-mac-caching" typ="alt { radius-mac-caching-disable: enum (disabled) { disabled:0 }
, radius-mac-caching-time: time
 }"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="enum (allowed | required | disabled) { allowed:0, required:1, disabled:2 }"></ArgTableRow>
<ArgTableRow arg="management-protection-key" typ="string"></ArgTableRow>
</ArgTable>
