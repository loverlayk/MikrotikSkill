# DHCP Client

> The RouterOS DHCP client gets an IPv4 address and network settings for an interface from a DHCP server. This page explains what the client applies from a lease, the options it requests and sends, the routes it adds,...

# DHCP Client

**Sub-menu:** `/ip/dhcp-client`

The DHCP client gets an IPv4 address and network settings for an interface from a DHCP server. It is typically used on the interface that connects the router to an ISP or another upstream network, and it can be enabled on any Ethernet-like interface. For how the DHCP exchange, leases and renewal work, see [DHCP concepts](./).

When the client gets a lease, it applies the received settings to the router:

- The IP address and netmask are added to the interface as a dynamic address.
- A dynamic default route through the received gateway, or the received classless static routes (option 121), are added to the routing table. The `add-default-route` property controls this.
- The received DNS servers are added to the dynamic servers of the DNS resolver (`use-peer-dns`), and the received NTP servers are added to the servers of the NTP client (`use-peer-ntp`).

The client renews the lease before it expires. When the lease is lost or the client is disabled, the dynamic address and routes are removed.

## Configuration Examples

### Simple DHCP client

Add a DHCP client on the ether1 interface:

```ros
/ip/dhcp-client/add interface=ether1
```

Use `print detail` to see the lease the client got and the settings it received:

```ros
[admin@MikroTik] > /ip/dhcp-client/print detail
 0   name="client1" interface=ether1 add-default-route=yes default-route-distance=1
     default-route-tables=default check-gateway=none use-peer-dns=yes use-peer-ntp=yes
     allow-reconfigure=no use-broadcast=both dhcp-options=hostname,clientid
     status=bound address=192.168.0.65/24 gateway=192.168.0.1 dhcp-server=192.168.0.1
     primary-dns=192.168.0.1 primary-ntp=192.168.0.1 expires-after=9m44s
```

## DHCP Options

The client asks the DHCP server for the following options:

- Option 1 - Subnet Mask.
- Option 3 - Gateway Addresses.
- Option 6 - DNS Server Addresses.
- Option 15 - Domain Name.
- Option 33 - Static Routes.
- Option 42 - NTP Server Addresses.
- Option 43 - Vendor Specific Information.
- Option 121 - Classless Static Routes.
- Option 138 - CAPWAP Access Controller Addresses.

The client sends the options listed in its `dhcp-options` property, chosen from the options defined in `/ip/dhcp-client/option`. Three options are predefined:

| Name | Code | Value |
| :-- | --: | :-- |
| clientid\_duid | 61 | 0xff$(CLIENT\_DUID) |
| clientid | 61 | 0x01$(CLIENT\_MAC) |
| hostname | 12 | $(HOSTNAME) |

By default, the client sends `hostname` and `clientid`: the router's identity as its hostname, and a client identifier based on the MAC address of the client interface. To identify the client by the router's DUID instead (RFC 4361), replace `clientid` with `clientid_duid` in `dhcp-options`. Option values use the same syntax as DHCP server options. The variables they can contain are listed in the [`/ip/dhcp-client/option`](../../cli-reference/ip/dhcp-client/option) reference.

## Properties

All properties, status values and commands of the DHCP client are described in the [`/ip/dhcp-client`](../../cli-reference/ip/dhcp-client/) CLI reference. The routes the client adds need more explanation.

### Routes from the lease

The `add-default-route` property controls which of the received routes the client adds:

- `yes` (default): the client adds the classless static routes (option 121) when the server sends them, and otherwise a default route through the received gateway (option 3). When option 121 is present, the gateway from option 3 is ignored, as RFC 3442 requires, so the server must include the default route in option 121.
- `special-classless`: the client adds both the classless static routes and a default route through the received gateway. Use it when the server sends classless static routes without a default route, and the default route should still come from option 3.
- `no`: the client adds no routes.

The routes get the distance set in `default-route-distance` (1 by default) and go to the routing tables listed in `default-route-tables`. The `default` entry is the main routing table, or the VRF routing table when the client interface belongs to a VRF. An entry can also set its own distance, for example `default-route-tables=backup:5`.

If another default route already exists, the route with the lower distance is used. When the distances are equal, both routes are active and traffic is shared between them (ECMP). Use `default-route-distance` to control which route is preferred, and `check-gateway` to stop using a route when its gateway does not respond.

## Script Examples

The variables a lease script receives are listed with the `script` property in the [`/ip/dhcp-client`](../../cli-reference/ip/dhcp-client/) CLI reference.

### Lease script example

This example adds a default route to the `WAN1` routing table through the received gateway, updates the route when the gateway changes, and removes it when the lease ends. Create the routing table first, then add the client with the script:

:::warning
Be aware that some variables might be reserved in specific menus and cannot be used there. For details, see [reserved variable names](../../developer-guides/scripting/#reserved-variable-names).

:::

```ros
/routing/table/add name=WAN1 fib
/ip/dhcp-client/add interface=ether2 add-default-route=no script={
    :local count [/ip/route/print count-only where comment="WAN1"]
    :if ($bound=1) do={
        :if ($count = 0) do={
            /ip/route/add gateway=$"gateway-address" comment="WAN1" routing-table=WAN1
        } else={
            :if ($count = 1) do={
                :local test [/ip/route/find where comment="WAN1"]
                :if ([/ip/route/get $test gateway] != $"gateway-address") do={
                    /ip/route/set $test gateway=$"gateway-address"
                }
            } else={
                :error "Multiple routes found"
            }
        }
    } else={
        /ip/route/remove [find comment="WAN1"]
    }
}
```

### Using received option 43 to set the ACS URL

A DHCP server can send the URL of a TR-069 Auto Configuration Server (ACS) in the vendor-specific information option (option 43). The client script receives this option in the `vendor-specific` variable, so it can set the ACS URL of the TR-069 client when the lease is bound. The TR-069 client is a separate package.

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    :if ($bound=1) do={
        /tr069-client/set acs-url=$"vendor-specific"
    }
}
```

### Default gateway outside the leased subnet

Some DHCP servers send a gateway (option 3) that is not in the leased subnet. For example, the server offers 192.168.88.100/24 and the gateway 172.16.1.1. The default route the client adds then stays inactive, because the gateway cannot be reached:

```ros
[admin@MikroTik] > /ip/route/print
Flags: D - DYNAMIC; I - INACTIVE, A - ACTIVE; c - CONNECT, d - DHCP
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS      GATEWAY     DISTANCE
DId 0.0.0.0/0        172.16.1.1         1
DAc 192.168.88.0/24  ether1             0
```

To make the gateway reachable, add the leased address again as a /32 address with the gateway as its network. This creates a connected route to the gateway. Do it in the client script, which receives the leased address, the gateway and the interface:

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    /ip/address/add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface
}
```

This short script adds another address with every new lease. The following script keeps a single address and replaces it when the leased address or the gateway changes:

```ros
/ip/dhcp-client/set [find interface=ether1] script={
    /ip/address {
        :local ipId [find where comment="dhcpL address"]
        :if ($ipId != "") do={
            :if (!([get $ipId address] = ($"lease-address" . "/32") && [get $ipId network]=$"gateway-address")) do={
                remove $ipId
                add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface comment="dhcpL address"
            }
        } else={
            add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface comment="dhcpL address"
        }
    }
}
```
