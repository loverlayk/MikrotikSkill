# EoIP

> Ethernet over IP (EoIP) Tunneling in MikroTik RouterOS creates secure Layer 2 bridges over IP networks using GRE encapsulation, supporting flexible topologies like LAN extension and encrypted connections with IPsec.

# EoIP

Ethernet over IP (EoIP) Tunneling is a MikroTik RouterOS protocol designed to create an Ethernet tunnel between two routers over an IP network. It is based on GRE encapsulation (RFC 1701) and allows Ethernet frames to be transported across routed IP infrastructure, effectively extending a Layer 2 network between remote sites.

The EoIP tunnel interface appears as a virtual Ethernet interface in RouterOS and can be used in conjunction with the bridging functionality. When added to a bridge, all Ethernet traffic, including broadcasts and non-IP protocols, is forwarded across the tunnel as if the endpoints were directly connected by a physical Ethernet link.

EoIP tunnels can operate over IPIP, PPTP, or any other IP-based transport that supports GRE encapsulation. This provides flexibility in building various network topologies.

Typical use cases for EoIP include bridging LAN segments over the internet, extending LANs across encrypted tunnels (when combined with IPsec or other secure transport), and connecting networks over wireless point-to-point or ad-hoc links.

EoIP encapsulates Ethernet frames inside GRE (IP protocol 47) packets and forwards them to the remote tunnel endpoint. The receiving router decapsulates the packets and injects the original Ethernet frames into the local bridge domain.

EoIP is configured in [`/interface/eoip`](../cli-reference/interface/eoip.md) and [`/interface/eoipv6`](../cli-reference/interface/eoipv6.md)menus.

## Configuration Examples

The parameter tunnel-id is a method of identifying a tunnel. It must be unique for each EoIP tunnel.

:::tip
EoIP tunnel adds at least 42-byte overhead (8-byte GRE + 14-byte Ethernet + 20-byte IP). Set MTU to 1500 to eliminate packet fragmentation inside the tunnel, allowing transparent bridging of Ethernet-like networks so you can transport full-sized Ethernet frames over the tunnel.
:::

When bridging EoIP tunnels, you should set unique MAC addresses for each tunnel for the bridge algorithms to work correctly. For EoIP interfaces you can use MAC addresses in the range from **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF**, which IANA has reserved for such cases. Alternatively, you can set the second bit of the first byte to modify the auto-assigned address into a 'locally administered address', assigned by the network administrator, and thus use any MAC address. You just need to ensure they are unique between the hosts connected to one bridge.

### Example

This example shows how to bridge two networks: 'Station' and 'AP'. With EoIP, you can set up the network so that Station and AP LANs share the same Layer 2 broadcast domain.

Consider the following setup:

![](./img/eoip-01.webp)

Wireless stations cannot be bridged. To overcome this limitation without WDS, create an EoIP tunnel over the wireless link and bridge it with interfaces connected to local networks.

This example does not cover wireless configuration. Assume the wireless link is already established.

First, create an EoIP tunnel on the AP:

```ros
/interface/eoip/add name="eoip-remote" tunnel-id=0 remote-address=10.0.0.2 disabled=no
```

Verify the interface is created:

```ros
[admin@AP] > /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-remote" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:A5:6C:3F:26:C5 arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.2 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes 
```

Station router:

```ros
/interface/eoip/add name="eoip-main" tunnel-id=0 remote-address=10.0.0.1 disabled=no
```

Verify the interface is created:

```ros
[admin@Station] >  /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-main" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:4B:71:05:EA:8B arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.1 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes  
```

Next, bridge the local interfaces with the EoIP tunnel on the AP. If you already have a local bridge interface, add the EoIP interface to it:

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-remote
```

The bridge port list shows all local LAN interfaces and the EoIP interface:

```ros
[admin@AP] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE       BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2          bridge1  yes     1  0x80             10                  10  none   
1  H ether3          bridge1  yes     1  0x80             10                  10  none    
2    eoip-remote     bridge1  yes     1  0x80             10                  10  none    
```

On the Station router, if you do not have a local bridge interface, create a new bridge and add both EoIP and local LAN interfaces to it:

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=ether2
/interface/bridge/port/add bridge=bridge1 interface=eoip-main
```

Verify the bridge port section:

```ros
[admin@Station] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE     BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2        bridge1  yes     1  0x80             10                  10  none    
2    eoip-main     bridge1  yes     1  0x80             10                  10  none    
```

Now both sites are in the same Layer2 broadcast domain. You can set up IP addresses from the same network on both sites.
