# OpenFlow

> RouterOS supports OpenFlow protocols 1.0 and 1.3 for SDN integration, enabling centralized traffic management through controller applications that access switch data paths. It includes basic statistics support and...

# OpenFlow

RouterOS supports OpenFlow [1.0](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.0.0.pdf) and [1.3](https://opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf), which allow communication between the OpenFlow controller and the OpenFlow agent.

OpenFlow is used to centralize management of network equipment in Software Defined Networks (SDNs).

Applications on the OpenFlow controller have access to the switch's data-path and can perform custom tasks, such as flow steering and traffic monitoring.

The controller sends flows to be added to the agent's flow table. Packet lookup, modification, and forwarding are based on the agent's flow table.

RouterOS supports OpenFlow fast path in simple setups where "goto table" flows are not used.

OpenFlow overrides regular packet processing. Packets received on interfaces that are OpenFlow switch ports do not pass through the regular networking stack unless the OpenFlow controller sets up flows that enable this; for example, an IP address on such a port does not answer. Be careful not to disable access to the device when configuring OpenFlow: manage the router and reach the controller through a port that is not an OpenFlow port.

OpenFlow support is in the `openflow` extra package (see [Packages](../getting-started/installation-and-upgrade/packages)).

When the connection to the controller is lost, the router keeps the installed flows and forwards by
them; it does not fall back to regular forwarding. The router connects to the controllers in
`controllers`, or listens on `passive-port` for a controller to connect; TLS connections use
`certificate` and `verify-peer` (see the [CLI reference](../cli-reference/openflow/)).

## Supported basic capabilities

- OFPC\_FLOW\_STATS
- OFPC\_TABLE\_STATS
- OFPC\_PORT\_STATS
- OFPC\_GROUP\_STATS

## Unsupported basic capabilities

- OFPC\_IP\_REASM
- OFPC\_QUEUE\_STATS
- OFPC\_PORT\_BLOCKED

## Unsupported configuration parameters and actions (version 1)

- OFPAT\_SET\_NW\_SRC
- OFPAT\_SET\_NW\_DST
- OFPAT\_SET\_NW\_TOS
- OFPAT\_SET\_TP\_SRC
- OFPAT\_SET\_TP\_DST
- OFPAT\_ENQUEUE
- OFPAT\_VENDOR

## Unsupported configuration parameters and actions (version 1.3)

- OFPT\_SET\_ASYNC
- OFPAT\_SET\_NW\_TTL
- OFPAT\_DEC\_NW\_TTL
- OFPAT\_COPY\_TTL\_OUT
- OFPAT\_COPY\_TTL\_IN

## Configuration example

This example forwards untagged packets between ether2 and ether3 under the control of a
[Faucet](https://faucet.nz/) controller at 192.0.2.10.

```routeros
/openflow
add controllers=tcp/192.0.2.10/6653 datapath-id=1/52:54:00:AA:00:01 \
    disabled=no name=faucet

/openflow/port
add disabled=no interface=ether2 port-id=1 switch=faucet
add disabled=no interface=ether3 port-id=2 switch=faucet
```

:::note
If you also intend to use Gauge, add Gauge's IP address and port to the controllers list. In this example, 6654 is the Gauge port: `controllers=tcp/192.0.2.10/6653,tcp/192.0.2.10/6654`
:::

In the Faucet configuration (`faucet.yaml`), `dp_id` must match the `datapath-id` from the RouterOS
configuration in hex format (`1/52:54:00:AA:00:01` → `0x0001525400aa0001`), and the interface numbers
are the `port-id` values:

```yaml
vlans:
    100:
        description: "untagged"

acls:
    1:
        - rule:
            actions:
                allow: 1

dps:
    test_switch:
        dp_id: 0x0001525400aa0001
        hardware: "Generic"
        drop_broadcast_source_address: false
        drop_spoofed_faucet_mac: false
        interfaces:
            1:
                name: "h1"
                description: "host1"
                native_vlan: 100
                acl_in: 1
            2:
                name: "h2"
                description: "host2"
                native_vlan: 100
                acl_in: 1
```

When the controller is connected, the hosts on ether2 and ether3 reach each other, and the flows that
Faucet installs are in the `/openflow/flow` menu. With `version=default`, the router and Faucet agree
on OpenFlow 1.3, shown as `version=4` in the flows. Faucet uses several tables; this shows table 0:

```routeros
/openflow/flow/print detail where table-id=0
```

```text
0  switch=faucet version=4 match=" []" actions=" []"
   info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
      removenotify 0" table-id=0

1  switch=faucet version=4 match=" [ { inport=00000002 } ]"
   actions=" [ { goto=1 } ]"
   info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928,
      removenotify 0" table-id=0

2  switch=faucet version=4 match=" [ { inport=00000001 } ]"
   actions=" [ { goto=1 } ]"
   info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928,
      removenotify 0" table-id=0
```

The full flow table shows Faucet's pipeline: table 0 checks the input port, table 1 adds VLAN 100 to
untagged packets, table 2 sends unknown source addresses to the controller (port `4294967293`) for
learning, table 3 forwards to learned destinations, and table 4 floods. Learned flows have timeouts:

<details>
<summary>All flows</summary>

```text
 0  switch=faucet version=4 match=" [ { ethdst_m=01000cccccccffffffffffff } ]"
    actions=" []"
    info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 1  switch=faucet version=4 match=" [ { ethdst_m=01000ccccccdffffffffffff } ]"
    actions=" []"
    info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 2  switch=faucet version=4 match=" [ { ethdst_m=0180c2000000fffffffffff0 } ]"
    actions=" []"
    info="priority 8236, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 3  switch=faucet version=4
    match=" [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } }; { output={ port=2; max_len=0 } } ] } ]"
    info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 4  switch=faucet version=4
    match=" [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } }; { output={ port=2; max_len=0 } } ] } ]"
    info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 5  switch=faucet version=4
    match=" [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } }; { output={ port=2; max_len=0 } } ] } ]"
    info="priority 8208, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 6  switch=faucet version=4 match=" [ { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } }; { output={ port=2; max_len=0 } } ] } ]"
    info="priority 8192, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 7  switch=faucet version=4 match=" []" actions=" []"
    info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

 8  switch=faucet version=4 match=" []" actions=" [ { goto=4 } ]"
    info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=3

 9  switch=faucet version=4 match=" [ { ethtype=9000 } ]" actions=" []"
    info="priority 20490, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=2

10  switch=faucet version=4 match=" [ { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { output={ port=4294967293; max_len=96 } }
       ] }; { goto=3 } ]"
    info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=2

11  switch=faucet version=4 match=" []" actions=" [ { goto=3 } ]"
    info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=2

12  switch=faucet version=4 match=" []" actions=" []"
    info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=1

13  switch=faucet version=4 match=" []" actions=" []"
    info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=0

14  switch=faucet version=4
    match=" [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } }; { output={ port=2; max_len=0 } } ] } ]"
    info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=4

15  switch=faucet version=4 match=" [ { inport=00000002 }; { vlanvid=0000 } ]"
    actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; {
       setfield={ vlanvid=1064 } } ] }; { goto=2 } ]"
    info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=1

16  switch=faucet version=4 match=" [ { inport=00000002 } ]"
    actions=" [ { goto=1 } ]"
    info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=0

17  switch=faucet version=4 match=" [ { inport=00000001 }; { vlanvid=0000 } ]"
    actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; {
       setfield={ vlanvid=1064 } } ] }; { goto=2 } ]"
    info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=1

18  switch=faucet version=4 match=" [ { inport=00000001 } ]"
    actions=" [ { goto=1 } ]"
    info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=0

19  switch=faucet version=4
    match=" [ { ethdst=525400bb0001 }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1;
       max_len=0 } } ] } ]"
    info="priority 8192, idletimeout 403, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=3

20  switch=faucet version=4
    match=" [ { ethdst=525400bb0002 }; { vlanvid=1064 } ]"
    actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=2;
       max_len=0 } } ] } ]"
    info="priority 8192, idletimeout 445, hardtimeout 0, cookie 1524372928,
       removenotify 0" table-id=3

21  switch=faucet version=4
    match=" [ { inport=00000002 }; { ethsrc=525400bb0002 }; { vlanvid=1064 } ]"
    actions=" [ { goto=3 } ]"
    info="priority 8191, idletimeout 0, hardtimeout 295, cookie 1524372928,
       removenotify 0" table-id=2

22  switch=faucet version=4
    match=" [ { inport=00000001 }; { ethsrc=525400bb0001 }; { vlanvid=1064 } ]"
    actions=" [ { goto=3 } ]"
    info="priority 8191, idletimeout 0, hardtimeout 253, cookie 1524372928,
       removenotify 0" table-id=2
```

</details>

To view flow statistics, use the `stats` parameter:

```routeros
/openflow/flow/print stats where table-id=0
```

```text
Columns: SWITCH, MATCH, BYTES, PACKETS, DURATION
# SWITCH  MATCH                     BYTES  PACKETS  DURATION
0 faucet   []                           0        0  29s820ms
1 faucet   [ { inport=00000002 } ]   1107       11  29s790ms
2 faucet   [ { inport=00000001 } ]   1107       11  29s690ms
```

## Statistics

Fast path statistics can be viewed with `/openflow/print fast-path`. With the multi-table flows that
Faucet installs, the fast path is not used:

```routeros
/openflow/print fast-path
```

```text
  openflow-fast-path-packets: 0
    openflow-fast-path-bytes: 0
```

Port statistics are in the `/openflow/port` menu:

```routeros
/openflow/port/print stats
```

```text
Columns: INTERFACE, PORT-ID, RX-BYTES, TX-BYTES, RX-PACKETS, TX-PACKETS
# INTERFACE  PORT-ID  RX-BYTES  TX-BYTES  RX-PACKETS  TX-PACKETS
0 ether2           1      1107       830          11           9
1 ether3           2      1107       830          11           9
```
