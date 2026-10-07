# Load Balancing

> Network load balancing in MikroTik RouterOS allows distributing traffic across multiple links without dynamic routing, with options for per-connection or per-packet methods. The documentation includes setup examples...

# Load Balancing

- [Failover (WAN Backup)](./failover-wan-backup.md)
- [Firewall Marking](../../firewall-and-quality-of-service/firewall/mangle.md)
- [Bonding Load Balancing](../bonding.md)
- [OSPF Load Balancing](../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md)
- [Per connection classifier](./per-connection-classifier.md)

## Introduction

Network load balancing is the ability to balance traffic across two or more links.

There are two types of balancing methods:

- per-packet - each packet of a single stream can be forwarded over different links. This method will work reliably especially on TCP and secure connections only when you are able to control both balancing endpoints.
- per-connection - all packets of the same connection (stream) are always sent over one link. This method is mandatory in setups where only one end of the balancing is under our control, for example, a home router with multiple WAN connections.

| Method |  | Per-connection | Per-packet |
| :-- | :-- | :-- | :-- |
|  Firewall Mangle | Nth | **Yes** | **Yes** |
|  | PCC (Per Connection Classifier) | **Yes** | No |
|  | Other matchers | **Yes** | **Yes** |
| ECMP (Equal Cost Multi-Path) |  | **Yes** | **No** |
| Bonding |  | No | **Yes** |
| OSPF |  | **Yes** | No |
| BGP |  | **Yes** | No |

## Simple Failover Example

The simplest failover setup would be to use multiple gateways when one gateway is active and another one takes over when the first one fails.

To make this work, configure a larger **distance** value for the secondary one, and **check-gateway** for the first one:

```ros
/ip/route/add gateway=192.168.1.1 distance=1 check-gateway=ping
/ip/route/add gateway=192.168.2.1 distance=2
```

The *check-gateway* will make sure the gateway is up only when actual traffic can reach the gateway. When the ping fails the first gateway will become inactive and the second one will take over,  and when the first gateway recovers  it will become active and make the second gateway work again as a backup.

## Related topics

<DocCardList />
