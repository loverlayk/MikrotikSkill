# DHCPv6 Server

> The RouterOS DHCPv6 server delegates IPv6 prefixes (DHCPv6-PD) and assigns IPv6 addresses to clients, with static bindings, RADIUS support and per-binding rate limiting.

# DHCPv6 Server

**Sub-menu:** `/ipv6/dhcp-server`

**Standards:** RFC 8415

The DHCPv6 server delegates IPv6 prefixes (DHCPv6-PD) and assigns IPv6 addresses to clients. It is typically used by a router that hands out prefixes to downstream routers, for example to the customer routers of an ISP. The server takes prefixes from the IPv6 pool set in `prefix-pool`, and addresses from the IPv6 pool set in `address-pool`, which must have a prefix length of 128. Bindings can also be static, or assigned by a RADIUS server.

Each binding is identified by the client's DUID and IAID. When a client is bound to a prefix, the server adds a dynamic route to that prefix through the client (`route-distance`), so traffic for the delegated prefix reaches the client router.

Most hosts only request addresses with DHCPv6 when the router advertisements on their network have the managed flag set, as shown in the address delegation example that follows. RouterOS uses the same DUID for its DHCPv6 server and client. For how DHCPv6 works, see [DHCP concepts](./).

## Configuration Example

### Enabling IPv6 Prefix delegation

To enable IPv6 prefix delegation, first create an IPv6 pool:

```ros
/ipv6/pool/add name=myPool prefix=2001:db8:7501::/60 prefix-length=62
```

With `prefix-length=62`, clients receive /62 prefixes from the /60 pool.

Then add the DHCPv6 server with this pool:

```ros
/ipv6/dhcp-server/add name=myServer prefix-pool=myPool interface=local
```

To test the server, you can use a RouterOS DHCPv6 client (see [DHCPv6 Client](./dhcpv6-client)) or, as in this example, the wide-dhcpv6 client on a Linux host:

1. Install wide-dhcpv6-client.
2. Configure `/etc/wide-dhcpv6/dhcp6c.conf` to request a prefix on eth2 and number eth3 from it:

   ```text
   interface eth2{
   send ia-pd 0;
   };

   id-assoc pd {
   prefix-interface eth3{
   sla-id 1;
   sla-len 2;
   };
   };
   ```

3. Run the client:

   ```bash
   sudo dhcp6c -d -D -f eth2
   ```

4. Check that eth3 got an address from the delegated prefix:

   ```text
   mrz@bumba:/media/aaa$ ip -6 addr
   ...
   2: eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qlen 1000
       inet6 2001:db8:7501:1:200:ff:fe00:0/64 scope global
          valid_lft forever preferred_lft forever
       inet6 fe80::224:1dff:fe17:81f7/64 scope link
          valid_lft forever preferred_lft forever
   ```

The server shows the binding. To give this client the same prefix every time, make the binding static:

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: D - DYNAMIC
Columns: ADDRESS, DUID, SERVER, STATUS
#   ADDRESS             DUID                    SERVER    STATUS
0 D 2001:db8:7501::/62  0x0003000100241d1781f7  myServer  bound
[admin@MikroTik] > /ipv6/dhcp-server/binding/make-static 0
```

The server also adds a route to the delegated prefix through the client's link-local address:

```ros
[admin@MikroTik] > /ipv6/route/print where dst-address=2001:db8:7501::/62
Flags: D - DYNAMIC; A - ACTIVE; d - DHCP
Columns: DST-ADDRESS, GATEWAY, ROUTING-TABLE, DISTANCE
    DST-ADDRESS         GATEWAY                          ROUTING-TABLE  DISTANCE
DAd 2001:db8:7501::/62  fe80::224:1dff:fe17:81f7%local   main                  1
```

### Enabling IPv6 Address delegation

An address server is configured like a prefix server, except that it uses `address-pool` instead of `prefix-pool`, and its pool must hand out /128 prefixes. A server that only gives out static bindings needs no pool.

```ros
[admin@MikroTik] > /ipv6/pool/print detail 
Flags: D - dynamic 
 0   name="myAddressPool" prefix=2001:db8:7501::/120 prefix-length=128 
[admin@MikroTik] > /ipv6/dhcp-server/print detail                                 
Flags: D - dynamic; X - disabled, I - invalid 
 0    name="myDHCP" interface=ether2 prefix-pool=static-only 
      address-pool=myAddressPool lease-time=3d rapid-commit=yes use-radius=no 
      preference=255 dhcp-option="" route-distance=1 use-reconfigure=no 
      address-lists="" duid="0x00030001b813f4840556" 
```

This is enough for DHCPv6 clients such as a RouterOS DHCPv6 client:

```ros
[admin@MikroTik] > /ipv6/dhcp-client/print detail 
Flags: D - dynamic; X - disabled, I - invalid 
 0    interface=ether2 status=bound duid="0x00030001b123f48407f0" 
      dhcp-server-v6=fe80::ba69:f4af:fe14:558 request=address 
      add-default-route=no use-peer-dns=yes allow-reconfigure=no 
      dhcp-options="" pool-name="" pool-prefix-length=64 prefix-hint=::/0 
      prefix-address-lists="" dhcp-options="" 
      address=2001:db8:7501::, 2d23h59m51s
```

Hosts such as computers do not look for a DHCPv6 server on their own: the router advertisements on their network tell them whether to use DHCPv6. To make hosts request addresses with DHCPv6, set the managed address configuration flag (`managed-address-configuration`) in the router advertisements of the interface. This does not require advertising a prefix for SLAAC:

```ros
[admin@MikroTik] > /ipv6/nd/print detail 
Flags: X - disabled, I - invalid; * - default 
 0    interface=ether2 ra-interval=3m20s-10m ra-delay=3s mtu=unspecified 
      reachable-time=unspecified retransmit-interval=unspecified 
      ra-lifetime=30m ra-preference=medium hop-limit=unspecified 
      advertise-mac-address=yes advertise-dns=yes 
      managed-address-configuration=yes other-configuration=no
[admin@MikroTik] > /ipv6/nd/prefix/print detail 
Flags: X - disabled, I - invalid; D - dynamic 
 0    prefix=::/64 6to4-interface=none interface=ether2 on-link=yes 
      autonomous=yes valid-lifetime=4w2d preferred-lifetime=1w 
```

A computer connected to ether2 then receives router advertisements with the managed flag set, which on most hosts starts a DHCPv6 client that requests an address.

The complete server configuration, with comments:

```ros
# Address pool for the bridge network; the prefix length must be 128
/ipv6/pool
add name=myLocalLan prefix=2001:db8::/100 prefix-length=128
# DHCPv6 server that gives out addresses from the pool
/ipv6/dhcp-server
add address-pool=myLocalLan interface=bridge name=myLocalServer
# Set the managed flag (M) in router advertisements, so hosts on the bridge use DHCPv6
/ipv6/nd
add interface=bridge managed-address-configuration=yes
# Enable router advertisements on the bridge; no prefix is needed, only the managed flag
/ipv6/nd/prefix
add interface=bridge
```

:::warning
Clients behave differently with this configuration. For example, macOS gets an address at startup, but might not renew the lease after sleep when no prefix is advertised, because macOS does not use its DHCPv6 client without a SLAAC address. Other clients might need `autonomous=no` on the advertised prefix before they use DHCPv6. Adjust the configuration to the clients on your network.

:::

## Properties

All properties of the DHCPv6 server are described in the [`/ipv6/dhcp-server`](../../cli-reference/ipv6/dhcp-server/) CLI reference. The following behavior needs more explanation.

### Server-initiated renewal

With `use-reconfigure=yes`, clients that accept Reconfigure messages, for example RouterOS DHCPv6 clients with `allow-reconfigure=yes`, get a reconfigure key. The server then sends them a Reconfigure message by itself when its `address-pool`, `lease-time` or `dhcp-option` change, or when the settings of their binding change, so the clients renew and pick up the change at once. The `send-reconfigure` command of a binding sends one manually.

### DNS entries for clients

With `add-dns-entries=yes`, the server adds a dynamic DNS entry (type AAAA) for each address binding. The name is the FQDN the client sends, followed by `add-dns-entries-suffix` (`lan` by default), and the TTL of the entry is the lease time. Prefix bindings get no DNS entry.

## Bindings

**Sub-menu:** `/ipv6/dhcp-server/binding`

A dynamic binding is tied to the DUID of the client, so a client whose DUID changes gets a different prefix than before. A static binding gives a client, identified by its DUID and IAID, a fixed prefix or address. All binding properties, status values and commands are described in the [`/ipv6/dhcp-server/binding`](../../cli-reference/ipv6/dhcp-server/binding/) CLI reference.

For example, dynamically assigned /62 prefix

```ros
[admin@RB493G] /ipv6/dhcp-server/binding> print detail
Flags: X - disabled, D - dynamic
 0 D address=2001:db8:7501:ff00::/62 duid="1605fcb400241d1781f7" iaid=0
     server=local-dhcp life-time=3d status=bound expires-after=2d23h40m10s
     last-seen=19m50s

 1 D address=2001:db8:7501:ff04::/62 duid="0019d1393535" iaid=2
     server=local-dhcp life-time=3d status=bound expires-after=2d23h43m47s
     last-seen=16m13s
```

### Rate limiting

You can limit the bandwidth of a client with the `rate-limit` property of its binding. The server then adds a dynamic simple queue for the prefix or address of the binding.

:::warning
Queues do not apply to FastTracked traffic. Make sure the firewall does not FastTrack the traffic you want to limit.

:::

First, make the binding static:

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: X - disabled, D - dynamic
 #   ADDRESS                   DUID            SERVER         STATUS
 0 D fdb4:4de7:a3f8:418c::/66  0x6c3b6b7c413e  DHCPv6_Server  bound

[admin@MikroTik] > /ipv6/dhcp-server/binding/make-static 0

[admin@MikroTik] > /ipv6/dhcp-server/binding/print
Flags: X - disabled, D - dynamic
 #   ADDRESS                   DUID            SERVER         STATUS
 0   fdb4:4de7:a3f8:418c::/66  0x6c3b6b7c413e  DHCPv6_Server  bound
```

Then set the rate limit. The server creates a dynamic simple queue for the binding:

```ros
[admin@MikroTik] > /ipv6/dhcp-server/binding/set 0 rate-limit=10M/10M
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic
 0  D name="dhcp<6c3b6b7c413e fdb4:4de7:a3f8:418c::/66>" target=fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8
      queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
      bucket-size=0.1/0.1
```

:::note
`allow-dual-stack-queue` is enabled by default, so a DHCPv6 binding and a DHCP lease of the same client share one dynamic simple queue. Without it, the server creates separate queues for IPv6 and IPv4.

:::

The shared queue contains both the IPv4 and the IPv6 address:

```ros
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic
 0  D name="dhcp-ds<6C:3B:6B:7C:41:3E>" target=192.168.1.200/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8
      queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s
      bucket-size=0.1/0.1
```

## RADIUS Support

A RADIUS server can assign a rate limit to each DHCPv6 binding with the Mikrotik-Rate-Limit attribute. First, set the DHCPv6 server to use RADIUS:

```ros
/radius 
add address=10.0.0.1 secret=VERYsecret123 service=dhcp 
/ipv6/dhcp-server 
set dhcp1 use-radius=yes
```

Then configure the RADIUS server to send the Mikrotik-Rate-Limit attribute. For FreeRADIUS with MySQL, add entries to the `radcheck` and `radreply` tables for the client, for example:

```sql
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES
('000c4200d464', 'Auth-Type', ':=', 'Accept');

INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES
('000c4200d464', 'Delegated-IPv6-Prefix', '=', 'fdb4:4de7:a3f8:418c::/66'),
('000c4200d464', 'Mikrotik-Rate-Limit', '=', '10M');
```

:::note
A shared queue is created only when the server recognizes the DHCP lease and the DHCPv6 binding as the same client: by the MAC address of the lease, or by its DUID when the DHCP client sends a DUID-based client identifier (RFC 4361), and by the DUID of the binding. A DHCPv6 client generates its DUID per device, not necessarily from the MAC address of the interface it runs on, so the server can create separate queues instead.

:::
