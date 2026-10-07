# vrrp

> RouterOS directory reference for /interface/vrrp.

-----------

## interface/vrrp 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The VRRP interface is disabled by the user.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The VRRP interface is in the invalid state, for example due to a configuration error.</ArgTableRow>
<ArgTableRow arg="G" typ="grp-authority">The VRRP interface is `group-authority`. It controls the state of the other group members and is the only interface that sends VRRP advertisements.</ArgTableRow>
<ArgTableRow arg="g" typ="grp-member">The VRRP interface is a group member. Its state machine follows the state of the specified `group-authority` interface.</ArgTableRow>
<ArgTableRow arg="R" typ="running">running.</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
<ArgTableRow arg="M" typ="master">The VRRP interface is in the master state.</ArgTableRow>
<ArgTableRow arg="B" typ="backup">The VRRP interface is in the backup state.</ArgTableRow>
<ArgTableRow arg="F" typ="failure">The VRRP interface is in the failure state, for example due to a link-down on its parent interface.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">VRRP interface name.</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[Address Resolution Protocol](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) mode.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">How long the ARP record is kept in the ARP table after no packets are received from IP. Value `auto` equals the value of `arp-timeout` in IP/Settings, default is 30s.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface name on which VRRP instance will be running.</ArgTableRow>
<ArgTableRow arg="group-master" typ="iface_enum { :0, none:0, self }">deprecated.</ArgTableRow>
<ArgTableRow arg="group-authority" typ="iface_enum { :0, none:0, self }">
Allows multiple VRRP interfaces to be grouped so they share the same VRRP state. Within a group, a single group authority interface is selected. It controls the state of the other group members and is the only interface that sends VRRP advertisements. When the group-authority VRRP interface transitions to the backup state, all group members also transition to the backup state. If a failure is detected on any group member, for example due to a link-down on its parent interface, all group members transition to the failure state.
- `none` - The VRRP interface is not grouped and operates independently, with its own VRRP state machine.
- `self` - The VRRP interface acts as the group authority. It controls the state machines of other grouped VRRP interfaces and is responsible for sending and receiving VRRP advertisements.
- `vrrp-interface` - The VRRP interface is a group member. Its state machine follows the state of the specified VRRP interface.
</ArgTableRow>
<ArgTableRow arg="vrid" typ="num">Virtual Router identifier. Each Virtual router must have a unique id number.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Priority of VRRP node used in Master election algorithm. A higher number means higher priority. `255` is reserved for the router that owns the VR IP and `0` is reserved for the Master router to indicate that it is releasing responsibility.</ArgTableRow>
<ArgTableRow arg="interval" typ="time">
The VRRP interval defines how often the VRRP master router sends Advertisement packets to backup routers. This interval directly determines the frequency at which backups receive keepalive information confirming that the master is operational.
A shorter interval increases the rate of Advertisement packets, allowing faster detection of master failure, but also increases sensitivity to packet loss, processing delays, and timer inaccuracies. Longer intervals reduce control traffic and improve stability, at the cost of slower failover detection. The Master Down interval is derived from the configured VRRP interval and the router's priority, and is calculated to allow multiple missed Advertisements before triggering failover.

**Warning:** Configuring VRRP intervals below 1 second can lead to unpredictable behavior and unintended master role changes.
</ArgTableRow>
<ArgTableRow arg="preemption-mode" typ="bool">Whether the master node always has the priority. When set to `no` the backup node will not be elected to be a master until the current master fails, even if the backup node has higher priority.</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | simple | ah) { none:0, simple:1, ah:2 }">
Authentication method to use for VRRP advertisement packets.
- `none` - Use only in low-security networks, for example, two VRRP nodes on a LAN.
- `ah` - IP Authentication Header. This algorithm provides strong protection against configuration errors, replay attacks, and packet corruption or modification. You should use it when you have limited control over the administration of nodes on a LAN. HMAC-MD5 is used.
- `simple` - Uses a clear-text password. Protects against accidental misconfiguration of routers on a local network.
</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password required for authentication. Can be ignored if authentication is not used.</ArgTableRow>
<ArgTableRow arg="on-backup" typ="alt { script: string
 }">Script to execute when the node is switched to the backup state.</ArgTableRow>
<ArgTableRow arg="on-master" typ="alt { script: string
 }">Script to execute when the node is switched to the master state.</ArgTableRow>
<ArgTableRow arg="on-fail" typ="alt { script: string
 }">Script to execute when the node fails.</ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3) { 2:2, 3:3 }">Which VRRP version to use.</ArgTableRow>
<ArgTableRow arg="v3-protocol" typ="enum (ipv4 | ipv6) { ipv4:1, ipv6:2 }">A protocol that will be used by VRRPv3. Valid only if the `version` is 3.</ArgTableRow>
<ArgTableRow arg="v3-checksum-as-v2" typ="bool">
Controls whether the VRRPv3 IPv4 checksum is calculated with or without the IPv4 pseudoheader.
Different vendors interpret RFC 5798 section 5.2.8 differently regarding the pseudoheader in IPv4 checksum calculation. Linux-based implementations (including FRR) include the pseudoheader for both IPv4 and IPv6, while Cisco includes it only for IPv6.
- `no` (default) - Include the IPv4 pseudoheader in the checksum calculation. Compatible with other Linux-based VRRPv3 implementations.
- `yes` - Exclude the IPv4 pseudoheader from the checksum calculation. Use this setting for compatibility with Cisco and other vendors that do not include the pseudoheader for IPv4.

This setting applies only to VRRPv3 with IPv4. It has no effect on VRRPv3 IPv6 or VRRPv2.

All VRRP routers in the same Virtual Router must use the same value for this setting. Mismatched values will cause "bad checksum" errors and VRRP advertisement packets will be discarded.
</ArgTableRow>
<ArgTableRow arg="sync-connection-tracking" typ="bool">Synchronize connection tracking entries from Master to Backup device. The VRRP connection tracking synchronization requires that RouterOS connection tracking is running.</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">
Specifies the remote address of the other VRRP router for connection tracking synchronization. If not set, the system autodetects the remote address through VRRP. The remote address is used only if `sync-connection-tracking` is enabled. Explicitly setting a remote address has the following benefits:
- Connection tracking synchronization starts faster because there is no need to wait for VRRP's initial message exchange to detect the remote address.
- VRRP Master election is faster.
- Connection tracking data can be sent through a different network interface, for example, a dedicated secure line between two routers.
Sync connection tracking uses UDP port 8275.
</ArgTableRow>
<ArgTableRow arg="connection-tracking-mode" typ="enum (passive-active | active-active) { passive-active:0, active-active:1 }">
Specifies the mode for connection tracking synchronization. This setting is relevant only when `sync-connection-tracking` is enabled.
- `passive-active` - Use this mode for traditional VRRP setups, where one master and one or more backup routers are used. In this mode, only the master device performs connection tracking synchronization by sending updates to the backup devices. Backup devices do not send connection tracking data.
- `active-active` - Use this mode for setups with multiple VRRP groups to achieve load balancing. Each VRRP group has its own master, and these masters can reside on different physical devices. With active-active mode, all active masters can synchronize connection tracking data with each other. Each VRRP group in active-active mode must use a unique connection-tracking-port value. Reusing the same port across multiple groups can cause a non-synchronized connection tracking table.

Using multiple VRRP groups with **passive-active** mode can lead to unsynchronized connection tracking tables because only one master handles synchronization, and the others do not exchange tracking data.
</ArgTableRow>
<ArgTableRow arg="connection-tracking-port" typ="num">Specifies UDP port for connection tracking synchronization. This setting is only relevant when `sync-connection-tracking` is enabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mtu" typ="num">Layer3 MTU size. The VRRP interface always uses slave interface MTU.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the VRRP interface.</ArgTableRow>
</ArgTable>
