# discovery-settings

> RouterOS settings reference for /ip/neighbor/discovery-settings.

-----------

## ip/neighbor/discovery-settings 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="discover-interface-list" typ="super { !
, discover-interface-list: enum
 }">Interface list whose members the discovery protocol will run on. Default: static.</ArgTableRow>
<ArgTableRow arg="discover-interval" typ="time">Frequency at which neighbor discovery packets are transmitted. Also adjusts the TTL TLV value for CDP and LLDP packets using the formula: (discover-interval * 4) + 1. Range: 5s..9h6m8s. Default: 30s.</ArgTableRow>
<ArgTableRow arg="lldp-med" typ="bool">Whether to advertise the LLDP-MED Media Capabilities TLV. Must be enabled when lldp-med-net-policy-vlan is used. Default: yes.</ArgTableRow>
<ArgTableRow arg="lldp-med-net-policy-vlan" typ="alt { constant: enum (disabled)
, vlan-id: num [ .. 4094]
 }">Advertised VLAN ID for LLDP-MED Network Policy TLV. Allows assigning a VLAN ID for LLDP-MED-capable devices such as VoIP phones. The TLV is only added to interfaces where LLDP-MED-capable devices are discovered and lldp-med is enabled. Other TLV values (Application Type, VLAN Type, L2 Priority, DSCP Priority) are predefined. CDP should be excluded using the protocol setting to avoid LLDP-MED misconfiguration. Default: disabled.</ArgTableRow>
<ArgTableRow arg="lldp-mac-phy-config" typ="bool">Whether to send MAC/PHY Configuration/Status TLV in LLDP, indicating interface capabilities, duplex status, bit rate, and auto-negotiation. Only applies to Ethernet interfaces. Automatically included when sending LLDP-MED. Default: no.</ArgTableRow>
<ArgTableRow arg="lldp-max-frame-size" typ="bool">Whether to send Maximum Frame Size TLV in LLDP, indicating the maximum frame size capability of the interface in bytes (l2mtu + 18). Only applies to Ethernet interfaces. Default: no.</ArgTableRow>
<ArgTableRow arg="lldp-vlan-info" typ="bool">Whether to send IEEE 802.1 Organizationally Specific TLVs in LLDP related to VLANs. When enabled, three TLVs are advertised: Port VLAN ID (bridge port pvid), Port And Protocol VLAN ID (not supported), and VLAN Name (up to 10 active VLANs from the bridge VLAN table). Relevant to interfaces on a vlan-filtering bridge. Default: no.</ArgTableRow>
<ArgTableRow arg="lldp-poe-power" typ="bool" syscap="poe">Whether to transmit the IEEE 802.3 Organizationally Specific Power Via MDI TLV in LLDP messages. Replaces the PoE-out port poe-lldp-enabled setting. Relevant only for Ethernet interfaces with PoE-Out support. Default: yes.</ArgTableRow>
<ArgTableRow arg="lldp-poe-in-power" typ="bool" syscap="poe-in">Whether to transmit PoE input power TLVs in LLDP messages.</ArgTableRow>
<ArgTableRow arg="lldp-dcbx" typ="bool" syscap="crs_prestera">Whether to send Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs, communicating switch QoS settings and capabilities with neighboring devices using LLDP. Only applies to devices with a Marvell Prestera switch (e.g. CRS3xx). Includes ETS Configuration, Priority Assignment, Bandwidth Allocation, and TSA tables. Default: no.</ArgTableRow>
<ArgTableRow arg="protocol" typ="ubit (cdp, lldp, mndp)">List of discovery protocols to use. Default: cdp,lldp,mndp.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (tx-and-rx | tx-only | rx-only)">Neighbor discovery packet sending and receiving mode. Default: tx-and-rx.</ArgTableRow>
<ArgTableRow arg="dying-gasp" typ="bool">Whether to send a neighbor discovery packet with TTL=0 before a graceful reboot, shutdown, or upgrade. Not sent in case of power loss or kernel panic. On the receiving side, a TTL=0 packet immediately removes the corresponding neighbor entry. Default: no.</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">Whether to create dynamic DNS entries for discovered neighbors, using their identity as the domain name.</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">Suffix added to dynamic DNS entries created for each neighbor.</ArgTableRow>
</ArgTable>
