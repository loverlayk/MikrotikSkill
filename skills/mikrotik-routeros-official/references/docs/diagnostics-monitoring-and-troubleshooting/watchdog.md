# Watchdog

> Watchdog reboots the router when the system stops responding or when one IP address stops answering pings, and writes a support output file after a software failure.

# Watchdog

The watchdog reboots the router by itself in two cases, each with its own settings in `/system/watchdog`:

- The software watchdog timer reboots the router when the system stops responding. This is mostly caused by a hardware malfunction, and the reboot lets the device recover by itself. It is on by default (`watchdog-timer=yes`).
- The ping watchdog reboots the router when one IP address stops answering pings. It is off by default (`watch-address=none`).

A watchdog reboot is an automatic `/system/reboot`, not a software failure. The watchdog timer reboots the router because a service does not respond as fast as it should. Reasons can be damaged hardware, a slow software implementation of a service, a DDoS attack, a bad configuration and others.

## Reboot when an address stops answering

A remote router can lose its uplink or its VPN and stay unreachable until someone restarts it, for example a router on a mast whose wireless link hangs. The ping watchdog reboots such a router when an address on the other side of the link stops answering:

```ros
/system/watchdog/set watch-address=192.0.2.1
```

Use an address that is reliably up and that the router reaches through the link you care about, such as the gateway of the uplink. For a VPN, watch an address inside the tunnel, such as the tunnel address of the far end, not its public address: the public address can still answer when the tunnel is down. An address that is down for its own reasons reboots a router that works.

The router pings the address six times, spread over `ping-timeout` (1 minute by default, so one ping every 10 seconds), and reboots when all six pings fail. After a boot, it waits `ping-start-after-boot` (5 minutes by default) before the first ping. On a router that has been up longer than `ping-start-after-boot`, setting `watch-address` starts the pings at once.

Set `ping-start-after-boot` longer than the link needs to come up after a boot, for example a VPN or an LTE connection. Otherwise the router reboots before the link is up. After each reboot, this time is also your window to log in and set `watch-address=none`.

:::warning
If the address stays unreachable, the router reboots again after each boot, every `ping-start-after-boot` plus `ping-timeout`: about every 6 minutes with the defaults. Choose the address carefully, and keep another way in, such as console access or MAC Telnet from a neighbor.
:::

To turn the ping watchdog off:

```ros
/system/watchdog/set watch-address=none
```

The ping watchdog reboots for as long as the address does not answer. For a limited number of reboots, or for other actions when an address stops answering, use [Netwatch](netwatch) with a script.

## See why the router rebooted

After a ping watchdog reboot, the log shows these entries (topics `system,error,critical` for the first one):

```text
System rebooted because of ping watchdog timeout
router rebooted
```

A ping watchdog reboot does not write a support output file (`autosupout.rif`).

## Support output after a crash

When the software fails, the router writes `autosupout.rif` by itself (`automatic-supout=yes`, on by default) and renames the previous file to `autosupout.old.rif`. Send these files to MikroTik support with the problem description. For more about support output files, see [Supout.rif](../getting-started/supout-rif).

The router can also send the file by email. For example, to send it to `support@example.com` through the SMTP server `192.0.2.1`:

```ros
/system/watchdog/set auto-send-supout=yes \
    send-email-to=support@example.com send-smtp-server=192.0.2.1
```

When `send-email-from` or `send-smtp-server` is not set, the router uses the values from [`/tool/e-mail`](../system-information-and-utilities/e-mail). While `auto-send-supout=no`, `print` does not show the email settings.

## Technical details

### Ping interval

The interval between the pings is `ping-timeout` divided by six: 10 seconds with the default `1m`, 20 seconds with `2m`. The reboot follows a few seconds after the sixth failed ping, so it comes about `ping-timeout` after the first failed ping.

Older exports call `ping-start-after-boot` `no-ping-delay`.

### Software watchdog timer

With `watchdog-timer=yes`, the router reboots when the system is unresponsive for a minute. Set `watchdog-timer=no` to turn it off.

For all parameters, see the [`/system/watchdog`](../cli-reference/system/watchdog) CLI reference.
