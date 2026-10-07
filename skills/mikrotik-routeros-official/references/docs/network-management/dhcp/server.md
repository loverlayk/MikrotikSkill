# DHCP Server

> The RouterOS DHCP server assigns IPv4 addresses and network settings to clients from IP pools, with static leases, networks, DHCP options and option sets, option matchers, RADIUS support, rate limiting and rogue DHCP...

# DHCP Server

**Sub-menu:** `/ip/dhcp-server`

The DHCP server assigns IPv4 addresses and network settings to clients on the networks the router serves. It leases addresses from an IP pool and sends the settings of the matching DHCP network: gateway, DNS servers, domain name, NTP and WINS servers, and other options. It can also hand out static leases bound to specific clients, and get leases from a RADIUS server. For how the DHCP exchange, leases and renewal work, see [DHCP concepts](./).

A DHCP server needs:

- An IP address on the server interface. Without one, the server is shown as invalid.
- An IP pool with the addresses to hand out (`/ip/pool`). Do not include the router's own address in the pool.
- A DHCP network (`/ip/dhcp-server/network`) with the settings sent to clients in that subnet.
- The DHCP server itself (`/ip/dhcp-server`), which ties the interface to the pool.

The `setup` command creates the pool, network and server in one step. The following configuration examples show both ways.

Each interface can have one DHCP server for directly connected clients. More servers on the same interface are possible for requests that come through DHCP relays, one for each relay address (see the `relay` property).

:::warning
The DHCP server needs a real interface to receive raw Ethernet packets. When it runs on a bridge, the bridge needs at least one port that receives these packets; the server does not work correctly on an empty bridge.

:::

## Configuration Examples

### Setup

The `setup` command creates the IP pool, the network and the DHCP server in one step. It asks for each value in turn and suggests values based on the address of the interface.

First, add an IP address to the interface:

```ros
/ip/address/add address=192.168.88.1/24 interface=ether3
```

Then run `setup` and confirm or change each suggested value:

```ros
[admin@MikroTik] > /ip/dhcp-server/setup
Select interface to run DHCP server on
dhcp server interface: ether3
Select network for DHCP addresses
dhcp address space: 192.168.88.0/24
Select gateway for given network
gateway for dhcp network: 192.168.88.1
Select pool of ip addresses given out by DHCP server
addresses to give out: 192.168.88.2-192.168.88.254
Select whether the DHCP server sends DNS servers to clients
send dns: yes
Select DNS servers (leave empty to use servers from DNS settings)
dns servers: 192.168.88.1
Select lease time
lease time: 1800s
```

The DHCP server is now active on ether3.

### Manual configuration

To configure the same DHCP server manually, create each part yourself:

1. Add the IP address of the router on the interface the server runs on. In this example, the router is also the gateway of the network:

   ```ros
   /ip/address/add address=192.168.88.1/24 interface=bridge1
   ```

2. Create an IP pool with the addresses to give out. Do not include the router's own address in the pool:

   ```ros
   /ip/pool/add name=dhcp_pool0 ranges=192.168.88.2-192.168.88.254
   ```

3. Add a network entry with the settings sent to clients, such as the gateway and DNS servers:

   ```ros
   /ip/dhcp-server/network/add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
   ```

4. Add the DHCP server on the interface, with the pool:

   ```ros
   /ip/dhcp-server/add address-pool=dhcp_pool0 interface=bridge1 name=dhcp1
   ```

## Properties

All properties of the DHCP server are described in the [`/ip/dhcp-server`](../../cli-reference/ip/dhcp-server/) CLI reference. The following behavior needs more explanation.

### Requests for unknown addresses

A client that moved from another network, or whose lease the server no longer has, can ask for an address the server cannot give. With `authoritative=yes` (the default), the server answers such requests with DHCPNAK, so the client starts over immediately instead of waiting for its request to time out. With `authoritative=no`, the server ignores such requests when they are broadcast, for example from a rebinding client, and leaves them to another server. A unicast renewal request is answered with every setting: with DHCPNAK, or with a new lease when the requested address is free in the pool.

To let another server answer first, for example a primary server with this router as a backup, set `delay-threshold`. The server then ignores requests until the client has been trying for the set time, which the client reports in the `secs` field of its requests.

### Clients behind a DHCP relay

A server answers relayed requests only when its `relay` property is set: to the address of the relay, which is the relay's `local-address`, or to `255.255.255.255` for any relay. Several servers can then run on the same interface, one for each relay. For a complete example, see [DHCP Relay](./relay).

### DNS entries for clients

With `add-dns-entries=yes`, the server adds a dynamic DNS entry (type A) for each bound lease, so clients can be reached by name through the router's DNS resolver. The name is the host name the client sends, followed by `add-dns-entries-suffix` (`lan` by default), for example `laptop.lan`, and the TTL of the entry is the lease time. When the network has no `domain`, the server also sends the suffix to clients as their domain name.

## Network

**Sub-menu:** `/ip/dhcp-server/network`

A network entry holds the settings sent to clients whose address is in that network: gateway, DNS and NTP servers, domain name, options and network boot settings. When `dns-server` or `ntp-server` is not set, the server sends the DNS or NTP servers the router itself uses; set `dns-none` or `ntp-none` to send none. All properties are described in the [`/ip/dhcp-server/network`](../../cli-reference/ip/dhcp-server/network) CLI reference.

## Leases

**Sub-menu:** `/ip/dhcp-server/lease`

The lease menu shows the leases the server has given out, as dynamic entries, and the static leases you add to give a client a fixed address, an address from a specific pool, or its own settings. All lease properties, status values and commands are described in the [`/ip/dhcp-server/lease`](../../cli-reference/ip/dhcp-server/lease/) CLI reference.

When a client asks for an address, the server picks one:

- A client with a static lease gets the address of its lease. Static addresses are not checked for conflicts.
- Other clients get a free address from the pool. With `conflict-detection` (the default), the server first checks the address with an ARP request and an ICMP echo request, which delays the offer by about half a second. If another host answers, the address is kept as a lease with the `conflict` status for the lease time, and the client is offered another free address.

The server then offers the address, and the lease is bound when the client requests it. When a client releases its address or its lease expires, a dynamic lease is removed and the address returns to the pool; a static lease stays and is used again when the client returns.

### Lease storage

The server saves its leases to disk periodically, every 5 minutes by default, to reduce writes to the flash storage. This interval and the RADIUS accounting settings are set in `/ip/dhcp-server/config`, see the [`/ip/dhcp-server/config`](../../cli-reference/ip/dhcp-server/config) CLI reference.

### Rate limiting

You can limit the bandwidth of a client with the `rate-limit` property of its lease. The server then adds a dynamic simple queue for the address of the lease.

:::warning
Queues do not apply to FastTracked traffic. Make sure the firewall does not FastTrack the traffic you want to limit.

:::

Only static leases can have a rate limit, so first make the lease static:

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/print 
Flags: X - disabled, R - radius, D - dynamic, B - blocked 
 #   ADDRESS               MAC-ADDRESS       HOST-NAME               SERVER               RATE-LIMIT               STATUS 
 0 D 192.168.88.254        6C:3B:6B:7C:41:3E MikroTik                DHCPv4_Server                                 bound 

[admin@MikroTik] > /ip/dhcp-server/lease/make-static 0

[admin@MikroTik] > /ip/dhcp-server/lease/print 
Flags: X - disabled, R - radius, D - dynamic, B - blocked 
 #   ADDRESS               MAC-ADDRESS       HOST-NAME               SERVER               RATE-LIMIT               STATUS 
 0   192.168.88.254        6C:3B:6B:7C:41:3E MikroTik                DHCPv4_Server                                 bound
```

Then set the rate limit. The server creates a dynamic simple queue for the lease:

```ros
[admin@MikroTik] > /ip/dhcp-server/lease/set 0 rate-limit=10M/10M

[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<MikroTik/6C:3B:6B:7C:41:3E>" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s 
      bucket-size=0.1/0.1
```

:::note
`allow-dual-stack-queue` is enabled by default, so a DHCP lease and a DHCPv6 binding of the same client share one dynamic simple queue. Without it, the server creates separate queues for IPv4 and IPv6.

:::

The shared queue contains both the IPv4 and the IPv6 address:

```ros
[admin@MikroTik] > /queue/simple/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="dhcp-ds<MikroTik/6C:3B:6B:7C:41:3E>" target=192.168.88.254/32,fdb4:4de7:a3f8:418c::/66 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 
      burst-time=0s/0s bucket-size=0.1/0.1 
```

## RADIUS Support

The DHCP server can also get leases from a RADIUS server (`use-radius=yes`). It sends and accepts the following RADIUS attributes.

### Access-Request

- NAS-Identifier - router identity.
- NAS-IP-Address - IP address of the router itself.
- NAS-Port - the ID of the interface where the DHCP server is configured. This value is the same as the IF-MIB::ifIndex.
- NAS-Port-Id - the name of the interface where the DHCP server is configured.
- NAS-Port-Type - Ethernet.
- Calling-Station-Id - client identifier (active-client-id).
- Framed-IP-Address - IP address of the client (active-address).
- Called-Station-Id - the name of the DHCP server.
- User-Name - MAC address of the client (active-mac-address).
- Password - " ".

### Access-Accept

- Framed-IP-Address - IP address that will be assigned to a client.
- Framed-Pool - IP pool from which to assign an IP address to a client.
- Rate-Limit - Data rate limitation for DHCP clients. Format is: `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time][priority] [rx-rate-min[/tx-rate-min]]]]`. All rates should be numbers with optional 'k' (1,000s) or 'M' (1,000,000s). If tx-rate is not specified, rx-rate is used as tx-rate too. Same goes for tx-burst-rate and tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as the default. Priority takes values 1..8, where 1 implies the highest priority, but 8 - the lowest. If rx-rate-min and tx-rate-min are not specified, rx-rate and tx-rate values are used. The rx-rate-min and tx-rate-min values cannot exceed rx-rate and tx-rate values.
- Ascend-Data-Rate - TX/RX data rate limitation if multiple attributes are provided, the first limits the tx data rate, the second - the RX data rate. If used together with Ascend-Xmit-Rate, specifies the RX rate. 0 if unlimited.
- Ascend-Xmit-Rate - tx data rate limitation. It may be used to specify the TX limit only instead of sending two sequential Ascend-Data-Rate attributes (in that case Ascend-Data-Rate will specify the receive rate). 0 if unlimited.
- Session-Timeout - max lease time (lease-time).

### Rate limit per lease

A RADIUS server can assign a rate limit to each lease with the Mikrotik-Rate-Limit attribute. First, set the DHCP server to use RADIUS:

```ros
/radius
add address=10.0.0.1 secret=VERYsecret123 service=dhcp
/ip/dhcp-server
set dhcp1 use-radius=yes
```

Then configure the RADIUS server to send the Mikrotik-Rate-Limit attribute. For FreeRADIUS with MySQL, add entries to the `radcheck` and `radreply` tables for the MAC address of the client, for example:

```sql
INSERT INTO `radcheck` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Auth-Type', ':=', 'Accept');

INSERT INTO `radreply` (`username`, `attribute`, `op`, `value`) VALUES
('00:0C:42:00:D4:64', 'Framed-IP-Address', '=', '192.168.88.254'),
('00:0C:42:00:D4:64', 'Mikrotik-Rate-Limit', '=', '10M');
```

## Alerts

The DHCP alert finds rogue DHCP servers on an interface. It watches the DHCP replies on the interface and checks whether each one comes from a valid DHCP server. A reply from an unknown server is logged, and the alert can also run a script:

```ros
[admin@MikroTik] > /log/print where topics~"dhcp"
 00:34:23 dhcp,critical,error dhcp alert on Public: discovered unknown dhcp server, mac 00:02:29:60:36:E7, ip 10.5.8.236
```

Because DHCP replies can be unicast, the alert might not see the offers other servers send to clients. So the alert also acts as a DHCP client: it sends its own DHCPDISCOVER about once a minute.

:::warning
Do not use the DHCP alert on a router that is a DHCP client on the same interface: the DHCPDISCOVER messages the alert sends can disturb the DHCP client. Use the alert on DHCP servers or on routers with a static IP address.

:::

**Sub-menu:** `/ip/dhcp-server/alert`

New alerts are created disabled; enable them after adding. All alert properties are described in the [`/ip/dhcp-server/alert`](../../cli-reference/ip/dhcp-server/alert/) CLI reference.

## DHCP Options

**Sub-menu:** `/ip/dhcp-server/option`

You can define additional options for the DHCP server to send. When the same option is set on several levels, the first of these levels wins:

1. RADIUS.
2. Lease.
3. Server.
4. Network.

The server sends an option only when the client asks for it in its parameter request list (option 55). To send an option even when the client does not ask for it, set `force` on the option, for example on the `auto-proxy-config` option from the following examples:

```ros
/ip/dhcp-server/option/set [find name=auto-proxy-config] force=yes
```

All option properties, including how option values are written and which variables they can contain, are described in the [`/ip/dhcp-server/option`](../../cli-reference/ip/dhcp-server/option/) CLI reference.

### DHCP Option Sets

**Sub-menu:** `/ip/dhcp-server/option/sets`

This menu allows combining multiple options in option sets, which later can be used to override the default DHCP server option set.

### Example

**Classless Route**

The classless static routes option (option 121, RFC 3442) sends routes to the client. This example sends a route to 160.0.0.0/24 and a default route, both through 10.1.101.1. The value consists of:

- `18` - Prefix length 24.
- `A00000` - The significant octets of the destination, 160.0.0.
- `0A016501` - The gateway, 10.1.101.1.
- `00` - Prefix length 0, which is the default route.
- `0A016501` - The gateway of the default route, 10.1.101.1.

A client that receives option 121 ignores the router option (option 3), so the default route is included here as well.

```ros
/ip/dhcp-server/option
add code=121 name=classless value=0x18A000000A016501000A016501
/ip/dhcp-server/network
set 0 dhcp-option=classless
```

Result on the client:

```ros
[admin@MikroTik] > /ip/route/print
Flags: D - DYNAMIC; A - ACTIVE; c - CONNECT, d - DHCP
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS   GATEWAY     DISTANCE
DAd 0.0.0.0/0     10.1.101.1         1
DAd 160.0.0.0/24  10.1.101.1         1
```

With the `$(NETWORK_GATEWAY)` variable, the gateway is taken from the network settings instead of being written into the value:

```ros
/ip/dhcp-server/option
add name=classless code=121 value="0x18A00000\$(NETWORK_GATEWAY)0x00\$(NETWORK_GATEWAY)"
```

**Auto proxy config**

```ros
/ip/dhcp-server/option 
  add code=252 name=auto-proxy-config value="'https://autoconfig.something.lv/wpad.dat'"
```

## Option matcher

The option matcher identifies DHCP clients by any DHCP option in their requests, and gives them an address from a specific IP pool. It compares the option either exactly (`exact`) or looks for the value anywhere in the option (`substring`). Use substring matching when the option contains more than the part you want to match, for example a vendor class identifier that also contains the device model or MAC address.

:::note
When two substring matchers match the same option, for example one for "ABC" and one for "ABCDE" with an option value of "ABCDEF", it is random which of them applies.

:::

:::note
Clients with a static lease keep their static address, even when a matcher matches them.

:::

All matcher properties are described in the [`/ip/dhcp-server/matcher`](../../cli-reference/ip/dhcp-server/matcher) CLI reference.

### Option matcher examples

Match *dhcp1* server clients by *exact* Vendor class identifier (DHCP option 60) and assign an address from the *pool1*:

```ros
/ip/dhcp-server/matcher
add address-pool=pool1 code=60 matching-type=exact name=test1 server=dhcp1 value=android-dhcp-11
```

Match clients on all DHCP servers by *exact* Client Id (DHCP option 61) configured as hex value and assign address from the *pool2*:

```ros
/ip/dhcp-server/matcher
add address-pool=pool2 code=61 matching-type=exact name=test2 server=all value=0x016c3b6bed8364
```

Match *dhcp2* server clients *partially* by Hostname (DHCP option 12) and assign an address from the *pool3*:

```ros
/ip/dhcp-server/matcher
add address-pool=pool3 code=12 matching-type=substring name=test3 server=dhcp2 value=MikroTik
```
