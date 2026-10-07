# RoMON

> RoMON is a Router Management Overlay Network that establishes an independent MAC layer network for secure router management, using EtherType 0x88bf and DST-MAC 01:80:c2:00:88:bf. It allows ports to participate with...

# RoMON

## Summary

RoMON stands for "Router Management Overlay Network". RoMON works by establishing an independent MAC layer peer discovery and data forwarding network. RoMON packets are encapsulated with EtherType 0x88bf and DST-MAC 01:80:c2:00:88:bf and its network operates independently of L2 or L3 forwarding configuration. When RoMON is enabled, any received RoMON packets are not displayed by sniffer or torch tools.

Each router on the RoMON network is assigned its RoMON ID. The RoMON ID can be selected from the port MAC address or specified by the user.

The RoMON protocol does not provide encryption services. Encryption is provided at the "application" level, for example, by using ssh or by using a secure WinBox.

:::info
RoMON packets can be forwarded through network switches or bridges, unless there are specific restrictions on multicast traffic. When using a MikroTik bridge with hardware offloading, these packets are treated like regular multicast packets and are flooded across the network.

Since RouterOS v7.17, if the RoMON service is enabled and the switch chip supports ACL rules, dynamic rules are automatically created to redirect these packets to the CPU, where the RoMON service operates. However, if the switch does not support ACL rules and the configuration does not align, such as when the CPU and RoMON untagged packets are not in the same VLAN, the RoMON service might not function as expected.

**RB5009** (switch‑chip 88E6393X) does not support this path. The chip's frame‑types=admit‑only‑vlan‑tagged filter drops RoMON frames before any ACL rule can be applied, so the packets never reach the CPU.

:::

## Configuration

For a device to participate in the RoMON network, the RoMON feature must be enabled and the ports that participate in the RoMON network must be specified.

Romon is configured from [`/tool/romon`](../cli-reference/tool/romon) menu.

When RoMON is enabled without specifying an ID, the ID is automatically selected:

```routeros
[admin@MikroTik] /tool/romon> print 
     enabled: yes              
          id: 00:00:00:00:00:00
     secrets:                  
  current-id: DC:2C:6E:9E:11:27
```

Ports that participate in the RoMON network are configured in the [`/tool/romon/port`](../cli-reference/tool/romon/port) menu. The port list is a list of entries that match either a specific interface or interface-list. Each entry defines whether the matched interface is allowed or forbidden to participate in the RoMON network. If participation is allowed, the entry also specifies the port's cost.

:::info
A default entry with the interface-list "all" is preconfigured. This means that when the RoMON service is enabled, all interfaces are allowed to participate in the RoMON network by default. This default entry cannot be removed or enabled/disabled, but you can still modify its `cost`, set it to `forbid` participation, or configure `secrets`.

:::

## Secrets

RoMON protocol secrets are used for message authentication, integrity check and replay prevention by means of hashing message contents with MD5.

For each interface, if the interface-specific secret list is empty, a global secret list is used. When sending out, messages are hashed with the first secret in the list if the list is not empty and the first is not "empty secret" (empty string = ""), otherwise, messages are sent unhashed. When received, unhashed messages are only accepted if a secret list is empty or contains "empty secret", hashed messages are accepted if they are hashed with any of the secrets in the list.

This design allows for the incremental introduction and/or change of secrets in-network without RoMON service interruption and can happen over RoMON itself, for example:

- Initially, all routers are without secrets.
- Configure each router one by one with secrets="","mysecret" - this makes all routers still send unprotected frames, but they all are ready to accept frames protected with the secret "mysecret".
- Configure each router one by one with secrets="mysecret","" - this makes all routers use the secret "mysecret", but also still accept unprotected frames (from routers that have not yet been changed).
- Configure each router with secrets="mysecret" - this makes all routers use the secret "mysecret" and also only accept frames protected with "mysecret".

Changing a secret in a network should be performed in a similar fashion where for some time both secrets are in use in the network.

## Peer discovery

To discover all routers on the RoMON network the [`/tool/romon/discover`](../cli-reference/tool/romon/discover) command must be used:

```ros
[admin@MikroTik] > /tool/romon/discover 
Flags: A - active
Columns: ADDRESS, COST, HOPS, PATH, L2MTU, IDENTITY, VERSION, BOARD
   ADDRESS            COS  H  PATH               L2MT  IDENTITY   VERSION    BOARD              
A  6C:3B:6B:48:0E:8B  200  1  6C:3B:6B:48:0E:8B  1500  hEX        6.47beta7  RB750Gr3           
A  6C:3B:6B:ED:83:69  200  1  6C:3B:6B:ED:83:69  1500  CCR1009    6.47beta7  CCR1009-7G-1C-1S+  
A  B8:69:F4:B3:1B:D2  200  1  B8:69:F4:B3:1B:D2  1500  4K11       6.47beta7  RB4011iGS+5HacQ2HnD
A  CC:2D:E0:26:22:4D  200  1  CC:2D:E0:26:22:4D  1500  CCR1036    6.47beta7  CCR1036-8G-2S+     
A  CC:2D:E0:8D:01:88  200  1  CC:2D:E0:8D:01:88  1500  CRS328     6.47beta7  CRS328-24P-4S+     
A  E4:8D:8C:1C:D3:0E  200  1  E4:8D:8C:1C:D3:0E  1500  MikroTik   6.47beta7  RB2011iLS          
A  E4:8D:8C:49:49:DB  200  1  E4:8D:8C:49:49:DB  1500  hAP        6.47beta7  RB962UiGS-5HacT2HnT

```

## Configuration Examples

For a device to participate in the RoMON network, the RoMON feature must be enabled and the ports that participate in the RoMON network must be specified.

```ros
/tool/romon/set enabled=yes secrets=testing
```

Ports that participate in the RoMON network are configured in **the RoMON port** menu. The port list is a list of entries that match either a specific port or all ports and specifies if matching port(s) is forbidden to participate in the RoMON network and in case the port is allowed to participate in the RoMON network, the entry also specifies the port cost. All specific port entries have higher priority than the wildcard entry with **interface=all**.

For example, the following list specifies that all ports participate in the RoMON network with cost 100 and the ether7 interface with cost 200:

```ros
[admin@MikroTik] > /tool/romon/port/print
Flags: * - default
Columns: INTERFACE, FORBID, COST
#     INTERF  FO  COS
0  *  all     no  100
1     ether7  no  200
```

By default, one wildcard entry with **forbid=no** and **cost=100** is created.

### Applications

Multiple applications can be run over the RoMON network.

To test the reachability of a specific router on the RoMON network the RoMON ping command can be used:

```ros
[admin@MikroTik] > /tool/romon/ping id=6C:3B:6B:48:0E:8B count=5
  SEQ HOST                                    TIME  STATUS                                                    
    0 6C:3B:6B:48:0E:8B                       1ms                                                             
    1 6C:3B:6B:48:0E:8B                       0ms                                                             
    2 6C:3B:6B:48:0E:8B                       1ms                                                             
    3 6C:3B:6B:48:0E:8B                       0ms                                                             
    4 6C:3B:6B:48:0E:8B                       1ms                                                             
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=1ms
```

To establish a secure terminal connection to a router on a RoMON network the RoMON SSH command can be used:

```ros
[admin@MikroTik] > /tool/romon/ssh 6C:3B:6B:48:0E:8B
```

### Run RoMON in WinBox by using CLI

To establish the RoMON session directly by using the command line on a computer, you must specify RoMON agents and desired router addresses. The RoMON agent must be saved on the Managed routers list in WinBox to make a successful connection:

```ros
winbox.exe --romon 192.168.88.1 6C:3B:6B:48:0E:8B admin ""
```

### Connect to RoMON through WinBox GUI

Watch a [video tutorial](https://www.youtube.com/watch?v=Peg6UcSJ_eA).
