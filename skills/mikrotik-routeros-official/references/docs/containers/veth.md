# VETH

> A veth connects a container to RouterOS: one end is a router interface, the other the container's network interface. Put a container behind NAT or on the LAN with DHCP, IPv4 and IPv6.

# VETH

A veth (virtual Ethernet) is a pair of connected Ethernet ends. One end is a RouterOS interface in `/interface/veth`; the other end is the network interface of a container. Inside the container, that interface has the veth's name and the `container-mac-address`. The address, gateway and DHCP settings of the veth are applied inside the container, not on the router.

A veth is not running until a container that uses it starts. Until then, its MAC addresses show as `00:00:00:00:00:00` and an IP address that the router has on it is marked invalid.

To create and run containers, see [Container](./). [Apps](apps/) create their veths automatically.

## Put a container behind NAT

The container gets its own subnet, and the router is its gateway and translates its traffic to the internet. Create the veth with the container's address and gateway, give the router the gateway address on the veth, and masquerade the subnet:

```ros
/interface/veth/add name=veth1 address=172.17.0.2/24 \
    gateway=172.17.0.1
/ip/address/add address=172.17.0.1/24 interface=veth1
/ip/firewall/nat/add chain=srcnat action=masquerade \
    src-address=172.17.0.0/24
```

Then use the veth for the container:

```ros
/container/add remote-image=alpine:latest interface=veth1 \
    root-dir=usb1/alpine
```

The container gets 172.17.0.2/24 and a default route through 172.17.0.1, the router's address on the veth. The masquerade rule gives it access to the internet. To reach a service in the container from outside, add a `dst-nat` rule that forwards the port to 172.17.0.2 (see [NAT](../firewall-and-quality-of-service/firewall/nat)).

## Put a container on the LAN

The container gets an address from the LAN's DHCP server, like any other device on the LAN. Create the veth with `dhcp=yes` and add it to the LAN bridge:

```ros
/interface/veth/add name=veth2 dhcp=yes
/interface/bridge/port/add bridge=bridge interface=veth2
```

RouterOS runs the DHCP client for the container and applies the lease inside it: the container gets the leased address and the default route from DHCP. The `dhcp-address` column of `/interface/veth/print` shows the leased address.

The DHCP server sees the veth's router-side MAC address (`mac-address`) and the host name `<identity>-<veth name>`, for example `MikroTik-veth2`. A static lease for the container must use `mac-address`, not `container-mac-address`.

The container's DNS server comes from the container settings, not from DHCP; see [Container](./).

With router advertisements on the bridge, the container also configures an IPv6 address from the advertised prefix (SLAAC) and an IPv6 default route.

## Static IPv4 and IPv6 addresses

`address` takes several addresses, separated by commas, IPv4 and IPv6. `gateway` and `gateway6` set the IPv4 and IPv6 default routes inside the container. Give the router the matching gateway addresses on the veth:

```ros
/interface/veth/add name=veth1 \
    address=172.17.0.2/24,2001:db8:17::2/64 \
    gateway=172.17.0.1 gateway6=2001:db8:17::1
/ip/address/add address=172.17.0.1/24 interface=veth1
/ipv6/address/add address=2001:db8:17::1/64 interface=veth1 \
    advertise=no
```

Stop the container before you change the settings of its veth, and start it again afterwards.

## Check the veth

In `/interface/veth/print`, the flag `R` shows that a running container uses the veth. `MAC-ADDRESS` is the router's end and `CONTAINER-MAC-ADDRESS` the container's end; both are set when the container starts. For a veth with `dhcp=yes`, `DHCP-ADDRESS` shows the leased address.

To see the addresses and routes from inside the container, open its shell with `/container/shell` and run `ip addr` and `ip route` (if the container image has the `ip` command).

For all parameters, see the [`/interface/veth`](../cli-reference/interface/veth) CLI reference.
