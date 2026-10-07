# Nv2

> Nv2 is a MikroTik proprietary wireless protocol using TDMA for efficient media access in PtMP networks, supporting both Atheros 802.11n and legacy devices without hardware upgrades. It offers dynamic rate selection,...

# Nv2

Nv2 is a proprietary wireless protocol developed by MikroTik for use with Atheros 802.11 wireless chips. It is based on TDMA (Time Division Multiple Access) media access technology, as opposed to the CSMA (Carrier Sense Multiple Access) technology used in regular 802.11 devices. TDMA solves the hidden node problem and improves media usage, resulting in better throughput and latency — especially in PtMP networks.

Nv2 is supported on Atheros 802.11n chips and legacy 802.11a/b/g chips starting from AR5212, but is not supported on the older AR5211 and AR5210 chips. This means both 11n and legacy devices can participate in the same network, and no hardware upgrades are required to implement Nv2.

Media access in an Nv2 network is controlled by the Nv2 Access Point. The AP divides time into fixed-size "periods", which are then dynamically split into downlink (AP to clients) and uplink (clients to AP) portions based on the queue state on the AP and clients. Uplink time is further divided between connected clients according to their bandwidth requirements. At the beginning of each period, the AP broadcasts a schedule that tells clients when they should transmit and how much time they can use.

To allow new clients to connect, the Nv2 AP periodically assigns uplink time for an "unspecified" client. A new client uses this interval to initiate registration with the AP. The AP then estimates the propagation delay between itself and the client, and begins periodically scheduling uplink time for that client to complete registration and receive data.

Nv2 implements dynamic rate selection on a per-client basis, along with ARQ for data transmissions, enabling reliable communication across Nv2 links.

For QoS, Nv2 supports a variable number of priority queues with a built-in default QoS scheduler. This can be complemented by fine-grained QoS policies based on firewall rules or priority information propagated across the network using VLAN priority or MPLS EXP bits.

The Nv2 protocol supports a maximum of 511 clients per interface.

## Nv2 Protocol Implementation Status

Nv2 includes the following features:

| Feature | Description |
|---|---|
| TDMA media access | Time Division Multiple Access for media control |
| WDS support | Wireless Distribution System compatibility |
| QoS support | Variable number of priority queues |
| Data encryption | Encryption of transmitted data |
| RADIUS authentication | RADIUS-based authentication features |
| Statistics fields | Available statistics and reporting fields |
| Fixed Downlink mode | Support for fixed downlink operation |
| Uplink/Downlink ratio | Configurable uplink/downlink ratio support |
| Nv2 AP synchronization | Experimental support for AP synchronization |

## Compatibility and Coexistence with Other Wireless Protocols

Nv2 protocol is not compatible with or based on any other available wireless protocols or implementations, whether TDMA-based or any other kind. This means that **only Nv2-supporting and enabled devices can participate in an Nv2 network**.

Regular 802.11 devices will not recognize or be able to connect to an Nv2 AP. RouterOS devices that have Nv2 support (i.e., running RouterOS version 5.0rc1 or higher) will see Nv2 APs when issuing the scan command, but will only connect to an Nv2 AP if properly configured.

Because Nv2 does not use CSMA technology, it may disturb other networks operating on the same channel. Equally, other networks may disturb an Nv2 network, since every non-Nv2 signal is treated as noise.

The key points regarding compatibility and coexistence are:

* Only RouterOS devices can participate in an Nv2 network.
* Only RouterOS devices will see an Nv2 AP when scanning.
* An Nv2 network will disturb other networks on the same channel.
* An Nv2 network may be affected by any other network on the same channel, whether Nv2 or not.
* An Nv2-enabled device will not connect to any other TDMA-based network.

## How Nv2 compares with Nstreme and 802.11

### Nv2 vs 802.11

The key differences between Nv2 and 802.11:

* Media access is scheduled by AP - this eliminates the hidden node problem and allows implementing a centralized media access policy - AP controls how much time is used by every client and can assign time to clients according to some policy instead of every device contending for media access.
* Reduced propagation delay overhead - There are no per-frame ACKs in Nv2 - this significantly improves throughput, especially on long-distance links where data frame and following ACK frame propagation delay significantly reduces the effectiveness of media usage.
* Reduced per frame overhead - Nv2 implements frame aggregation and fragmentation to maximize assigned media usage and reduce per-frame overhead (interframe spaces, preambles).

### Nv2 vs Nstreme

The key differences between Nv2 and Nstreme:

* Reduced polling overhead - instead of polling each client, Nv2 AP broadcasts an uplink schedule that assigns time to multiple clients; this can be considered "group polling" - no time is wasted on polling each client individually, leaving more time for actual data transmission. This improves throughput, especially in PtMP configurations.
* Reduced propagation delay overhead - Nv2 must not poll each client individually; this allows the creation of an uplink schedule based on estimated distance (propagation delay) to clients such that media usage is most effective. This improves throughput, especially in PtMP configurations.
* More control over latency - reduced overhead, adjustable period size and QoS features allow for more control over latency in the network.

## Configuring Nv2

The **wireless-protocol** setting controls which wireless protocol is selected and used. Note that the meaning of this setting depends on the interface role (either AP or client) that depends on the interface **mode** setting. Find possible values of **wireless-protocol** and their meaning in the table below.

| value | AP | client |
| :-- | :-- | :-- |
| unspecified | establish nstreme or 802.11 network based on old **nstreme** setting | connect to nstreme or 802.11 network based on old **nstreme** setting |
| any | same as **unspecified** | scan for all matching networks, no matter what protocol, connect using protocol of chosen network |
| 802.11 | establish 802.11 network | connect to 802.11 networks only |
| nstreme | establish Nstreme network | connect to Nstreme networks only |
| Nv2 | establish Nv2 network | connect to Nv2 networks only |
| Nv2-nstreme-802.11 | establish Nv2 network | scan for Nv2 networks, if suitable network found - connect, otherwise scan for Nstreme networks, if suitable network found - connect, otherwise scan for 802.11 network and if suitable network found - connect. |
| Nv2-nstreme | establish Nv2 network | scan for Nv2 networks, if suitable network found - connect, otherwise scan for Nstreme networks and if suitable network found - connect |

Note that **wireless-protocol** values **Nv2-nstreme-802.11** and **Nv2-nstreme** **DO NOT** specify some hybrid or special kind of protocol - these values are implemented to simplify client configuration when the protocol of the network that the client must connect to can change. Using these values can help in migrating the network to Nv2 protocol.

Most of the Nv2 settings are significant only to the Nv2 AP - Nv2 client automatically adapts necessary settings from the AP. The following settings are relevant to the Nv2 AP:

* **Nv2-queue-count** - Specifies how many priority queues are used in Nv2 network. For more details see [QoS in Nv2 network](#qos-in-nv2-network).
* **Nv2-qos** - Controls the frame to priority queue mapping policy. For more details see [QoS in Nv2 network](#qos-in-nv2-network).
* **Nv2-cell-radius** - Specifies the distance to the farthest client in the Nv2 network in km. This setting affects the size of the contention time slot that AP allocates for clients to initiate a connection and also the size of time slots used for estimating distance to the client. If this setting is too small, clients that are farther away may have trouble connecting and/or disconnect with a "ranging timeout" error. Although during normal operation the effect of this setting should be negligible, in order to maintain maximum performance, it is advised to not increase this setting if not necessary, so the AP is not reserving time that is actually never used, but instead allocates it for actual data transfer.
* **tdma-period-size** - Specifies the size in ms of time periods that Nv2 AP uses for media access scheduling. A smaller period can potentially decrease latency (because AP can assign time for client sooner), but will increase protocol overhead and therefore decrease throughput. On the other hand - increasing period will increase throughput but also increase latency. It may be required to increase this value for especially long links to get acceptable throughput. This necessity can be caused by the fact that there is a "propagation gap" between downlink (from AP to clients) and uplink (from clients to AP) data during which no data transfer is happening. This gap is necessary because the client must receive the last frame from the AP - this happens after propagation delay after AP's transmission, and only then the client can transmit - as a result, the frame from the client arrives at the AP after propagation delay after client's transmission (so the gap is propagation delay times two). The longer the distance, the bigger the necessary propagation gap in every period. If the propagation gap takes a significant portion of period, actual throughput may become unacceptable and period size should get increased at the expense of increased latency. Basically value of this setting must be carefully chosen to maximize throughput but also to keep latency at acceptable levels.
* **Nv2-mode** - Specifies to use dynamic or fixed downlink/uplink ratio. Default value is "dynamic-downlink".

"sync-master" - works as nv2-mode=fixed-downlink (so uses nv2-downlink-ratio), but allows slaves to sync to this master; "sync-slave" - tries to sync to the master (or already synced slave) and adapt period-size and downlink ratio settings from the master.

* **Nv2-downlink-ratio** - specifies the Nv2 downlink ratio. Uplink ratio is automatically calculated from the downlink-ratio value. When using dynamic-downlink mode the downlink-ratio is also used when link gets fully saturated. Minimum value is 20 and maximum 80. Default value is 50.

The following settings are significant on both - Nv2 AP and Nv2 client:

* **Nv2-security** - specifies Nv2 security mode, for more details see [Security in Nv2 network](#security-in-nv2-network).
* **Nv2-preshared-key** - specifies a preshared key to be used, for more details see [Security in Nv2 network](#security-in-nv2-network).
* **nv2-sync-secret** - specifies a secret key for use in the Nv2 synchronization. The secret should match on Master and Slave devices in order to establish the synced state.

## Migrating to Nv2

Using **wireless-protocol** setting makes migration or evaluation of Nv2 protocol in existing networks really simple and reduces downtime as much as possible. These are the recommended steps:

* Upgrade AP to a version that supports Nv2, but do not enable Nv2 on AP yet.
* Upgrade clients to a version that supports Nv2.
* Configure all clients with **wireless-protocol=Nv2-nstreme-802.11**. Clients will still connect to AP using the protocol that was used previously, because AP is not changed over to Nv2 yet.
* Configure Nv2 related settings on AP.
* If it is necessary to use data encryption and secure authentication, configure Nv2 security related settings on AP and clients (refer to [Security in Nv2 network](#security-in-nv2-network)).
* Set **wireless-protocol=Nv2** on AP. This will make the AP change to Nv2 protocol. Clients should now connect using Nv2 protocol.
* In case of some trouble you can easily switch back to previous protocol by simply changing it back to whatever was used before on the AP.
* Fine tune Nv2 related settings to get acceptable latency and throughput.
* Implement a QoS policy for maximum performance.

The basic troubleshooting guide:

* Clients have trouble connecting or disconnect with "ranging timeout" error - check that **Nv2-cell-radius** setting is set appropriately.
* Unexpectedly low throughput on long distance links although signal and rate are fine - try to increase **tdma-period-size** setting.

## Nv2 AP Synchronization

This feature will let multiple MikroTik Nv2 APs on the same location coexist in a better fashion by reducing the interference between each other. This feature will synchronize the transmit/receive time windows of APs on the same frequency, so that all synced MikroTik Nv2 APs transmit/receive at the same time. That allows reusing the same wireless frequency on the location for multiple APs giving more flexibility in frequency planning.

To make Nv2 synced setup:

* For Nv2 Synchronization a Master Nv2 AP should be chosen and "nv2-mode=sync-master" should be specified together with "nv2-sync-secret".
* For Nv2 Slave APs the same wireless frequency as Master AP should be used and "nv2-mode=sync-slave" should be specified with the same "nv2-sync-secret" as in the Master AP configuration.
* When Master AP is enabled Slave APs will try to start searching for Master AP by matching it against specified "nv2-sync-secret".
* After Master AP is found the Slave AP will calculate the distance to the Master AP as it is possible that Master AP is located not at the same location.
* Then Slave AP starts operating as an AP and it adapts the period size and downlink ratio from the synced Master AP.
* In addition after the Slave AP is operational other Slave APs can use this Slave AP to sync with.
* Slave AP periodically listens for the Master AP and checks if the "nv2-sync-secret" still matches and adapts the parameters again. If Master AP interface is disabled/enabled all the Slaves will also be disabled and will start the synchronization process from the beginning.
* If Master AP stops working Slave APs will also stop working as they do not have sync information.

### Configuration example

Master AP:

```
 /interface/wireless/set wlan1 mode=ap-bridge ssid=Sector1 frequency=5220 nv2-mode=sync-master nv2-preshared-key=clients1 nv2-sync-secret=Tower1
```

Slave AP:

```
 /interface/wireless/set wlan1 mode=ap-bridge ssid=Sector2 frequency=5220 nv2-mode=sync-slave nv2-preshared-key=clients2 nv2-sync-secret=Tower1
```

Monitor interface on the Slave AP:

```
[admin@SlaveAP] /interface/wireless> monitor wlan1
                   status: running-ap
                  channel: 5220/20/an
        wireless-protocol: nv2
              noise-floor: -110dBm
       registered-clients: 1
    authenticated-clients: 1
           nv2-sync-state: synced
          nv2-sync-master: 4C:5E:0C:57:84:38
        nv2-sync-distance: 1
     nv2-sync-period-size: 2
  nv2-sync-downlink-ratio: 50
```

Debug logs on the Master AP:

```
 09:22:08 wireless,debug wlan1: 4C:5E:0C:57:85:BE attempts to sync
```

Debug logs on the Slave AP:

```
09:22:08 wireless,debug wlan1: attempting to sync to 4C:5E:0C:57:84:38 
09:22:09 wireless,debug wlan1: synced to 4C:5E:0C:57:84:38 
```

## QoS in Nv2 network

QoS in Nv2 is implemented by means of a variable number of priority queues. A queue is considered for transmission based on the rule recommended by 802.1D-2004 - only if all higher priority queues are empty. In practice this means that at first all frames from the queue with higher priority will be sent, and only then the next queue is considered. Therefore QoS policy must be designed with care so that higher priority queues do not make lower priority queues starve.

QoS policy in an Nv2 network is controlled by the AP, clients adapt the policy from the AP. On the AP QoS policy is configured with **Nv2-queue-count** and **Nv2-qos** parameters. **Nv2-queue-count** parameter specifies the number of priority queues used. Mapping of frames to queues is controlled by the **Nv2-qos** parameter.

### Nv2-qos=default

In this mode the outgoing frame is first inspected by the built-in QoS policy algorithm that selects the queue based on packet type and size. If built-in rules do not match, the queue is selected based on the frame priority field, as in **Nv2-qos=frame-priority** mode.

### Nv2-qos=frame-priority

In this mode the QoS queue is selected based on the frame priority field. Note that the frame priority field is not some field in headers and therefore it is valid only while the packet is processed by the given device. The frame priority field must be set either explicitly by firewall rules or implicitly from the ingress priority by the frame forwarding process, for example, from MPLS EXP bits. For more information on the frame priority field see:

* [EXP bit and MPLS Queuing](../../user-guides/routing-and-networking-protocols/mpls/exp-bit-and-mpls-queuing.md)
* [WMM and VLAN priority](../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)

Queue is selected based on frame priority according to 802.1D recommended user priority to traffic class mapping. Mapping depends on the number of available queues (**Nv2-queue-count** parameter). For example, if the number of queues is 4, mapping is as follows (pay attention to how this mapping resembles mapping used by WMM):

* Priority 0,3 -> queue 0.
* Priority 1,2 -> queue 1.
* Priority 4,5 -> queue 2.
* Priority 6,7 -> queue 3.

If the number of queues is 2 (default), mapping is as follows:

* priority 0,1,2,3 -> queue 0.
* priority 4,5,6,7 -> queue 1.

If the number of queues is 8 (maximum possible), mapping is as follows:

* Priority 1 -> queue 0.
* Priority 2 -> queue 1.
* Priority 0 -> queue 2.
* Priority 3 -> queue 3.
* Priority 4 -> queue 4.
* Priority 5 -> queue 5.
* Priority 6 -> queue 6.
* Priority 7 -> queue 7.

For other mappings, discussion on the rationale for these mappings and recommended practices please see 802.1D-2004.

## Security in Nv2 network

Nv2 security implementation has the following features:

* Hardware accelerated data encryption using AES-CCM with 128 bit keys.
* 4-way handshake for key management (similar to that of 802.11i).
* Preshared key authentication method (similar to that of 802.11i).
* Periodically updated group keys (used for broadcast and multicast data).

Being a proprietary protocol, Nv2 does not use security mechanisms of 802.11, therefore security configuration is different. An interface using Nv2 protocol ignores **security-profile** setting. Instead, security is configured by the following interface settings:

* **Nv2-security** - this setting enables/disables use of security in the Nv2 network. Note that when security is enabled on the AP, it will not accept clients with disabled security. In the same way clients with enabled security will not connect to unsecure APs.
* **Nv2-preshared-key** - preshared key to use for authentication. Data encryption keys are derived from the preshared key during the 4-way handshake. The preshared key must be the same in order for 2 devices to establish a connection. If the preshared key differs, the connection will time out because the remote party will not be able to correctly interpret key exchange messages.
