# FAQ

> Frequently asked questions.

# FAQ

## Neighbors Stuck in Init State or Frequently Flapping

The most common misconfiguration reasons:

- [`router-id`](../../../../cli-reference/routing/ospf/instance.md#router-id) is not unique.
- A firewall is blocking OSPF protocol or multicast addresses used by OSPF.
- NAT is configured and is changing OSPF packets.

The most common network problems:

- Neighbors are connected via an L2 device that blocks or modifies multicast packets.
- Neighbors are connected via a wireless link, which cannot reliably deliver multicast packets.
The solution for both of these cases is to configure NBMA.
