# Group Management Protocol

> Group Management Protocol enables interfaces to receive multicast streams without dedicated clients, supporting IGMP and MLD protocols. It allows testing multicast routing by sending membership reports and responding...

# Group Management Protocol

The Group Management Protocol allows any of the interfaces to become a receiver for the multicast stream. It allows testing the multicast routing and switching setups without using dedicated IGMP or MLD clients. The option has been available since RouterOS v7.4 and it supports IGMP v1, v2, v3 and MLD v1, v2 protocols.

Interfaces are using IGMP v3 and MLD v2 by default. In case IGMP v1, v2 or MLD v1 queries are received, the interfaces will fall back to the appropriate version. Once the Group Management Protocol is created on the interface, it will send an unsolicited membership report (join) packet and respond to query messages. If the configuration is removed or disabled, the interface will send a leave message.

## Examples

---

This example shows how to configure a simple multicast listener on the interface.

First, add an IP address on the interface:

```ros
/ip/address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
```

Then configure Group Management Protocol on the same interface:

```ros
/routing/gmp
add groups=229.1.1.1 interfaces=ether1
```

It is now possible to check your multicast network to see if routers or switches have created the appropriate multicast forwarding entries and whether multicast data is being received on the interface (see the interface stats, or use a [Packet Sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) and [Torch](../../../diagnostics-monitoring-and-troubleshooting/torch.md)).
