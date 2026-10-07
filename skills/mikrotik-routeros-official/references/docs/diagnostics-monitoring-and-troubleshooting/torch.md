# Torch

> Torch shows the traffic that passes one interface right now, grouped into flows by address, protocol, port and DSCP, with the rate in each direction. Find the host that uses the bandwidth, watch one protocol or port,...

# Torch

Torch shows the traffic that passes one interface right now. It groups the packets into flows, one row for each combination of addresses, protocol, ports and DSCP value, and shows the rate of each flow in both directions. Use it to find out who uses a link, which protocols run over it, or whether the packets of a connection arrive at all.

Torch sees received packets before the firewall filters them, so traffic that a firewall rule drops still appears on the interface it arrives on. Packets the router sends are counted as they leave, so traffic dropped in the forward chain does not appear on the outgoing interface. While Torch runs, the router turns IP fast path and FastTrack off, as it does for the [packet sniffer](packet-sniffer); on a busy router the CPU load rises for that time. To see the contents of packets or save them to a file, use the packet sniffer instead.

Torch runs until you stop it with <kbd>Control</kbd>+<kbd>C</kbd>. To stop it after a set time, add `duration`, for example `duration=10s`.

Watch the [video about Torch](https://youtu.be/45E2uwI3xhc).

## See what passes an interface

Give Torch the interface to watch. The interface name can be given without `interface=`:

```ros
/tool/torch bridge
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, SRC-PORT, DST-ADDRESS, DST-PORT, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    SRC-PORT  DST-ADDRESS   DST-PORT        TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21            192.168.88.1                  197.3kbps  197.3kbps          48          48
ip            tcp             0  192.168.88.20     58910  192.168.88.1  2000 (btserv)   1152bps    1152bps             2           2
ip            udp             0  192.168.88.20      2257  192.168.88.1  2001 (glimpse)  2.0Mbps    0bps              172           0
```

The table updates every second until you stop Torch. In this example, 192.168.88.21 pings the router, and 192.168.88.20 runs a bandwidth test in which it receives 2 Mbps from the router.

Each row is one flow between two addresses:

- `SRC-ADDRESS` and `SRC-PORT` - The address and port on the far side of the interface: the side whose traffic the interface receives. This holds even when the router started the conversation, and for traffic that the router forwards.
- `DST-ADDRESS` and `DST-PORT` - The other end of the flow. Port numbers are shown with their service names, such as `2000 (btserv)`.
- `RX` - The rate of the traffic that the interface receives from `SRC-ADDRESS`, in bits per second.
- `TX` - The rate of the traffic that the interface sends towards `SRC-ADDRESS`, in bits per second.
- `TX-PACKETS` and `RX-PACKETS` - The same two directions in packets per second.

A column appears only when a flow has a value for it: the port columns appear only when TCP or UDP flows are present.

## Find the host that uses the bandwidth

On the LAN interface, `SRC-ADDRESS` is the LAN host, so `TX` is what the host downloads and `RX` what it uploads. The rows with the highest rates show who uses the connection. A host with many connections, such as a web browser, has many rows; filter by its address to see them together. Watch the LAN interface, not the WAN interface: after source NAT, the flows on the WAN interface have the router's public address instead of the hosts' addresses.

To watch one host, filter by its address:

```ros
/tool/torch bridge src-address=192.168.88.21/32
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21  192.168.88.1  197.3kbps  197.3kbps          48          48
```

The address filters match the columns as Torch shows them: `src-address` matches `SRC-ADDRESS`, the far side of the interface, and `dst-address` matches `DST-ADDRESS`. On a LAN interface, filter the hosts with `src-address`; `dst-address` set to a LAN host usually matches nothing there. For IPv6, use `src-address6` and `dst-address6`.

## Watch one protocol or port

To show only one IP protocol or one port, use `ip-protocol` and `port`:

```ros
/tool/torch bridge ip-protocol=tcp port=443
```

`port` matches either `SRC-PORT` or `DST-PORT`. It takes one port or `any`; a list such as `port=80,443` fails with `expected end of command`. The port filter applies only to flows that have ports: flows without ports, such as ICMP, still appear with a port filter.

## Check VLAN tags and DSCP marking

On an interface that carries tagged VLANs, Torch adds a `VLAN-ID` column for the tagged traffic. To check that traffic arrives in the right VLAN with the right DSCP value, for example voice traffic in VLAN 99 with DSCP 46 (Expedited Forwarding), watch the parent interface. In this example, a test ping marked with DSCP 46 runs in VLAN 99:

```ros
/tool/torch ether1
```

```text
Columns: VLAN-ID, MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
VLAN-ID  MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS   DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
     99  ip            icmp           46  198.51.100.1  198.51.100.2  237.3kbps  235.7kbps          48          48
         ip            icmp            0  203.0.113.1   203.0.113.2   120.5kbps  120.5kbps          48          48
```

The first row is tagged with VLAN 99 and marked with DSCP 46; the second row is untagged. `vlan-id=99` or `dscp=46` shows only the matching flows. On the VLAN interface itself, the frames are already untagged, so the `VLAN-ID` column does not appear there. For an untagged device, such as a phone on a bridge port, watch the bridge and filter by the phone's address, for example `src-address=192.168.88.30/32`.

The DSCP value is part of a flow, so when the two directions of a conversation are marked differently, they show as two rows: one with only `RX` and one with only `TX`. Here the requests arrive with DSCP 46 and the answers leave with DSCP 0:

```ros
/tool/torch ether1
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS  DST-ADDRESS  TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  203.0.113.1  203.0.113.2  165.6kbps  0bps               50           0
ip            icmp           46  203.0.113.1  203.0.113.2  0bps       165.6kbps           0          50
```

Torch does not show the VLAN priority (PCP) of the frames; use the [packet sniffer](packet-sniffer) to check it.

## See traffic that the firewall drops

Torch counts packets before the firewall, so it shows traffic that a firewall rule drops. In this example, a rule in the input chain drops the pings from 192.168.88.21:

```ros
/tool/torch bridge src-address=192.168.88.21/32
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX    RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21  192.168.88.1  0bps  197.3kbps           0          48
```

The requests arrive (`RX`), and the router sends nothing back (`TX` is 0). The same picture, with traffic in one direction only, also shows a connection whose replies take another path or never come, so check the counters of the rule itself to confirm that it drops the traffic: `/ip/firewall/filter/print stats` (see [Filter](../firewall-and-quality-of-service/firewall/filter)).

## See which CPU handles the traffic

On routers with several CPUs, `cpu=any` adds a `CPU` column, with one row for each CPU that handled packets of a flow. Use it to see whether one heavy flow keeps a single CPU busy:

```ros
/tool/torch bridge cpu=any
```

```text
Columns: CPU, MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
CPU  MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
  0  ip            icmp            0  192.168.88.20  192.168.88.1  170.3kbps  389.3kbps          21          48
  0  ip            icmp            0  192.168.88.21  192.168.88.1  201.4kbps  201.4kbps          49          49
  1  ip            icmp            0  192.168.88.20  192.168.88.1  32.4kbps   0bps                4           0
  3  ip            icmp            0  192.168.88.20  192.168.88.1  186.5kbps  0bps               23           0
```

Here the router's pings to 192.168.88.20 leave from CPUs 0, 1 and 3, and the replies are received on CPU 0.

## Technical details

### Fast path

While Torch runs, the router turns IP fast path and FastTrack off for all traffic, not only on the watched interface. Both come back on when Torch stops.

### Traffic that Torch does not see

Torch sees the packets that reach the router's CPU on the watched interface:

- On a bridge with hardware offloading, the switch chip forwards traffic between ports without the CPU, so Torch does not see it. Unknown unicast, broadcast and some multicast traffic still reach the CPU and remain visible. See [Packet flow with hardware offloading and MAC learning](../bridging-and-switching/user-guides/layer2-misconfiguration#packet-flow-with-hardware-offloading-and-mac-learning).
- With [L3 hardware offloading](../bridging-and-switching/l3-hardware-offloading), routed traffic that the switch chip forwards does not reach the CPU either.
- Unicast traffic between wireless clients with client-to-client forwarding enabled is not visible to Torch.

Torch shows protocols and IP addresses, not MAC addresses. To find the MAC address of a host, see its lease in the [DHCP server](../network-management/dhcp/server#leases).

For all parameters, see [`/tool/torch`](../cli-reference/tool/torch) in the CLI reference.
