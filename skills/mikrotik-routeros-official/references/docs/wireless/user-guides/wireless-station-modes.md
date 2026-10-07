# Wireless Station Modes

> This page describes MikroTik RouterOS wireless station modes, explaining their differences in L2 address handling and suitability for bridging. It covers standard station mode, station-wds for WDS connections, and...

# Wireless Station Modes

## Overview

A wireless interface in any of the *station* modes will search for an acceptable access point (AP) and connect to it. The connection between station and AP will behave in a slightly different way depending on the type of *station* mode used, so the correct mode must be chosen for a given application and equipment. This article attempts to describe differences between available *station* modes.

The primary difference between *station* modes is in how L2 addresses are processed and forwarded across the wireless link. This directly affects the ability of the wireless link to be part of L2 bridged infrastructure.

If L2 bridging over wireless link is not necessary - as in the case of routed or MPLS switched network, basic **mode=station** setup is suggested and will provide the highest efficiency.

Availability of a particular *station* mode depends on the **wireless-protocol** that is used in the wireless network and the drivers installed ([`wireless` or `wifi-qcom`](/docs/wireless/#which-section-is-for-my-device)). Please refer to the [applicability matrix](#applicability-matrix) for information on mode support in protocols. It is possible that a connection between a station and an AP will be established even if a particular mode is not supported for a given protocol. Beware that such a connection will not behave as expected with respect to L2 bridging.

## 802.11 limitations for L2 bridging

Historically 802.11 AP devices were supposed to be able to bridge frames between a wired network segment and wireless, but a station device was not supposed to do L2 bridging.

Consider the following network:

```
[X]---[AP]-(     )-[STA]---[Y]
```

where X-to-AP and STA-to-Y are ethernet links, but AP-to-STA is connected wirelessly. According to 802.11, the AP can transparently bridge traffic between X and STA, but it is not possible to bridge traffic between the AP and Y, or X and Y.

The 802.11 standard specifies that frames between a station and an AP device must be transmitted in a so-called *3 address* frame format, meaning that the header of the frame contains 3 MAC addresses. The frame transmitted from AP to station has the following addresses:

- Destination address - address of station device, also radio receiver address;
- Radio transmitter address - address of AP;
- Source address - address of originator of particular frame.

A frame transmitted from a station to an AP has the following addresses:

- radio receiver address - address of AP;
- source address - address of station device, also radio transmitter address;
- destination address.

Considering that every frame must include radio transmitter and receiver addresses, it is clear that *3 address* frame format is not suitable for transparent L2 bridging over a station, because a station can not send a frame with a source address different from its address - e.g. a frame from Y, and at the same time the AP can not format a frame in a way that would include the address of Y.

802.11 includes an additional frame format, so-called *4 address* frame format, intended for "wireless distribution system" (WDS) - a system to interconnect APs wirelessly. In this format an additional address is added, producing a header that contains the following addresses:

- radio receiver address;
- radio transmitter address;
- destination address;
- source address.

This frame format includes all necessary information for transparent L2 bridging over a wireless link. Unluckily 802.11 does not specify how WDS connections should be established and managed, therefore any usage of *4 address* frame format (and WDS) is implementation specific.

Different *station* modes attempt to solve shortcomings of the standard station mode to provide support for L2 bridging.

## Applicability Matrix

The following matrix specifies *station* modes available for each supported wireless protocol and drivers. Note that there are 2 columns for 802.11 protocol: **802.11** specifies availability of the mode in a "pure" 802.11 network (when connecting to any vendor AP) and **ROS 802.11** specifies availability of the mode when connecting to a RouterOS AP that implements necessary proprietary extensions for the mode to work.

*The table applies to RouterOS v5rc11 and above:*

|  | 802.11 | ROS 802.11 `wireless` | nstreme `wireless` | nv2 `wireless` | ROS 802.11 `wifi-qcom` |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| **station** | V | V | V | V | V |
| **station-wds** |  | V | V | V | |
| **station-pseudobridge** | V | V | V |  | V |
| **station-pseudobridge-clone** | V | V | V |  | |
| **station-bridge** |  | V | V | V | V |

## Mode *station*

This is a standard mode that does not support L2 bridging on station - attempts to put the wireless interface in the bridge will not produce expected results. On the other hand, this mode can be considered the most efficient and therefore should be used if L2 bridging on station is not necessary - as in the case of a routed or MPLS switched network. This mode is supported for all wireless protocols.

## Mode *station-wds*

This mode works only with RouterOS APs. As a result of negotiating a connection, a separate WDS interface is created on the AP for the given station. This interface can be thought of as a point-to-point connection between the AP and the given station - whatever is sent out the WDS interface is delivered to the station (and only to the particular station) and whatever the station sends to the AP is received from the WDS interface (and not subject to forwarding between AP clients), preserving L2 addresses.

This mode is supported for all wireless protocols except when 802.11 protocol is used in connection to a non-RouterOS device. The mode uses *4 address* frame format when used with 802.11 protocol, for other protocols (such as nstreme or nv2), protocol internal means are used.

This mode is safe to use for L2 bridging and gives most administrative control on the AP by means of a separate WDS interface, for example, use of bridge firewall, RSTP for loop detection and avoidance, etc.

With station-wds mode, it is not possible to connect to CAPsMAN controlled CAP.

## Mode *station-pseudobridge*

From the wireless connection point of view, this mode is the same as standard station mode. It has limited support for L2 bridging by means of some services implemented in station:

- MAC address translation for IPv4 packets - the station maintains an IPv4-to-MAC mapping table and replaces the source MAC address with its own address when sending a frame to the AP (in order to be able to use *3 address* frame format), and replaces the destination MAC address with the address from the mapping table for frames received from the AP. IPv4-to-MAC mappings are built also for VLAN encapsulated frames.
- Single MAC address translation for the rest of the protocols - the station learns the source MAC address from the first forwarded non-IPv4 frame and uses it as the default for reverse translation - this MAC address is used to replace the destination MAC address for frames received from the AP if IPv4-to-MAC mapping can not be performed (e.g. - non-IPv4 frame or missing mapping).

This mode is limited to complete L2 bridging of data to a single device connected to the station (by means of single MAC address translation) and some support for IPv4 frame bridging - bridging of non-IP protocols to more than one device will not work. Also MAC address translation limits access to the station device from the AP side to IPv4-based access - the rest of the protocols will be translated by single MAC address translation and will not be received by the station itself.

This mode is available for all protocols except nv2 and ***should be avoided when possible***. The usage of this mode can only be justified if the AP does not support a better mode for L2 bridging (e.g. when a non-RouterOS AP is used) or if only one end-user device must be connected to the network by means of a station device.

## Mode *station-pseudobridge-clone*

This mode is the same as *station-pseudobridge* mode, except that it connects to the AP using a "cloned" MAC address - that is either the address configured in the **station-bridge-clone-mac** parameter (if configured) or the source address of the first forwarded frame. This essentially appears on the AP as if an end-user device connected to the station connected to the AP.

## Mode *station-bridge*

This mode works only with RouterOS APs and provides support for transparent protocol-independent L2 bridging on the station device. RouterOS AP accepts clients in *station-bridge* mode when enabled using the **bridge-mode** parameter. In this mode, the AP maintains a forwarding table with information on which MAC addresses are reachable over which station device.

This mode is MikroTik proprietary and cannot be used to connect to other brands of devices.

This mode is safe to use for L2 bridging and is the preferred mode unless there are specific reasons to use *station-wds* mode. With station-bridge mode, it is not possible to connect to a CAPsMAN-controlled CAP.
