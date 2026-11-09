# Policy Routing

> Policy routing in RouterOS allows steering traffic based on criteria to specific gateways, using custom routing tables and rules. It supports dynamic routing decisions with firewall mangle marking or basic routing...

# Policy Routing

Policy routing steers traffic that matches criteria to a specific gateway. Use it to force selected customers or protocols, such as HTTP traffic, to always use a particular gateway. It can also route local and overseas traffic through different gateways.

RouterOS provides these components for policy routing:

- Routing tables.
- Routing rules.
- Firewall mangle marking.

## Routing Tables

A router can have multiple routing tables, each with its own routes for the same destination and different gateways.

See and configure tables from the `/routing/table` menu.

By default, RouterOS has only the **main** routing table:

```text
[admin@rack1_b33_CCR1036] /routing/table> print
Flags: D - dynamic; X - disabled, I - invalid; U - used
0 D name="main" fib

```

Define a custom routing table in this menu before using it elsewhere in the configuration.

Consider a basic example with two gateways, 172.16.1.1 and 172.16.2.1, and a route for 8.8.8.8 in the routing table named **myTable** that uses gateway 172.16.2.1:

```ros
/routing/table/add name=myTable fib
/ip/route/add dst-address=8.8.8.8 gateway=172.16.1.1
/ip/route/add dst-address=8.8.8.8 gateway=172.16.2.1@main routing-table=myTable
```

:::tip
For a user-created table to be able to resolve the destination, the main routing table should be able to resolve the destination too.
:::

In this example, the **main** routing table should also include a route to 8.8.8.8 or at least a default route. Because DHCP dynamically adds the default route for safety, add 8.8.8.8 explicitly to the main table.

```text
[admin@rack1_b33_CCR1036] /ip/route> print detail Flags: D - dynamic; X - disabled, I - inactive, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, y - cop
y;
H - hw-offloaded; + - ecmp
   DAd   dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10
         vrf-interface=ether8 suppress-hw-offload=no

 0  As   dst-address=8.8.8.8/32 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

    DAc   dst-address=172.16.1.0/24 routing-table=main gateway=ether8 immediate-gw=ether8
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.1.2%ether8

    DAc   dst-address=172.16.2.0/24 routing-table=main gateway=ether7 immediate-gw=ether7
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.2.2%ether7

 1  As   dst-address=8.8.8.8/32 routing-table=myTable pref-src="" gateway=172.16.2.1
         immediate-gw=172.16.2.1%ether7 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

```

The configuration above is not enough. You need a way to force traffic to use the new table. RouterOS provides two options:

- firewall mangle - gives more control over the criteria used to steer traffic, such as per connection or per packet balancing. For examples, see [Firewall Marking](../../firewall-and-quality-of-service/firewall/mangle.md).
- routing rules - a basic set of parameters for quickly steering traffic. This example uses routing rules.

Do not use both methods at the same time unless necessary. If mangle and routing rules are used together, mangle by default has higher priority. If mangle-marked traffic can be resolved in the table, routing rules never see that traffic. The order of execution can be [changed](./routing-decision.md#routing-table-lookup).

:::warning
Routing table count is limited to 4096 unique tables.
:::

## Routing Rules

Routing rules steer traffic based on basic parameters such as source address, destination address, in-interface, and others.

In this example, select traffic destined for 8.8.8.8 and prevent fallback to the **main** table:

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable
```

If a customer is connected to ether4 and only that customer should route 8.8.8.8 to a specific gateway, use this rule:

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable interface=ether4
```

If the gateway used in the table goes down, the lookup fails and the destination becomes unreachable. In active-backup setups, allow traffic to fall back to the **main** table by changing the action from `lookup-only-in-table` to `lookup`.

Routing rules can also act as a basic firewall. For example, to block a customer on ether4 from accessing 192.168.1.0/24:

```ros
/routing/rule/add dst-address=192.168.1.0/24 interface=ether4 action=drop
```

## Example: Send one device through a second WAN

The router has two internet connections: WAN1 on ether1, with the default route from its DHCP client, and WAN2 on ether2, with the gateway 10.20.0.1. All devices on the LAN, 192.168.88.0/24, use WAN1, except 192.168.88.50, which must use WAN2. Give the device a fixed address, so the rule keeps matching it (see [Give a device a fixed address](../../network-management/dhcp/server#give-a-device-a-fixed-address)).

1. Create a routing table with a default route through WAN2. With `check-gateway=ping`, the route becomes inactive when the gateway stops answering:

   ```ros
   /routing/table/add name=to-wan2 fib
   /ip/route/add dst-address=0.0.0.0/0 gateway=10.20.0.1 routing-table=to-wan2 check-gateway=ping
   ```

2. Send the traffic of the device to the table:

   ```ros
   /routing/rule/add src-address=192.168.88.50/32 action=lookup table=to-wan2
   ```

   With `action=lookup`, the device falls back to WAN1 while the route through WAN2 is inactive. To keep it off WAN1, use `lookup-only-in-table`.

3. Masquerade the traffic that leaves through WAN2, as for WAN1:

   ```ros
   /ip/firewall/nat/add chain=srcnat out-interface=ether2 action=masquerade
   ```

The rule sends all traffic of the device to the table, including traffic to other networks on the router, such as a guest LAN or the network of the WAN1 modem. To reach such a network directly, add a rule for it before the first rule:

```ros
/routing/rule/add dst-address=192.168.1.0/24 action=lookup-only-in-table table=main place-before=0
```

Connections the device opened before you added the rule can keep using WAN1 until they end. To check the path, run a traceroute on the device: the hop after the router is the WAN2 gateway.
