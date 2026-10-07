# configuration

> RouterOS directory reference for /interface/wifi/configuration.

-----------

## interface/wifi/configuration 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="security" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="steering" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="chains" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit ()" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (outdoor | indoor)" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap | station | station-bridge | station-pseudobridge)" unset="1"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="beacon-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="dtim-period" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="multicast-enhance" typ="enum (disabled | enabled) { disabled:0, enabled:1 }" unset="1"></ArgTableRow>
<ArgTableRow arg="qos-classifier" typ="enum (priority | dscp-high-3-bits) { priority:0, dscp-high-3-bits:1 }" unset="1"></ArgTableRow>
<ArgTableRow arg="station-roaming" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="max-clients" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)" unset="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ap)" unset="1"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="max-sta-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="multicast-helper" typ="enum (default | disabled | full | dhcp) { default:0, disabled:1, full:2, dhcp:3 }" unset="1"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="guard-interval" typ="enum (any | long) { any:0, long:1 }" unset="1"></ArgTableRow>
<ArgTableRow arg="country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)" unset="1"></ArgTableRow>
<ArgTableRow arg="load-balancing-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="enum (indoors | dynamic) { indoors:0, dynamic:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-retries" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self) { none:0, rts-cts:1, cts-to-self:2 }" unset="1"></ArgTableRow>
<ArgTableRow arg="hw-protection-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="frame-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="disconnect-timeout" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="keepalive-frames" typ="enum (enabled | disabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.group-encryption" typ="enum (tkip | ccmp | gcmp | ccmp-256 | gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.group-key-update" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="security.passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.multi-passphrase-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="security.disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.management-protection" typ="enum (disabled | allowed | required)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.beacon-protection" typ="enum (disabled | enabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.management-encryption" typ="enum (cmac | gmac | cmac-256 | gmac-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.wps" typ="enum (disable | push-button)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.dh-groups" typ="ubit (19, 20, 21)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.sae-anti-clogging-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="security.sae-max-failure-rate" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="security.sae-pwe" typ="enum (hunting-and-pecking | hash-to-element | both)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.owe-transition-interface" typ="iface_enum { auto }" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-methods" typ="multi { array-id, method: enum (tls | ttls | peap) { tls:13, ttls:21, peap:25 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-certificate-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-tls-certificate" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-username" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-anonymous-identity" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-password" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-mobility-domain" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-over-ds" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-reassociation-deadline" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-nas-identifier" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-r0-key-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="security.ft-preserve-vlanid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.connect-group" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.connect-priority" typ="super { connect-accept-priority: num
, [connect-hold-priority] /num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192)" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.network-type" typ="enum (private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard) { private:0, private-with-guest:1, public-chargeable:2, public-free:3, personal-device:4, emergency-only:5, test:14, wildcard:15 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.internet" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.esr" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.uesa" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.venue" typ="enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.hessid" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.hotspot20" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.hotspot20-dgaf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.roaming-ois" typ="multi { array-id, roaming-oi: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.venue-names" typ="object { venue-name: composite { venue-name-name: string
, venue-name-lang: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.authentication-types" typ="object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) { terms-and-conditions:0, online-enrollment:1, https-redirection:2, dns-redirection:3 }
, authentication-type-url: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.ipv4-availability" typ="enum (not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown) { not-available:0, public:1, port-restricted:2, single-nated:3, double-nated:4, port-restricted-single-nated:5, port-restricted-double-nated:6, unknown:7 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.ipv6-availability" typ="enum (not-available | available | unknown) { not-available:0, available:1, unknown:2 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.realms" typ="object { realm: composite { realm-name: string
, realm-auth: enum (not-specified | eap-sim | eap-tls | eap-aka)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.realms-raw" typ="multi { array-id, realm-raw: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.3gpp-info" typ="object { 3gpp: composite { 3gpp-mcc: string
, 3gpp-mnc: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.3gpp-info-raw" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.domain-names" typ="multi { array-id, domain-name: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.operator-names" typ="object { operator-name: composite { operator-name-name: string
, operator-name-lang: string
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-status" typ="enum (reserved | up | down | test) { reserved:0, up:1, down:2, test:3 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-symmetric" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-at-capacity" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-downlink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-uplink" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-downlink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-uplink-load" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.wan-measurement-duration" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.connection-capabilities" typ="object { connection-cap: composite { protocol: num
, connection-cap2: composite { port: num
, status: enum (closed | open | unknown) { closed:0, open:1, unknown:2 }
 }
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="interworking.operational-classes" typ="multi { array-id, operational-class: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.bridge" typ="iface_enum { none }" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.openflow-switch" typ="enum" unset="1" syscap="openflow"></ArgTableRow>
<ArgTableRow arg="datapath.client-isolation" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.traffic-processing" typ="enum (on-cap | on-capsman | on-capsman-secure)" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath.interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.frequency" typ="object" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.band" typ="enum (60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be)" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.width" typ="enum (20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz)" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.skip-dfs-channels" typ="enum (disabled | all | 10min-cac)" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.deprioritize-unii-3-4" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.reselect-time" typ="super { reselect-time-min: date
, [reselect-time-max] ..date
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.preamble-puncturing" typ="alt { preamble-puncturing: enum (yes | no) { yes:-1, no:0 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.afc" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.username-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.password-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.called-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.calling-format" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.mac-caching" typ="alt { mac-caching-disable: enum (disabled) { disabled:0 }
, mac-caching-time: time
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.interim-update" typ="alt { interim-update-disable: enum (disabled) { disabled:0 }
, interim-update-time: time [1 .. ]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="aaa.nas-identifier" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.neighbor-group" typ="multi { array-id, neighbor-group: string
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.rrm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.wnm" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.2g-probe-delay" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.transition-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.transition-threshold-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.transition-request-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.transition-request-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="steering.transition-time" typ="alt { value: enum (unlimited | immediate) { unlimited:-1, immediate:0 }
, time: time
 }" unset="1"></ArgTableRow>
</ArgTable>
