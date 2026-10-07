# Cloud

> MikroTik cloud services in RouterOS: a DDNS name for the router, the clock and time zone at startup, cloud backup, Back To Home VPN and File Share. Which services are on by default and how the router reaches the...

# Cloud

MikroTik runs free cloud services for RouterOS devices. They give the router a DNS name, set its clock and time zone, store a backup, and let you reach your home network or share files from the router, even when the router has no public IP address. The router always opens the connection to the MikroTik servers, so none of the services needs port forwarding on another device.

## Services

| Service | Menu | On by default | Use it to |
| :-- | :-- | :-- | :-- |
| DDNS | `/ip/cloud` | No | Get a DNS name that follows the router's public IP address. |
| Time update | `/ip/cloud`, `/system/clock` | Yes | Set the clock and time zone when the router starts. |
| [Cloud backup](./cloud-backup) | `/system/backup/cloud` | No | Store an encrypted backup on the MikroTik servers. |
| [Back To Home](./back-to-home) | `/ip/cloud` | No | Reach your home network over a WireGuard VPN from a phone or computer. |
| [File Share](./file-share) | `/ip/cloud/back-to-home-file` | No | Share files from the router's storage through an HTTPS link. |

[Communication with MikroTik Cloud Services](./communication-mikrotik-cloud-servers) lists every connection RouterOS makes to MikroTik servers and how to turn each one off.

:::info
Cloud services work on MikroTik devices and on Cloud Hosted Router (CHR) with a paid perpetual license. They are not available in RouterOS for x86.
:::

## DDNS

Dynamic DNS (DDNS) gives the router a DNS name under `sn.mynetname.net` that follows its public IP address. Use it to reach the router by name when your ISP changes the address.

To enable DDNS and see the name:

```ros
[admin@MikroTik] > /ip/cloud/set ddns-enabled=yes
[admin@MikroTik] > /ip/cloud/print
          ddns-enabled: yes
  ddns-update-interval: none
           update-time: yes
        public-address: 203.0.113.10
              dns-name: hf1234abcd5.sn.mynetname.net
                status: updated
      back-to-home-vpn: revoked-and-disabled
```

The name stays the same for the device, and the router keeps it up to date by itself. To send an update right away, for example after you change the internet connection:

```ros
/ip/cloud/force-update
```

The name only makes the router easier to find. It does not open any access: the default firewall drops connections to the router from the internet. To reach the router remotely, use [Back To Home](./back-to-home), or [allow the services in the firewall](../../getting-started/securing-your-router#opening-management-access-from-wan-advanced). You can also get a [Let's Encrypt certificate](../../authentication-authorization-accounting/certificates#lets-encrypt-certificate) for the name.

To make the name resolve to the router's own address instead of the public one, for example to reach the router by name inside your network:

```ros
/ip/cloud/advanced/set use-local-address=yes
```

To turn DDNS off:

```ros
/ip/cloud/set ddns-enabled=auto
```

The router then asks the cloud server to delete the name. With `auto`, DDNS stays on while Back To Home is enabled, so turn off Back To Home first if you use it.

## Time update

When the router starts, it sets its clock and time zone from the cloud server, unless the [NTP client](../../system-information-and-utilities/ntp) is enabled. This does not need DDNS. The cloud time is approximate: for an accurate clock, use the NTP client.

To stop the router from asking the cloud for the time and time zone:

```ros
/ip/cloud/set update-time=no
/system/clock/set time-zone-autodetect=no
```

## Technical details

### How the router reaches the cloud

The router sends encrypted requests to `cloud2.mikrotik.com` on UDP port 15252. The cloud server replies with the address it received the request from, and the router shows it in `public-address`, and in `public-address-ipv6` when the router also reaches the server over IPv6. Behind NAT, this is the public address of the NAT device, not an address on the router. On a router with several internet connections, it is the address of the connection that the route to `cloud2.mikrotik.com` uses.

When the router cannot be reached from the internet directly, Back To Home and File Share connect through MikroTik relay servers. The router keeps a connection open to the nearest relay, and clients reach the router through it. The traffic stays end-to-end encrypted: the keys are only on the router and on the client, so the relay cannot read the data.

### DDNS updates

- The name is the serial number of the device in lower case followed by `.sn.mynetname.net`. It resolves to `public-address` with a time to live (TTL) of 60 seconds, and when the router also has `public-address-ipv6`, to that address as well.
- Behind NAT, where the router cannot see its public address on its own interfaces, the router sends an update every minute.
- `force-update` does nothing while DDNS is off (`ddns-enabled=auto` without Back To Home).
- When DDNS turns off, the router sends a delete request to the cloud server, and the name stops resolving within a few minutes.
- With `use-local-address=yes`, the name resolves to the address the router sends its requests from, and `public-address` still shows the public address.
- While the cloud server does not answer, `status` shows `updating...` and the router retries with growing intervals. `failed to connect` means a request got no reply.

### Time update at startup

- The router asks the cloud server for the time once after it starts, also with `ddns-enabled=auto`. DDNS updates and `force-update` do not set the clock again.
- While the NTP client is enabled, the router does not use the cloud time, even when the NTP client cannot reach any server.
- The router logs each change of the clock, for example:

  ```text
  system,critical,info cloud change time Sep/24/2026 03:01:57 => Sep/24/2026 06:25:50
  ```

- For `time-zone-autodetect`, the cloud server looks up the location of the router's public IP address, and the router applies that time zone, including daylight saving time.

For all properties, see [`/ip/cloud`](../../cli-reference/ip/cloud/) and [`/ip/cloud/advanced`](../../cli-reference/ip/cloud/advanced) in the CLI reference.
