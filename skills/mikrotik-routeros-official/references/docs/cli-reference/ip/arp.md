# arp

> Even though IP packets are addressed using IP addresses, hardware addresses must be used to transport data from one host to another. Address Resolution Protocol is used to map OSI level 3 IP addresses to OSI level 2...

-----------

## ip/arp 
**Type:** Directory

Even though IP packets are addressed using IP addresses, hardware addresses must be used to transport data from one host to another. Address Resolution Protocol is used to map OSI level 3 IP addresses to OSI level 2 MAC addresses. A router has a table of currently used ARP entries. Normally the table is built dynamically, but to increase network security, it can be partially or completely built statically by adding static entries. To know more on how ARP works, read [networking fundamentals](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together).

:::info
The default maximum number of ARP entries depends on the installed amount of RAM. It can be adjusted with the command "`/ip/settings/set max-neighbor-entries=`x", see more details on [IPv4 Settings](./settings.md).
:::

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether the ARP entry is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">Whether the entry is not valid.</ArgTableRow>
<ArgTableRow arg="H" typ="dhcp">Whether the ARP entry is added by DHCP server.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the entry is dynamically created.</ArgTableRow>
<ArgTableRow arg="P" typ="published">published</ArgTableRow>
<ArgTableRow arg="C" typ="complete">Complete flag is included in ARP entries when the ARP `status` is permanent, reachable, stale, probe, or delay.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr">IP address to be mapped.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address to be mapped to.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface name the IP address is assigned to.</ArgTableRow>
<ArgTableRow arg="published" typ="bool">Static proxy-arp entry for individual IP addresses. When an ARP query is received for the specific IP address, the device will respond with its own MAC address. No need to set proxy-arp on the interface itself for all the MAC addresses to be proxied. The interface will respond to an ARP request only when the device has an active route towards the destination.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">
Shows the ARP entry state.
- `delay` - neighbor entry validation is currently delayed.
- `failed` - ARP resolution has failed.
- `incomplete` - system does not have the MAC address information for the IP address.
- `permanent` - ARP entry is considered permanent and will not be removed.
- `probe` - neighbor is being probed.
- `reachable` - ARP resolution is successful, the MAC address is known.
- `stale` - entry is still valid but aged.
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Indicates which VRF this ARP entry is associated with.</ArgTableRow>
</ArgTable>
