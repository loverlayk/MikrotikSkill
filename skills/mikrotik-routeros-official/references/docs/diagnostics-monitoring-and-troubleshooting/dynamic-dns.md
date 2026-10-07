# DNS update

> The DNS update tool sends an RFC 2136 dynamic update, signed with a TSIG hmac-md5 key, to the authoritative DNS server of a zone to point a name at an IPv4 address.

# DNS update

The `/tool/dns-update` command sends one dynamic update (RFC 2136) to the authoritative DNS server of a zone and points a name in that zone at an IPv4 address. The update is signed with a TSIG key (RFC 8945), so the server can check that it comes from you, as in a secure dynamic update (RFC 3007). Use it for a zone that you run yourself, for example on a BIND server.

You do not need this command in two common cases:

- For a name that follows the router's own public address without running a DNS server, use the DDNS service of [IP Cloud](../network-management/cloud/#ddns).
- Dynamic DNS services that take updates over HTTP, such as DynDNS, are updated with [Fetch](../system-information-and-utilities/fetch) instead.

## Prerequisites

- A DNS server that is authoritative for the zone and accepts dynamic updates over TCP port 53.
- A TSIG key that the server accepts for updates of the zone, with the algorithm hmac-md5. RouterOS signs with hmac-md5 only; the command has no algorithm setting.
- The name of the key and its secret in base64, as configured on the server. For example on BIND, create the key with `tsig-keygen -a hmac-md5 dns-update-key`, because BIND creates keys with another algorithm by default, and allow this key to update only the name it needs (`update-policy`).
- A router clock that differs from the server's clock by less than 5 minutes. The signature allows 300 seconds of difference, so keep the clock synchronized with [NTP](../system-information-and-utilities/ntp).
- A firewall on the server side that accepts TCP port 53 from the router.

## Point a name at an address

Point `office.example.com` at 198.51.100.20 on the DNS server 192.0.2.53, with the key `dns-update-key`. Replace the key with the base64 secret of your key, and keep the quotes, because a base64 value can end in `=`:

```ros
/tool/dns-update dns-server=192.0.2.53 zone=example.com \
    name=office address=198.51.100.20 ttl=300 \
    key-name=dns-update-key key="c2VjcmV0LWtleS1mb3ItZXhhbXBsZQ=="
```

`ttl=300` keeps the record for 5 minutes in the caches of other DNS servers, so they pick up a changed address soon. Without `ttl`, the record gets one day.

When the server accepts the update, the command prints nothing. When it does not, the command stops with a `failure:` message; the Troubleshoot section lists what each one means.

How the parameters work:

- `name` is relative to `zone`: `name=office` with `zone=example.com` updates `office.example.com`. A full name is doubled: `name=office.example.com` updates `office.example.com.example.com`. A name with a trailing dot is refused with `failure: bad name`.
- The update first deletes all A records of the name and then adds the new one, so it replaces the address instead of adding a second one.
- `ttl` sets the time to live of the record in seconds. Without `ttl`, the record gets 86400 seconds (one day), which is long for an address that changes.
- `address` takes one IPv4 address. Two addresses fail with `failure: only one address allowed`, and an IPv6 address is refused. The command updates A records only.

## Keep the name current

The command sends one update each time it runs. To keep a name pointing at an address that changes, run it from a script when the address changes, for example from the lease script of the [DHCP client](../network-management/dhcp/client) on the WAN interface, or regularly from a [scheduler](../system-information-and-utilities/scheduler) entry. The script reads the current address, removes the prefix length (see [Strip netmask](../developer-guides/scripting/scripting-examples#strip-netmask)), and passes the address to `/tool/dns-update`.

Things to keep in mind for such a script:

- Each update changes the zone on the server. Compare the address with the address the name has now (`:resolve`), and send the update only when it differs.
- At startup, wait until [NTP](../system-information-and-utilities/ntp) has synchronized the clock, so that the server accepts the signature.
- Behind NAT or carrier-grade NAT, the address on the WAN interface is not the public one. The router's public address is in `public-address` of [IP Cloud](../network-management/cloud/).
- The key is part of the command, so every user who can read the script can read the key.

## Troubleshoot

| Message | Meaning |
| :-- | :-- |
| `failure: update send failed` | The router could not open a TCP connection to port 53 of the server: the server is down, does not listen on TCP, or a firewall blocks it. |
| `failure: reply not signed` | The server rejected the signature, for example because the key name or the key is wrong. |
| `failure: refused` | The server refuses the update, for example because the key has no permission to update this zone, or because the update was sent without a key. |
| `failure: name not within zone` | The name is not in the zone. Check `zone` and `name`. |
| `failure: bad name` | `name` is not valid, for example because it ends with a dot. |

## Technical details

### Protocol

The update goes to TCP port 53 of `dns-server`. The message is a DNS UPDATE for the zone (zone section `example.com. IN SOA`). Its update section deletes the A records of the name (`office.example.com. ANY A`) and adds the new record (`office.example.com. 86400 IN A 198.51.100.20`).

### Signature

With `key-name` and `key`, the message carries a TSIG record with the algorithm `hmac-md5.sig-alg.reg.int` and a fudge of 300 seconds, the allowed clock difference. `key` is the base64 secret of the key. Without `key-name` and `key`, the update is sent unsigned, and most servers refuse it.

For all parameters, see the [`/tool/dns-update`](../cli-reference/tool/dns-update) CLI reference.
