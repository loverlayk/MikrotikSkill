# VRRP

> VRRP provides a redundant default gateway by combining RouterOS routers into a virtual router. The page covers the protocol, virtual MAC addresses, master election and preemption, IPv4 and IPv6 configuration,...

# VRRP

VRRP (Virtual Router Redundancy Protocol) gives a LAN a redundant default gateway. Two or more
routers form a virtual router with a shared virtual IP address and a shared virtual MAC address. One
router is the master and forwards traffic for that address; the others are backups and take over if
the master fails. Hosts keep using one gateway address, so their configuration does not change.
RouterOS implements VRRPv2 (RFC 3768) and VRRPv3 (RFC 5798); VRRPv3 supports IPv4 and IPv6.

A statically configured first hop is a single point of failure: if that router stops, hosts lose
connectivity until their gateway is reconfigured. Dynamic routing protocols such as OSPF or RIP can
provide another path, but they add complexity that a small network may not need. In IPv6, Neighbor
Discovery detects an unreachable router only after several missed advertisements, which can take
tens of seconds. VRRP detects a failed master within a few seconds without adding traffic for every
host.

:::note
Use the same RouterOS version on all routers that share a VRID.
:::

The configuration examples are on [VRRP configuration examples](./user-guides/vrrp-configuration-examples).

## How VRRP works

A virtual router is identified by a Virtual Router ID (VRID) and a set of virtual IP addresses.
Every router in the group is configured with the same VRID and the same virtual addresses. All
members receive VRRP advertisements, but only the master sends them periodically; backups listen and
wait for the master to stop.

VRRP advertisements are IPv4 or IPv6 multicast packets with IP protocol number 112:

- IPv4 destination `224.0.0.18`, multicast MAC `01:00:5E:00:00:12`.
- IPv6 destination `FF02::12`, multicast MAC `33:33:00:00:00:12`.

The source address is the primary IPv4 address of the parent interface for IPv4, or the link-local
address of the VRRP interface for IPv6. Advertisements are sent with TTL 255 and are not forwarded by
routers.

Every member must use the same advertisement interval. A router discards an advertisement whose
interval differs from its own and records `misconfigured interval` in the log.

### Virtual MAC address

VRRP assigns each virtual router a MAC address derived from the VRID. It cannot be set or edited.

- IPv4 uses `00:00:5E:00:01:VRID`.
- IPv6 uses `00:00:5E:00:02:VRID`.

The last octet is the VRID in hexadecimal. VRID 49 gives the IPv4 address `00:00:5E:00:01:31`. The
master uses the virtual MAC address as the source of its advertisements and answers ARP or Neighbor
Discovery requests for the virtual IP address with it. The VRRP interface also derives an IPv6
link-local address from this MAC address.

When a router becomes master, it sends an ARP announcement for the virtual IPv4 address from the
virtual MAC address, so hosts update their ARP tables as soon as the master changes.

A VRID must be unique on a parent interface. An IPv4 and an IPv6 virtual router on the same
interface need different VRIDs.

### Master election and preemption

The member with the highest priority becomes the master. Priorities range from 1 to 254; the default
is 100. If two members have the same priority, the one with the higher primary IP address becomes
master.

Priority 255 is reserved for the owner, a router whose real address is the virtual address, and
priority 0 for a master that releases the role. RouterOS accepts neither value and cannot be
configured as an owner, so the virtual address must differ from the real address on every RouterOS
member.

The current master's `preemption-mode` setting decides whether it gives up the role to a router with
a higher priority that appears later:

- `yes` (default) - The master yields, and the higher-priority router becomes master.
- `no` - The master keeps the role until it fails, even when a higher-priority router is available.

The setting on a backup does not change this decision. Set the same value on all members so the
result does not depend on which router is master.

## Configuration

### IPv4

Create the VRRP interface on the LAN-facing interface, add the router's real address to that
interface, and add the shared virtual address to the VRRP interface:

```ros
/interface/vrrp/add name=vrrp1 interface=ether5
/ip/address/add address=192.168.1.2/24 interface=ether5
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

Only the `interface` argument is required. The other settings take their defaults: `vrid=1`,
`priority=100`, `interval=1s` and `authentication=none`. Name the interface explicitly, because
RouterOS does not reuse automatically assigned names after an interface is deleted.

The real address on the parent interface is required; without it, the VRRP interface stays invalid
with the status comment `No IPv4 address!`. The virtual address needs a `/32` netmask when it belongs
to the same subnet as an address on another interface of the router.

:::note
With strict reverse path filtering (`rp-filter=strict`), traffic sent to the virtual address can be
dropped: packets arrive on the parent interface, but the route to the virtual address points at the
VRRP interface. Set `rp-filter=loose` on routers that must reach the virtual address.
:::

Configure the second router the same way with its own real address, the same VRID and the same
virtual address. The [configuration examples](./user-guides/vrrp-configuration-examples) show both
routers and the failover test. Set the virtual address as the default gateway on the LAN hosts, for
example with the `gateway` setting of the DHCP server, not the real address of either router.

Check the state:

```ros
/interface/vrrp/print
Flags: R - RUNNING; M - MASTER
Columns: NAME, INTERFACE, MAC-ADDRESS, VRID, PRIORITY, INTERVAL, VERSION, 
         V3-PROTOCOL, SYNC-CONNECTION-TRACKING
#    NAME   INTERFACE  MAC-ADDRESS        VRID  PRIORITY  IN  V  V3-P  SY
0 RM vrrp1  ether5     00:00:5E:00:01:01     1       100  1s  3  ipv4  no
```

The `M` flag marks the master, `B` the backup and `F` the failure state. An instance that cannot
start shows `I` (invalid) and the reason as a status comment, for example `No IPv4 address!`.

### IPv6

VRRPv3 is required for IPv6. Create the interface with `v3-protocol=ipv6` and add a global address
with `advertise=yes`:

```ros
/interface/vrrp/add name=vrrp6 interface=ether5 vrid=6 v3-protocol=ipv6
/ipv6/address/add address=fd00:1::1/64 advertise=yes interface=vrrp6
```

The VRRP interface receives a link-local address automatically and uses it for advertisements. With
`advertise=yes`, the master advertises the prefix in Router Advertisements. The IPv6 virtual router is
independent of an IPv4 one on the same interface and needs its own VRID.

## Connection tracking synchronization

Connection tracking synchronization copies connection tracking entries from the master to the
backup, so established connections can continue after a failover. The log and the status refer to it
as CTSYNC. It requires connection tracking on both routers. Connection tracking is in `auto` mode by
default, which disables it until a firewall rule needs it; enable it explicitly when the routers have
no such rule:

```ros
/ip/firewall/connection/tracking/set enabled=yes
```

Enable synchronization on both routers of the pair:

```ros
/interface/vrrp/set [find name=vrrp1] sync-connection-tracking=yes
```

The routers exchange synchronization data over UDP port 8275. If the firewall filters traffic between
the routers, allow this port in the input chain on both of them.

The log shows the synchronization state, for example on the master:

```text
2026-11-13 14:52:10 vrrp,info vrrp1 now MASTER, master down timer
2026-11-13 14:52:10 vrrp,info vrrp1 stop CTSYNC
2026-11-13 14:52:10 vrrp,info vrrp1 starting CTSYNC MASTER
2026-11-13 14:52:10 vrrp,info Obtaining CTSYNC Backup IP address...
2026-11-13 14:52:11 vrrp,info Waiting for CTSYNC Backup...
2026-11-13 14:52:11 vrrp,info CTSYNC Backup ready
2026-11-13 14:52:11 vrrp,info Initial CTSYNC complete
```

In the default `passive-active` mode, only the master sends connection tracking data. Use
`active-active` mode when several VRRP groups spread the master role across routers; every group then
needs its own `connection-tracking-port`. See the [`/interface/vrrp`](../cli-reference/interface/vrrp)
CLI reference for the synchronization arguments.

## Group authority

Several VRRP interfaces on the same router can be grouped so that they share one state. This matters
when the router performs NAT between two interfaces: if the LAN instance is master and the WAN
instance is backup, the router forwards traffic for one interface but not the other, and NAT fails.
In a group, all members share one state, so they are master or backup together.

One interface is the group authority. It controls the state of the other members and is the only
interface that sends advertisements. A group member follows the authority. A failure on any member,
for example a link-down on its parent interface, moves the whole group to the failure state.

Create the group from the interfaces and their addresses:

```ros
/interface/vrrp/add name=vrrp-lan interface=bridge vrid=2
/interface/vrrp/add name=vrrp-wan interface=ether1 vrid=1
/ip/address/add address=192.168.10.2/24 interface=bridge
/ip/address/add address=192.168.10.1/32 interface=vrrp-lan
/ip/address/add address=192.0.2.2/24 interface=ether1
/ip/address/add address=192.0.2.1/32 interface=vrrp-wan
/interface/vrrp/set [find name=vrrp-lan] group-authority=self
/interface/vrrp/set [find name=vrrp-wan] group-authority=vrrp-lan
```

Use the LAN interface as the authority so that VRRP control traffic stays in the internal network.
Every member needs a real address on its parent interface and a virtual address; otherwise it stays
invalid with the status comment `No IPv4 address!`, and a member whose authority is not ready shows
`VRRP Group is not ready!`.

## Hardware offloading

A master VRRP instance is hardware-offloaded when L3 hardware offloading is enabled. The switch then
uses the virtual MAC address as the source for routed traffic and routes frames addressed to the
virtual MAC address. The instance reports the read-only `hw-offloaded` property as the `H` flag in
`/interface/vrrp/print`.

Offloading is removed when the instance is not master or when L3 hardware offloading is disabled.
VRRP hardware offloading is not available on every switch that supports L3 hardware offloading. See
[L3 Hardware Offloading](../bridging-and-switching/l3-hardware-offloading) for the configuration and
the list of supported devices.

## Troubleshooting

### All routers are master

Members that cannot hear each other all become master. Check that both routers use the same VRID,
version, `v3-protocol`, virtual addresses and advertisement interval. The log shows why an
advertisement was rejected:

- `misconfigured interval (1 != 2)` - The advertisement intervals differ.
- `misconfigured authentication type` or `simple authentication failed` - VRRPv2 authentication does
  not match.
- `bad checksum` - The `v3-checksum-as-v2` setting differs between the routers.
- `misconfigured IP addresses [192.168.1.253](my) != [192.168.1.1](received)` - The virtual address
  sets differ.

A firewall that drops IP protocol 112 also prevents the routers from hearing each other. Allow VRRP
in the input chain on both routers.

### The VRRP interface is invalid

An `I` flag means that the instance cannot run. The status comment gives the reason:

- `No IPv4 address!` - The parent interface has no address, or the VRRP interface has no virtual
  address.
- `VRRP Group is not ready!` - The group authority is not ready.

### A backup does not take over

Check that the backup has the same virtual address and VRID and that its parent interface is up.
When the master is still reachable, a backup with a lower priority stays backup; if the priorities
are equal, the router with the lower primary IP address stays backup. Only a higher priority, or an
equal priority with a higher primary IP address, triggers preemption. If the master's
`preemption-mode` is `no`, it also keeps the role after a higher-priority router returns.

### Connection tracking synchronization does not start

Check that `sync-connection-tracking` is enabled on both routers and that connection tracking is
enabled; otherwise the VRRP interface shows the status comment `Connection tracking inactive!` and
nothing is synchronized. Allow UDP port 8275 between the routers. If the synchronization data must
use a different path than the VRRP advertisements, set `remote-address` to the other router's
address.

### No traffic after a failover

Confirm that the backup became master and has the virtual address configured. Check the ARP or
Neighbor Discovery entry for the virtual address on a host: it must resolve to the virtual MAC
address, not to the MAC address of a physical interface.

## Technical details

### Router states

![VRRP state transitions between Init, Backup and Master](./img/vrrp-03.webp)

The protocol defines three states:

- **Init** - The instance is waiting to start. RouterOS instances do not use the owner startup path,
  because priority 255 is rejected.
- **Backup** - The instance listens for advertisements and does not forward traffic for the virtual
  addresses. It becomes master when the master-down timer expires, when it receives an advertisement
  with priority 0, or when preemption applies and its own priority is higher.
- **Master** - The instance forwards traffic for the virtual addresses, answers ARP and Neighbor
  Discovery requests, and sends advertisements. If it receives an advertisement with a higher
  priority, or with an equal priority from a router with a higher primary IP address, it returns to
  the backup state. When its VRRP interface is disabled, it sends an advertisement with priority 0,
  so the backups take over without waiting for the master-down timer.

RouterOS reports an additional failure state with the `F` flag when the parent interface is down or a
group member has failed; the instance cannot forward traffic for the virtual addresses until the
failure clears.

The master-down timer is three advertisement intervals plus a priority-dependent skew. A backup that
receives an advertisement with a differing interval, authentication or virtual address set discards
it and logs the reason.

### Owner

RFC 3768 and RFC 5798 define an owner as the router whose interface address is the virtual address;
it has priority 255 and becomes master immediately. RouterOS cannot be configured as an owner:
`priority=255` is rejected with `value of priority out of range (1..254)`, and the virtual address
must be a separate address (a floating or pure virtual address). Use the same floating virtual
address on every member, and configure it on the VRRP interface on each router.

### Authentication

VRRPv2 supports `none`, `simple` (a cleartext password) and `ah` (IP Authentication Header with
HMAC-MD5). RFC 5798 deprecates authentication for VRRPv3. All members of a VRRPv2 virtual router
must use the same authentication method and password.

The menu and its arguments are described in the
[`/interface/vrrp`](../cli-reference/interface/vrrp) CLI reference.
