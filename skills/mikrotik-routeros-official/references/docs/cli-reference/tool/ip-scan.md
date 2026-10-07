# ip-scan

> Finds the hosts on a network, IPv4 only. With address-range, the router probes every address of the range and lists the hosts that answer; with only interface, it probes nothing and lists the addresses it sees in the...

-----------

## tool/ip-scan 
**Conditions:** !smips
**Type:** Command

Finds the hosts on a network, IPv4 only. With `address-range`, the router probes every address of the range and lists the hosts that answer; with only `interface`, it probes nothing and lists the addresses it sees in the traffic on that interface. The scan runs until you stop it or for `duration`. For examples, see [IP Scan](../../diagnostics-monitoring-and-troubleshooting/ip-scan).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dhcp">dhcp</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface to listen on. Without `address-range`, the router sends no probes to the hosts and lists the addresses it sees in the traffic on this interface, including addresses from other subnets.</ArgTableRow>
<ArgTableRow arg="address-range" typ="ipRange">Addresses to scan: a prefix such as `192.168.88.0/24`, a range such as `192.168.88.1-192.168.88.254`, or a single address. On a directly connected subnet, the router finds hosts with ARP requests; on other networks, with ICMP echo requests. When `interface` is also given, the router scans the range.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr">Address of the host. The router's own address in the range is listed too.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC address of the host, from its ARP reply. Only for hosts on a directly connected subnet.</ArgTableRow>
<ArgTableRow arg="time" typ="num">Response time to an ICMP echo request. Empty when the host does not answer ping.</ArgTableRow>
<ArgTableRow arg="dns" typ="string">Name from a reverse DNS lookup of the address through the router's DNS resolver.</ArgTableRow>
<ArgTableRow arg="snmp" typ="string">System name (`sysName`) of the host, when it answers an SNMPv1 request with the community `public`.</ArgTableRow>
<ArgTableRow arg="netbios" typ="string">NetBIOS name of the host, when it answers a NetBIOS name query on UDP port 137.</ArgTableRow>
</ArgTable>
