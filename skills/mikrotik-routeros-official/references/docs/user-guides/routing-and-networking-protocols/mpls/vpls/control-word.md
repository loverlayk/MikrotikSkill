# Control Word

> VPLS uses Control Words (CW) for packet fragmentation and reassembly in RouterOS, adding 4-byte overhead to handle L2MTU limitations. CW fields include flags, fragmentation indicators, length, and sequence numbers...

# Control Word

VPLS allows remote sites to share an Ethernet broadcast domain by connecting sites through **pseudo-wires (PW)** tunnels over a packet switching network (PSN). Since VPLS encapsulation adds additional overhead, each interface in the LSP should be able to transmit a large enough packet.

Each ethernet chipset has hardware limitations on the maximum packet size that it can transmit. Even now there are Ethernets that support only one Vlan tag, meaning that the maximum packet size without Ethernet header and checksum (L2MTU) is 1504 bytes. Obviously, it is not enough to forward a VPLS encapsulated Ethernet frame without fragmentation (at least 1526 L2MTU support is required). See [MTU in RouterOS](../../../../hardware/mtu-in-routeros.md) for maximum supported L2MTUs on RouterBOARDs.

Since not even all RouterBOARDs support enough L2MTU to transmit a VPLS encapsulated packet without fragmentation, RouterOS has added Pseudowire Fragmentation and Reassembly (PWE3) support according to RFC 4623 using 4-byte **Control Word (CW)**.

## Control Word Usage

In RouterOS, Control Word is used for packet fragmentation and reassembly inside the VPLS tunnel. This is done by utilizing the optional **Control Word (CW)**. CW is added between the PW label (demultiplexor) and the packet payload and adds an additional 4-byte overhead.

:::warning
Reordering OOO packets is not implemented, out of order fragments will be dropped
:::

CW usage is controlled by the `use-control-word` parameter in VPLS configuration.

![](img/VPLS_CW_light.jpg#gh-light-mode-only)
![](img/VPLS_CW_dark.png#gh-dark-mode-only)

As you can see **Control Word** is divided into 5 fields:

- 0000 - 4-bit identifies that the packet is PW (not IP).
- Flags - 4bits.
- Frag - 2bits value that indicates payload fragmentation.
- Len - 6bits.
- Seq - 16bits sequence number used to detect packet loss / misordering.

According to RFC, generation and processing of sequence numbers are optional.
