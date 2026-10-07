# interface

> RouterOS directory reference for /caps-man/interface.

-----------

## caps-man/interface 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="M" typ="master"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="B" typ="bound"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="radio-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum { none }"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="security" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="datapath" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rates" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.mode" typ="enum (ap)" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.hide-ssid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.max-sta-count" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.multicast-helper" typ="enum (default | disabled | full | dhcp) { default:0, disabled:1, full:2, dhcp:3 }" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.tx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.rx-chains" typ="ubit (0, 1, 2, 3)" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.guard-interval" typ="enum (any | long) { any:0, long:1 }" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.country" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.installation" typ="enum (any | indoor | outdoor)" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.load-balancing-group" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.distance" typ="enum (indoors | dynamic) { indoors:0, dynamic:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.hw-retries" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.hw-protection-mode" typ="enum (none | rts-cts | cts-to-self) { none:0, rts-cts:1, cts-to-self:2 }" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.hw-protection-threshold" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.frame-lifetime" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.disconnect-timeout" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="configuration.keepalive-frames" typ="enum (enabled | disabled)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.encryption" typ="ubit (aes-ccm, tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.group-encryption" typ="enum (aes-ccm | tkip)" unset="1"></ArgTableRow>
<ArgTableRow arg="security.group-key-update" typ="time"></ArgTableRow>
<ArgTableRow arg="security.passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-methods" typ="multi { array-id, method: enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="security.eap-radius-accounting" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="security.tls-mode" typ="enum (verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)"></ArgTableRow>
<ArgTableRow arg="security.tls-certificate" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="security.disable-pmkid" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="client-to-client-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="openflow-switch" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="local-forwarding" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)" unset="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.frequency" typ="multi { array-id, frequency: num
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.secondary-frequency" typ="multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled)
, secondary-frequency-num: num
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.control-channel-width" typ="enum (5mhz | 10mhz | 20mhz | 40mhz-turbo) { 5mhz:5000, 10mhz:10000, 20mhz:20000, 40mhz-turbo:40000 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX)" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.tx-power" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.save-selected" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.reselect-interval" typ="super { reselect-interval-min: time [1 .. 60*60*24*300]
, [reselect-interval-max] ..time [1 .. 60*60*24*300]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="channel.skip-dfs-channels" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.basic" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.supported" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps, 6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23)" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.vht-basic-mcs" typ="multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rates.vht-supported-mcs" typ="multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-state" typ="string"></ArgTableRow>
<ArgTableRow arg="current-channel" typ="string"></ArgTableRow>
<ArgTableRow arg="current-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="current-basic-rate-set" typ="string"></ArgTableRow>
<ArgTableRow arg="current-registered-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="current-authorized-clients" typ="num"></ArgTableRow>
</ArgTable>
