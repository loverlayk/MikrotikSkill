# MACVLAN

> MACVLAN creates additional virtual interfaces with their own MAC addresses on one parent interface, for several DHCP or PPPoE sessions on a single port. The page covers parent requirements, VLAN precedence, private...

# MACVLAN

A MACVLAN interface adds a virtual interface with its own MAC address on top of an existing
interface. It shares the parent's Layer 2 segment, and its frames are not tagged. Use it to make
one port appear as more than one host: an ISP that assigns an address per MAC, two DHCP client
sessions on one link, or several PPPoE client sessions, each with its own MAC. For several VLANs
over one port, use [VLAN](./vlan.md); to join segments at Layer 2, use
[bridging](./index.md).

A MACVLAN is configured like a physical interface: assign addresses and routes, or run a DHCP
client or a PPPoE client on it. RouterOS generates the MAC address automatically when
`mac-address` is not set.

## How MACVLAN works

The MACVLAN sends and receives through its parent interface, so the remote end sees the MACVLAN's
own MAC address. Several MACVLAN interfaces can use the same parent, each with a separate MAC
address.

A MACVLAN receives broadcast traffic, traffic addressed to its own MAC address, and a limited
number of multicast addresses. It does not receive unicast traffic addressed to another MAC
address on the segment. If a VLAN interface is configured on the parent, that VLAN interface
receives the VLAN's tagged traffic first, so the MACVLAN does not receive it.

The parent can be any interface with a MAC address, such as an Ethernet, VLAN or bond interface. It
cannot be in use as an active bridge port: creating the MACVLAN then fails with `failed to create
device`, and the system log names the busy parent:

```text
macvlan1 parent device is busy (code -16), please make sure other devices are not using the
same parent (ether5)
```

The nesting order is VLAN first, then MACVLAN: create the VLAN interface on the physical parent,
then create the MACVLAN on the VLAN interface when that segment needs another MAC address. A VLAN
interface cannot be created on a MACVLAN; RouterOS does not offer MACVLAN interfaces as VLAN
parents. A MACVLAN can be added to a bridge as a port, but it then works as a bridge port, and a
DHCP client cannot run on it. For bridging and complex Layer 2 setups with VLANs, use a dedicated
switch.

MACVLAN does not support FastPath, so its traffic is processed by the CPU.

### Private and bridge mode

The `mode` property controls communication between MACVLAN interfaces on the same parent:

- `bridge` - the default. MACVLAN interfaces on the same parent can communicate with each other.
- `private` - they cannot. With either interface set to `private`, communication between them
  stops.

Communication between two MACVLAN interfaces requires `bridge` mode on both. With either
interface set to `private`, communication stops. To isolate two MACVLAN interfaces that share a
parent, set both to `private` (one is enough):

```ros
/interface/macvlan/set macvlan1 mode=private
/interface/macvlan/set macvlan2 mode=private
```

The commands assume two interfaces named `macvlan1` and `macvlan2` on the same parent.

The MTU defaults to 1500 and cannot be higher than the parent's MTU. To use a lower value, set
`mtu`; if the parent's MTU is lower than 1500, set `mtu` when creating the interface, otherwise
creation fails with `could not set mtu`.

## Two DHCP clients on one port

This example uses ether5, which connects to an uplink that assigns one address per MAC address.
ether5 is not part of a bridge; if it is a bridge port, remove it from the bridge first. The router
needs two addresses, one for each MAC. Create a MACVLAN on the port and run a DHCP client on both
interfaces:

```ros
/interface/macvlan/add interface=ether5 name=macvlan1
/ip/dhcp-client/add interface=ether5 name=dhcp-ether5 \
    add-default-route=no
/ip/dhcp-client/add interface=macvlan1 name=dhcp-macvlan1 \
    add-default-route=no
```

Check the interface and the leases:

```ros
/interface/macvlan/print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
#   NAME       MTU  INTERFACE  MAC-ADDRESS        MODE  
0 R macvlan1  1500  ether5     56:97:C6:D3:58:D5  bridge

/ip/dhcp-client/print where name~"dhcp-"
Columns: NAME, INTERFACE, USE-PEER-DNS, ADD-DEFAULT-ROUTE, STATUS, ADDRESS
# NAME           INTERFACE  USE-PEER-DNS  AD  STATUS  ADDRESS          
3 dhcp-ether5    ether5     yes           no  bound   198.51.100.117/24
4 dhcp-macvlan1  macvlan1   yes           no  bound   198.51.100.120/24
```

Each client is bound and uses the MAC address of its own interface: the parent's MAC for
`dhcp-ether5` and the generated MAC for `dhcp-macvlan1`. The index numbers depend on the clients
already configured on the router. Each lease is added as an address to its interface, so
`/ip/address/print` lists both.

The generated MAC address is stored in the configuration, so it stays the same after a reboot. Set
`mac-address` to use a specific address, for example one the provider has registered.

Both clients in the example ignore the default route. Remove `add-default-route=no` from the
client that should provide the default route.

## Troubleshooting

### The MACVLAN cannot be created

- **The parent is a bridge port.** A MACVLAN cannot use a bridge port that is forwarding traffic.
  The command fails with `failed to create device`, and the log says `parent device is busy (code
  -16), please make sure other devices are not using the same parent (<interface>)`. Remove the port
  from the bridge, or use another interface as the parent.
- **The parent's MTU is lower than 1500.** Creation fails with `could not set mtu`. Create the
  interface
  with a matching `mtu`, for example `/interface/macvlan/add interface=ether5 name=macvlan1
  mtu=1400`.

### The MACVLAN runs but receives no traffic

- **VLAN on the parent.** A VLAN interface on the same parent handles that VLAN's tagged traffic;
  the MACVLAN does not receive it. If the MACVLAN must work inside that VLAN, create it on the VLAN
  interface instead.
- **Traffic for another MAC address.** The MACVLAN receives broadcast, traffic to its own MAC
  address and limited multicast. Unicast traffic addressed to another MAC on the segment does not
  reach it.
- **The uplink allows one MAC address.** Some ISPs accept only one MAC address per port and drop
  traffic from a second one. Check the provider's policy before adding a MACVLAN.

### A DHCP client does not obtain a lease

A client that stays in `searching` receives no DHCP reply. Check that the client runs on the
MACVLAN interface and that the provider accepts a second MAC address on the port.
`/interface/macvlan/print` shows the MAC address of each MACVLAN.

### A DHCP client or VLAN interface does not work

- **DHCP client on a bridge port.** If the MACVLAN was added to a bridge, the client is invalid with
  the comment `DHCP client can not run on slave or passthrough interface!`. Remove the MACVLAN from
  the bridge, or run the client on the parent interface instead.
- **VLAN on a MACVLAN.** Not supported. Create the VLAN interface on the parent instead.

## Technical details

MACVLAN is implemented by the Linux MACVLAN driver. A parent interface can carry several MACVLAN
interfaces; each has its own MAC address and receives only the traffic the driver passes to it.
RouterOS exposes the `private` and `bridge` modes. In `bridge` mode the driver delivers frames
between the MACVLAN interfaces on the same parent locally; in `private` mode it drops them.

Because the interfaces share the parent's broadcast domain, a MACVLAN is not a substitute for a
VLAN: a VLAN interface adds an 802.1Q tag and separates broadcast domains, whereas a MACVLAN adds
a MAC address to the same segment.

The menu and its arguments are described in the
[`/interface/macvlan`](../cli-reference/interface/macvlan) CLI reference.
