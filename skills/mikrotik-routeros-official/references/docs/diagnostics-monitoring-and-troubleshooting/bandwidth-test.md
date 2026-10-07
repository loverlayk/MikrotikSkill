# Bandwidth test

> The bandwidth test measures TCP or UDP throughput between two MikroTik routers: the client in /tool/bandwidth-test sends to or receives from the bandwidth test server of the other router. It covers prerequisites,...

# Bandwidth test

The bandwidth test measures the throughput between two MikroTik routers. The client (`/tool/bandwidth-test`) on one router connects to the bandwidth test server (`/tool/bandwidth-server`) of the other router, sends or receives TCP or UDP traffic, and shows the rate every second. Use it to check a wireless or WAN link, or to find the bottleneck on a path.

To measure latency, jitter and TCP and UDP throughput in both directions in one run, use [Speed test](speed-test).

:::warning
A test without a speed limit uses all the bandwidth the path can give and a large part of the routers' CPU time, and other traffic on the link, routing protocols and management access suffer. On a link in use, set a speed limit or test when the link is quiet.
:::

## Prerequisites

On the router that runs the server:

- The bandwidth test server is on. It is on by default, with authentication:

  ```ros
  [admin@MikroTik] > /tool/bandwidth-server/print
                    enabled: yes
               authenticate: yes
    allocate-udp-ports-from: 2000
               max-sessions: 100
         allowed-addresses4:
         allowed-addresses6:
  ```

- [Device mode](../system-information-and-utilities/device-mode) allows the bandwidth test, on the server and on the client: `/system/device-mode/print` shows `bandwidth-test: yes`. Most routers delivered with RouterOS 7.17 or later come in the `home` or `basic` mode, which turn it off (CCR and 1100 series routers come in `advanced`). Turning it on needs physical access to the router, so check it before you install a router at a remote site.
- A user on the server for the client to log in with, in a group with both the `test` and the `winbox` policy; the server checks both. The default `read` and `full` groups have both, so an existing administrator works too. A group with only these two policies is enough:

  ```ros
  /user/group/add name=btest policy=test,winbox
  /user/add name=btest group=btest password=change-this-password
  ```

- The firewall accepts TCP port 2000 and UDP ports 2000-65535 from the client. The default firewall drops them from the WAN side; when the server is reachable only over the internet, add rules for the test, as in [Open the firewall for a test over the internet](speed-test#open-the-firewall-for-a-test-over-the-internet), and remove them afterwards.

On the client, UDP tests in the `receive` and `both` directions need the server's UDP packets to arrive: a client behind NAT or a firewall that drops them receives nothing. Use TCP in that case, or accept UDP from the server on the client.

After the tests, remove the test user (`/user/remove btest` and `/user/group/remove btest`) and any firewall rules you added.

## Test a link

To check that a wireless link carries 50 Mbit/s in each direction without taking it over, set a speed limit in both directions:

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password protocol=tcp direction=both \
    local-tx-speed=50M remote-tx-speed=50M duration=10s
                status: done testing
              duration: 11s
            tx-current: 50.3Mbps
  tx-10-second-average: 49.9Mbps
      tx-total-average: 49.9Mbps
            rx-current: 51.3Mbps
  rx-10-second-average: 49.8Mbps
      rx-total-average: 49.8Mbps
           random-data: no
             direction: both
      connection-count: 20
        local-cpu-load: 9%
       remote-cpu-load: 0%
```

`local-tx-speed` limits what the client sends, `remote-tx-speed` what the server sends. Without `duration`, the test runs until you press <kbd>Control</kbd>+<kbd>C</kbd>.

### Check a link for packet loss

To check that a link delivers a rate without loss, send UDP at that rate and watch `lost-packets`:

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password direction=receive \
    remote-tx-speed=500M duration=10s
                status: done testing
              duration: 11s
            rx-current: 491.1Mbps
  rx-10-second-average: 486.2Mbps
      rx-total-average: 486.2Mbps
          lost-packets: 3
           random-data: no
             direction: receive
               rx-size: 1500
      connection-count: 20
        local-cpu-load: 3%
       remote-cpu-load: 6%
```

At 491 Mbit/s of 1500-byte packets, about 41,000 packets arrive per second, so 3 lost packets in the last second are a loss of less than 0.01%. A link that loses a share of the packets at a rate below its capacity has a problem, for example interference on a wireless link. TCP does not show such loss: it sends the lost data again and only slows down.

Most wireless links share the air time between the two directions. Test each direction on its own (`direction=transmit`, then `direction=receive`) to see what each direction gets, and `direction=both` to see what the link carries in total.

### Measure the maximum throughput

Without speed limits, the test sends as much as it can:

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password protocol=tcp direction=both \
    duration=10s
                status: done testing
              duration: 10s
            tx-current: 920.3Mbps
  tx-10-second-average: 918.0Mbps
      tx-total-average: 918.0Mbps
            rx-current: 748.4Mbps
  rx-10-second-average: 674.0Mbps
      rx-total-average: 674.0Mbps
           random-data: no
             direction: both
      connection-count: 20
        local-cpu-load: 16%
       remote-cpu-load: 4%
```

TCP shows what TCP applications get on the path: TCP slows down when packets are lost or delayed. With the default 20 connections, the result is the total of many connections; one connection (`connection-count=1`) is closer to a single download, which the latency of the path limits more. UDP shows how much the path delivers when the sender does not slow down, and how much it loses. The default test is UDP, with the server sending (`direction=receive`) 1500-byte packets:

```ros
[admin@MikroTik] > /tool/bandwidth-test address=10.0.0.2 user=btest \
    password=change-this-password duration=10s
                status: done testing
              duration: 11s
            rx-current: 957.3Mbps
  rx-10-second-average: 943.9Mbps
      rx-total-average: 943.9Mbps
          lost-packets: 18632
           random-data: no
             direction: receive
               rx-size: 1500
      connection-count: 20
        local-cpu-load: 5%
       remote-cpu-load: 7%
```

To test with other packet sizes, set `local-udp-tx-size` (client) and `remote-udp-tx-size` (server). The size is the whole IP packet, from 52 to 64000 bytes over IPv4; packets larger than the smallest MTU on the path are fragmented. Small packets test how many packets per second a path forwards, large packets how many bits.

To test to a router's IPv6 link-local address, add the interface: `address=fe80::34:23ff:fe6a:570c%ether1`.

## Read the results

- `tx-` values are what the client sends, `rx-` values what it receives.
- `current` is the last second, `10-second-average` the last 10 seconds, and `total-average` the whole test.
- UDP counts the whole IP packet, headers included. TCP counts only the data, so a TCP result is a few percent lower than the traffic on the link, and the acknowledgements that flow back are not counted at all. On a wireless link, they also use air time.
- `lost-packets` (UDP) is the number of packets that did not arrive in the last second, not a total. The client shows it for what it receives (`receive` and `both`); for what the client sends, the server's session list shows it.
- `local-cpu-load` and `remote-cpu-load` are the CPU load of the client and the server during the test. A load near 100% means that the router, not the link, limits the result. A lower value does not rule this out: one busy CPU core can limit a test while the others idle, so check the cores in `/system/resource/cpu/print`.
- `connection-count` is the number of TCP connections, or of UDP streams with their own ports: 20, or the number of CPU cores on routers with more than 20. Several connections spread the load over the CPU cores.

Without a speed limit, a UDP sender sends at full rate for about the first second, then more than the receiver reports. On a link slower than the sender, `lost-packets` therefore stays above zero, and the `rx-` values are the throughput of the link. To check a link for loss, set a speed below its capacity, as in Check a link for packet loss.

To test a link that compresses data, set `random-data=yes`: the test then sends data that cannot be compressed. It costs more CPU time on both routers, and on routers with slow CPUs it can limit the result.

## Test a router's forwarding capacity

Generating and receiving the test traffic takes CPU time on the client and the server. To measure how much a router forwards, do not run the test from or to that router: connect three routers in a chain, run the server on one end, the client on the other, and test through the router in the middle. Route the end routers' subnets through the middle router, and watch `local-cpu-load` and `remote-cpu-load`: when an end router is near 100%, it limits the result, not the router in the middle. The end routers must be able to send and receive more than the router in the middle forwards. Use 1500-byte packets to measure the bit rate, and small UDP packets (`local-udp-tx-size=64`) to measure the packet rate, which limits most routers first. When one pair of routers cannot load the router under test, use more pairs or the [traffic generator](traffic-generator).

## Secure the server

The server answers every client that reaches TCP port 2000. With `authenticate=yes` (the default), a client must log in with a user that has the `test` and `winbox` policies. Do not set `authenticate=no` on a router that untrusted networks reach: anyone could then load the router and its links. The default firewall drops TCP port 2000 from the WAN side; keep it that way, or accept it only from known addresses.

To accept tests only from known addresses, list them; other clients get `can not connect`. A user's own `address` setting does not limit bandwidth test logins, so use these lists. Set `allowed-addresses6` too when the router has IPv6 addresses:

```ros
/tool/bandwidth-server/set allowed-addresses4=192.0.2.0/24 \
    allowed-addresses6=2001:db8::/32
```

To turn the server off:

```ros
/tool/bandwidth-server/set enabled=no
```

`max-sessions` limits how many tests run at once (100 by default), whatever their number of connections. A single test cannot use more connections than `max-sessions` either, so keep it at or above the clients' `connection-count`.

The server lists the running tests in `/tool/bandwidth-server/session`, from the server's view (`send` means that the server sends):

```ros
[admin@MikroTik] > /tool/bandwidth-server/session/print \
    proplist=protocol,direction,user,tx-current,rx-current
Columns: PROTOCOL, DIRECTION, USER, TX-CURRENT, RX-CURRENT
#  PROTOCOL  DIRECTION  USER   TX-CURRENT  RX-CURRENT
0  tcp       both       admin  624.1Mbps   917.2Mbps
```

## Troubleshoot

| Status or symptom | Cause and fix |
| :-- | :-- |
| `authentication failed` | Wrong user or password, or no user when the server has `authenticate=yes`. The user must exist on the server, in a group with both the `test` and `winbox` policies (`/user/group/print` on the server). |
| `can not connect` | The server is off or not reachable on TCP port 2000, the client is not in `allowed-addresses4`/`allowed-addresses6`, or the server already runs `max-sessions` tests. |
| `disconnected` | The connection was lost during the test, or the test uses more connections than the server's `max-sessions`. |
| `not allowed by device-mode` | Device mode on the router that runs the test has `bandwidth-test: no`. |
| A UDP `receive` test shows 0 bps. | The server's UDP packets do not reach the client: the client is behind NAT or a firewall. Use TCP, or allow UDP from the server. UDP `transmit` tests work from behind NAT. |
| The result is lower than the link speed, with a CPU load near 100%. | The router limits the test; test through the router instead (see Test a router's forwarding capacity). |

## Technical details

### Ports and connections

The client opens a TCP connection to port 2000 of the server (the `btest` service in `/ip/service`), logs in and exchanges the results over it. UDP test data uses ports from `allocate-udp-ports-from` (2000 by default) upward on both routers: the server one port per test, the client one port per stream. Each router takes free ports, so the numbers move up while other tests run. TCP tests use `connection-count` TCP connections to port 2000. The server shows IPv4 clients in IPv4-mapped IPv6 form (the IPv4 address after `::ffff:`), for example `::ffff:192.0.2.1`.

### Packet size and counting

`local-udp-tx-size` and `remote-udp-tx-size` set the IP packet size: 1500 bytes is 1472 bytes of UDP data. The UDP rate counts the IP packets, the TCP rate the TCP data. Interface counters also include the Ethernet header, so they show slightly more than the test.

For all parameters, see the [`/tool/bandwidth-test`](../cli-reference/tool/bandwidth-test), [`/tool/bandwidth-server`](../cli-reference/tool/bandwidth-server/) and [`/tool/bandwidth-server/session`](../cli-reference/tool/bandwidth-server/session) CLI reference.
