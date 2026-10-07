# IPv6 PD over PPP

> This page demonstrates configuring IPv6 Prefix Delegation over PPPoE in RouterOS, showing how to set up DHCPv6-PD pools on servers and clients, including interface configuration and verification of dynamic prefix...

# IPv6 PD over PPP

This example demonstrates how to set up PPPoE server and client to use IPv6 Prefix Delegation.

IPv6 Prefixes can be delegated over PPP interfaces. When a client connects, PPP will automatically add a dynamic  [DHCPv6-PD server](../../network-management/dhcp/dhcpv6-server). This allows running a DHCPv6 client on PPP interfaces.

### Configuration

### Server

The dhcpv6-pd-pool parameter under PPP Profiles is used to enable PPP-PD. PPP will use the specified  [IPv6 pool](../../cli-reference/ipv6/pool/pool.md) to create a dynamic DHCP server.

So the first step is to add an IPv6 pool:

```ros
/ipv6/pool
add name=myPool prefix=2001:db8:7501:ff00::/60 prefix-length=62
```

Now we can configure a PPP profile and add a PPPoE server

```ros
/ppp/profile/set default dhcpv6-pd-pool=myPool

/interface/pppoe-server/server 
add service-name=test interface=ether1
```

### Client

On the client side we need to set up PPPoE client interface and run DHCP client on it.

```ros
/interface/pppoe-client
add name=client-test interface=ether1 user=a1 service-name=test

/ipv6/dhcp-client 
add interface=client-test pool-name=ppp-test pool-prefix-length=64
```

### Testing status

On the server side check if a dynamic DHCP server is added and prefix is bound to a specific client:

```ros
[admin@RB1100] /ipv6/dhcp-server> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    NAME              INTERFACE            ADDRESS-POOL            LEASE-TIME
 0 D  <pppoe-a1>        <pppoe-a1>           myPool                  3d        

[admin@RB1100] /ipv6/dhcp-server/binding> print 
Flags: X - disabled, D - dynamic 
 #   ADDRESS                                        DU       IAID SER.. STATUS 
 1 D 2001:db8:7501:ff04::/62                                  247 <pp.. bound  
 
```

On the client side, check if DHCP client is bound and pool is added:

```ros
[admin@x86-test] /ipv6/dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    INTERFACE           STATUS        PREFIX                            EXPIRES-AFTER  
0    client-test          bound         2001:db8:7501:ff04::/62           2d23h18m17s  

[admin@x86-test] /ipv6/pool> print 
Flags: D - dynamic 
 #   NAME                        PREFIX                                   PREFIX-LENGTH
 0 D ppp-test                    2001:db8:7501:ff04::/62                             64
```
