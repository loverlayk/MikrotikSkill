# SNMP

> Enable the SNMP agent, control which communities can read the router and what they can change, and receive traps. Covers the community access model, SNMPv3 security, finding OIDs, traps, and writing router settings...

# SNMP

Simple Network Management Protocol (SNMP) is an Internet-standard protocol used to monitor and manage devices on IP networks. RouterOS runs an SNMP agent that answers queries about the router and its interfaces. Tools such as [The Dude](https://mikrotik.com/product/the-dude), LibreNMS, Zabbix, Cacti, or MRTG use those answers to collect, visualize, and graph system data.

The agent is disabled until you turn it on. Enable it with `/snmp/set enabled=yes`; the router then answers SNMP queries on UDP port 161. By default a single community, `public`, can read anything, so restrict it before you put the router on an untrusted network.

![SNMP traffic graph rendered by The Dude (RRDtool), showing download traffic for a router interface](./img/snmp-01.webp)

:::tip
Enabling SNMP is enough to start monitoring: the router answers on UDP port 161 and the default `public` community has read access to everything, so a collector on the same network can read the router immediately. That also means the configuration is open to anyone on that network, so restrict or delete `public` ([Restrict a community](#restrict-a-community)) before the router goes live.
:::

## Enable SNMP for a collector

Turn the agent on and give the collector a community limited to its network. The community name works as a password for SNMPv1 and v2c, and it travels in clear text every time the router is polled. The examples use the documentation address range `192.0.2.0/24`; replace it with your collector network and `192.0.2.1` with the router address.

```ros
/snmp/set enabled=yes contact="NOC" location="Server room"
/snmp/community/add name=monit addresses=192.0.2.0/24 \
    security=none read-access=yes
```

```text
           enabled: yes
           contact: NOC
          location: Server room
  engine-id-suffix:
         engine-id: 80003a8c04cca063f65a2d89956b75a4daa36094f61e08c68fc99350599b77b4
       src-address: ::
       trap-target:
    trap-community: public
      trap-version: 1
   trap-generators: temp-exception
               vrf: main
```

The community printout shows which addresses the collector can use and what it can do:

```ros
[admin@MikroTik] /snmp/community> print detail where name=monit or name=public
```

```text
Flags: * - DEFAULT
0  * name="public" addresses=::/0 security=none read-access=yes write-access=no
     denied-oids="" authentication-protocol=MD5 encryption-protocol=DES
 
1    name="monit" addresses=192.0.2.0/24 security=none read-access=yes
     write-access=no denied-oids="" authentication-protocol=MD5
     encryption-protocol=DES
```

Check that the router answers from the collector, for example with `snmpwalk` (part of net-snmp on Linux and macOS; other operating systems have equivalent SNMP tools):

```bash
snmpwalk -v2c -c monit 192.0.2.1 1.3.6.1.4.1.14988.1.1.4.1.0
```

```text
SNMPv2-SMI::enterprises.14988.1.1.4.1.0 = STRING: "QMBK-S7GS"
```

The value is the router's software ID; it differs per router.

The default `public` community stays readable from any address (`addresses=::/0`). Either delete it and keep only the communities you created, or narrow it to your management network:

```ros
/snmp/community/set [find name=public] addresses=192.0.2.0/24
```

## Restrict a community

All properties are covered in the [`/snmp` CLI reference](../cli-reference/snmp/) and the [`/snmp/community` CLI reference](../cli-reference/snmp/community).

Each community is a set of access rules: which source addresses (`addresses`), which security level (`security`), and whether it can read, write, or both. A request is answered only when it comes from an address inside `addresses` and names a community with matching rules; everything else gets **no reply at all**, which looks like a dead host to the collector. Use prefixes, not single hosts, when several collectors share a network, and give IPv6 collectors IPv6 prefixes.

Read access (`read-access=yes`) lets a collector walk every MIB the agent implements. Write access (`write-access=yes`) additionally allows changing the system identity, running [scripts](../developer-guides/scripting/), and rebooting the router; a write community is a powerful credential and should have a hard-to-guess name and a narrow `addresses` range. See the [SNMP write](#snmp-write) section.

`denied-oids` blacklists specific OIDs or subtrees that a community cannot read: a direct GET of a blacklisted OID returns "No Such Object", and walks skip the blocked subtree, so the poll does not fail. The setting is per community, so set it on every community that could query that OID. Use it when a monitoring tool walks something expensive or irrelevant on the router, for example an empty table or a subtree another tool already covers. Pass several OIDs as a comma-separated list:

```ros
/snmp/community/set [find name=monit] \
    denied-oids=1.3.6.1.4.1.14988.1.1.13,1.3.6.1.4.1.14988.1.1.7.1.0
```

### SNMPv3 security

For a community with `security=none`, the community name is the only protection, and v1 and v2c clients can use it directly. The `authorized` and `private` levels use SNMPv3, which authenticates the client (`authorized`) or authenticates and encrypts it (`private`). A request that does not match the level is ignored, so a v1/v2c poll with the same name gets no answer from these communities.

| Security | Meaning | Protocols |
| :-- | :-- | :-- |
| `none` | No authentication, no encryption (`noAuthNoPriv`) | community name only |
| `authorized` | Authentication required (`authNoPriv`) | MD5, SHA1, SHA256, SHA384, SHA512 |
| `private` | Authentication and encryption required (`authPriv`) | MD5, SHA1, SHA256, SHA384, SHA512 with DES or AES |

Passwords must be at least 8 characters. The router refuses a shorter one with `failure: authentication password minimum length is 8 symbols`.

To add a `private` community, pick an authentication protocol (SHA256 is a good default), an encryption protocol, and two passwords:

```ros
/snmp/community/add name=monit-v3 security=private \
    addresses=192.0.2.0/24 authentication-protocol=SHA256 \
    encryption-protocol=AES \
    authentication-password=change-me-a1 \
    encryption-password=change-me-b2
```

Test it with `/tool/snmp-get`, so the syntax is the same as the one a monitoring tool uses. Run it from a router on that network (a router can also poll itself by its own address); the testing address must be inside the community's `addresses` (add it if it is not):

```ros
/tool/snmp-get address=192.0.2.1 oid=1.3.6.1.2.1.1.5.0 version=3 \
    security=private community=monit-v3 authentication-protocol=SHA256 \
    authentication-password=change-me-a1 encryption-protocol=AES \
    encryption-password=change-me-b2
```

```text
OID                            TYPE             VALUE
1.3.6.1.2.1.1.5.0              octet-string     MikroTik
```

## Find an OID

Each value the agent can answer has an object identifier (the OID). RouterOS prints the OID of every parameter of a page directly in the console, so you can build a collector template without reading the MIB file. Run the same `print` command with the `oid` keyword at any menu:

```ros
[admin@MikroTik] /interface> print oid where name=ether1
```

The trailing number (`.4`) is the interface's index on this router; on yours the index, and so the OIDs, differ. The leading dot marks an absolute OID; monitoring tools accept it with or without. The `S` flag only marks the interface as a bridge slave and does not affect the OIDs.

```text
Flags: S - SLAVE
0 S name=.1.3.6.1.2.1.2.2.1.2.4 actual-mtu=.1.3.6.1.2.1.2.2.1.4.4
    mac-address=.1.3.6.1.2.1.2.2.1.6.4 admin-status=.1.3.6.1.2.1.2.2.1.7.4
    oper-status=.1.3.6.1.2.1.2.2.1.8.4 bytes-in=.1.3.6.1.2.1.31.1.1.1.6.4
    packets-in=.1.3.6.1.2.1.31.1.1.1.7.4 discards-in=.1.3.6.1.2.1.2.2.1.13.4
    errors-in=.1.3.6.1.2.1.2.2.1.14.4 bytes-out=.1.3.6.1.2.1.31.1.1.1.10.4
    packets-out=.1.3.6.1.2.1.31.1.1.1.11.4 discards-out=.1.3.6.1.2.1.2.2.1.19.4
    errors-out=.1.3.6.1.2.1.2.2.1.20.4
```

The same command on any other menu enumerates that menu's OIDs. The complete definition of those OIDs and the list of tables lives in the [MIKROTIK-MIB file](https://mikrotik.com/download/tools), published with every RouterOS release. Most monitoring tools expect the standard MIBs (MIB-2, IF-MIB, HOST-RESOURCES-MIB, IP-MIB, IP-FORWARD-MIB, IPv6-MIB, BRIDGE-MIB), which the agent implements together with MIKROTIK-MIB; the exact list is in [Technical details](#technical-details).

## Receive traps

SNMP traps let the router push events to a collector instead of waiting to be polled. The collector listens on UDP port 162; the router sends the trap there on the interface that reaches the target.

```ros
/snmp/set trap-target=192.0.2.50,192.0.2.51 \
    trap-community=monit \
    trap-version=2 \
    trap-generators=interfaces
```

- `trap-target` - IP address of the collector that should receive the traps.
- `trap-community` - community used for the trap. It must exist under `/snmp/community`; its security level decides how the trap is protected (plain when `none`, authenticated or encrypted when `authorized` or `private`). The community's `addresses` restrict who can query the agent and do not affect where traps are sent, so the collector does not have to be in the list.
- `trap-version` - protocol version for the trap: `1`, `2`, or `3`.
- `trap-generators` - events that generate a trap. `interfaces` sends `linkDown`/`linkUp` for interface state changes, `temp-exception` sends a trap when the CPU temperature reaches the value from [`/system/health`](./health). By default `trap-generators` is `temp-exception`, so temperature traps are on as soon as `trap-target` is set.

Use `trap-interfaces` to narrow `interfaces` to the interfaces whose changes matter: traps are generated only for the listed interfaces, and other interfaces stay quiet. The `interfaces` notifications are the standard `linkDown`/`linkUp` traps and carry the index of the affected interface, so the collector learns which port went down.

```ros
/snmp/set trap-interfaces=ether1,ether2
```

To check the collector and trapping path without changing a live interface, send one trap by hand with `send-trap`:

```ros
/snmp/send-trap oid=1.3.6.1.2.1.1.5.0 type=string value="test trap"
```

The collector receives a packet from the router with the community and, in the payload, the MikroTik trap OID `1.3.6.1.4.1.14988.1.1.9.0.1` followed by the OID and value you passed (with `trap-version=1` the packet is a classic v1 enterprise trap without that wrapper). Confirm on the collector with a sniffer, for example Wireshark filtering `udp port 162`.

## SNMP write

Write access lets a management system change the router instead of only reading it. It requires a community with `write-access=yes` and works only for a fixed set of OIDs: the system identity, the script execution entries, and the reboot control, described in this section.

Restrict a write community to the monitoring network and give it a name that is hard to guess, because the name is the password. The commands in this section assume such a community named `monit-admin`.

```ros
/snmp/community/add name=monit-admin addresses=192.0.2.0/24 \
    security=none read-access=yes write-access=yes
```

:::danger
A community with write access lets anyone who knows its name change the router identity, run scripts, and reboot the router. Do not enable write access on a community that is also readable from an untrusted network, and use SNMPv3 for write communities where possible.
:::

### Change the identity

Set the router identity over SNMP by writing to `sysName.0` (`1.3.6.1.2.1.1.5.0`), for example with `snmpset` on Linux or macOS:

```bash
snmpset -v 1 -c monit-admin 192.0.2.1 1.3.6.1.2.1.1.5.0 s Branch-GW
```

```text
SNMPv2-MIB::sysName.0 = STRING: Branch-GW
```

In the example, `-v 1` selects the protocol version, `-c monit-admin` the community, and the `s` marks the value as a string (the argument types of `snmpset` are not the OID types; these OIDs accept string values).

The `public` community, which has no write access, refuses the same request with `readOnly`. A community with write access can also change other settings and reboot the router, which is why it needs the restrictions described earlier. See [Identity](../system-information-and-utilities/identity) for the same operation from the console and WinBox.

### Run a script

A collector can run a script on the router, which is a way to let a monitoring system perform a maintenance or reporting step without logging in. The script must exist in [system scripts](../developer-guides/scripting/):

```ros
/system/script/add name=status-report owner=admin \
    policy=read,write,test source=":put \"status ok\""
```

Running a script needs a community with write access (like `monit-admin`), because it can change the router. The script is started with an SNMP GET to `1.3.6.1.4.1.14988.1.1.18.1.1.2.<N>`, where `<N>` is the script's position in `/system/script/print` (the first entry is 1, the second 2, and so on). The GET returns whatever the script prints:

```bash
snmpget -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.18.1.1.2.1
```

```text
SNMPv2-SMI::enterprises.14988.1.1.18.1.1.2.1 = STRING: "status ok"
```

The list of scripts and their numbers is available as an SNMP table at `1.3.6.1.4.1.14988.1.1.8`, so a collector can discover them with a walk instead of fixing the number.

```bash
snmpwalk -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.8
```

```text
iso.3.6.1.4.1.14988.1.1.8.1.1.2.1 = STRING: "status-report"
iso.3.6.1.4.1.14988.1.1.8.1.1.3.1 = INTEGER: 0
```

The same script can also be started with a SET to `1.3.6.1.4.1.14988.1.1.8.1.1.3.<N>`. The value written is irrelevant — a `0` runs it exactly as any other value does:

```bash
snmpset -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.8.1.1.3.1 s 1
```

SNMP runs a script only with a limited set of policies: `ftp`, `reboot`, `read`, `write`, `test`, and `romon`. A script that needs any other policy (for example `password`, `sniff`, or `sensitive`) is refused, and the GET returns `error: not enough permissions`. Keep the scripts you run over SNMP to that set of policies.

### Reboot the router

Writing the value `1` to the reboot OID `1.3.6.1.4.1.14988.1.1.7.1.0` restarts the router:

```bash
snmpset -v 1 -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.7.1.0 s 1
```

This disconnects every client, including the management system that sent the request, for the time the router takes to boot.

:::note
The default `public` community has no write access, so a router left on the default configuration cannot be changed or rebooted over SNMP.

To see which router menus expose password-like values over management channels, see the [list of menus with sensitive parameters](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters).
:::

## Check and troubleshoot

- To see what the agent logged: add the `snmp` topic (`/system/logging/add topics=snmp`). The `snmp,debug` level also logs requests and replies; on a busy router it gets verbose.
- A collector times out: besides the agent checks that follow, make sure no [firewall](../firewall-and-quality-of-service/firewall) rule or other filter drops UDP 161 (and UDP 162 for traps) from the collector.
- A collector times out with all settings correct: check that the agent is enabled, that the request comes from an address inside the community's `addresses`, and that the community name is spelled exactly. A request that fails any of these gets no reply at all, which looks like a dead host.
- A v1/v2c collector cannot read a community with `security=authorized` or `private`: those levels require SNMPv3. Create a `security=none` community for v1/v2c collectors, restricted to their address.
- Polling breaks after you set `src-address`: the router then answers only requests addressed to that address (and, for an IPv4 value, no IPv6 requests), so a collector that queries any other address times out. Clear `src-address` or set it to the address the collector polls.
- The router answers a walk slowly and logs `snmp,warning` entries such as `timeout while waiting for program` or `SNMP did not get OID data within expected time, ignoring OID` when a service is busy or an OID is expensive to answer (for example a full routing-table walk on a large router). The agent records the OID, skips it for a while, and answers the following requests as usual. Exclude such OIDs from the collector, or blacklist them with `denied-oids` as described in the community section, instead of polling them constantly.

## Technical details

### SNMP engine ID

The agent identifies itself to SNMPv3 clients with the engine ID, shown by `/snmp/print` as `engine-id`. The configurable `engine-id-suffix` is only the tail of that value: the router writes the suffix into the engine ID as ASCII hex, so `engine-id-suffix=1234` produces the engine ID `80003a8c0431323334`. Leave the suffix empty to use the automatically generated engine ID, which is different on each router and stays the same across reboots; most SNMPv3 collectors discover it, so you rarely need a fixed suffix.

### Reply source and `src-address`

By default the agent answers from the address of the interface that received the request, so replies use the same source address as the one the collector sent the request to. Setting `src-address` forces the agent onto that address: it then answers only requests addressed to the value you set, and stops answering over IPv6 when the value is IPv4. Set it only when polling reaches the router through an address you cannot change on the collector, and point the collector at that same address.

### SNMP write OIDs

Write access covers a fixed set of OIDs: the system identity (`1.3.6.1.2.1.1.5.0`), the script execution entries under `1.3.6.1.4.1.14988.1.1.8` and `1.3.6.1.4.1.14988.1.1.18`, and the reboot control (`1.3.6.1.4.1.14988.1.1.7.1.0`). Other MIB objects are read-only.

### MIBs the agent implements

The agent answers the standard MIB-2 groups (system, interfaces, IP, IP forwarding, IPv6, ICMP, TCP, UDP) and the [HOST-RESOURCES-MIB](https://datatracker.ietf.org/doc/html/rfc2790), [IF-MIB](https://datatracker.ietf.org/doc/html/rfc2863), [IP-MIB](https://datatracker.ietf.org/doc/html/rfc4293), [IP-FORWARD-MIB](https://datatracker.ietf.org/doc/html/rfc4292), [IPV6-MIB](https://datatracker.ietf.org/doc/html/rfc4293), [BRIDGE-MIB](https://datatracker.ietf.org/doc/html/rfc4188), plus [UPS-MIB](https://datatracker.ietf.org/doc/html/rfc1628) and the SQUID-MIB used by the [web proxy](../network-management/proxy/web-proxy). The proprietary [MIKROTIK-MIB](https://mikrotik.com/download/tools) carries the RouterOS values that fit no standard MIB, such as the software ID, the health values, and the script table.

All parameters of `/snmp` and `/snmp/community`, and the `/snmp/send-trap` command, are documented in the [SNMP CLI reference](../cli-reference/snmp/).
