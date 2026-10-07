# Understanding OSPF

> Overview of OSPF protocol basics.

# Understanding OSPF

OSPF is an Interior Gateway Protocol (IGP) designed to distribute routing information between routers in the same Autonomous System (AS).

The protocol is based on link-state technology with several advantages over distance-vector protocols such as RIP:

- No hop count limitations exist.
- Multicast addressing sends routing information updates.
- Updates are sent only when network topology changes occur.
- Networks are logically defined by dividing routers into areas.
- External routes injected into the AS are transferred and tagged.

However, OSPF has some disadvantages:

- OSPF is CPU and memory intensive because the SPF algorithm must maintain multiple copies of routing information.
- It is more complex to implement than RIP.

## Terminology

Review the following terms to understand how OSPF operates. You will encounter these terms throughout the documentation.

- **Neighbor**: A connected (adjacent) router running OSPF with the adjacent interface assigned to the same area. Hello packets discover neighbors unless you configure neighbors manually.
- **Adjacency**: A logical connection between a router and its corresponding DR and BDR. Routers do not exchange routing information unless adjacencies are formed.
- **Link**: A network or router interface assigned to any given network.
- **Interface**: A physical interface on the router. When you add the interface to OSPF, it becomes a link used to build the link database.
- **LSA**: Link State Advertisement, a data packet with link-state and routing information shared among OSPF neighbors.
- **DR**: Designated Router, a router chosen to minimize the number of adjacencies formed. OSPF uses this option in broadcast networks.
- **BDR**: Backup Designated Router, a hot standby for the DR. The BDR receives all routing updates from adjacent routers but does not flood LSA updates.
- **[Area](./areas-and-virtual-links.md)**: A logical grouping to establish a hierarchical network.
- **ABR**: Area Border Router, a router connected to multiple areas. ABRs are responsible for summarization and update suppression between connected areas.
- **ASBR**: Autonomous System Boundary Router, a router connected to an external network (in a different AS). A router becomes an ASBR when you import routes from other protocols into OSPF on that router.
- **NBMA**: Non-broadcast multi-access networks. These networks allow multi-access but have no broadcast capability. You must configure OSPF neighbors manually on these networks.
- **Broadcast**: A network with broadcast capability. For example, Ethernet.
- **Point-to-point**: A network type where DRs and BDRs are not required.
- **Router-ID**: An IP address used to identify the OSPF router. If you do not configure the OSPF [`router-id`](../../../../cli-reference/routing/ospf/instance.md#router-id) manually, the router uses one of its assigned IP addresses as its Router-ID.
- **Link State**: The status of a link between two routers. It defines the relationship between a router's interface and its neighboring routers.
- **Cost**: A value assigned to each link by link-state protocols. The [`cost`](../../../../cli-reference/routing/ospf/interface-template.md#cost) value depends on the speed of the media. Each router interface has an associated cost on its output side, referred to as the interface output cost.
- **Autonomous System**: A group of routers that use a common routing protocol to exchange routing information.

## Supported standards

- RFC [2328](https://tools.ietf.org/html/rfc2328) - OSPF Version 2
- RFC [3101](https://tools.ietf.org/html/rfc3101) - The OSPF Not-So-Stubby Area (NSSA) Option
- RFC [3630](https://tools.ietf.org/html/rfc3630) - Traffic Engineering (TE) Extensions to OSPF Version 2
- RFC [4577](https://tools.ietf.org/html/rfc4577) - OSPF as the Provider/Customer Edge Protocol for BGP/MPLS IP Virtual Private Networks (VPNs)
- RFC [5329](https://tools.ietf.org/html/rfc5329) - Traffic Engineering Extensions to OSPF Version 3
- RFC [5340](https://tools.ietf.org/html/rfc5340) - OSPF for IPv6
- RFC [5643](https://tools.ietf.org/html/rfc5643) - Management Information Base for OSPFv3
- RFC [6549](https://tools.ietf.org/html/rfc6549) - OSPFv2 Multi-Instance Extensions
- RFC [6565](https://tools.ietf.org/html/rfc6565) - OSPFv3 as a Provider Edge to Customer Edge (PE-CE) Routing Protocol
- RFC [6845](https://tools.ietf.org/html/rfc6845) - OSPF Hybrid Broadcast and Point-to-Multipoint Interface Type
- RFC [7471](https://tools.ietf.org/html/rfc7471) - OSPF Traffic Engineering (TE) Metric Extensions
