# NAT-PMP

> NAT-PMP lets LAN clients learn the router's external IPv4 address and request port mappings, so applications accept incoming connections behind NAT without manual port forwarding. Covers enabling the RouterOS NAT-PMP...

# NAT-PMP

NAT Port Mapping Protocol (NAT-PMP, [RFC 6886](https://www.rfc-editor.org/rfc/rfc6886)) lets applications on the local network learn the router's external IPv4 address and request port mappings, so applications that accept incoming connections, for example games, peer-to-peer clients and voice or video calls, can work behind NAT without manual port forwarding. NAT-PMP is common on Apple devices. RouterOS also supports [UPnP](upnp), an alternative protocol with the same purpose.

A client sends its requests to the router over UDP port 5351, and each mapping is valid for a limited lifetime which the client renews. When the lifetime expires, the mapping is removed. The NAT-PMP service is disabled by default.

A mapping applies only to the address the request was sent from: a client cannot create mappings for other devices, so only connect trusted networks as internal interfaces. The protocol has no authentication.

## Configuration example

![Network diagram: the router connects to the Internet on ether1 (10.0.0.1/24) and to a LAN switch on ether2 (192.168.88.1/24); two computers, PC1 (192.168.88.10/24) and PC2 (192.168.88.11/24), are on the 192.168.88.0/24 LAN](./img/nat-pmp-01.webp)

Prerequisites: the LAN is masqueraded towards the external interface, for example:

```ros
/ip/firewall/nat/add action=masquerade chain=srcnat out-interface=ether1
```

Enable the service and mark the Internet-facing interface as external and the client-facing interface as internal:

```ros
/ip/nat-pmp/set enabled=yes
/ip/nat-pmp/interfaces/add interface=ether1 type=external
/ip/nat-pmp/interfaces/add interface=ether2 type=internal
```

Clients on the internal interfaces can now request their external address and port mappings. Only one external interface can be assigned; a second one is refused with `failure: only one external interface can be added to the list`. If the external interface has several addresses, set `forced-ip` on the interface entry to choose which address is reported to the clients.

:::warning
In setups with VLANs, specify the VLAN interface itself as the internal interface: the client traffic arrives on it.
:::

## Technical details

### Service ports and announcements

The service listens for client requests on UDP port 5351 of the internal interfaces, shown as a dynamic `natpmp` entry in `/ip/service` while the service is enabled. Clients choose the source port of their requests themselves.

When the router's external address changes, the router multicasts gratuitous external address announcements to `224.0.0.1` on UDP port 5350 from each internal interface, as described in RFC 6886. Clients that want those announcements listen on UDP port 5350.

### Mapping lifetime

Per RFC 6886: a client requests a mapping with a lifetime in seconds (the recommended value is two hours), the gateway can grant a shorter lifetime, and the client renews the mapping halfway to its expiry. A mapping with an expired lifetime is removed automatically, and sending a request with a lifetime of 0 removes the client's mapping immediately.

For all properties, see [`/ip/nat-pmp`](../cli-reference/ip/nat-pmp/) and [`/ip/nat-pmp/interfaces`](../cli-reference/ip/nat-pmp/interfaces) in the CLI reference.
