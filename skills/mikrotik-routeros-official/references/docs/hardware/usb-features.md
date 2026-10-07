# USB Features

> This page documents USB features in MikroTik RouterOS, including USB power reset functionality with configurable duration and bus selection, USB port type routing options (auto/USB-type-A/mini-PCIe), and micro USB...

# USB Features

## Summary

**Sub-menu:** `/system/routerboard/usb`  
**Package:** `system (v6, v7)`

This article describes RouterBoard device-supported USB features.

## USB Power Reset

USB power reset turns off USB port power for a specified time. It is useful when a 3G/LTE modem needs to be restarted but there is no physical access to it.

## Available properties

- duration (*time*; Default: "3s") - Time interval during which power is turned off.

For example, turn off USB port power for 10 seconds:

```ros
/system/routerboard/usb/power-reset duration=10s 
```

RouterBoards with multiple USB buses also require a bus to be specified in order to do a USB power reset.  

## Available properties

- duration (*time*; Default: "3s") - Time interval of how long power is turned off.
- bus (*integer*; Default: 1) - USB bus where power reset is applied.

:::warning
**RB953GS**: The miniPCIe slot closer to Ethernet ports on the RB953GS board is the one which is shared with USB port and has configurable  [USB port type](#usb-port-type), its USB bus number is 1. Depending on  [USB port type](#usb-port-type) the power reset is done on USB port or miniPCIe slot. The other miniPCIe slot closer to SFP slots has independent bus - 2.

:::

:::warning
**RB922UAG**: The USB port has an independent bus - 1. The miniPCIe slot has an independent bus - 2.

:::

:::warning
**CCR1072-1G-8S+**: The micro USB port has an independent bus - 0. The USB Type-A port has an independent bus - 1.

:::

## USB Port Type

Boards with switchable USB port routing have shared USB lines which can be routed to an external USB-Type port or a mini-PCIe slot. For more reference see the board block diagram in the document section on the board specification page.

```ros
[admin@MikroTik] > /system/routerboard/usb/set type=
USB-type-A     auto     mini-PCIe 
```

|  |  |
| :-- | :-- |
| **auto**(default) | During RouterOS startup check if a USB device is present in mini-PCIe slot: if present - use device in mini-PCIe slotif not present - defaults to the external USB Type A port |
| **USB-type-A** | Use USB devices connected to USB  Type A connector |
| **mini-PCIe** | Route USB lines to corresponding mini-PCIe slot |

:::warning
**RB953GS:** The miniPCIe slot closer to Ethernet ports on the RB953GS board is the one which is shared with the USB port and has a configurable  [USB port type](#usb-port-type), its USB bus number is 1. Depending on the  [USB port type](#usb-port-type) the power reset is done on the USB port or the miniPCIe slot. The other miniPCIe slot closer to SFP slots has an independent bus - 2.

:::

## USB Port Mode

RB2011 series, CRS1xx series, and mAP have a micro USB port which operates in host mode when a USB device is attached through a USB OTG cable. Some vendor cables require forced host mode to recognize the connected device.

## Available Properties

- usb-mode (*automatic | force-host*; Default: "automatic") - Defines USB port mode.

:::warning
Warning

On RB2011 and CRS1xx series boards USB devices may not work the first time they are plugged in. In such cases a power cycle (not reboot) is required.

:::

## RouterBoard USB Port Limitations

Some RouterBoard devices have notable USB port limitations.

\* RB mAP 2n - does not support USB Power Reset  
\* RB750UP - does not support USB Power Reset  
\* RB751U-2HnD - does not support USB Power Reset  
\* RB751G-2HnD - does not support USB Power Reset  
\* RB411U - does not support USB Power Reset  
\* RB411UAHR - does not support USB Power Reset and USB Powering ([USB power injector](https://mikrotik.com/product/5VUSB) is required)  
\* RB433UAH - does not support USB Power Reset  
\* RB435G - does not support USB Power Reset  
\* RB493G - does not support USB Power Reset and USB Powering ([USB power injector](https://mikrotik.com/product/5VUSB) is required)

:::warning
RouterOS does not support memory slots from USB modems.

:::
