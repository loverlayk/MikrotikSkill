# wifi

> A WiFi network definition replicated to the selected devices. The arguments extend the standard RouterOS /interface/wifi configuration parameters.

-----------

## cmr/wifi 
**Package:** cmr
**Type:** Directory

A WiFi network definition replicated to the selected devices. The arguments extend the standard RouterOS `/interface/wifi` configuration parameters.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">WiFi network is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices the WiFi network is replicated to using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1">VLAN ID applied to the network: none (default) or 1-4095.</ArgTableRow>
<ArgTableRow arg="mlo" typ="bool" unset="1">Enable MLO (Multi-Link Operation).</ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1">Network SSID.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap | station | station-bridge | station-pseudobridge)" unset="1">Network operating mode.</ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1">Hide the SSID in beacon frames.</ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="time" unset="1">Beacon interval.</ArgTableRow>
<ArgTableRow arg="dtim-period" typ="num" unset="1">DTIM period.</ArgTableRow>
<ArgTableRow arg="multicast-enhance" typ="enum (disabled | enabled) { disabled:0, enabled:1 }" unset="1">Multicast enhancement: `disabled` or `enabled`.</ArgTableRow>
<ArgTableRow arg="qos-classifier" typ="enum (priority | dscp-high-3-bits) { priority:0, dscp-high-3-bits:1 }" unset="1">QoS classifier: `priority` or `dscp-high-3-bits`.</ArgTableRow>
<ArgTableRow arg="station-roaming" typ="bool" unset="1">Enable station roaming.</ArgTableRow>
<ArgTableRow arg="max-clients" typ="num" unset="1">Maximum number of connected clients.</ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)" unset="1">Hardware protection mode: `none`, `rts-cts`, `cts-to-self`.</ArgTableRow>
<ArgTableRow arg="security.encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1">Allowed encryption ciphers.</ArgTableRow>
<ArgTableRow arg="security.group-encryption" typ="enum (tkip | ccmp | gcmp | ccmp-256 | gcmp-256)" unset="1">Group encryption cipher.</ArgTableRow>
<ArgTableRow arg="security.group-key-update" typ="time" unset="1">Group key update interval.</ArgTableRow>
<ArgTableRow arg="security.passphrase" typ="string" unset="1">Network passphrase.</ArgTableRow>
<ArgTableRow arg="security.multi-passphrase-group" typ="enum" unset="1">Multi-passphrase group.</ArgTableRow>
<ArgTableRow arg="security.disable-pmkid" typ="bool" unset="1">Disable PMKID.</ArgTableRow>
<ArgTableRow arg="security.management-protection" typ="enum (disabled | allowed | required)" unset="1">Management frame protection: `disabled`, `allowed`, `required`.</ArgTableRow>
<ArgTableRow arg="security.beacon-protection" typ="enum (disabled | enabled)" unset="1">Beacon protection: `disabled` or `enabled`.</ArgTableRow>
<ArgTableRow arg="security.management-encryption" typ="enum (cmac | gmac | cmac-256 | gmac-256)" unset="1">Management frame encryption cipher.</ArgTableRow>
<ArgTableRow arg="security.wps" typ="enum (disable | push-button)" unset="1">WPS mode: `disable` or `push-button`.</ArgTableRow>
<ArgTableRow arg="security.dh-groups" typ="ubit (19, 20, 21)" unset="1">SAE Diffie-Hellman groups.</ArgTableRow>
<ArgTableRow arg="security.sae-anti-clogging-threshold" typ="num" unset="1">SAE anti-clogging threshold.</ArgTableRow>
<ArgTableRow arg="security.sae-max-failure-rate" typ="num" unset="1">SAE maximum failure rate.</ArgTableRow>
<ArgTableRow arg="security.sae-pwe" typ="enum (hunting-and-pecking | hash-to-element | both)" unset="1">SAE PWE derivation: `hunting-and-pecking`, `hash-to-element`, `both`.</ArgTableRow>
<ArgTableRow arg="security.owe-transition-interface" typ="iface_enum { auto }" unset="1">OWE transition interface.</ArgTableRow>
<ArgTableRow arg="security.eap-methods" typ="multi { array-id, method: enum (tls | ttls | peap) { tls:13, ttls:21, peap:25 }
 }" unset="1">Allowed EAP methods.</ArgTableRow>
<ArgTableRow arg="security.eap-certificate-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)" unset="1">EAP certificate verification mode.</ArgTableRow>
<ArgTableRow arg="security.eap-tls-certificate" typ="enum" unset="1">EAP-TLS certificate.</ArgTableRow>
<ArgTableRow arg="security.eap-username" typ="string" unset="1">EAP username.</ArgTableRow>
<ArgTableRow arg="security.eap-anonymous-identity" typ="string" unset="1">EAP anonymous identity.</ArgTableRow>
<ArgTableRow arg="security.eap-password" typ="string" unset="1">EAP password.</ArgTableRow>
<ArgTableRow arg="security.eap-accounting" typ="bool" unset="1">Enable EAP accounting.</ArgTableRow>
<ArgTableRow arg="security.ft" typ="bool" unset="1">Enable Fast Transition (802.11r).</ArgTableRow>
<ArgTableRow arg="security.ft-mobility-domain" typ="num" unset="1">FT mobility domain.</ArgTableRow>
<ArgTableRow arg="security.ft-over-ds" typ="bool" unset="1">FT over the distribution system.</ArgTableRow>
<ArgTableRow arg="security.ft-reassociation-deadline" typ="time" unset="1">FT reassociation deadline.</ArgTableRow>
<ArgTableRow arg="security.ft-nas-identifier" typ="string" unset="1">FT NAS identifier.</ArgTableRow>
<ArgTableRow arg="security.ft-r0-key-lifetime" typ="time" unset="1">FT R0 key lifetime.</ArgTableRow>
<ArgTableRow arg="security.ft-preserve-vlanid" typ="bool" unset="1">FT preserve VLAN ID.</ArgTableRow>
<ArgTableRow arg="security.connect-group" typ="string" unset="1">Connect group.</ArgTableRow>
<ArgTableRow arg="security.connect-priority" typ="super { connect-accept-priority: num
, [connect-hold-priority] /num
 }" unset="1">Connect priority.</ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1">Supported authentication types.</ArgTableRow>
</ArgTable>
