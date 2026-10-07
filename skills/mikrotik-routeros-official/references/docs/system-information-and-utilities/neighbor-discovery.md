# Neighbor Discovery

> Neighbor discovery protocols enable detection of devices using MNDP, CDP, or LLDP in Layer2 domains, displaying connected neighbors' IP/MAC addresses and interfaces. Configuration options include protocol selection,...

# Neighbor Discovery

Neighbor Discovery protocols allow you to find devices compatible with MNDP (MikroTik Neighbor Discovery Protocol), CDP (Cisco Discovery Protocol), or LLDP (Link Layer Discovery Protocol) in the Layer 2 broadcast domain. They can be used to map out your network.

All read-only neighbor parameters are documented in the [`/ip/neighbor`](../cli-reference/ip/neighbor) CLI reference.

LLDP-discovered neighbors are shown in a separate read-only menu in [`/ip/neighbor/lldp`](../cli-reference/ip/neighbor/lldp).

Unlike the general `/ip/neighbor` menu which aggregates neighbors from all discovery protocols (MNDP, CDP, and LLDP), `/ip/neighbor/lldp` shows only LLDP-discovered entries.

The `lldpRemTable` SNMP table reports only neighbors discovered through LLDP. Entries discovered exclusively by CDP or MNDP are excluded from the SNMP LLDP-MIB.

## View and configure discovery in WinBox

Open **IP > Neighbors** to see discovered devices and the interfaces through which they were found. Select the **LLDP** tab for LLDP-only entries. To configure discovery, select **Discovery Settings** in the right panel:

1. Select the interface list in **Interface**. This corresponds to `discover-interface-list`; choose a list containing the interfaces that should participate in discovery.
2. Select the required **Protocol** checkboxes and review **Mode**, which controls whether discovery transmits, receives, or does both. Select **OK** to save the settings.

![WinBox Discovery Settings dialog with interface list, protocol, and mode controls](./img/neighbor-discovery-winbox.webp)

The screenshot shows an existing configuration. Choose the interface list for your network rather than copying its selection.

Discovery settings are configured in the [`/ip/neighbor/discovery-settings`](../cli-reference/ip/neighbor/discovery-settings) menu.

You can change whether an interface participates in neighbor discovery by using an [interface list](../cli-reference/interface/list). If the interface is included in the discovery interface list, it will send out basic information about the system and process received discovery packets broadcast in the Layer 2 network. Removing an interface from the interface list will disable both the discovery of neighbors on this interface and the possibility of discovering this device itself on that interface.

Neighbor discovery works on individual slave interfaces. When a master interface (e.g. bonding or bridge) is included in the discovery interface list, all its slave interfaces will automatically participate in neighbor discovery. To allow neighbor discovery only on some slave interfaces, include the particular slave interface in the list and make sure the master interface is not included.

```ros
/interface/bonding
add name=bond1 slaves=ether5,ether6
/interface/list
add name=only-ether5
/interface/list/member
add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings
set discover-interface-list=only-ether5
```

Now the neighbor list shows a master interface and the actual slave interface on which a discovery message was received:

```ros
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
    bond1    
```

### LLDP-MED Network Policy VLAN example

This example configures a switch port for a VoIP phone that daisy-chains a PC. The phone uses tagged traffic for voice, assigned through the LLDP-MED Network Policy TLV. The PC uses untagged traffic, which is assigned to a different VLAN by the bridge port PVID.

In this setup:

- **ether1** is the upstream trunk port, carrying all VLANs tagged to a router.
- **ether2** is the phone port. The VoIP phone connects directly, and the PC connects through the phone.
  - Voice traffic uses **VLAN 100** (tagged), advertised through `lldp-med-net-policy-vlan`.
  - Data traffic from the PC uses **VLAN 200** (untagged on the phone port), assigned by the bridge port `pvid`.

Create the bridge and add the ports:

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged

/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=200
```

Create the bridge VLAN table. The trunk port carries both VLANs tagged. The phone port carries the voice VLAN as tagged. The data VLAN for the PC is assigned by the bridge port `pvid`, which dynamically adds an untagged membership — no explicit `untagged=ether2` is needed:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2 vlan-ids=100
add bridge=bridge1 tagged=ether1 vlan-ids=200
```

Enable LLDP-MED and set the voice VLAN. Disable CDP to avoid interference with LLDP-MED:

```ros
/ip/neighbor/discovery-settings
set lldp-med=yes lldp-med-net-policy-vlan=100 protocol=lldp,mndp
```

Enable VLAN filtering on the bridge:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::note
The LLDP-MED Network Policy TLV is sent only on interfaces where an LLDP-MED-capable device is discovered. It is not broadcast on interfaces without MED-capable neighbors.
:::

:::info
For more details on bridge VLAN configuration, see [Bridge VLAN Filtering](../bridging-and-switching/index.md#bridge-vlan-filtering).
:::

## LLDP

Depending on RouterOS configuration, different type-length-values (TLVs) can be sent in the LLDP message. This includes:

- Chassis ID (MAC address).
- Port ID (interface name).
- Time To Live.
- System Name (system identity).
- System Description (platform - MikroTik, software version - RouterOS version, hardware name - RouterBoard name).
- Management Address (all IP addresses configured on the port).
- System Capabilities (enabled system capabilities, e.g. bridge or router).
- Port Description (combined interface name like "bridge/ether1" if the sending interface is part of a bridge or bond, or interface name the same as Port ID).
- IEEE 802.1 Port VLAN ID.
- IEEE 802.1 Port And Protocol VLAN ID.
- IEEE 802.1 VLAN Name.
- IEEE 802.3 MAC/PHY Configuration/Status.
- IEEE 802.3 Power Via MDI.
- IEEE 802.3 Maximum Frame Size.
- LLDP-MED Media Capabilities (list of MED capabilities).
- LLDP-MED Network Policy (assigned VLAN ID for voice traffic).
- LLDP-MED Extended Power via MDI.
- End of LLDPDU.
