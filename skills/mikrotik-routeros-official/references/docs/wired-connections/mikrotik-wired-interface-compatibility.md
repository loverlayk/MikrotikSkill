# MikroTik wired interface compatibility

> This article shows the compatibility of MikroTik devices with SFP, SFP+, SFP28, QSFP+, QSFP28 and QSFP56-DD transceivers. It features detailed compatibility tables that provide valuable insights into which...

# MikroTik wired interface compatibility

## MikroTik SFP/SFP+/SFP28/QSFP+/QSFP28/QSFP56-DD compatibility

This article shows the compatibility of MikroTik devices with SFP, SFP+, SFP28, QSFP+, QSFP28 and QSFP56-DD transceivers. It features detailed compatibility tables that provide valuable insights into which transceivers are suitable for use with MikroTik devices. Additionally, some practical configuration examples are provided using the RouterOS CLI to set different data transmission rates. For more detailed descriptions of properties, please refer to the [Ethernet](./ethernet.md) user manual.

:::info
MikroTik devices and SFP, SFP+, SFP28, QSFP+, QSFP28 and QSFP56-DD modules do not have any restrictions for other vendor equipment.

While MikroTik cannot ensure full compatibility with modules from all manufacturers, as long as the other vendor modules and devices comply with the transceiver multi-source agreement (MSA) they should be compatible with MikroTik.

**Warning:** RouterOS uses a disabled **FEC** mode as the default setting for SFP28 and QSFP28 interfaces. To ensure a successful link with other vendor devices, you may need to enable FEC mode by configuring it to either `fec74` or `fec91`. For more information please refer to the [Ethernet](./ethernet.md) user manual.
:::

### 1G SFP

<WideTable>

|  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Model** | **[S-RJ01](https://mikrotik.com/product/S-RJ01)** | **[S-85DLC05D](https://mikrotik.com/product/S-85DLC05D-180)** | **[S-31DLC20D](https://mikrotik.com/product/S-31DLC20D-181)** | **[S-3553LC20D](https://mikrotik.com/product/S-3553LC20D)** | **[S-55DLC80D](https://mikrotik.com/product/s_55dlc80d)** | **[S-4554LC80D](https://mikrotik.com/product/s_4554lc80d)** | **[SFP CWDM](https://i.mt.lv/cdn/product_files/splitter_modules_180841.pdf)** | **SFP [1m](https://mikrotik.com/product/SplusDA0001)/[3m](https://mikrotik.com/product/SplusDA0003) DAC** | **[S+AO0005](https://mikrotik.com/product/s_ao0005) AOC** | **SFP28 [1m](https://mikrotik.com/product/xs_da0001)/[3m](https://mikrotik.com/product/xs_da0003) DAC** |
| CCR1072-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1036-12G-4S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1016-12S-1S+ | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1009-8G-1S-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2004-1G-2XS-PCIe | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |
| CCR2004-1G-12S+2XS | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2004-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2116-12G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS125-24G-1S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS305-1G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS309-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS312-4C+8XG | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS318-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS320-8P-8B-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS418-8P-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS317-1G-16S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS328-4C-20S-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS328-24P-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS226-24G-2S+ | **-** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+** | **+** | **+** | **+** |
| CRS212-1G-10S-1S+ | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+ 1** | **+** | **+** | **+** | **+** |
| CRS210-8G-2S+ | **-** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+ 2** | **+** | **+** | **+** | **+** |
| CRS112-8G/P-4S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS109-8G-1S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS106-1C-5S/FiberBox | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB5009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB3011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB2011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| L009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| RB260/CSS106 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB922/921 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB953GS | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hAP AC | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hAP ax S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| hEX PoE/PowerBox Pro | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hEX S | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| hEX S (2025) | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| RBFTC11 | **+** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** |
| FTC11XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| FTC21 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| LHG XL 52 ac | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| L22/mANTBox ax 15s L23/NetMetal ax | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 14** | **+ 14** | **+ 14** |
| GPEN21 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS610 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |

</WideTable>

### 10G SFP+/25G SFP28

<WideTable>

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Model** | **[S+RJ10](https://mikrotik.com/product/s_rj10)** | **[S+85DLC03D](https://mikrotik.com/product/Splus85DLC03D)** | **[S+31DLC10D](https://mikrotik.com/product/s_31dlc10d)** | **[S+2332LC10D](https://mikrotik.com/product/Splus2332LC10D)** | **[SFP+ CWDM](https://i.mt.lv/cdn/product_files/splitter_modules_180841.pdf)** | **SFP+ [1m](https://mikrotik.com/product/SplusDA0001)/[3m](https://mikrotik.com/product/SplusDA0003) DAC** | **[S+AO0005](https://mikrotik.com/product/s_ao0005) AOC** | **[Q+BC0003-S+](https://mikrotik.com/product/q_bc0003_s)** | **[XQ+BC0003-XS+](https://mikrotik.com/product/xq_bc0003_xs_)** | **SFP28 [1m](https://mikrotik.com/product/xs_da0001)/[3m](https://mikrotik.com/product/xs_da0003) DAC** | **SFP28 [XS+31LC10D](https://mikrotik.com/product/xs_31lc10d)** | **SFP28 [XS+2733LC15D](https://mikrotik.com/product/xs_2733lc15d)** | **SFP28 [XS+85LC01D](https://mikrotik.com/product/xs_85lc01d)** |
| CCR1072-1G-8S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1036-12G-4S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1016-12S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 1,5** | **+ 1,5** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CCR1009-8G-1S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR1009-7G-1C-1S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-1G-2XS-PCIe | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-1G-12S+2XS | **+ 11** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2004-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2116-12G-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS125-24G-1S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS305-1G-4S+ | **+ 7** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS309-1G-8S+ | **+ 4** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS312-4C+8XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CSS318-16G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS320-8P-8B-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+ 6** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS418-8P-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+ 9** | **+ 9** | **+** |
| CRS317-1G-16S+ | **+ 3** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS328-4C-20S-4S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS328-24P-4S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+ 9** | **+ 9** | **+** |
| CRS226-24G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS212-1G-10S-1S+ | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS210-8G-2S+ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS112-8G/P-4S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS109-8G-1S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| CRS106-1C-5S/FiberBox | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB5009 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RB3011 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB2011 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| L009 | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| RB260/CSS106 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB922/921 | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RB953GS | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hAP AC | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hAP ax S | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| hEX PoE/PowerBox Pro | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hEX S | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| hEX S (2025) | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| RBFTC11 | **-** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **+ 8** | **-** | **-** | **+ 8** | **+ 8** | **+ 8** | **+ 8** |
| FTC11XG | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| FTC21 | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| LHG XL 52 ac | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **+** | **+** | **+** | **+** | **+** | **+** | **-** | **-** | **+** | **+** | **+** | **+** |
| L22/mANTBox ax 15s L23/NetMetal ax | **-** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** | **+ 14** |
| CSS610 | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+ 10** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+ 5** | **+ 5** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |

</WideTable>

### 40G QSFP+

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **Model** | **QSFP+ [Q+DA0001](https://mikrotik.com/product/q_da0001)** | **[Q+85MP01D](https://mikrotik.com/product/q_85mp01d)** | **[Q+BC0003-S+](https://mikrotik.com/product/q_bc0003_s)** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **+** | **+** | **+** |
| CRS504-4XQ-IN | **+** | **+** | **+** |
| CRS504-4XQ-OUT | **+13** | **+** | **+13** |
| CRS510-8XS-2XQ | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** |

### 100G QSFP28

<WideTable>

|  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Model** | **[XQ+31LC10D](https://mikrotik.com/product/xq_31lc10d)** | **[XQ+31LC02D](https://mikrotik.com/product/xq_31lc02d)** | **[XQ+85MP01D](https://mikrotik.com/product/xq_85mp01d)** | **[XQ+DA0001](https://mikrotik.com/product/xq_da0001)** | **[XQ+DA0003](https://mikrotik.com/product/xq_da0003)** | **[XQ+BC0003-XS+](https://mikrotik.com/product/xq_bc0003_xs_)** | **[XQ+CM0000-XS+](https://mikrotik.com/product/xq_cm0000_xs_)** |
| CRS326-4C+20G+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS354-48G/P-4S+2Q+ | **-** | **-** | **+** | **+** | **+** | **+** | **+** |
| CRS504-4XQ-IN | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS504-4XQ-OUT | **+** | **+** | **+** | **+13** | **+13** | **+13** | **+** |
| CRS510-8XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS518-16XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS520-4XS-16XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CCR2216-1G-12XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| RDS2216-2XG-4S+4XS-2XQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** | **+** | **+** | **+** | **+** |

</WideTable>

### 400G QSFP56-DD

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **Model** | **[DDQ+DA0001](https://mikrotik.com/product/ddq_da0001)** | **[DDQ+DA0003](https://mikrotik.com/product/ddq_da0003)** | **[DDQ+85MP01D](https://mikrotik.com/product/ddq_85mp01d)** |
| CRS812-8DS-2DQ-2DDQ | **+** | **+** | **+** |
| CRS804-4DDQ | **+** | **+** | **+** |

|  |  |  |
| :-- | :-- | :-- |
| **Legend** |  |  |
| Color codes: | Not supported | Check notes below |

:::note
Notes:

1. **CCR1016-12S-1S+**, **CRS212-1G-10S-1S+** - the SFP+1 interface does not work on any other link speed than 10G (does not support 1.25G fiber optic transceivers)
2. **CRS226-24G-2S+**, **CRS210-8G-2S+**- the SFP+1 interface also supports SFP 1.25G fiber optic transceivers, SFP+2 works only with 10G transceivers/links.
3. **CSS/CRS317-1G-16S+**- power controller supports up to 10 simultaneous S+RJ10 modules.
4. **CSS/CRS309-1G-8S+**- supports up to 4 simultaneous S+RJ10 modules. We do not recommend using S+RJ10 in passive cooling devices without additional cooling, as they have relatively high power consumption and in turn high operating temperature.
5. **Q+BC0003-S+**, **XQ+BC0003-XS+**- SFP+ connector support in the SFP+/SFP28 cages
6. **CSS/CRS326-24S+2Q+**- supports up to 12 simultaneous S+RJ10 modules
7. **CSS/CRS305-1G-4S+**- supports up to 2 simultaneous S+RJ10 modules.
8. **RBFTC11**- works connected to another device's 1G SFP port.
9. **XS+31LC10D**, **XS+2733LC15D** - full support has been added to CSS/CRS326-24G-2S+ and CRS328-24P-4S+ switches manufactured from October 2021.
10. **S+RJ10** - support in the SFP+ cages.
11. **CCR2004-1G-12S+2XS**- supports up to 6 simultaneous S+RJ10 modules.
12. **CCR2004-1G-2XS-PCIe**- supports only the same speed in both SFP28 ports (2 x 25G or 2 x 10G modes).
13. **CRS504-4XQ-OUT**- [reduced IP code from IP66 to IP54.](https://help.mikrotik.com/docs/display/UM/CRS504-4XQ-OUT#heading-Quickstart)
14. **10G SFP+/25G SFP28 modules** - device SFP supports up to 2.5G rate, manual speed setting is required to work.
15. **CRS312-4C+8XG, CRS326-4C+20G+2Q+** - Combo SFP+ interfaces support 1G and 10G speeds (do not support 2.5G and 5G)

:::

## S-RJ01

Table that states in what link rates if mounted in specific MikroTik devices the S-RJ01 module will be able to work. Use these modules only with auto-negotiation enabled. Forced link speeds are not supported. They will negotiate to the correct duplex and the highest possible rate.

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| **Model** | **1000** | **100** | **10** |
| RB5009 | **+** | **+** | **+** |
| RB4011 | **+** | **+** | **+** |
| RB3011 | **+** | **+** | **+** |
| RB922 | **+** | **+** | **+** |
| RB921 | **+** | **+** | **+** |
| hAP ac | **+** | **+** | **+** |
| hEX PoE | **+** | **+** | **+** |
| hEX S | **+** | **-** | **-** |
| RB953 | **+/+** | **-/+** | **-/+** |
| RB2011 | **+** | **-** | **-** |
| RB260/CSS106 | **+** | **-** | **-** |
| RBFTC11 | **+** | **-** | **-** |
| LHG XL 52 ac | **-** | **-** | **-** |
| RBD22/D23 mANTBox 52 15s/NetMetal ac² | **-** | **-** | **-** |
| CRS106 | **+** | **+** | **+** |
| CRS112 | **+** | **+** | **+** |
| CRS125/CRS109 | **+** | **+** | **+** |
| CRS212 | **+** | **+** | **+** |
| CRS226/CRS210 | **-** | **-** | **-** |
| CSS/CRS305-1G-4S+ | **+** | **+** | **+** |
| CSS/CRS309-1G-8S+ | **+** | **+** | **+** |
| CRS318-1Fi-15Fr-2S | **+** | **+** | **+** |
| CRS318-16P-2S+ | **+** | **+** | **+** |
| CSS/CRS326-24G-2S+ | **+** | **+** | **+** |
| CRS354 | **+** | **+** | **+** |
| CSS/CRS328-4C-20S-4S+ | **+** | **+** | **+** |
| CSS/CRS328-24P-4S+ | **+** | **+** | **+** |
| CSS/CRS317-1G-16S+ | **+** | **+** | **+** |
| CRS326-4C+20G+2Q+ | **+** | **+** | **+** |
| CRS326-24S+2Q+ | **+** | **+** | **+** |
| CSS610 | **+** | **+** | **+** |
| FTC11XG | **+** | **+** | **+** |
| CRS310-1G-5S-4S+/netFiber 9 | **+** | **+** | **+** |
| CRS310-8G+2S+IN | **+** | **+** | **+** |
| CCR1009 | **+/+** | **+/+** | **+/+** |
| CCR1016-12S-1S+ | **+** | **+** | **+** |
| CCR1036-12G-4S | **+** | **+** | **+** |
| CCR1036-8G-2S+ | **+** | **+** | **+** |
| CCR1072-1G-8S+ | **+** | **+** | **+** |

:::note
Notes

- The rate works fine: **+**
- The rate does not work: **-**
- RB953: SFP1/SFP2
- CCR1009: SFP+/SFP

:::

## 10 Gigabit Ethernet

### S+RJ10

Use these modules **only in 10G SFP+ ports with auto-negotiation enabled**. Forced link speeds and configurable link speed advertisements are not supported. They will negotiate to correct duplex and highest possible rate. For proper S+RJ10 module installation and recommended use case scenarios, see [S+RJ10 general guidance](../hardware/s-plus-rj10-general-guidance.md).

| Speed | Cable type | S+RJ10 to Ethernet port |
| :-- | :-- | :-- |
| 10BASE-T | Cat5e/6 | 100m |
| 100BASE-T | Cat5e/6 | 100m |
| 1000BASE-T | Cat5e/6 | 100m |
| 2.5GBASE-T | Cat5e/6 UTP | 100m |
| 2.5GBASE-T | Cat5e/6 STP | 100m |
| 5GBASE-T | Cat5e/6 | 100m |
| 10GBASE-T | Cat6/7 | 30m |

:::info
The negotiated speed is highly dependent on the quality and length of the cables used.

**Important:** S+RJ10 to S+RJ10 will always negotiate to the highest possible rate.
:::

The latest revision of S+RJ10 contains "/r2" by the end of the serial number. It comes with the following improvements:

- Jumbo frames up to 10218 Bytes at 2.5G, 5G and 10G speeds.
- Actual link speed reporting.
- DDM monitoring (Supply Voltage, Module temperature).

| Link Speed | Max MTU |
| :-- | --: |
| 10Gbps | 10218 |
| 5Gbps | 10218 |
| 2.5Gbps | 10218 |
| 1000Mbps | 1504 |
| 100Mbps | 1504 |
| 10Mbps | 1504 |

### CRS312-4C+8XG

10GE ports maximum supported cable length.

| Speed | Cable type | 10 Gigabit Ethernet ports |
| :-- | :-- | :-- |
| 10BASE-T | Cat5e/6 | 100m |
| 100BASE-T | Cat5e/6 | 100m |
| 1000BASE-T | Cat5e/6 | 100m |
| 2.5GBASE-T | Cat5e/6 | 100m |
| 5GBASE-T | Cat5e/6 | 100m |
| 10GBASE-T | Cat6/7 | 30m |

:::warning
The negotiated speed is highly dependent on the quality and length of the cables used.

**Caution:** 10GE ports do not support half-duplex mode with forced link speeds.
:::

## SFP interface compatibility with 100M optical transceivers

The SFP interface on the listed devices is compatible with [fast ethernet fiber](https://en.wikipedia.org/wiki/Fast_Ethernet#Fiber_optics) links.

### Compatible devices (interface)

- CCR1009-7G-1C (combo1)
- CCR1009-7G-1C-1S+ (combo1)
- CRS106-1C-5S (combo1)
- CRS328-4C-20S-4S+ (combo1 - combo4 and SFP1 - SFP20)
- LHG XL 52 ac
- RBD22/D23/mANTBox 52 15s/NetMetal ac²

## SFP+ interface compatibility with 1G optical transceivers

For MikroTik devices with SFP+ interfaces that support both 10G and 1G link rates, the following settings must be set on both linked devices for the required interfaces. These settings only relate when optical SFP transceivers are used. In order to get them working in 1G link rate, use the following configuration:

```ros
# Since RouterOS v7.12
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=1G-baseX

# Older RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=1Gbps full-duplex=yes 
```

- Auto-negotiation disabled.
- Port speed 1G.
- Full-duplex.

### Devices which SFP+ ports support 1G links

- CCR2004-1G-12S+2XS - All SFP+ interfaces can be used in 1G mode if required.
- CCR2004-16G-2S+ - All SFP+ interfaces can be used in 1G mode if required.
- CCR1072-1G-8S+ - All SFP+ interfaces can be used in 1G mode if required.
- CCR1036-8G-2S+ - All SFP+ interfaces can be used in 1G mode if required.
- CCR1009-8G-1S-1S+ - All SFP+ interfaces can be used in 1G mode if required.
- CCR1009-7G-1C-1S+ - All SFP+ interfaces can be used in 1G mode if required.
- CSS3xx series switches - All SFP+ interfaces can be used in 1G mode if required.
- CRS3xx series switches - All SFP+ interfaces can be used in 1G mode if required.
- RB5009 series - SFP+1 interface can be used in 1G mode if required.
- RB4011 series - SFP+1 interface can be used in 1G mode if required.
- CRS226-24G-2S+ - Only SFP+1 supports 1G link speed, SFP+2 is for 10G links only.
- CRS210-8G-2S+ - Only SFP+1 supports 1G link speed, SFP+2 is for 10G links only.
- CSS610 series switches - All SFP+ interfaces can be used in 1G mode if required.
- FTC11XG - SFP+1 interface can be used in 1G mode if required.

### Devices which SFP+ interfaces can be used only for 10G links

- CCR1016-12S-1S+
- CRS212-1G-10S-1S+

## SFP+ interface compatibility with 10G/25G optical transceivers

MikroTik devices with SFP+ ports can establish 10G links using 10G/25G optical fiber transceivers; however, an additional SFP Rate Select setting must be configured to avoid data corruption during transmission. The following settings are required on the SFP+ interface:

```ros
# Since RouterOS v7.12
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=10G-baseSR-LR sfp-rate-select=low

# Older RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=10Gbps full-duplex=yes sfp-rate-select=low
```

This requirement applies to MikroTik 10G/25G modules:

- XS+31LC10D
- XS+2733LC15D

## SFP+/SFP28 interface compatibility with 2.5G transceivers

The 2.5G link rate support has been implemented since RouterOS v7.3. MikroTik devices with SFP+ and SFP28 interfaces that support 2.5G link rate require the following settings to be set on both linked device interfaces.

```ros
# Since RouterOS v7.12
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=2.5G-baseX

# Older RouterOS
/interface/ethernet/set sfp-sfpplus1 auto-negotiation=no speed=2.5Gbps full-duplex=yes
```

- Auto-negotiation disabled.
- Port speed 2.5G.
- Full-duplex.

### Devices which support 2.5G links in SFP/SFP+/SFP28 ports

- CRS3xx series switches - All SFP+ interfaces can be used in 2.5G mode if required.
- CCR2004-1G-12S+2XS - All SFP+ and SFP28 interfaces can be used in 2.5G mode if required.
- CCR2116-12G-4S+ - All SFP+ interfaces can be used in 2.5G mode if required.
- CRS5xx series - All SFP28 interfaces can be used in 2.5G mode if required.
- CCR2216-1G-12XS-2XQ - All SFP28 interfaces can be used in 2.5G mode if required.
- RB5009 series - The SFP+ interface can be used in 2.5G mode if required.
- L009 series - The SFP interface can be used in 2.5G mode if required.
- L23 series - The SFP interface can be used in 2.5G mode if required.
- CSS610 series switches - All SFP+ interfaces can be used in 2.5G mode if required.
- FTC11XG - The SFP+1 interface can be used in 2.5G mode if required.
- E60/E62 - The SFP interface can be used in 2.5G mode if required.

## QSFP+/QSFP28/QSFP56/QSFP56-DD interface supported link rates

In RouterOS, QSFP+, QSFP28, QSFP56 and QSFP56-DD interfaces are designed to handle high-speed data transmission by utilizing multiple channels. Each QSFP+, QSFP28 or QSFP56 interface is divided into four sub-interfaces and QSFP56-DD is divided into eight sub-interfaces, each corresponding to a transmission channel necessary for proper operation.

:::info
The naming convention for QSFP+, QSFP28, QSFP56 and QSFP56-DD sub-interfaces includes two parts:

- The first digit following "qsfpplus", "qsfp28-", "qsfp56-" or "qsfp56-dd-" represents the QSFP+, QSFP28, QSFP56 or QSFP56-DD physical port.
- The second digit, ranging from 1 to 4 for QSFP+, QSFP28, QSFP56 and from 1 to 8 for QSFP56-DD, denotes each of the individual channels.

:::

Below are examples of how QSFP+, QSFP28, QSFP56 and QSFP56-DD interfaces appear in RouterOS:

```ros
# QSFP+
/interface/ethernet/print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME            MTU  MAC-ADDRESS        ARP      SWITCH 
 1   qsfpplus1-1    1500  48:8F:5A:B6:09:8C  enabled  switch1
 2   qsfpplus1-2    1500  48:8F:5A:B6:09:8D  enabled  switch1
 3   qsfpplus1-3    1500  48:8F:5A:B6:09:8E  enabled  switch1
 4   qsfpplus1-4    1500  48:8F:5A:B6:09:8F  enabled  switch1

# QSFP28
/interface/ethernet/print
Flags: R - RUNNING
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME         MTU  MAC-ADDRESS        ARP      SWITCH 
 1   qsfp28-1-1  1500  DC:2C:6E:9E:11:14  enabled  switch1
 2   qsfp28-1-2  1500  DC:2C:6E:9E:11:15  enabled  switch1
 3   qsfp28-1-3  1500  DC:2C:6E:9E:11:16  enabled  switch1
 4   qsfp28-1-4  1500  DC:2C:6E:9E:11:17  enabled  switch1

# QSFP56
/interface/ethernet/print
Flags: R - RUNNING; S - SLAVE
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #   NAME            MTU  MAC-ADDRESS        ARP      SWITCH 
 2   qsfp56-1-1     1500  04:F4:1C:1A:82:A1  enabled  switch1
 3   qsfp56-1-2     1500  04:F4:1C:1A:82:A2  enabled  switch1
 4   qsfp56-1-3     1500  04:F4:1C:1A:82:A3  enabled  switch1
 5   qsfp56-1-4     1500  04:F4:1C:1A:82:A4  enabled  switch1

# QSFP56-DD
/interface/ethernet/print
Flags: R - RUNNING; S - SLAVE
Columns: NAME, MTU, MAC-ADDRESS, ARP, SWITCH
 #    NAME            MTU  MAC-ADDRESS        ARP      SWITCH
 10   qsfp56-dd-1-1  1500  04:F4:1C:1A:82:91  enabled  switch1
 11   qsfp56-dd-1-2  1500  04:F4:1C:1A:82:92  enabled  switch1
 12   qsfp56-dd-1-3  1500  04:F4:1C:1A:82:93  enabled  switch1
 13   qsfp56-dd-1-4  1500  04:F4:1C:1A:82:94  enabled  switch1
 14   qsfp56-dd-1-5  1500  04:F4:1C:1A:82:95  enabled  switch1
 15   qsfp56-dd-1-6  1500  04:F4:1C:1A:82:96  enabled  switch1
 16   qsfp56-dd-1-7  1500  04:F4:1C:1A:82:97  enabled  switch1
 17   qsfp56-dd-1-8  1500  04:F4:1C:1A:82:98  enabled  switch1
```

Configuration and monitoring for these sub-interfaces may vary based on factors such as auto-negotiation, advertised speeds, and the type of transceiver (e.g., break-out cable or single fiber). The following sections will provide guidance on the configuration necessary for each use case.

:::warning
Disabling or enabling any of the physical port sub-interfaces will trigger a reconfiguration of the entire port group, restarting all channels.
:::

### QSFP+

For MikroTik CRS3xx series devices, QSFP+ interfaces support the following link speeds:

- 1x 40G
- 4x 10G
- 4x 1G

#### Link Configuration

- **40G**: Can be configured with either auto-negotiation or a forced 40G speed.
- **4x10G and 4x1G**: Must be set with a forced speed mode and auto-negotiation disabled.

Starting from RouterOS version 7.12, in addition to choosing the right transmission rate, it's important to specify the correct link mode. For example, you might use **CR4** for DAC(Direct Attach Copper) or **SR4-LR4** for optical fiber.

#### Configuration Examples

*For RouterOS v7.12 and later:*

```ros
# 1x40G - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40G-baseCR4

# 1x40G - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40G-baseSR4-LR4

# 4x10G - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR  

# 4x10G - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR  
```

:::warning
In single-link mode, only the first QSFP+ sub-interface needs to be configured, while the remaining sub-interfaces should remain enabled.
:::

*For RouterOS versions earlier than v7.12:*

```routeros
# 1x40G - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=40Gbps full-duplex=yes

# 4x10G - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes 
```

### QSFP28

For MikroTik CRS5xx series and CCR2216 devices, QSFP28 interfaces support the following link speeds:

- 1x 100G.
- 2x 50G (available since RouterOS v7.12).
- 1x 40G.
- 4x 25G.
- 4x 10G.
- 4x 1G.

:::warning
Not supported: 50G over single channel, 2x 40G
:::

#### Link Configuration

- **100G**: Can be configured with either auto-negotiation or a forced 100G speed.
- **2x50G, 1x40G, 4x25G, 4x10G, and 4x1G**: Must be set with a forced speed mode and auto-negotiation disabled.

Starting from RouterOS version 7.12, in addition to choosing the right transmission rate, it's important to specify the correct link mode. For example, you might use **CR4** for DAC(Direct Attach Copper) or **SR4-LR4** for optical fiber.

#### Configuration Examples

*For RouterOS v7.12 and later:*

```ros
# 1x100G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=100G-baseCR4

# 1x100G - Optical
/interface/ethernet/set qsfp28-2-1 auto-negotiation=no speed=100G-baseSR4-LR4

# 2x50G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2

# 4x25G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR

# 4x25G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR
```

:::warning
In single-link mode, only the first QSFP28 sub-interface needs to be configured, while the remaining sub-interfaces should remain enabled. Similarly, for 2x50G link mode, only the master interfaces (e.g., qsfp28-1-1 and qsfp28-1-3) need to be configured, but the other sub-interfaces must remain enabled.
:::

*For RouterOS versions earlier than v7.12:*

```ros
# 1x100G - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=100Gbps full-duplex=yes

# 4x25G - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```

### QSFP56

For the MikroTik CRS812 device, QSFP56 interfaces support the following link speeds:

- 1x 200G
- 2x 100G
- 4x 50G
- 2x 50G
- 1x 40G
- 4x 25G
- 4x 10G
- 4x 1G

#### Link Configuration

- **2x100G, 4x50G, 1x100G,  2x50G, 1x40G, 4x25G, 4x10G and 4x1G**: Must be set with a forced speed mode and auto-negotiation disabled.

It's important to specify the correct link mode. For example, you might use **CR4** for DAC(Direct Attach Copper) or **SR4-LR4** for optical fiber.

#### Configuration Examples

```ros
# 1x200G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=200G-baseCR4

# 1x200G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=200G-baseSR4-LR4

# 2x100G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=100G-baseCR2

# 2x100G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=100G-baseSR2-LR2

# 4x50G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=50G-baseCR

# 4x50G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=50G-baseSR-LR

# 1x100G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseCR4

# 1x100G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=100G-baseSR4-LR4

# 2x50G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=50G-baseSR2-LR2

# 4x25G - DAC
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=25G-baseCR

# 4x25G - Optical
/interface/ethernet/set qsfp56-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-1-4 auto-negotiation=no speed=25G-baseSR-LR
```

### QSFP56-DD

For MikroTik CRS812 and CRS804 devices, QSFP56-DD interfaces support the following link speeds:

- 1x 400G
- 2x 200G
- 4x 100G
- 8x 50G
- 8x 25G
- 2x 40G
- 8x 10G
- 8x 1G

#### Link Configuration

- **400G**: Can be configured with either auto-negotiation or a forced 400G speed.
- **2x200G, 4x100G, 8x50G,  8x25G, 2x40G, 8x10G and 8x1G**: Must be set with a forced speed mode and auto-negotiation disabled.

It's important to specify the correct link mode. For example, you might use **CR8** for DAC(Direct Attach Copper) or **SR8-LR8** for optical fiber.

#### Configuration Examples

```ros
# 1x400G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=400G-baseCR8

# 1x400G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=400G-baseSR8-LR8

# 2x200G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=200G-baseCR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=200G-baseCR4

# 2x200G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=200G-baseSR4-LR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=200G-baseSR4-LR4

# 4x100G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=100G-baseCR2
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=100G-baseCR2

# 4x100G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=100G-baseSR2-LR2
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=100G-baseSR2-LR2

# 8x50G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=50G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=50G-baseCR

# 8x50G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=50G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=50G-baseSR-LR

# 8x25G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=25G-baseCR

# 8x25G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=25G-baseSR-LR

# 2x40G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=40G-baseCR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=40G-baseCR4

# 2x40G  - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=40G-baseSR4-LR4
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=40G-baseSR4-LR4

# 8x10G - DAC
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=10G-baseCR

# 8x10G - Optical
/interface/ethernet/set qsfp56-dd-1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-4 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-5 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-6 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-7 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp56-dd-1-8 auto-negotiation=no speed=10G-baseSR-LR
```

## QSFP+/QSFP28 interface compatibility with breakout cables

MikroTik devices can establish links between QSFP+/QSFP28 and SFP+/SFP28 ports using breakout cables.

### Configuration Examples

*For RouterOS v7.12 and later:*

```ros
# QSFP+ - DAC
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseCR

# QSFP+ - Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10G-baseSR-LR

# QSFP28 - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseCR

# QSFP28 - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25G-baseSR-LR

```

It is also possible to use QSFP28 to 2x50G QSFP28 Breakout Cables:

```routeros
# 2x50G - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseCR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseCR2

# 2x50G - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=50G-baseSR2-LR2
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=50G-baseSR2-LR2
```

Or to configure different speed rates for each QSFP+/QSFP28 sub-interface:

```routeros
# QSFP28 - DAC
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseCR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=10G-baseCR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=10G-baseCR

# QSFP28 - Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25G-baseSR-LR
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=10G-baseSR-LR
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=10G-baseSR-LR
```

*For RouterOS versions earlier than v7.12:*

```routeros
# QSFP+ - DAC/Optical
/interface/ethernet/set qsfpplus1-1 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-2 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-3 auto-negotiation=no speed=10Gbps full-duplex=yes
/interface/ethernet/set qsfpplus1-4 auto-negotiation=no speed=10Gbps full-duplex=yes

# QSFP28 - DAC/Optical
/interface/ethernet/set qsfp28-1-1 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-2 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-3 auto-negotiation=no speed=25Gbps full-duplex=yes
/interface/ethernet/set qsfp28-1-4 auto-negotiation=no speed=25Gbps full-duplex=yes
```
