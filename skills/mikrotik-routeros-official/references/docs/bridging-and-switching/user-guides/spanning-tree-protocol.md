# Spanning Tree Protocol

> This page explains the Spanning Tree Protocol (STP) in MikroTik RouterOS, detailing how it prevents network loops by selecting a root bridge and optimizing port usage through Bridge Protocol Data Units (BPDUs). It...

# Spanning Tree Protocol

---

The purpose of the spanning tree protocol is to provide the ability to create loop-free Layer 2 topologies while having redundant links. While connecting multiple bridges or just cross-connecting bridge ports, it's possible to create network loops that can severely impact the stability of the network. Spanning tree protocol aims to resolve this problem by introducing the concept of the root bridge. All bridges in the same Layer 2 domain will exchange information about the shortest path to the root bridge. Afterward, each bridge will negotiate which ports to use to reach the root bridge. This information exchange is done with the help of Bridge Protocol Data Units (BPDUs). STP will disable certain ports for each bridge to avoid loops, while still ensuring that all bridges can communicate with each other. For an in-depth description of the protocol please refer to IEEE 802.1D.

As a best practice, it is always recommended to manually set up each bridge's priority, port priority, and port path cost to ensure proper Layer2 functionality at all times. Leaving STP related values to defaults is acceptable for a network that consists of 1 to 2 bridges running with (R/M)STP enabled, but it is highly recommended to manually set these values for larger networks. Since STP elects a root bridge and root ports by checking STP related values from bridges over the network, leaving STP settings to automatic may elect an undesired root bridge and root ports and in case of a hardware failure can result in an inaccessible network.

:::info
RouterOS bridge does not work with PVST and its variants. The PVST BPDUs (with a MAC destination 01:00:0C:CC:CC:CD) are treated by RouterOS bridges as typical multicast packets. In simpler terms, they undergo RouterOS bridge/switch forwarding logic and may get tagged or untagged.
:::

## Monitoring

---

You can check the STP status of a bridge by using the `/interface/bridge/monitor`  command, for example:

```ros
/interface/bridge/monitor bridge1
                    state: enabled                         
      current-mac-address: 74:4D:28:6F:31:10               
                bridge-id: 0x8000.74:4D:28:6F:31:10        
              root-bridge: no                              
           root-bridge-id: 0.74:4D:28:11:70:6B             
  regional-root-bridge-id: 0.74:4D:28:11:70:6B             
           root-path-cost: 0                               
                root-port: combo1                          
               port-count: 2                               
    designated-port-count: 0                               
        mst-config-digest: 4e22fbb9ede77faa45ec995c4ffa8085
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1      
```

Note that the root bridge doesn't have any root ports, only designated ports.

You can check the STP status of a bridge port by using the `/interface/bridge/port/monitor` command, for example:

```ros
/interface/bridge/port/monitor [find interface=combo1]
                  interface: combo1             
                     status: in-bridge          
                    port-id: 0x80.1             
                       role: root-port          
                  edge-port: no                 
        edge-port-discovery: yes                
        point-to-point-port: yes                
               external-fdb: no                 
               sending-rstp: yes                
                   learning: yes                
                 forwarding: yes                
           actual-path-cost: 2000               
    internal-root-path-cost: 2000               
       designated-bridge-id: 0.74:4D:28:11:70:6B
   designated-internal-cost: 0                  
         designated-port-id: 0x80.1             
  designated-remaining-hops: 20                 
                 bpdu-tx-rx: 3/7791             
        discard-transitions: 0                  
        forward-transitions: 1                  
                   tc-tx-rx: 2/2                
           topology-changes: 1                  
       last-topology-change: 4h19m43s           
           multicast-router: no                 
           hw-offload-group: switch1            
          declared-vlan-ids: 1                  
                             100                
        registered-vlan-ids: 1                  
                             100                
                             200-203     
```

Note that `root-bridge-id` consists of the bridge priority and the bridge's MAC address; for non-root bridges the root bridge will be shown as `designated-bridge`.

:::warning
When using bridges that are set to use 802.1Q as EtherType, they will send out BPDUs to 01:80:C2:00:00:00, which are used by MSTP, RSTP, and STP. When using 802.1ad as the bridge VLAN protocol, the BPDUs are not compatible with 802.1Q bridges and they are sent to 01:80:C2:00:00:08. (R/M)STP will not function properly if there are different bridge VLAN protocols across the Layer2 network.
:::

## STP and RSTP

---

STP and Rapid STP are used widely across many networks, but almost all networks have switched over to using only RSTP because of its benefits. STP is a very old protocol and has a convergence time (the time needed to fully learn network topology changes and to continue properly forwarding traffic) of up to 50 seconds. RSTP has a lot of smaller convergence time, a few seconds or even a few milliseconds. It is recommended to use RSTP instead of STP since it is a lot faster and is also backward compatible with STP. One of the reasons why RSTP is faster is because of reduced possible port states, below is a list of possible STP port states:

- **Forwarding** - port participates in traffic forwarding and is learning MAC addresses, and is receiving BPDUs.
- **Listening** - port does not participate in traffic forwarding and is not learning MAC addresses, and is receiving BPDUs.
- **Learning** - port does not participate in traffic forwarding but is learning MAC addresses.
- **Blocking** - port is blocked since it is causing loops but is receiving BPDUs.
- **Disabled** - port is disabled or inactive.

In RSTP the disabled, listening, and blocking port states are replaced with just one state called the **Discarding** state:

- **Forwarding** - port participates in traffic forwarding and is learning MAC addresses and is receiving BPDUs (forwarding=yes).
- **Learning** - port does not participate in traffic forwarding but is learning MAC addresses (learning=yes).
- **Discarding** - port does not participate in traffic forwarding and is not learning MAC addresses and is receiving BPDUs (forwarding=no).

In STP ports are primarily categorized by states (e.g., Forwarding, Listening, Learning, Blocking, Disabled). Port behavior is determined dynamically based on the spanning tree algorithm but without explicitly assigning roles. The logic of forwarding or blocking traffic is derived from the calculation of Root Bridge, Root Ports, and Designated Ports, but these are considered part of the spanning tree topology rather than formalized port roles. RSTP explicitly defines port roles and introduces the concept of backup paths, which are explicitly represented through the Alternate Port and Backup Port roles. These roles did not exist in STP because STP treated blocked ports generically, without distinguishing their function as potential backups.

Here is a breakdown of the port roles for the RSTP protocol:

- **Root Port** - port that is facing towards the root bridge and has the best (lowest cost) path to the root bridge. Only one root port is elected per bridge (except the root bridge itself).
- **Designated Port** - port that is facing away from the root bridge and forwards traffic away from the root bridge to downstream devices.
- **Alternate Port** - port that is facing towards the root bridge, but is not going to forward traffic. The port provides a backup path to the root bridge if the current root port fails.
- **Backup Port** - port that is facing away from the root bridge, but is not going to forward traffic. The port that serves as a backup for a designated port on the same segment.
- **Disabled Port** - disabled or inactive port.

In STP connectivity between bridges is determined by sending and receiving BPDUs between neighbor bridges. Designated ports are sending BPDUs to root ports. If a BPDU is not received 3 times the **HelloTime** in a row, then the connection is considered unavailable and network topology convergence will commence. It is possible to reduce STP convergence time in certain scenarios by reducing the `forward-delay` timer, which is responsible for how long the port can be in the learning/listening state.

In RouterOS, it is possible to specify which bridge ports are edge ports. Edge ports are ports that are not supposed to receive any BPDUs. This is beneficial since this allows STP to skip the learning and the listening state and directly go to the forwarding state. This feature is sometimes called **PortFast**. You can leave this parameter to the default value, which is **auto**, but you can also manually specify it. You can set a port as an edge port manually for ports that should not have any more bridges behind them. Usually, these are access ports.

Additionally, bridge port `point-to-point` specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property to `yes`, you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits for BPDUs from other devices from this single link. By setting this property to `no`, you are implying that a link can receive BPDUs from multiple devices. By setting the property to `yes`, you are significantly improving (R/M)STP convergence time. In general, you should only set this property to `no`, if it is possible that another device can be connected between a link. This is mostly relevant to Wireless media and Ethernet hubs. If the Ethernet link is full-duplex, `auto` enables point-to-point functionality. This property has no effect when `protocol-mode` is set to `none`.

### Default values

When creating a bridge or adding a port to the bridge the following are the default values that are assigned by RouterOS:

- Default bridge priority: **32768** / **0x8000**
- Default bridge port path cost: **based on interface speed**
- Default bridge port priority: **0x80**
- BPDU message age increment: **1**
- HelloTime: **2**
- Default max message age: **20**

The bridge interface setting `port-cost-mode` changes the port `path-cost` and `internal-path-cost` mode for bridged ports, utilizing automatic values based on interface speed. This setting does not impact bridged ports with manually configured `path-cost`  or `internal-path-cost` properties. Below are examples illustrating the path-costs corresponding to specific data rates (with proportionate calculations for intermediate rates):

| Data rate | Long | Short |
| :-- | :-- | --: |
| 10 Mbps | 2,000,000 | 100 |
| 100 Mbps | 200,000 | 19 |
| 1 Gbps | 20,000 | 4 |
| 10 Gbps | 2,000 | 2 |
| 25 Gbps | 800 | 1 |
| 40 Gbps | 500 | 1 |
| 50 Gbps | 400 | 1 |
| 100 Gbps | 200 | 1 |

For bonded interfaces, the highest `path-cost` among all bonded member ports is applied, this value remains unaffected by the total link speed of the bonding. For virtual interfaces (such as VLAN, EoIP, VXLAN), as well as wifi, wireless, and 60GHz interfaces, a `path-cost` of 20,000 is assigned for long mode, and 10 for short mode. For dynamically bridged interfaces (e.g. wifi, wireless, PPP, VPLS), the `path-cost` defaults to 20,000 for long mode and 10 for short mode. However, this can be manually overridden by the service that dynamically adds interfaces to bridge, for instance, by using the CAPsMAN `datapath.bridge-cost` setting. RouterOS versions prior to 7.13 do not change port path cost based on the link speed, for 10M, 100M, 1000M, and 10000M link speeds the default path cost value when a port is added to a bridge was always **10**.

The age of a BPDU is determined by how many bridges the BPDU has passed times the message age since RouterOS uses **1** as the message age increment, then the BPDU packet can pass as many bridges as specified in the `max-message-age` parameter. By default this value is set to **20**. This means that after the 20th bridge the BPDU packet will be discarded and the next bridge will become a root bridge. Note that if `max-message-age=20` is set, then it is hard to predict which ports will be the designated port on the 21st bridge and may result in traffic not being able to be forwarded properly.

:::warning
In case bridge filter rules are used, make sure you allow packets with DST-MAC address **01:80:C2:00:00:00** since these packets carry BPDUs that are crucial for STP to work properly.
:::

### Election process

To properly configure STP in your network, you need to understand the election process and which parameters are involved in which order. In RouterOS, the root bridge will be elected based on the smallest priority and the smallest MAC address in this particular order:

1. Bridge priority (lowest).
2. Bridge MAC address (lowest).

In RouterOS root ports are elected based on the lowest Root port path cost, lowest bridge identifier, and lowest bridge port ID in this particular order:

1. Root port path cost (lowest)
2. Bridge identifier (lowest)
3. Bridge port ID (lowest)

First, when the device considers which of its ports to elect as the root port, it will check the **root path cost** seen by its ports. If the root path cost is the same for two or more ports then the **Bridge identifier** of the **upstream** device will be checked and the port connected to the lowest bridge identifier will become the root port. If the same bridge identifier is seen on two or more ports, then the **Bridge port ID** of the **upstream** device will be checked.

## Explanation of attributes

Root path cost: all bridges have a Root Path Cost. The root bridge has a root path cost of 0. For all other Bridges, it is the sum of the Port Path Costs on the least-cost path to the Root Bridge. You can modify the local port path cost under `/interface/bridge/port`.
The bridge identifier is a combination of "bridge priority" and "bridge MAC", configurable under `/interface/bridge`.

Bridge port ID is a combination of "unique ID" and "bridge port priority". The unique ID is automatically assigned to the bridge port upon adding it to the bridge. It cannot be edited. It can be seen in WinBox under the "Bridge Port" "Port Number" column, or with `/interface/bridge/port/monitor`, as `port-number`.

:::tip Understanding STP Port Election
Make sure you apply path cost and priority to the correct ports:

- **Path Cost** affects ports facing *towards* the root bridge. (Setting path cost on a root bridge port has no effect).
- **Port Priority** affects ports facing *away* from the root bridge.
- **Bridge Identifier** does not impact the device's own root port election; it affects the root port election for *downstream* devices.
:::

:::warning Bridge Priority Compatibility
RouterOS allows setting any bridge priority value between 0 and 65535. However, the IEEE 802.1W standard strictly requires bridge priorities to be in steps of 4096. To avoid incompatibility with other vendors' equipment, use **only** these priority values:
`0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440`
:::

### Examples

#### Root path cost example

![Root Path](./img/spanning-tree-protocol-01.webp)

This example outlines how the root path cost works. SW1 will be the root bridge, due to it having the lowest priority of 0x1000, as the root bridge. Each bridge will calculate the path cost to the root bridge. When calculating root path cost, bridges take into account the configured path cost on their ports + root path cost advertised by neighboring bridges.

**SW1**: due to it being the root bridge, it advertises a root path cost of 0 to its neighbors, even though it has a configured path cost of 10.

**SW2:****ether1** has a root path cost of 0 + 25=**25**. On the **ether2** path the cost will be 10+10+10+0=**30**

**SW3:** **ether2** has a root path cost of 0 + 10=**10**. On the **ether4** path, the path cost will be 10+5+25+0=**40**

**SW4:** **ether1** has a root path cost of 0+25+5=**30**. On **ether4**, path cost will be 10+10+0=**20**.

The Port with the lowest path cost will be elected as the root port. Every bridge in the STP topology needs a path to the root bridge. After the best path has been found, the redundant path will be blocked, in this case, the path between SW2 and SW4.

:::warning
You can configure path cost on the root bridge, but it will only be taken into account when the bridge loses its root status.
:::

#### STP example

![STP Example 1](./img/spanning-tree-protocol-02.webp)

In this example, we want to ensure Layer2 redundancy for connections from ServerA to ServerB. If a port is connected to a device that is not a bridge and not running (R)STP, then this port is considered as an edge port. In this case, ServerA and ServerB are connected to an edge port. This is possible by using STP in a network. Below are configuration examples for each switch:

- Configuration for SW1:

```ros
/interface/bridge
add name=bridge priority=0x1000
/interface/bridge/port
add bridge=bridge interface=ether1 priority=0x60
add bridge=bridge interface=ether2 priority=0x50
add bridge=bridge interface=ether3 priority=0x40
add bridge=bridge interface=ether4 priority=0x30
add bridge=bridge interface=ether5
```

- Configuration for SW2:

```ros
/interface/bridge
add name=bridge priority=0x2000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- Configuration for SW3

```ros
/interface/bridge
add name=bridge priority=0x3000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
```

- Configuration for SW4:

```ros
/interface/bridge
add name=bridge priority=0x4000
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 path-cost=20
add bridge=bridge interface=ether3
```

In this example, **SW1** is the root bridge since it has the lowest bridge priority. **SW2** and **SW3** have ether1,ether2 connected to the root bridge, and ether3 is connected to **SW4**. When all switches are working properly, the traffic will be flowing from ServerA through SW1\_ether2, through SW2, and through SW4 to ServerB. In the case of **SW1** failure, **SW2** becomes the root bridge because of the next lowest priority, indicated by the dotted line in the diagram. Below is a list of ports and their role for each switch:

- **root-port** - SW2\_ether2, SW3\_ether2, SW4\_ether1
- **alternate-port** - SW2\_ether1, SW3\_ether1, SW4\_ether2
- **designated-port** - SW1\_ether1, SW1\_ether2, SW1\_ether3, SW1\_ether4, SW1\_ether5, SW2\_ether3, SW3\_ether3, SW4\_ether3

:::note
**Note:** According to the 802.1Q recommendations, you should use bridge priorities in steps of 4096. To set a recommended priority, it is more convenient to use hexadecimal notation, for example, 0 is 0x0000, 4096 is 0x1000, 8192 is 0x2000, and so on (0..F).
:::

## Multiple Spanning Tree Protocol

---

Multiple Spanning Tree Protocol (MSTP) is used on a bridge interface to ensure loop-free topology across multiple VLANs. MSTP can also provide Layer2 redundancy and can be used as a load balancing technique for VLANs since it has the ability to have different paths across different VLANs. MSTP is operating very similarly to (R)STP and many concepts from (R)STP can be applied to MSTP and it is highly recommended to understand the principles behind (R)STP before using MSTP, but there are some differences that must be taken into account when designing an MSTP-enabled network.

In case (R)STP is used, the BPDUs are sent across all physical interfaces in a bridge to determine loops and stop ports from being able to forward traffic if it causes a loop. In case there is a loop inside a certain VLAN, (R)STP might not be able to detect it. Some STP variants solve this problem by running an STP instance on every single VLAN (PVST), but this has been proven to be inefficient, and some STP variants solve this problem by running a single STP instance across all VLANs (CST), but it lacks the possibility to do load balancing for each VLAN or VLAN group. MSTP tends to solve both problems by using MST instances that can define a group of VLANs (VLAN mapping) that can be used for load balancing and redundancy, which means that each VLAN group can have a different root bridge and a different path. Note that it is beneficial to group multiple VLANs in a single instance to reduce the number of CPU cycles for each network topology change.

:::danger
In RouterOS with MSTP enabled the bridge priority is the CIST's root bridge priority, as stated in the IEEE 802.1Q standard the bridge priority must be in steps of 4096, the 12 lowest bits are ignored. These are valid bridge priorities: 0, 4096, 8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, 61440. When setting an invalid bridge priority, RouterOS will warn you about it and truncate the value to a valid value, but will save the original value in the configuration since invalid bridge priority values can still be used in (R)STP between devices running RouterOS, though it is recommended to use a valid bridge priority instead.
:::

### MSTP Regions

MSTP works in groups called regions. For each region there will be a regional root bridge, and between regions, there will be a root bridge elected. MSTP will use an Internal Spanning Tree (IST) to build the network topology inside a region and a Common Spanning Tree (CST) outside a region to build the network topology between multiple regions. MSTP combines these two protocols into Common and Internal Spanning Tree (CIST), which holds information about topology inside a region and between regions. From CST's perspective, a region will seemingly be a single virtual bridge, because of this MSTP is considered very scalable for large networks. For bridges to be in the same region, their configuration must match. BPDUs will not include VLAN mappings since they can be large, rather a computed hash is being transmitted. If a bridge receives a BPDU through a port and the configuration does not match, then MSTP will consider that port as a boundary port and that it can be used to reach other regions. Below is a list of parameters that need to match for MSTP to consider a BPDU from the same region:

- Region name
- Region revision
- VLAN mappings to MST Instance IDs (computed hash)

It is possible to create an MSTP enabled network without regions, though to be able to do load balancing per VLAN group it is required for a bridge to receive a BPDU from a bridge that is connected to it with the same parameters mentioned above. In RouterOS the default region name is empty and the region revision is 0, which are valid values, but you must make sure that they match to get multiple bridges in a single MSTP region. A region cannot exist if its bridges are scattered over the network; these bridges must be connected in at least one way, in which they can send and receive BPDUs without leaving the region, for example, if a bridge with different region related parameters is between two bridges that have the same region related parameters, then there will exist at least 3 different MSTP regions.

![MSTP Topology](./img/spanning-tree-protocol-03.webp)

The downside of running every single bridge in a single MSTP region is the excess CPU cycles. In comparison, PVST(+) creates a Spanning Tree Instance for each VLAN ID that exists on the network, since there will be very limited paths that can exist in a network, this approach creates a lot of overhead and unnecessary CPU cycles. This also means that this approach does not scale very well and can overload switches with not very powerful CPUs. MSTP solves this problem by dividing the network into MSTP regions, where each bridge inside this region will exchange and process information about VLANs that exist inside the same region, but will run a single instance of Spanning Tree Protocol in the background to maintain the network topology between regions. This approach has been proven to be much more effective and much more scalable. This means that regions should be used for larger networks to reduce CPU cycles.

In regions, you can define MST Instances, which are used to configure load balancing per VLAN group and to elect the regional root bridge. It is worth mentioning that in each region there exists a pre-defined MST Instance, in most documentation, this is referred to as **MSTI0**· This MST Instance is considered as the default MST Instance. There are certain parameters that apply to this special MST Instance. When traffic passes through an MSTP-enabled bridge, MSTP will look for an MST Instance that has a matching VLAN mapping, but if a VLAN mapping does not exist for a certain VLAN ID, then traffic will fall under **MSTI0**.

:::warning
Since MSTP requires VLAN filtering on the bridge interface to be enabled, then make sure that you have allowed all required VLAN IDs in `/interface/bridge/vlan`, otherwise, the traffic will not be forwarded and it might seem as if MSTP is misconfigured, although this is a VLAN filtering misconfiguration.
:::

### Election process

The election process in MSTP can be divided into two sections, intra-region and inter-region. For MSTP to work properly there will always need to be a regional root, that is the root bridge inside a region, and a CIST root, that is the root bridge between regions. A regional root is the root bridge inside a region, and the regional root bridge will be needed to properly set up load balancing for VLAN groups inside a region. The CIST root will be used to configure which ports will be alternate/backup ports (inactive) and which ports will be root ports (active).

:::warning
Between regions, there is no load balancing per VLAN group, no root port election process, and port blocking between MSTP regions is done the same way as in (R)STP. If CIST has blocked a port that is inside an MSTP region to prevent traffic loops between MSTP regions, then this port can still be active for IST to do load balancing per VLAN group inside an MSTP region.
:::

- The following parameters are involved in electing a regional root bridge or root ports inside an MSTP region:

| Property | Description |
| :-- | :-- |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | `/interface/bridge/msti`, MST Instance priority, used to elect a regional root inside an MSTP region. Must be set in steps of 4096 (0x1000); the 12 lowest bits are ignored. Valid values: 0x0000, 0x1000, 0x2000, ..., 0xf000 (or decimal equivalents: 0, 4096, 8192, ..., 61440). |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port`, path cost to the regional root for unknown VLAN IDs (MSTI0), used on a root port inside an MSTP region. |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; Default: **0x80**) | `/interface/bridge/port/mst-override`, MST port priority for a defined MST Instance, used on a bridge port on the regional root bridge. Must be set in steps of 16 (0x10). |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port/mst-override`, MST port path cost for a defined MST Instance, used on a non-root bridge port inside an MSTP region. |

- The following parameters are involved in electing a CIST root bridge or CIST root ports:

| Property | Description |
| :-- | :-- |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | `/interface/bridge`, CIST bridge priority, used to elect a CIST root bridge. Must be set in steps of 4096 (0x1000); the 12 lowest bits are ignored. |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; Default: **0x80**) | `/interface/bridge/port`, CIST port priority, used on a CIST root bridge to elect CIST root ports. Must be set in steps of 16 (0x10). |
| **path-cost** (*integer: 1..200000000*; Default: ) | `/interface/bridge/port`, CIST port path cost, used on a CIST non-root bridge port to elect CIST root ports. |

:::warning
The sequence of parameters in which MSTP checks to elect root bridge/ports is the same as in (R)STP, you can read more about it in the (R)STP Election Process section.
:::

### MST Instance

**Sub-menu:** `/interface/bridge/msti`

This section is used to group multiple VLAN IDs into a single instance to create a different root bridge for each VLAN group inside an MSTP region.

| Property | Description |
| :-- | :-- |
| **bridge** (*text*; Default: ) | Bridge to which the MST instance is assigned. |
| **identifier** (*integer: 1..31*; Default: ) | MST instance identifier. |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | MST instance priority is used to determine the root bridge for a group of VLANs in an MSTP region. |
| **vlan-mapping** (*integer: 1..4094*; Default: ) | The list of VLAN IDs to assign to the MST instance. This setting accepts the VLAN ID range, as well as comma-separated values. E.g. `vlan-mapping=100-115,120,122,128-130` |

### MST Override

**Sub-menu:** `/interface/bridge/port/mst-override`

This section is used to select the desired path for each VLAN mapping inside an MSTP region.

| Property | Description |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | Whether the entry is disabled. |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | Path cost for an MST instance's VLAN mapping, used on VLANs that are facing towards the root bridge to manipulate path selection; lower path cost is preferred. |
| **identifier** (*integer: 1..31*; Default: ) | MST instance identifier. |
| **priority** (*integer: 0..240*; Default: **128**) | The priority of an MST instance's VLAN, used on VLANs that are facing away from the root bridge to manipulate path selection; lower priority is preferred. |
| **interface** (*name*; Default: ) | Name of the port on which to use configured MST instance's VLAN mappings and defined path cost and priority. |

### Monitoring

Similarly to (R)STP, it is also possible to monitor MSTP status. By monitoring the bridge interface itself it is possible to see the current CIST root bridge and the current regional root bridge for MSTI0. It is also possible to see the computed hash of MST Instance identifiers and VLAN mappings. This is useful when making sure that certain bridges are in the same MSTP region. Below you can find an example of monitoring an MSTP bridge:

```ros
/interface/bridge/monitor bridge
                    state: enabled
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA 
              root-bridge: no
           root-bridge-id: 0x1000.64:D1:54:24:23:72
  regional-root-bridge-id: 0x4000.6C:3B:6B:7B:F0:AA
           root-path-cost: 10
                root-port: ether4
               port-count: 5
    designated-port-count: 3
        mst-config-digest: 74edbeefdbf82cf63a70cf60e43a56f3
             fast-forward: no                              
         multicast-router: yes                             
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1
```

In MSTP it is possible to monitor the MST Instance. This is useful to determine the current regional root bridge for a certain MST Instance and VLAN group. Below you can find an example to monitor an MST Instance:

```ros
/interface/bridge/msti/monitor 1
                    state: enabled
               identifier: 2
      current-mac-address: 6C:3B:6B:7B:F0:AA
                bridge-id: 0x8000.6C:3B:6B:7B:F0:AA
              root-bridge: no
           root-bridge-id: 0.00:00:00:00:00:00
  regional-root-bridge-id: 0x1002.6C:3B:6B:7B:F9:08
           root-path-cost: 0
                root-port: ether2
               port-count: 5
    designated-port-count: 1
```

It is also possible to monitor a certain MST Override entry. This is useful to determine the port role for a certain MST Instance when configuring root ports and alternate/backup ports in an MSTP region. Below you can find an example to monitor an MST Override entry:

```ros
/interface/bridge/port/mst-override/monitor 1
                      port: ether3
                    status: active
                identifier: 2
                   port-id: 0x80.1     
                      role: alternate-port
                  learning: no
                forwarding: no
   internal-root-path-cost: 15
         designated-bridge: 0x1002.6C:3B:6B:7B:F9:08
  designated-internal-cost: 0
        designated-port-id: 0x80.1  
 designated-remaining-hops: 20                      
                tx-rx-bpdu: 3/7991                  
       discard-transitions: 0                       
       forward-transitions: 1                       
                  tx-rx-tc: 2/2                     
          topology-changes: 1                       
```

### MSTP example

Let's say that we need to design a topology and configure MSTP in a way that VLAN 10,20 will be forwarded in one path, but VLAN 30,40 will be forwarded in a different path, while all other VLAN IDs will be forwarded in one of those paths. This can easily be done by setting up MST Instances and assigning port path costs. Below you can find a network topology that needs to do load balancing per VLAN group with 3 separate regions as an example:

![MSTP Example](./img/spanning-tree-protocol-04.webp)

The topology of an MSTP-enabled network with load balancing per VLAN group

Start by adding each interface to a bridge. Initially, you should create a (R)STP bridge without VLAN filtering enabled. This is to prevent losing access to the CPU. Each device in this example is named by the region that it is in (Rx) and a device number (\_x). For larger networks configuring MSTP can be confusing because of the number of links and devices. We recommend using The Dude to monitor and design a network topology.

- Use the following commands on **R1\_1**, **R1\_3**, **R2\_1**, **R2\_3**, **R3\_1**, **R3\_3**:

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
add bridge=bridge interface=ether3
add bridge=bridge interface=ether4
```

- Use the following commands on **R1\_2**, **R2\_2**, **R3\_2**.

```ros
/interface/bridge
add name=bridge protocol-mode=rstp vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
```

- Make sure you allow the required VLAN IDs on these devices. Here we will consider that each device will receive tagged traffic that needs to be load balanced per VLAN group. Use these commands on **R1\_1**, **R1\_3**, **R2\_1**, **R2\_3**, **R3\_1**, **R3\_3**:

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2,ether3,ether4 vlan-ids=10,20,30,40
```

- Use the following commands on **R1\_2**, **R2\_2**, **R3\_2**:

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,ether2 vlan-ids=10,20,30,40
```

:::warning
Make sure you add all the needed VLAN IDs and ports to the bridge VLAN table, otherwise, your device will not forward all required VLANs, and/or you will lose access to the device.
:::

We need to assign a region name for each bridge that we want to be in a single MSTP region. You can also specify the region revision, but it is optional, though they need to match. In this example, if all bridges have the same region name, then they will all be in a single MSTP bridge. In this case, we want to separate a group of 3 bridges in a different MSTP region to do load balancing per VLAN group and to create diversity and scalability:

- Set the appropriate region name (and region revision) for each bridge, and use the following commands on each device (**change the region name!**):

```ros
/interface/bridge
set bridge region-name=Rx region-revision=1
```

After we have created 3 different MSTP regions, we need to decide which device is going to be a regional root for each VLAN group. For consistency, we are going to set the first device (\_1) in each region as the regional root for VLAN 10,20 and the third device (\_3) in each region as the regional root for VLAN 30,40. This can be done by creating an MST Instance for each VLAN group and assigning a bridge priority to it. The MST Instance identifier is only relevant inside an MSTP region, outside an MSTP region, these identifiers can be different and mapped to a different VLAN group.

- Use the following commands on **R1\_1**, **R2\_1**, **R3\_1**:

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x1000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x3000 vlan-mapping=30,40
```

- Use the following commands on **R1\_3**, **R2\_3**, **R3\_3**:

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x3000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x1000 vlan-mapping=30,40
```

- Use the following commands on **R1\_2**, **R2\_2**, **R3\_2**.

```ros
/interface/bridge/msti
add bridge=bridge identifier=1 priority=0x2000 vlan-mapping=10,20
add bridge=bridge identifier=2 priority=0x2000 vlan-mapping=30,40
```

Now we need to override the port `path-cost` and/or port priority for each MST Instance. This can be done by adding an MST-Override entry for each port and each MST Instance. To achieve that for a certain MST Instance the traffic flow path is different, we simply need to make sure that the port path cost and/or priority is larger. We can either increase the port path cost or decrease the port path cost for ports that are facing toward the regional root bridge. It doesn't matter if you increase or decrease all values; it is important that in the end, one port's path cost is larger than the other's.

- Use the following commands on **R1\_1**, **R2\_1**, **R3\_1**:

```ros
/interface/bridge/port/mst-override
add identifier=2 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=15
```

- Use the following commands on **R1\_2**, **R2\_2**, **R3\_2**:

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether1 internal-path-cost=5
add identifier=2 interface=ether2 internal-path-cost=9
```

- Use the following commands on **R1\_3**, **R2\_3**, **R3\_3**:

```ros
/interface/bridge/port/mst-override
add identifier=1 interface=ether2 internal-path-cost=5
add identifier=1 interface=ether3 internal-path-cost=9
```

In this case for VLAN 10,20 to reach the third device from the first device, it would choose between ether1 and ether2, one port will be blocked and set as an alternate port, and ether1 will have path cost as `5+9=14` and ether2 will have path cost as `10`, ether2 will be elected as the root port for MSTI1 on the third device. In case for VLAN 30,40 to reach the first device from the third device, ether1 will have path cost as `5+9=14` and ether2 will have path cost as `15`, ether1 will be elected as the root port for MSTI2 on the third device.

Now we can configure the root ports for **MSTI0**, which will fall under all VLANs that are not assigned to a specific MST Instance, like in our example VLAN 10,20, and VLAN 30,40. To configure this special MST Instance, you will need to specify `internal-path-cost` for a bridge port. This value is only relevant to MSTP regions, it does not have any effect outside an MSTP region. In this example we will choose that all unknown VLANs will be forwarded over the same path as VLAN 30,40, we will simply increase the path cost on one of the ports.

- Use the following commands on **R1\_3**, **R2\_3**, **R3\_3**:

```ros
/interface/bridge/port
set [find where interface=ether3] internal-path-cost=25
```

At this point, a single region MSTP can be considered configured, and in general, MSTP is fully functional. It is highly recommended to configure the CIST part, but for testing purposes, it can be left with the default values. Before doing any tests, you need to enable MSTP on all bridges.

- Use the following commands on **all** devices:

```ros
/interface/bridge
set bridge protocol-mode=mstp vlan-filtering=yes
```

When MSTP regions have been configured, you can check if they are properly configured by forwarding traffic, for example, sending tagged traffic from the first device to the third device and changing the VLAN ID for the tagged traffic to observe different paths based on VLAN ID. When this is working as expected, then you can continue to configure CIST-related parameters to elect a CIST root bridge and CIST root ports. For consistency, we will choose the first device in the first region to be the CIST root bridge and to ensure consistency in case of failure, we can set a higher priority to all other bridges.

- Use the following commands on **R1\_1:**

```ros
/interface/bridge
set bridge priority=0x1000
```

- Use the following commands on **R1\_2**:

```ros
/interface/bridge
set bridge priority=0x2000
```

- ...

- Use the following commands on **R3\_3**:

```ros
/interface/bridge
set bridge priority=0x9000
```

We also need to elect a root port on each bridge; for simplicity, we will choose the port that is closest to **R1\_1** as the root port and has the fewest hops. At this point, the procedure to elect root ports is the same as the procedure in (R)STP.

- Use the following commands on **R3\_3:**

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=30
set [find where interface=ether3] path-cost=40
set [find where interface=ether4] path-cost=20
```

- Use the following commands on **R1\_3** and **R2\_3:**

```ros
/interface/bridge/port
set [find where interface=ether2] path-cost=20
set [find where interface=ether3] path-cost=30
```

- Use the following commands on **R1\_2**:

```ros
/interface/bridge/port
set [find where interface=ether1] path-cost=30
```
