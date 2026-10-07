# monitor

> RouterOS command reference for /interface/ethernet/monitor.

-----------

## interface/ethernet/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (unknown | link-ok | no-link | initializing | auto-init-failed)"></ArgTableRow>
<ArgTableRow arg="auto-negotiation" typ="enum (incomplete | done | no-negotiation | failed | restarted | disabled | not-supported) { incomplete:0, done:1, no-negotiation:2, failed:3, restarted:4, disabled:5, not-supported:6 }"></ArgTableRow>
<ArgTableRow arg="rate" typ="enum (unknown | 10Mbps | 100Mbps | 1Gbps | 2.5Gbps | 5Gbps | 10Gbps | 25Gbps | 40Gbps | 50Gbps | 100Gbps | 200Gbps | 400Gbps) { unknown:0, 10Mbps:1, 100Mbps:2, 1Gbps:3, 2.5Gbps:4, 5Gbps:5, 10Gbps:6, 25Gbps:7, 40Gbps:8, 50Gbps:9, 100Gbps:10, 200Gbps:11, 400Gbps:12 }"></ArgTableRow>
<ArgTableRow arg="full-duplex" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="fec" typ="enum (off | fec74 | fec91) { off:0, fec74:2, fec91:3 }"></ArgTableRow>
<ArgTableRow arg="supported" typ="multi { array-id }"></ArgTableRow>
<ArgTableRow arg="sfp-supported" typ="multi { array-id }"></ArgTableRow>
<ArgTableRow arg="advertising" typ="multi { array-id }"></ArgTableRow>
<ArgTableRow arg="link-partner-advertising" typ="multi { array-id }"></ArgTableRow>
<ArgTableRow arg="default-cable-setting" typ="enum (short | standard) { short:0, standard:1 }"></ArgTableRow>
<ArgTableRow arg="combo-state" typ="enum (copper | sfp) { copper:1, sfp:2 }"></ArgTableRow>
<ArgTableRow arg="sfp-module-present" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-rx-loss" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-tx-fault" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-type" typ="enum (unknown | SFP/SFP+/SFP28/SFP56 | DWDM-SFP/SFP+ | QSFP | QSFP+ | QSFP28/QSFP56 | QSFPDD | QSFP-CMIS)"></ArgTableRow>
<ArgTableRow arg="sfp-cmis-revision" typ="composite { major: num
, minor: num
 }"></ArgTableRow>
<ArgTableRow arg="sfp-cmis-module-state" typ="enum (low-power | power-up | ready | power-down | fault)"></ArgTableRow>
<ArgTableRow arg="sfp-connector-type" typ="enum (unknown | SC | LC | optical-pigtail | multifiber-parallel-optic-1x12 | multifiber-parallel-optic-1x16 | copper-pigtail | no-separable-connector | RJ45)"></ArgTableRow>
<ArgTableRow arg="sfp-encoding" typ="enum (unspecified | 8B/10B | 4B/5B | nrz | manchester | sonet | 64B/66B | 256B/257B | pam4)"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-sm" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om1" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om2" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om3" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om4" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om5" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-cable-assembly" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-copper-active-om4" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-name" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-part-number" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-revision" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-serial" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-manufacturing-date" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-power-class" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-max-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-wavelength" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-dwdm-channel-spacing" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-supply-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-tx-bias-current" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-rx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="phy-regs" typ="multi { array-id, method: string
 }"></ArgTableRow>
<ArgTableRow arg="eeprom-checksum" typ="enum (bad | good)"></ArgTableRow>
<ArgTableRow arg="eeprom" typ="string"></ArgTableRow>
</ArgTable>
