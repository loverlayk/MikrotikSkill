# security

> RouterOS directory reference for /interface/wifi/security.

-----------

## interface/wifi/security 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1"></ArgTableRow>
<ArgTableRow arg="encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-encryption" typ="enum (tkip | ccmp | gcmp | ccmp-256 | gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="group-key-update" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="multi-passphrase-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="management-protection" typ="enum (disabled | allowed | required)" unset="1"></ArgTableRow>
<ArgTableRow arg="beacon-protection" typ="enum (disabled | enabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="management-encryption" typ="enum (cmac | gmac | cmac-256 | gmac-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="wps" typ="enum (disable | push-button)" unset="1"></ArgTableRow>
<ArgTableRow arg="dh-groups" typ="ubit (19, 20, 21)" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-anti-clogging-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-max-failure-rate" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="sae-pwe" typ="enum (hunting-and-pecking | hash-to-element | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="owe-transition-interface" typ="iface_enum { auto }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-methods" typ="multi { array-id, method: enum (tls | ttls | peap) { tls:13, ttls:21, peap:25 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-certificate-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-tls-certificate" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-username" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-anonymous-identity" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-password" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="eap-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-mobility-domain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-over-ds" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-reassociation-deadline" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-nas-identifier" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-r0-key-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="ft-preserve-vlanid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="connect-group" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="connect-priority" typ="super { connect-accept-priority: num
, [connect-hold-priority] /num
 }" unset="1"></ArgTableRow>
</ArgTable>
