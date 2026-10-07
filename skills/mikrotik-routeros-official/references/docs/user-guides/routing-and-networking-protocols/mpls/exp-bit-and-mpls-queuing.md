# EXP bit and MPLS Queuing

> This page explains the EXP bit in MPLS packets and how RouterOS handles it for QoS, including priority marking, queuing strategies, and MPLS mangle rules. It details how EXP bits are treated during packet switching,...

# EXP bit and MPLS Queuing

When the MPLS label is attached to the packet, it increases the packet length by 32 bits (4 bytes). These 32 bits are broken down as follows:

- Label value itself (20 bits).
- EXP ("experimental") field (3 bits).
- Time to live field (8 bits).
- Bottom of stack field (1 bit).

MPLS standards do not specify the use of "experimental" bits, but the most common use is to carry QoS information, similar to 802.1q priority in the VLAN tag. The EXP field contains only 3 bits, which means it can carry values from 0 to 7, allowing for 8 traffic classes.

## EXP field treatment in RouterOS

When RouterOS receives an MPLS packet, it sets the "ingress priority" value for the packet to the value carried inside the top label. "Ingress priority" is not a field inside packet headers—it is an additional mark that RouterOS assigns to a packet while processing it. When RouterOS labels an MPLS packet, it sets EXP bits to the "priority" (not "ingress priority") assigned to the packet. When RouterOS switches an MPLS packet, it automatically copies "ingress priority" to "priority". This way, regular MPLS switching communicates priority information over the entire label switched path.

Additional info on "ingress priority" and "priority" handling is also in [WMM and VLAN priority](../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md).

The EXP field behavior depends on the action taken on the packet:

- If RouterOS MPLS switches the packet (by popping the label and pushing a new one), the EXP field in the new label matches the received label because:
  - RouterOS sets "ingress priority" to the EXP bits in the received label.
  - Switching automatically sets "priority" to "ingress priority".
  - RouterOS labels the packet with a new label and sets its EXP bits to the value in "priority".
- If RouterOS MPLS switches the packet by using penultimate-hop-popping (the router pops the received label and does not push a new one), the EXP field priority remains in the "priority" field of the packet. Other MAC protocols, such as WMM or 802.1q VLAN, can then use this value:
  - RouterOS sets "ingress priority" to the EXP bits in the received label.
  - Switching automatically sets "priority" to "ingress priority".
  - RouterOS switches the packet to the next hop without pushing a label, and this occurs over the VLAN interface.
  - The VLAN interface sets the 802.1q priority in the VLAN header to the "priority" value of the packet.

Penultimate-hop-popping can lose QoS information carried over the label switched path at the last hop. If you need to preserve this information, disable penultimate-hop-popping by using the Explicit NULL label instead of the Implicit NULL label for the last hop in the label switched path. MPLS TE tunnels use the Explicit NULL label for the last hop by default.

- If RouterOS sends a packet over a label switched path (the router pushes the first label onto the packet), it sets EXP bits to the value in "priority". You can set this value properly using firewall rules or other means (for example, from the DSCP field in the IP header).
- If RouterOS receives a packet for local processing, it sets "ingress priority" to the EXP field of the received packet. You can then use this value to update the DSCP field of the packet or set "priority" from "ingress priority" using firewall rules.

## MPLS Mangle and Queuing

The RouterOS firewall works only with IP traffic, which means you cannot mark MPLS packets directly in mangle and limit them by queues. You must perform queuing on the ingress edge router before adding the MPLS header or on the egress edge router after removing the MPLS label.

Starting from ROS v7.17, RouterOS includes MPLS Mangle. This feature allows you to add a packet mark based on the EXP bit or change the assigned EXP bit on label switching (P) routers or on PE output after MPLS encapsulation.

This configuration is accessible from the `/mpls/mangle` menu.

### Basic Example

Let's look at a very basic example where on the label switching router (P) along the LSP we want to mark packets with exp bit 0, limit the bandwidth and change exp bit to 3:

```routeros
/mpls/mangle
add chain=forward exp=0 set-exp=3 set-mark=m0

/queue/tree
add limit-at=10M max-limit=10M name=mpls_queue packet-mark=m0 parent=sfp-sfpplus2
```

MPLS packets cannot be queued with queues that use IMQ interfaces (simple queue, queue tree global). You must use a queue tree with a "real" interface as the parent.

The MPLS Mangle table displays the matched packet count, which is useful for debugging your setup:

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> print 
Flags: X - DISABLED
Columns: CHAIN, EXP, SET-EXP, SET-MARK, PACKETS
#   CHAIN    EXP  SET-EXP  SET-MARK  PACKETS
0   forward    0        3  m0        221 654
```

MPLS mangle rules do not execute line by line like regular firewall mangle rules. Instead, MPLS Mangle applies all actions at once.

For example, review the following set of rules:

```routeros
/mpls/mangle
add chain=forward exp=0 set-mark=m0
add chain=forward exp=0 set-exp=3
add chain=forward exp=3 set-mark=m3
```

In this example, if an incoming packet has an EXP bit value of 0, the third rule does not apply.

After you set an action for a specific EXP bit, other rules cannot modify it:

```ros
[admin@CCR2004_2XS_111] /mpls/mangle> add chain=forward exp=0 set-mark=m4
failure: conflicting forward set-mark rule
```
