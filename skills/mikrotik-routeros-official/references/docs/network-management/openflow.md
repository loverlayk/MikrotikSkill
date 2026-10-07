# Openflow

> RouterOS supports OpenFlow protocols 1.0 and 1.3 for SDN integration, enabling centralized traffic management through controller applications that access switch data paths. It includes basic statistics support and...

# Openflow

RouterOS supports OpenFlow [1.0](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.0.0.pdf) and [1.3](https://opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf), which allow communication between the OpenFlow controller and the OpenFlow agent.

OpenFlow is used to centralize management of network equipment in Software Defined Networks (SDNs).

Applications on the OpenFlow controller have access to the switch's data-path and can perform custom tasks, such as flow steering and traffic monitoring.

The controller sends flows to be added to the agent's flow table. Packet lookup, modification, and forwarding are based on the agent's flow table.

RouterOS supports OpenFlow fast path in simple setups where "goto table" flows are not used.

OpenFlow overrides regular packet processing. Packets received on interfaces that are OpenFlow switch ports do not pass through the regular networking stack unless the OpenFlow controller sets up flows that enable this. Be careful not to disable access to the device when configuring OpenFlow.

OpenFlow support is available as a standalone OpenFlow package.

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

## Configuration Example

The example demonstrates very basic L2 untagged packet forwarding between the sfp-sfpplus1 and sfp-sfpplus2 ports. Faucet is used as a controller.

```routeros
/openflow
add controllers=tcp/10.155.101.182/6653 datapath-id=1/DC:2C:6E:A4:B4:2E disabled=no name=faucet

/openflow/port
add disabled=no interface=sfp-sfpplus1 port-id=1 switch=faucet
add disabled=no interface=sfp-sfpplus2 port-id=2 switch=faucet
```

:::info
If you also intend to use Gauge, add Gauge's IP address and port to the controllers list. In this example, 6654 is the Gauge port: `controllers=tcp/10.155.101.182/6653,tcp/10.155.101.182/6654`
:::

In the Faucet configuration, `dp_id` must match the `datapath-id` from the RouterOS configuration in hex format (`1/DC:2C:6E:A4:B4:2E` → `0x0001dc2c6ea4b42e`):

```routeros
---
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
        dp_id: 0x0001dc2c6ea4b42e
        hardware: "Generic"
        drop_broadcast_source_address: false
        drop_spoofed_faucet_mac: false
        interfaces:
            1:
                name: "h1"
                description: "host1 container"
                native_vlan: 100
                acl_in: 1
            2:
                name: "h2"
                description: "host2 container"
                native_vlan: 100
                acl_in: 1

```

The flows installed by Faucet can be viewed from the `/openflow/flow` menu:

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print detail 
Flags: I - inactive 
 0   switch=faucet version=4 match=" [ { ethdst_m=01000cccccccffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 1   switch=faucet version=4 match=" [ { ethdst_m=01000ccccccdffffffffffff } ]" actions=" []" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 2   switch=faucet version=4 match=" [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8240, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 3   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000fffffffffff0 } ]" actions=" []" 
     info="priority 8236, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 4   switch=faucet version=4 match=" [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 5   switch=faucet version=4 match=" [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8216, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 6   switch=faucet version=4 match=" [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8208, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 7   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } }; { output={ port=2; max_len=0 } } ] 
        } ]" 
     info="priority 8192, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 8   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=4 

 9   switch=faucet version=4 match=" []" actions=" [ { goto=4 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

10   switch=faucet version=4 match=" [ { ethtype=9000 } ]" actions=" []" 
     info="priority 20490, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

11   switch=faucet version=4 match=" [ { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { output={ port=4294967293; max_len=96 } } ] }; { goto=3 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

12   switch=faucet version=4 match=" []" actions=" [ { goto=3 } ]" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=2 

13   switch=faucet version=4 match=" [ { inport=00000001 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

14   switch=faucet version=4 match=" [ { inport=00000002 }; { vlanvid=0000 } ]" 
     actions=" [ { apply-actions= [ { pushvlan={ ethertype=33024 } }; { setfield={ vlanvid=1064 } } ] }; { goto=2 } ]" 
     info="priority 4096, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

15   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=1 

16   switch=faucet version=4 match=" [ { inport=00000001 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

17   switch=faucet version=4 match=" [ { inport=00000002 } ]" actions=" [ { goto=1 } ]" 
     info="priority 20480, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

18   switch=faucet version=4 match=" []" actions=" []" 
     info="priority 0, idletimeout 0, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=0 

19   switch=faucet version=4 match=" [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=1; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 413, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

20   switch=faucet version=4 match=" [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 263, cookie 1524372928, removenotify 0" 
     table-id=2 

21   switch=faucet version=4 match=" [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { apply-actions= [ { popvlan={} }; { output={ port=2; max_len=0 } } ] } ]" 
     info="priority 8192, idletimeout 417, hardtimeout 0, cookie 1524372928, removenotify 0" table-id=3 

22   switch=faucet version=4 match=" [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]" 
     actions=" [ { goto=3 } ]" info="priority 8191, idletimeout 0, hardtimeout 267, cookie 1524372928, removenotify 0" 
     table-id=2 

```

To view flow statistics, use the `stats` parameter:

```routeros
[admin@CCR2004_2XS_111] /openflow/flow>  print stats 
Columns: SWITCH, MATCH, BYTES, PACKETS, DURATION
 # SWITCH  MATCH                                                                BYTES  PACKETS  DURATION  
 0 faucet   [ { ethdst_m=01000cccccccffffffffffff } ]                            3590       25  6m26s890ms
 1 faucet   [ { ethdst_m=01000ccccccdffffffffffff } ]                               0        0  6m26s890ms
 2 faucet   [ { ethdst_m=ffffffffffffffffffffffff }; { vlanvid=1064 } ]          5552       26  6m26s890ms
 3 faucet   [ { ethdst_m=0180c2000000fffffffffff0 } ]                            4917       25  6m26s890ms
 4 faucet   [ { ethdst_m=0180c2000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 5 faucet   [ { ethdst_m=01005e000000ffffff000000 }; { vlanvid=1064 } ]             0        0  6m26s890ms
 6 faucet   [ { ethdst_m=333300000000ffff00000000 }; { vlanvid=1064 } ]          5992       25  6m26s890ms
 7 faucet   [ { vlanvid=1064 } ]                                                  340        5  6m26s890ms
 8 faucet   []                                                                      0        0  6m26s890ms
 9 faucet   []                                                                  20391      106  6m26s890ms
10 faucet   [ { ethtype=9000 } ]                                                    0        0  6m26s890ms
11 faucet   [ { vlanvid=1064 } ]                                                  530        8  6m26s890ms
12 faucet   []                                                                      0        0  6m26s890ms
13 faucet   [ { inport=00000001 }; { vlanvid=0000 } ]                           39135      463  6m26s890ms
14 faucet   [ { inport=00000002 }; { vlanvid=0000 } ]                           37936      459  6m26s890ms
15 faucet   []                                                                  17941      100  6m26s890ms
16 faucet   [ { inport=00000001 } ]                                             48664      515  6m26s890ms
17 faucet   [ { inport=00000002 } ]                                             46348      507  6m26s890ms
18 faucet   []                                                                      0        0  6m26s890ms
19 faucet   [ { ethdst=dc2c6ec5a7ff }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
20 faucet   [ { ethdst=dc2c6e46f893 }; { vlanvid=1064 } ]                       28340      408  6m26s780ms
21 faucet   [ { inport=00000001 }; { ethsrc=dc2c6ec5a7ff }; { vlanvid=1064 } ]  12020      142  2m660ms   
22 faucet   [ { inport=00000002 }; { ethsrc=dc2c6e46f893 }; { vlanvid=1064 } ]  10769      133  1m55s660ms
```

## Statistics

Fast path statistics can be viewed from `/openflow/print fast-path`. In this example, the fast path does not work because of the complexity of the flows Faucet installs.

```routeros
[admin@CCR2004_2XS_111] /openflow> print fast-path 
  openflow-fast-path-packets: 0 0
    openflow-fast-path-bytes: 0 0
```

Port statistics can be viewed from the `/openflow/port` menu.

```routeros
[admin@CCR2004_2XS_111] /openflow/port> print stats
Columns: INTERFACE, PORT-ID, RX-BYTES, TX-BYTES, RX-PACKETS, TX-PACKETS
# INTERFACE     PORT-ID  RX-BYTES  TX-BYTES  RX-PACKETS  TX-PACKETS
0 sfp-sfpplus1        1    115668     81180        1223        1035
1 sfp-sfpplus2        2    112200     82188        1215        1037
```
