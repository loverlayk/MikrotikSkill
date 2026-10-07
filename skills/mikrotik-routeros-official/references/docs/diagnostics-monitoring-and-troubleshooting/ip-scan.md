# IP Scan

> IP scan finds the devices on a network: scan an address range to list the hosts with their MAC addresses, response times, DNS and SNMP names, or listen on an interface to see the addresses that devices use, including...

# IP Scan

IP scan finds the devices on a network. It works in two ways:

- Scan an address range: the router probes every address in the range and lists the hosts that answer, with their MAC address, response time, DNS name and SNMP name.
- Listen on an interface: the router sends no probes to the hosts and lists the addresses it sees in the traffic on that interface.

Use it to find the address of a printer or a camera, to check that an address is free before you assign it, or to see which devices are on a network segment. IP scan works with IPv4 only. It is not available on devices with the SMIPS architecture; `architecture-name` in `/system/resource/print` shows the architecture of a router.

## Find the devices on your LAN

Scan the LAN subnet:

```ros
/tool/ip-scan address-range=192.168.88.0/24
```

```text
Columns: ADDRESS, MAC-ADDRESS, TIME, DNS, SNMP
ADDRESS        MAC-ADDRESS        TIME  DNS                  SNMP
192.168.88.1                      1ms
192.168.88.20  FE:2F:28:FC:FE:16  1ms   printer.office.lan.  Test2
192.168.88.21  FE:A2:FB:A4:C8:34  1ms
```

The scan runs until you stop it with <kbd>Control</kbd>+<kbd>C</kbd>, or for the time given in `duration`, for example `duration=30s`. The columns are:

- `ADDRESS` - The address of the host. The router's own address in the range is listed too, without a MAC address.
- `MAC-ADDRESS` - The MAC address from the host's ARP reply.
- `TIME` - The response time to an ICMP echo request.
- `DNS` - The name from a reverse DNS lookup through the router's [DNS resolver](../network-management/dns), for example from a static DNS entry. Many LANs have no reverse names, and then the column stays empty.
- `SNMP` - The system name of the host, when it answers an SNMP query with the community `public`. Printers, switches and routers often show their name or model here.
- `NETBIOS` - The NetBIOS name, when the host answers a NetBIOS name query, for example a Windows computer.

A column appears only when a host has a value for it. To match a host to a device, compare its MAC address with the label of the device or with the host names in the [DHCP server leases](../network-management/dhcp/server#leases).

A host is listed when it answers ARP, so a computer whose firewall drops ping still appears, with an empty `TIME`.

## Check that an address is free

To check one address, scan only that address:

```ros
/tool/ip-scan address-range=192.168.88.50 duration=5s
```

An empty list means that no device answered at that moment. A device that is switched off does not answer either, so before you give the address to a server as a static address, also check that it is outside the pool of the DHCP server and has no lease there.

## Find a device with an unknown address

A device with a static address from another subnet, for example a camera or a switch with its factory address, does not answer a scan of the LAN range. Listen on the interface instead: when the device sends traffic, for example an ARP request for its gateway, the router lists its address. A device sends such traffic when it starts, so restart it while the scan runs:

```ros
/tool/ip-scan interface=bridge duration=30s
```

```text
Columns: ADDRESS, MAC-ADDRESS, TIME
ADDRESS       MAC-ADDRESS        TIME
172.16.99.5   FE:6B:12:9C:3A:05
192.168.88.1                     0ms
```

The device at 172.16.99.5 is on the bridge, although its address is not in the LAN subnet. The router's own address is listed too. To reach the device from the router, add an address from its subnet to the bridge for the time you need it, and remove it afterwards:

```ros
/ip/address/add address=172.16.99.1/24 interface=bridge
/ping 172.16.99.5 count=3
/ip/address/remove [find address="172.16.99.1/24"]
```

The router reaches the device directly in its subnet. A computer on the LAN reaches it through the router only when the device's gateway is the address you added; otherwise, give the computer a second address from the device's subnet.

In this mode, the router lists the addresses it sees in the traffic that reaches its CPU on the interface. On a bridge with hardware offloading, that is broadcast traffic, such as ARP requests, and traffic to the router; traffic between two other devices is not seen. A device that sends nothing does not appear.

## Scan a remote network

The range can be a network behind a router, for example a branch office reached over a VPN. Hosts on such a network are found by ping, so the list has no MAC addresses, and hosts that drop ping do not appear:

```ros
/tool/ip-scan address-range=198.51.100.0/29 duration=8s
```

```text
Columns: ADDRESS, TIME, SNMP
ADDRESS       TIME  SNMP
198.51.100.1  0ms   Test2
198.51.100.2  0ms   Test2
198.51.100.3  0ms   Test2
```

The hosts found there also get the SNMP and NetBIOS queries.

When you give both `address-range` and `interface`, the router scans the range, and the results are the same as without `interface`.

## Technical details

For an address range on a directly connected subnet, the router sends an ARP request to each address. To each host that answers, it sends:

- An ICMP echo request, for `TIME`.
- An SNMPv1 request for the system name (`sysName`) with the community `public`, for `SNMP`.
- A NetBIOS name query to UDP port 137, for `NETBIOS`.

It also looks up the name of each address through its DNS resolver, for `DNS`.

In both modes, the router also sends one BOOTP request on the interface. A DHCP server that answers BOOTP requests can lease an address to the router's MAC address. The RouterOS DHCP server answers BOOTP requests only for static leases by default (`bootp-support=static`), and for all clients with `bootp-support=dynamic`.

For the parameters, see the [`/tool/ip-scan` CLI reference](../cli-reference/tool/ip-scan).
