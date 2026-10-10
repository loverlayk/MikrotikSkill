# Profiler

> The Profiler tool shows CPU usage for each RouterOS process classifier, summed or per core, to identify which process consumes CPU resources.

# Profiler

The Profiler tool shows CPU usage for each process running in RouterOS. It helps to identify which process is using most of the CPU resources. See the [video about this feature](https://youtu.be/BkRaW14p8_s).

```ros
[admin@MikroTik] > /tool/profile
```

Processes are grouped by type (classifiers), for example `wireless`, `bridging` or `console`, and each classifier's CPU usage is shown separately. Only the classifiers with running processes appear, so the rows depend on the device and the features in use.

On multi-core systems, the `cpu` parameter selects the view: `cpu=total` (the default) sums the usage of all cores, `cpu=all` shows every core separately with per-core `cpuN` summary rows, and `cpu=<number>` shows only that core. Both views are demonstrated in the example below.
Without a `duration`, the profile keeps refreshing until you stop it; `freeze-frame-interval` (in seconds) sets how often a new frame is printed, and each frame shows the usage measured since the previous frame. With `duration`, the tool stops after the given number of seconds. The first one or two frames show only the `total` row before the sampled data arrives.

For a plain per-core load summary without the process split (for example for scripts), use [`/system/resource/cpu/print`](../cli-reference/system/resource/cpu).

## Find a busy process

A runaway script keeps one core busy. In the summed view (`cpu=total`), 100% usage of one core of a 4-core router shows as 25%:

```ros
[admin@MikroTik] > /tool/profile cpu=total freeze-frame-interval=1 duration=5
Columns: NAME, USAGE
NAME            USAGE
interface-mgmt  0%   
bridging        0%   
console         25.1%
resource-mgmt   0%   
ssh             0%   
total           25.1%
```

`console` consuming the CPU points at script or console session activity (here a script loop). The per-core view shows the exact core and its total in the `cpuN` rows:

```ros
[admin@MikroTik] > /tool/profile cpu=all freeze-frame-interval=1 duration=3
Columns: NAME, CPU, USAGE
NAME         CPU  USAGE
console        0  95.5%
cpu0              95.5%
console        1  0.5% 
wireless       1  0.5% 
kernel         1  0.5% 
cpu1              1.5% 
console        2  4%   
certificate    2  0.5% 
cpu2              4.5% 
console        3  0.5% 
cpu3              0.5% 
```

## Classifiers

RouterOS processes are classified by type and the CPU usage of each type is displayed separately for ease of debugging. Besides the feature classifiers below, system rows such as `kernel`, `ipc`, `interface-mgmt` and `resource-mgmt` can also appear; anything without a classifier accounts under `unclassified`:

| Property | Description |
| :-- | :-- |
| backup | Backup service |
| bfd | BFD service |
| bgp | BGP service |
| bridging | Bridging service |
| btest | Bandwidth test. |
| certificate | Certificate service |
| console | Console |
| container | combined container usage |
| dhcp | DHCP-Server and DHCP-Client services |
| disk | storage-related services |
| dns | DNS-related services |
| dude | The Dude package services |
| e-mail | e-mail tool |
| encrypting | encrypting processes |
| eoip | EoIP |
| ethernet | Ethernet-related properties like link speed, auto-negotiation, duplex mode, monitor transceiver diagnostic information, etc. |
| fetcher | Fetch tool |
| fileman | File manager |
| firewall | Firewall-related processes |
| firewall-mgmt | Firewall Management: Filtering, NAT, Mangle |
| flash | storage-related services |
| ftp | FTP Service |
| gps | GPS Service |
| graphing | Graphing tool |
| gre | GRE |
| health | system monitoring, system health |
| hotspot | Hotspot service |
| idle | Free CPU resources |
| igmp-proxy | IGMP Proxy service |
| internet-detect | Detect Internet tool |
| ip-pool | IP Pool service |
| ipsec | IPsec service:  xfrm -  set of statistics showing numbers of packets dropped by the transformation code and why.  drivers/crypto - drivers that provide access to the hardware cryptographic accelerators. ipsec - processes that relate to the Internet Key Exchange (IKE) protocols, Authentication Header (AH), Encapsulating Security Payload (ESP). |
| kvm | KVM virtual machine functionality |
| l7-matcher | L7 matcher |
| lcd | LCD Interfaces system |
| ldp | Label Distribution Protocol (LDP) |
| logging | Logging system |
| management | different subsystems: scheduler, networking, file management, etc. |
| mpls | MPLS-related features |
| neighbor-discovery | Neighbor discovery service |
| networking | common set of services included in the networking |
| ntp | NTP service |
| ospf | OSPF service |
| ovpn | OVPN service |
| pim | Protocol Independent Multicast |
| profiling | Profiler service |
| queue-mgmt | Queues: Simple queues, Queue tree, Queue types |
| queuing | Intermediate Queuing |
| radius | RADIUS service |
| radvd | IPv6 Router Advertisement daemon (radvd) service |
| remote-access | accessing the device directly without logging into RouterOS |
| rip | Routing Information Protocol |
| routing | Routing-related services |
| serial | serial console and terminal tool |
| sniffing | packet Sniffer tool |
| snmp | SNMP |
| socks | Socket Secure |
| spi | storage-related services |
| ssh | SSH Server |
| ssl | SSL |
| supout.rif | supout.rif file generation |
| telnet | Telnet service |
| tftp | TFTP service |
| traffic-accounting | Traffic-Flow log system |
| traffic-flow | Traffic-Flow system |
| unclassified | processes or services that are not defined by this classifier |
| upnp | UPnP protocol |
| usb | USB features |
| user-manager | User Manager service |
| vrrp | VRRP |
| web-proxy | Web Proxy |
| winbox | Winbox |
| wireguard | Wireguard |
| wireless | common set of services using Wireless systems |
| www | Webfig HTTP service |
| zerotier | ZeroTier |

For all parameters, see the [`/tool/profile`](../cli-reference/tool/profile) CLI reference.
