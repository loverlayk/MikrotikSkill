# Connection rate

> Connection Rate is a MikroTik RouterOS firewall feature that monitors and filters traffic based on connection speed, using 'connection-bytes' and 'connection-rate' to detect high-speed connections for prioritization...

# Connection rate

Connection Rate is a firewall matcher that allows capturing traffic based on the present speed of the connection.

## Theory

Each entry in the connection tracking table represents bidirectional communication. Every time a packet gets associated with a particular entry, the packet size value (including the IP header) is added to the "connection-bytes" value for this entry. (In other words, "connection-bytes" includes both - upload and download).

Connection Rate calculates the speed of connection based on the change of "connection-bytes". The connection rate is recalculated every second and does not have any averages.

Both options "connection-bytes" and "connection-rate" work only with TCP and UDP traffic. (You need to specify a protocol to activate these options). In the "connection-rate" option you can specify a range of speed that you like to capture:

```ros
ConnectionRate ::= [!]From-To
  From,To ::= 0..4294967295    (integer number)
```

### Rule Example

These rules will capture TCP/UDP traffic that is going through the router when the connection speed is below 100kbps:

```ros
/ip/firewall/filter
add action=accept chain=forward connection-rate=0-100k protocol=tcp
add action=accept chain=forward connection-rate=0-100k protocol=udp
```

## Application Example - Traffic Prioritization

Connection-rate can be used in various ways, that still need to be realized, but the most common setup will be to detect and set lower priorities to the "heavy connections" (connections that maintain a fast rate for long periods (such as P2P, HTTP, FTP downloads)). By doing this you can prioritize all other traffic that usually includes VoIP and HTTP browsing and online gaming.

The method described in this example can be used together with other ways to detect and prioritize traffic. As the connection-rate option does not have any averages, we need to determine what will be the margin that identifies "heavy connections". If we assume that a normal HTTP browsing connection is less than 500kB (4Mb) long and VoIP requires no more than 200kbps speed, then every connection that after the first 500kB still has more than 200kbps speed can be assumed to be "heavy".

(You might have different "connection-bytes" for HTTP browsing and different "connection-rate" for VoIP in your network - so, please, do your own research before applying this example)

For this example, let's assume that we have a 6Mbps upload and download connection to the ISP.

### Quick Start for Impatient

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no

/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```

#### Explanation

In mangle, we need to separate all connections into two groups, and then mark packets from the 2 groups. As we are talking about client traffic, the most logical place for marking would be the mangle chain forward.

Keep in mind that as soon as a "heavy" connection has lower priority and the queue will hit max-limit - the heavy connection will drop speed, and connection-rate will be lower. This will result in a change to a higher priority and the connection will be able to get more traffic for a short while, when the connection-rate rises again and that will again result in a change to lower priority. To avoid this we must make sure that once detected, "heavy connections" will remain marked as "heavy connections" for all time.

#### IP Firewall mangle

This rule will ensure that "heavy" connections will remain heavy, and mark the rest of the connections with the default connection mark:

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
```

These two rules will mark all heavy connections based on our standards: that every connection that after the first 500kB still has more than 200kbps speed can be assumed to be "heavy":

```ros
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
```

The last two rules in mangle will simply mark all traffic from corresponding connections:

```ros
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no
```

#### Queue

This is a simple queue tree that is placed on the Interface HTB - "public" is an interface where your ISP is connected, and "local" is where your clients are. If you have more than 1 "public" or more than 1 "local" you will need to mangle upload and download separately and place the queue tree in global-out:

```ros
/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```
