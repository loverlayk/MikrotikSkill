# IPv6 PD over PPP

> IPv6 prefix delegation over PPP in RouterOS: give each PPPoE user an IPv6 prefix from a pool with a dynamic DHCPv6 server, request the prefix on the client, and use it on the LAN.

# IPv6 PD over PPP

A PPP server can give each user an IPv6 prefix for the network behind the user's router. This is DHCPv6 prefix delegation (PD) over the PPP link: when a user connects, the server adds a dynamic [DHCPv6 server](../../network-management/dhcp/dhcpv6-server) on the interface of the user, and the router of the user asks it for a prefix with a DHCPv6 client.

The example uses PPPoE.

## Server

Add an IPv6 pool. This pool gives a /60 prefix to each user from a /56 block:

```ros
/ipv6/pool/add name=pd-pool prefix=2001:db8:7501:ff00::/56 \
    prefix-length=60
```

Set the pool in `dhcpv6-pd-pool` of the PPP profile that the users have:

```ros
/ppp/profile/set subscribers dhcpv6-pd-pool=pd-pool
```

The setting applies to users that connect after the change. [PPPoE](./) shows how to add the server, the profile and the users.

## Client

On the router of the user, add a DHCPv6 client on the PPPoE client interface. It asks for a prefix and puts it into an IPv6 pool:

```ros
/ipv6/dhcp-client/add interface=pppoe-out1 request=prefix \
    pool-name=lan-pool pool-prefix-length=64 add-default-route=yes
```

Give the LAN an address from the pool. `advertise=yes` announces the prefix to the devices of the LAN:

```ros
/ipv6/address/add interface=bridge from-pool=lan-pool advertise=yes
```

## Check

On the server, a dynamic DHCPv6 server exists for the user, and the binding shows the prefix:

```ros
[admin@Server] > /ipv6/dhcp-server/print
Flags: D - DYNAMIC
Columns: NAME, INTERFACE, ADDRESS-POOL, PREFIX-POOL, PREFERENCE, LEASE-TIME
#   NAME           INTERFACE      ADDRESS-POOL  PREFIX-POOL  PREFERENCE  LE
0 D <pppoe-alice>  <pppoe-alice>  static-only   pd-pool             255  1d

[admin@Server] > /ipv6/dhcp-server/binding/print
Flags: D - DYNAMIC
Columns: ADDRESS, DUID, SERVER, STATUS
#   ADDRESS                  DUID                    SERVER         STATUS
0 D 2001:db8:7501:ff00::/60  0x0003000152540b7e0101  <pppoe-alice>  bound 
```

The server also adds a route for the prefix through the interface of the user.

On the client, the DHCPv6 client is `bound` and the pool has the prefix:

```ros
[admin@Client] > /ipv6/dhcp-client/print
Columns: INTERFACE, STATUS, REQUEST, PREFIX
# INTERFACE   STATUS  REQUEST  PREFIX                            
0 pppoe-out1  bound   prefix   2001:db8:7501:ff00::/60, 23h59m45s

[admin@Client] > /ipv6/pool/print
Flags: D - DYNAMIC
Columns: NAME, PREFIX, PREFIX-LENGTH, ACTUAL-PREFIX, VALID-LIFETIME
#   NAME      PREFIX                   PR  ACTUAL-PREFIX            VALID-LIF
0 D lan-pool  2001:db8:7501:ff00::/60  64  2001:db8:7501:ff00::/60  23h59m44s
```

The LAN interface then has a /64 prefix from the pool, here 2001:db8:7501:ff00::/64: see `/ipv6/address/print`.

## Read more

- [`/ppp/profile`](../../cli-reference/ppp/profile), [`/ipv6/dhcp-client`](../../cli-reference/ipv6/dhcp-client/), [`/ipv6/pool`](../../cli-reference/ipv6/pool/)
- [PPP AAA](../../authentication-authorization-accounting/ppp-aaa)
- [PPPoE](./)
- [DHCPv6 server](../../network-management/dhcp/dhcpv6-server)
