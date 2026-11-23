# Load Balancing

> Load balancing in RouterOS: use two or more links at the same time, the difference between per-connection and per-packet balancing, which method does which, and a simple failover example.

# Load Balancing

Load balancing spreads traffic over two or more links. A router with two internet links can use both at the same time, and keep working when one of them fails.

There are two kinds of balancing:

- **Per-connection.** All packets of one connection use the same link. This is the only kind that works when you control one end only, for example a home or office router with two internet providers: the other end sees each connection from one public address.
- **Per-packet.** The packets of one connection can use different links. This works reliably, especially for TCP and encrypted connections, only when you control both ends of the links.

| Method |  | Per-connection | Per-packet |
| :-- | :-- | :-- | :-- |
|  Firewall Mangle | Nth | **Yes** | **Yes** |
|  | PCC (Per Connection Classifier) | **Yes** | No |
|  | Other matchers | **Yes** | **Yes** |
| ECMP (Equal Cost Multi-Path) |  | **Yes** | **No** |
| Bonding |  | No | **Yes** |
| OSPF |  | **Yes** | No |
| BGP |  | **Yes** | No |

| You want to | See |
| :-- | :-- |
| Use the second internet link only when the first fails | [Failover (WAN Backup)](failover-wan-backup) |
| Use two internet links at the same time | [Per connection classifier](per-connection-classifier) |
| Join several links between two of your own devices | [Bonding](../bonding) |
| Balance over equal routes of a routing protocol | [OSPF](../../user-guides/routing-and-networking-protocols/unicast/ospf/) |
| Mark packets and connections for your own balancing rules | [Mangle](../../firewall-and-quality-of-service/firewall/mangle) |

## Simple failover

The simplest setup with two gateways uses one gateway and changes to the other when the first one fails. Give the second route a larger `distance`, and add `check-gateway` to the routes:

```ros
/ip/route/add gateway=192.168.1.1 distance=1 check-gateway=ping
/ip/route/add gateway=192.168.2.1 distance=2 check-gateway=ping
```

The router pings the gateway of each route. When the first gateway does not answer, its route becomes inactive and the second route takes over. When the first gateway answers again, its route is active again and the second is the backup. [Failover (WAN Backup)](failover-wan-backup) has the complete setup and a way to check the path behind the gateway.

## In this section

<DocCardList />
