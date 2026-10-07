# Speed Test

> Speed test measures ping, jitter and TCP and UDP throughput in both directions between two MikroTik routers in one run, through the bandwidth test server of the remote router.

# Speed Test

Speed test measures the link between this router and another MikroTik router in one command: latency and jitter with pings, then TCP and UDP throughput in both directions. It connects to the bandwidth test server of the other router and shows the CPU load of the routers next to the throughput results. Use it to check what a link between two sites, a wireless backhaul or a VPN tunnel delivers. To test one protocol or one direction, or to set packet sizes and speed limits, use [Bandwidth test](bandwidth-test) instead.

## Prerequisites

- The bandwidth test server runs on the remote router. It is enabled by default, with `authenticate=yes` (`/tool/bandwidth-server`).
- The remote router has a user for the test, in a group with the `test` and `winbox` policies. The default `read` and `full` groups have both.
- The firewalls let the test through: the remote router accepts ICMP (the default firewall does), TCP port 2000 and UDP ports 2000-65535 from the testing router, and the testing router accepts UDP from the remote router.
- [Device mode](../system-information-and-utilities/device-mode) allows `bandwidth-test` on both routers. Check it with `/system/device-mode/print` (`bandwidth-test: yes`). Most routers delivered with RouterOS 7.17 or later come in the `home` or `basic` mode, which turn it off (CCR and 1100 series routers come in `advanced`). Turning it on needs physical access to the router.

To limit which routers can run tests against a router, set `allowed-addresses4` and `allowed-addresses6` of its bandwidth test server. The `address` setting of the test user does not limit bandwidth test logins. Do not set `authenticate=no` on a router that the internet can reach.

## Test the link to another router

To check what the link from router A (192.168.88.1) to router B (192.168.88.2) delivers, add a user for the test on router B. A group with only the `test` and `winbox` policies is enough:

```ros
/user/group/add name=speedtest policy=test,winbox
/user/add name=speedtest group=speedtest password=YourStrongPassword
```

Run the test on router A. Use the address of router B on the path you want to measure: for a VPN, the tunnel address of router B. The test fills the link for its whole duration, so users of the link notice it. `test-duration=5s` makes each part of the test 5 seconds long, which is enough for a quick check. With the default, the whole test takes about a minute; on links with high latency, use the default or a longer duration:

```ros
/tool/speed-test address=192.168.88.2 test-duration=5s \
    user=speedtest password=YourStrongPassword
```

The router updates the results during the test. When the test ends, it shows:

```ros
              status: done
      time-remaining: 0s
    ping-min-avg-max: 225us / 265us / 432us
  jitter-min-avg-max: 0s / 29us / 164us
                loss: 0% (0/100)
        tcp-download: 930Mbps local-cpu-load:71%
          tcp-upload: 932Mbps local-cpu-load:61% remote-cpu-load:79%
        udp-download: 924Mbps local-cpu-load:46% remote-cpu-load:52%
          udp-upload: 953Mbps local-cpu-load:56% remote-cpu-load:43%
```

When you no longer need the test user, delete it and its group on router B:

```ros
/user/remove speedtest
/user/group/remove speedtest
```

## Open the firewall for a test over the internet

When the remote router is reachable only over the internet, behind the default firewall, both routers need rules for the test. In this example, router A (198.51.100.10) runs the test, and router B (203.0.113.20) is the remote router.

On router B, accept TCP port 2000 and the UDP ports of the test from router A:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=tcp \
    src-address=198.51.100.10 dst-port=2000 \
    comment="Speed test from router A" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    src-address=198.51.100.10 dst-port=2000-65535 \
    comment="Speed test from router A" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

On router A, accept UDP from router B. Without this rule, the default firewall of router A drops the UDP traffic that router B sends, and the result has no `udp-download` line:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    src-address=203.0.113.20 comment="Speed test to router B" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

Remove the rules after the test, on router B:

```ros
/ip/firewall/filter/remove [find comment="Speed test from router A"]
```

And on router A:

```ros
/ip/firewall/filter/remove [find comment="Speed test to router B"]
```

## Read the results

| Line | Shows |
| :-- | :-- |
| `ping-min-avg-max` | Shortest, average and longest round-trip time of the pings. |
| `jitter-min-avg-max` | Variation of the round-trip time between pings: smallest, average and largest. |
| `loss` | Lost pings in percent, then lost and sent pings: `(0/100)` means that none of 100 pings was lost. |
| `tcp-download`, `udp-download` | Throughput from the remote router to this router. |
| `tcp-upload`, `udp-upload` | Throughput from this router to the remote router. |
| `local-cpu-load`, `remote-cpu-load` | CPU load of this router and of the remote router during that part of the test. `tcp-download` shows only the local load. |

Download and upload are seen from the router that runs the test.

The pings run before the throughput parts, on an idle link, so they do not show the latency under load.

The throughput is the total of all connections of the test: 20 TCP connections by default (more on routers with more than 20 CPU cores), and the UDP parts also use several flows. One connection can get less, for example over bonding or per-connection load balancing, where each connection takes one path.

## Results limited by the CPU

When the CPU of a router is close to full load during the test, the results start with this line:

```text
;;; results can be limited by cpu, note that traffic generation/termination performance might not be representative of forwarding
;;; performance
```

Creating and receiving test traffic costs a router more CPU than forwarding the same traffic. When the warning appears, the test shows the limit of the routers as the source and the destination of the traffic. The link, and traffic that the routers only forward, can carry more. To measure a router or switch as a device under test, run the test between two other routers, one on either side of the device, so that the test traffic passes through it.

Between two sites, the result also depends on both internet connections: the upload of one site is the download of the other. Over a VPN, the encryption also loads the CPU of both routers.

## Troubleshoot

- `authentication failed` on every throughput line: the user name or password is wrong, the group of the test user lacks the `test` or `winbox` policy, or `user` was not given. Without `user`, the command sends no user name, which only a server with `authenticate=no` accepts. The ping part still runs, and the test still takes its full time.
- `loss: 100%`: the remote router does not answer the pings. Check the address and the path to it. When the throughput lines appear anyway, ICMP is filtered on the path or on the remote router.
- Only the ping results appear, without throughput lines: the bandwidth test server of the remote router is turned off, its firewall drops TCP port 2000, or its `allowed-addresses4` or `allowed-addresses6` do not include this router. The test still runs through all its parts.
- The TCP lines appear, but one or both UDP lines are missing: the firewall of the remote router or of this router drops the UDP traffic of the test. The firewall section of this page has the rules for both routers.
- The command fails with `not allowed by device-mode`: device mode turns off `bandwidth-test` on this router. See [Device mode](../system-information-and-utilities/device-mode).

## Technical details

### Test phases

The test runs five parts in this order, shown in `status`: `ping`, `tcp download`, `tcp upload`, `udp download` and `udp upload`, then `done`. `test-duration` sets the length of each part: 10 seconds by default, at least 5 seconds. The router pauses for about a second between the parts, so a test with the default takes about 55 seconds.

### Ping phase

The ping part sends ICMP echo requests, 20 per second: 200 pings with the default `test-duration`, 100 with `test-duration=5s`.

### Connections and ports

The TCP parts use `connection-count` TCP connections, from 1 to 255. The default is 20, or the number of CPU cores of the router that runs the test when it has more than 20: a 64-core router uses 64, also against a server with fewer cores. The session list of the remote server (`/tool/bandwidth-server/session/print detail`) shows the number as `tcp-connection-count`. The TCP connections go to port 2000 of the remote router. The UDP parts use ports from `allocate-udp-ports-from` on the remote router (2000 by default) upward.

For all parameters, see the [`/tool/speed-test`](../cli-reference/tool/speed-test) and [`/tool/bandwidth-server`](../cli-reference/tool/bandwidth-server/) CLI reference.
