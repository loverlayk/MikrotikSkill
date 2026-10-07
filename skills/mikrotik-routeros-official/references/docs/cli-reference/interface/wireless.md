# wireless

> RouterOS directory reference for /interface/wireless.

-----------

## interface/wireless 
**Package:** wireless-rep
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="prism-cardtype" typ="enum (200mW | 100mW | 30mW) { 200mW:0, 100mW:1, 30mW:2 }"></ArgTableRow>
<ArgTableRow arg="master-interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (station | station-wds | ap-bridge | bridge | alignment-only | nstreme-dual-slave | wds-slave | station-pseudobridge | station-pseudobridge-clone | station-bridge) { station:0, station-wds:6, ap-bridge:1, bridge:2, alignment-only:3, nstreme-dual-slave:4, wds-slave:5, station-pseudobridge:8, station-pseudobridge-clone:9 }"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="area" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency-mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="country" typ="enum"></ArgTableRow>
<ArgTableRow arg="installation" typ="enum (any | indoor | outdoor)"></ArgTableRow>
<ArgTableRow arg="antenna-gain" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency" typ="alt { frequency-mhz: num
, frequency-name: enum (auto) { auto:0 }
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)"></ArgTableRow>
<ArgTableRow arg="channel-width" typ="enum (20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC | 20/40/80/160mhz-Ceeeeeee | 20/40/80/160mhz-eCeeeeee | 20/40/80/160mhz-eeCeeeee | 20/40/80/160mhz-eeeCeeee | 20/40/80/160mhz-eeeeCeee | 20/40/80/160mhz-eeeeeCee | 20/40/80/160mhz-eeeeeeCe | 20/40/80/160mhz-eeeeeeeC | 20/40mhz-XX | 20/40/80mhz-XXXX | 20/40/80/160mhz-XXXXXXXX)"></ArgTableRow>
<ArgTableRow arg="secondary-frequency" typ="multi { array-id, secondary-channel: enum (auto) { auto:0xffffffff }
 }"></ArgTableRow>
<ArgTableRow arg="scan-list" typ="object { entry: alt { default: enum (default) { default:0 }
, range: super { range-start: num
, [range-end] -num
, [range-step] [ :num]
 }
, name: enum ()
 }
 }"></ArgTableRow>
<ArgTableRow arg="wireless-protocol" typ="enum (unspecified | any | 802.11 | nstreme | nv2 | nv2-nstreme-802.11 | nv2-nstreme) { unspecified:0, any:1, 802.11:2, nstreme:3, nv2:4, nv2-nstreme-802.11:5, nv2-nstreme:6 }"></ArgTableRow>
<ArgTableRow arg="rate-set" typ="enum (default | configured) { default:0, configured:1 }"></ArgTableRow>
<ArgTableRow arg="supported-rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="supported-rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="basic-rates-b" typ="ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps)"></ArgTableRow>
<ArgTableRow arg="basic-rates-a/g" typ="ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps)"></ArgTableRow>
<ArgTableRow arg="max-station-count" typ="num"></ArgTableRow>
<ArgTableRow arg="distance" typ="enum (indoors | dynamic) { indoors:0, dynamic:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-power-mode" typ="enum (default | all-rates-fixed | card-rates | manual-table) { default:0, all-rates-fixed:1, card-rates:2, manual-table:3 }"></ArgTableRow>
<ArgTableRow arg="noise-floor-threshold" typ="alt { default: enum (default) { default:5555 }
, threshold: num [-128 .. 127]
 }"></ArgTableRow>
<ArgTableRow arg="nv2-noise-floor-offset" typ="alt { default: enum (default) { default:5555 }
, threshold: num [0 .. 20]
 }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="enum (disabled) { disabled:0 }"></ArgTableRow>
<ArgTableRow arg="dfs-test-mode" typ="ubit (only-detect, duty-cycle, short-search)" syscap="dfstest"></ArgTableRow>
<ArgTableRow arg="antenna-mode" typ="enum (ant-a | ant-b | txa-rxb | rxa-txb) { ant-a:1, ant-b:2, txa-rxb:3, rxa-txb:4 }"></ArgTableRow>
<ArgTableRow arg="vlan-mode" typ="enum (no-tag | use-tag | use-service-tag)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-mode" typ="enum (disabled | static | dynamic | static-mesh | dynamic-mesh) { disabled:0, static:1, dynamic:2, static-mesh:3, dynamic-mesh:4 }"></ArgTableRow>
<ArgTableRow arg="wds-default-bridge" typ="iface_enum { none:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="wds-default-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="wds-cost-range" typ="range"></ArgTableRow>
<ArgTableRow arg="wds-ignore-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="update-stats-interval" typ="alt { disabled: enum (disabled) { disabled:0 }
, interval: time [10 .. 18000]
 }"></ArgTableRow>
<ArgTableRow arg="bridge-mode" typ="enum (enabled | disabled)"></ArgTableRow>
<ArgTableRow arg="default-authentication" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-forwarding" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-ap-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="default-client-tx-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="wmm-support" typ="enum (disabled | enabled | required) { disabled:0, enabled:1, required:2 }"></ArgTableRow>
<ArgTableRow arg="hide-ssid" typ="bool"></ArgTableRow>
<ArgTableRow arg="security-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="interworking-profile" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="wps-mode" typ="enum (disabled | push-button | push-button-virtual-only | push-button-5s)"></ArgTableRow>
<ArgTableRow arg="station-roaming" typ="enum (disabled | enabled)"></ArgTableRow>
<ArgTableRow arg="disconnect-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="on-fail-retry-time" typ="time"></ArgTableRow>
<ArgTableRow arg="preamble-mode" typ="enum (long | short | both) { long:0, short:1, both:2 }"></ArgTableRow>
<ArgTableRow arg="compression" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-sharedkey" typ="bool"></ArgTableRow>
<ArgTableRow arg="station-bridge-clone-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ampdu-priorities" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)"></ArgTableRow>
<ArgTableRow arg="guard-interval" typ="enum (any | long) { any:0, long:1 }"></ArgTableRow>
<ArgTableRow arg="ht-supported-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31)"></ArgTableRow>
<ArgTableRow arg="ht-basic-mcs" typ="ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31)"></ArgTableRow>
<ArgTableRow arg="vht-supported-mcs" typ="multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }"></ArgTableRow>
<ArgTableRow arg="vht-basic-mcs" typ="multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) { none:0, mcs0-7:1, mcs0-8:2, mcs0-9:3 }
 }"></ArgTableRow>
<ArgTableRow arg="tx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="rx-chains" typ="ubit (0, 1, 2, 3)"></ArgTableRow>
<ArgTableRow arg="amsdu-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="amsdu-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="tdma-period-size" typ="enum (auto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10) { auto:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10 }"></ArgTableRow>
<ArgTableRow arg="nv2-queue-count" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-qos" typ="enum (default | frame-priority) { default:0, frame-priority:1 }"></ArgTableRow>
<ArgTableRow arg="nv2-cell-radius" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-security" typ="enum (disabled | enabled) { disabled:0, enabled:1 }"></ArgTableRow>
<ArgTableRow arg="nv2-preshared-key" typ="string"></ArgTableRow>
<ArgTableRow arg="nv2-mode" typ="enum (dynamic-downlink | fixed-downlink | sync-master | sync-slave)"></ArgTableRow>
<ArgTableRow arg="nv2-downlink-ratio" typ="num"></ArgTableRow>
<ArgTableRow arg="nv2-sync-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="hw-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="frame-lifetime" typ="num"></ArgTableRow>
<ArgTableRow arg="adaptive-noise-immunity" typ="enum (none | client-mode | ap-and-client-mode) { none:0, client-mode:1, ap-and-client-mode:2 }"></ArgTableRow>
<ArgTableRow arg="hw-fragmentation-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self) { none:0, rts-cts:1, cts-to-self:2 }"></ArgTableRow>
<ArgTableRow arg="hw-protection-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-selection" typ="enum (advanced) { advanced:1 }"></ArgTableRow>
<ArgTableRow arg="multicast-helper" typ="enum (default | disabled | full | dhcp) { default:0, disabled:1, full:2, dhcp:3 }"></ArgTableRow>
<ArgTableRow arg="multicast-buffering" typ="enum (enabled | disabled)"></ArgTableRow>
<ArgTableRow arg="keepalive-frames" typ="enum (enabled | disabled)"></ArgTableRow>
<ArgTableRow arg="skip-dfs-channels" typ="enum (disabled | all | 10min-cac)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface-type" typ="enum (virtual | Atheros AR5212 | Atheros AR5211 | Atheros AR5210 | Prism | Atheros AR5213 | Atheros AR5413 | Atheros 11N | Atheros AR9271 | Atheros AR9300 | Atheros AR92xx | Atheros AR9888 | IPQ4019 | QCA9984 | QCA9888) { virtual:0, Atheros AR5212:1, Atheros AR5211:2, Atheros AR5210:3, Prism:4, Atheros AR5213:5, Atheros AR5413:6, Atheros 11N:7, Atheros AR9271:8, Atheros AR9300:9, Atheros AR92xx:10, Atheros AR9888:11, IPQ4019:12, QCA9984:13, QCA9888:14 }"></ArgTableRow>
<ArgTableRow arg="pci-info" typ="string"></ArgTableRow>
</ArgTable>
