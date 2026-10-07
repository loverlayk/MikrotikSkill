# IPsec

> This section covers IPsec examples and integrations. Use it to configure IKEv2, pre-shared-key and post-quantum key workflows, and third-party VPN connectivity.

# IPsec

This section covers IPsec examples and integrations. Use it to configure IKEv2, pre-shared-key and post-quantum key workflows, and third-party VPN connectivity.

**Internet Protocol Security (IPsec)** is a set of protocols defined by the Internet Engineering Task Force (IETF) to secure packet exchange over unprotected IP/IPv6 networks such as the Internet.

The IPsec protocol suite can be divided into the following groups:

- **Internet Key Exchange (IKE)** protocols that dynamically generate and distribute cryptographic keys for AH and ESP.
- **Authentication Header (AH)** RFC 4302.
- **Encapsulating Security Payload (ESP)** RFC 4303.

## Internet Key Exchange Protocol (IKE)

The Internet Key Exchange (IKE) is a protocol that provides authenticated keying material for the Internet Security Association and Key Management Protocol (ISAKMP) framework. Other key exchange schemes work with ISAKMP, but IKE is the most widely used one. Together, they provide means for authentication of hosts and automatic management of security associations (SAs).

The IKE daemon remains idle in most situations. It is activated in two cases:

Traffic matched by a policy rule needs to be encrypted or authenticated, but the policy does not have any SAs. The policy notifies the IKE daemon about that, and the IKE daemon initiates a connection to a remote host. The IKE daemon can also respond to a remote connection. In both cases, peers establish a connection and execute 2 phases:

- **Phase 1** - The peers agree upon the algorithms they use in subsequent IKE messages and authenticate each other. The keying material used to derive keys for all SAs and to protect subsequent ISAKMP exchanges between hosts is also generated. This phase should match the following settings:
  - Authentication method
  - DH group
  - Encryption algorithm
  - Exchange mode
  - Hash algorithm
  - NAT-T
  - DPD and lifetime (optional)

- **Phase 2** - The peers establish one or more SAs that are used by IPsec to encrypt data. All SAs established by the IKE daemon have lifetime values (either limiting the time after which the SA becomes invalid, the amount of data that can be encrypted by this SA, or both). This phase should match the following settings:
  - IPsec protocol
  - Mode (tunnel or transport)
  - Authentication method
  - PFS (DH) group
  - lifetime

:::warning
Two lifetime values exist - soft and hard. When an SA reaches its soft lifetime threshold, the IKE daemon is notified and initiates another phase 2 exchange to replace this SA with a fresh one. If an SA reaches a hard lifetime, it is discarded.

**Caution:** Phase 1 is not re-keyed if DPD is disabled when the lifetime expires; only Phase 2 is re-keyed. To force Phase 1 to re-key, enable DPD.

**Caution:** PSK authentication was known to be vulnerable to offline attacks in "aggressive" mode, however recent discoveries indicate that offline attacks are also possible in "main" and "ike2" exchange modes. You should avoid the PSK authentication method.
:::

IKE optionally provides Perfect Forward Secrecy (PFS), which is a property of key exchanges that, in turn, means for IKE that compromising the long-term Phase 1 key does not allow one to easily gain access to all IPsec data protected by SAs established through this Phase 1. This means that additional keying material is generated for each Phase 2.

The generation of keying material is computationally very expensive. For example, modp8192 group exchanges can take several seconds even on a very fast computer. It usually takes place once per Phase 1 exchange, which happens only once between any host pair and is then kept for a long time. PFS adds this expensive operation to each Phase 2 exchange as well.

### Diffie-Hellman Groups

The Diffie-Hellman (DH) key exchange protocol allows two parties without any initially shared secret to securely establish one. The following Modular Exponential (MODP) and ECP Diffie-Hellman (also known as "Oakley") groups are supported:

| Diffie-Hellman Group | Name | Reference |
| :-- | :-- | :-- |
| Group 1 | 768-bit MODP group | RFC 2409 |
| Group 2 | 1024-bit MODP group | RFC 2409 |
| Group 5 | 1536-bit MODP group | RFC 3526 |
| Group 14 | 2048-bit MODP group | RFC 3526 |
| Group 15 | 3072-bit MODP group | RFC 3526 |
| Group 16 | 4096-bit MODP group | RFC 3526 |
| Group 17 | 6144-bit MODP group | RFC 3526 |
| Group 18 | 8192-bit MODP group | RFC 3526 |
| Group 19 | 256-bit random ECP group | RFC 5903 |
| Group 20 | 384-bit random ECP group | RFC 5903 |
| Group 21 | 521-bit random ECP group | RFC 5903 |

More information about standards can be found [here](https://www.iana.org/assignments/ipsec-registry/ipsec-registry.xhtml).

Larger DH groups provide stronger security but require more CPU resources. Below are several common DH groups with different security levels and CPU impact:

DH Group 14 (2048-bit) - Provides a practical balance between security and CPU usage. It offers 2048-bit key exchange, which is considered secure for most modern applications and is widely supported.

DH Group 5 (1536-bit) - Provides a slightly lower level of security than DH Group 14 but has lower CPU overhead due to the smaller key size. It is still considered acceptable for many scenarios.

DH Group 2 (1024-bit) - Should be used with caution because it provides the lowest security among commonly used groups. Although it has lower CPU requirements, it is more susceptible to attacks as computational power increases. Do not use it for new deployments.

For optimal security, you should use **DH Group 19**. It is generally considered both fast and secure. DH Group 2 should typically be avoided unless required for compatibility with legacy devices.

:::info
To calculate the appropriate security level for your network infrastructure, first determine the number of security bits required and estimate how long it should take to decrypt protected data. Based on those requirements, choose the appropriate algorithms. For reference, see [https://www.keylength.com/en/4/](https://www.keylength.com/en/4/).
:::

### IKE Traffic

To avoid problems with IKE packets that hit some SPD rule and require encryption with a not established SA (that this packet perhaps is trying to establish), locally originated packets with UDP source port 500 are not processed with SPD. In the same way packets with UDP destination port 500 that are to be delivered locally are not processed in incoming policy checks.

### Setup Procedure

To get IPsec to work with automatic keying using IKE-ISAKMP you must configure policy, peer, and proposal (optional) entries.

:::danger
IPsec is very sensitive to time changes. If both ends of the IPsec tunnel are not synchronizing time equally (for example, different NTP servers not updating time with the same timestamp), tunnels break and must be re-established.
:::

### EAP Authentication methods

| Outer Auth | Inner Auth |
| :-- | :-- |
| EAP-GTC |  |
| EAP-MD5 |  |
| EAP-MSCHAPv2 |  |
| EAP-PEAPv0 | EAP-MSCHAPv2 EAP-GPSK EAP-GTC EAP-MD5 EAP-TLS |
| EAP-SIM |  |
| EAP-TLS |  |
| EAP-TTLS | PAP  CHAP  MS-CHAP  MS-CHAPv2  EAP-MSCHAPv2 EAP-GTC EAP-MD5 EAP-TLS |

**EAP-TLS** on Windows is called "Smart Card or other certificates".

:::info
AES-GCM encryption support for IKEv2 authentication is not supported.

**Important:** If using IPsec with certificate X.509, the certificate must contain "SubjectKeyIdentifier" extension, which is supported only in version 3.

**Important:** Using ed25519 authentication is not supported.
:::

## Authentication Header (AH)

AH is a protocol that provides authentication of either all or part of the contents of a datagram through the addition of a header that is calculated based on the values in the datagram. What parts of the datagram are used for the calculation, and the placement of the header depend on whether tunnel or transport mode is used.

The presence of the AH header allows verifying the integrity of the message but doesn't encrypt it. Thus, AH provides authentication but not privacy. Another protocol (ESP) is considered superior; it provides data privacy and also its own authentication method.

RouterOS supports the following authentication algorithms for AH:

- SHA2 (256, 512)
- SHA1
- MD5

### Transport mode

In transport mode, the AH header is inserted after the IP header. IP data and header are used to calculate the authentication value. IP fields that might change during transit, like TTL and hop count, are set to zero values before authentication.

### Tunnel mode

In tunnel mode, the original IP packet is encapsulated within a new IP packet. All of the original IP packets are authenticated.

## Encapsulating Security Payload (ESP)

Encapsulating Security Payload (ESP) uses shared key encryption to provide data privacy. ESP also supports its own authentication scheme like that used in AH.

ESP packages its fields in a very different way than AH. Instead of having just a header, it divides its fields into three components:

- **ESP Header** - Comes before the encrypted data and its placement depends on whether ESP is used in transport mode or tunnel mode.
- **ESP Trailer** - This section is placed after the encrypted data. It contains padding that is used to align the encrypted data.
- **ESP Authentication Data** - This field contains an Integrity Check Value (ICV), computed in a manner similar to how the AH protocol works, for when ESP's optional authentication feature is used.

### Transport mode

In transport mode, the ESP header is inserted after the original IP header. The ESP trailer and authentication value are added to the end of the packet. In this mode only the IP payload is encrypted and authenticated; the IP header is not secured.

![](./img/ipsec-01.webp)

### Tunnel mode

In tunnel mode, an original IP packet is encapsulated within a new IP packet thus securing the IP payload and the IP header.

![](./img/ipsec-02.webp)

### Encryption algorithms

RouterOS ESP supports various encryption and authentication algorithms.

#### Authentication

- **MD5**
- **SHA1**
- **SHA2 (256-bit, 512-bit)**

#### Encryption

- **AES** - 128-bit, 192-bit, and 256-bit key AES-CBC, AES-CTR, and AES-GCM algorithms.
- **Blowfish** - added since v4.5.
- **Twofish** - added since v4.5.
- **Camellia** - 128-bit, 192-bit, and 256-bit key Camellia encryption algorithm added since v4.5.
- **DES** - 56-bit DES-CBC encryption algorithm.
- **3DES** - 168-bit (3 x 56-bit) DES encryption algorithm.

### Hardware acceleration

Hardware acceleration enables faster encryption with a built-in encryption engine inside the CPU.

A list of devices with hardware acceleration is available [here](https://mikrotik.com/products?filter&s=c&f=%5B%22ipsec%22%5D)

<WideTable>

| CPU | DES and 3DES |  |  |  | AES-CBC |  |  |  | AES-CTR |  |  |  | AES-GCM |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 | MD5 | SHA1 | SHA256 | SHA512 |
| 88F7040 | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| AL21400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL32400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL52400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| AL73400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes |
| IPQ-4018 / IPQ-4019 | no | yes | yes | no | no | yes\* | yes\* | no | no | yes\* | yes\* | no | no | no | no | no |
| IPQ-5018 | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| IPQ-6010 | no | no | no | no | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| IPQ-8064 | no | yes | yes | no | no | yes\* | yes\* | no | no | yes\* | yes\* | no | no | no | no | no |
| IPQ-8072 | no | no | no | no | no | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes |
| MT7621A | yes\*\*\*\* | yes\*\*\*\* | yes\*\*\*\* | no | yes | yes | yes | no | no | no | no | no | no | no | no | no |
| EN7562CT | yes\*\*\*\* | yes\*\*\*\* | yes\*\*\*\* | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| P1023NSN5CFB | no | no | no | no | yes\*\* | yes\*\* | yes\*\* | yes\*\* | no | no | no | no | no | no | no | no |
| P202ASSE2KFB | yes | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | no | no | no |
| PPC460GT | no | no | no | no | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | no | no | no | no |
| TLR4 (TILE) | yes | yes | yes | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no |
| x86 (AES-NI) | no | no | no | no | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* | yes\*\*\* |

</WideTable>

\* supported only for 128 bit and 256 bit key sizes

\*\* Only manufactured since 2016, serial numbers that begin with numbers 5 and 7

\*\*\* AES-CBC and AES-CTR encryption only is accelerated, hashing done in software

\*\*\*\* DES is not supported, only 3DES and/or AES-CBC

IPsec throughput results of various encryption and hash algorithm combinations are published on the [MikroTik products page](https://mikrotik.com/products).

### RoadWarrior client with NAT

Consider the setup as illustrated below. RouterOS acts as a RoadWarrior client connected to Office allowing access to its internal resources.

![](./img/ipsec-03.webp)

A tunnel is established, a local mode-config IP address is received and a set of dynamic policies is generated.

```ros
[admin@mikrotik] > ip ipsec policy print 
Flags: T - template, X - disabled, D - dynamic, I - invalid, A - active, * - default 
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all proposal=default template=yes 

1 DA src-address=192.168.77.254/32 src-port=any dst-address=10.5.8.0/24 dst-port=any protocol=all 
action=encrypt level=unique ipsec-protocols=esp tunnel=yes sa-src-address=10.155.107.8 
sa-dst-address=10.155.107.9 proposal=default ph2-count=1 

2 DA src-address=192.168.77.254/32 src-port=any dst-address=192.168.55.0/24 dst-port=any protocol=all 
action=encrypt level=unique ipsec-protocols=esp tunnel=yes sa-src-address=10.155.107.8 
sa-dst-address=10.155.107.9 proposal=default ph2-count=1 
```

Only packets with a source address of 192.168.77.254/32 match the IPsec policies. For a local network to reach remote subnets, you must change the source address of local hosts to the dynamically assigned mode config IP address. Source NAT rules can be generated dynamically. Create a new address list that contains all local networks to which the NAT rule should apply. In this case, it is 192.168.88.0/24.

```ros
/ip/firewall/address-list/add address=192.168.88.0/24 list=local-RW
```

Specifying the address list under the mode-config initiator configuration dynamically generates source NAT rules.

```ros
/ip/ipsec/mode-config/set [ find name="request-only" ] src-address-list=local-RW
```

When the IPsec tunnel is established, the dynamically created source NAT rules appear for each network. Every host in 192.168.88.0/24 can now access Office's internal resources.

```ros
[admin@mikrotik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=192.168.55.0/24 src-address-list=local-RW

1 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 dst-address=10.5.8.0/24 src-address-list=local-RW
```

### Allow only IPsec encapsulated traffic

In some scenarios, for security reasons you want to drop access from/to specific networks if incoming/outgoing packets are not encrypted. For example, if you have an L2TP/IPsec setup you want to drop nonencrypted L2TP connection attempts.

You can achieve this in several ways:

- With an IPsec policy matcher in firewall.
- With a generic IPsec policy with action set to **drop** and lower priority (can be used in Road Warrior setups where dynamic policies are generated).
- By setting DSCP or priority in mangle and matching the same values in firewall after decapsulation.

#### IPsec policy matcher

Let's set up an IPsec policy matcher to accept all packets that match any of the IPsec policies and drop the rest:

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec
add action=drop chain=input comment="drop all" in-interface=WAN log=yes
```

IPsec policy matcher takes two parameters **direction, policy**. This example uses incoming direction and IPsec policy. The IPsec policy option allows you to inspect packets after decapsulation, so for example, to allow only GRE encapsulated packets from a specific source address and drop the rest:

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec protocol=gre src-address=192.168.33.1
add action=drop chain=input comment="drop all" in-interface=WAN log=yes
```

For L2TP, the rule set would be:

```ros
add chain=input comment="ipsec policy matcher" in-interface=WAN ipsec-policy=in,ipsec protocol=udp dst-port=1701
add action=drop chain=input protocol=udp dst-port=1701 comment="drop l2tp" in-interface=WAN log=yes
```

#### Using generic IPsec policy

This method works by adding a default policy with an action drop. This example assumes an L2TP/IPsec server on a public 1.1.1.1 address, dropping all non-encrypted L2TP:

```ros
/ip/ipsec/policy
add src-address=1.1.1.1 dst-address=0.0.0.0/0 sa-src-address=1.1.1.1 protocol=udp src-port=1701 tunnel=yes action=discard
```

The router drops any L2TP unencrypted incoming traffic, but after a successful L2TP/IPsec connection, a dynamic policy is created with higher priority than the default static rule, and packets matching that dynamic rule can be forwarded.

:::warning
Policy order is important! For this to work, ensure the static drop policy is below the dynamic policies. Move it below the policy template if necessary.
:::

```ros
[admin@rack2_10g1] /ip/ipsec/policy> print
Flags: T - template, X - disabled, D - dynamic, I - inactive, * - default
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all
proposal=default template=yes

1 D src-address=1.1.1.1/32 src-port=1701 dst-address=10.5.130.71/32
dst-port=any protocol=udp action=encrypt level=require
ipsec-protocols=esp tunnel=no sa-src-address=1.1.1.1
sa-dst-address=10.5.130.71

2 src-address=1.1.1.1/32 src-port=1701 dst-address=0.0.0.0/0
dst-port=any protocol=udp action=discard level=unique
ipsec-protocols=esp tunnel=yes sa-src-address=1.1.1.1
sa-dst-address=0.0.0.0 proposal=default manual-sa=none
```

### Manually specifying local-address parameter under Peer configuration

#### Using different routing table

IPsec, as any other service in RouterOS, uses the main routing table regardless of what local-address parameter is used for Peer configuration. You must apply routing marks to both IKE and IPSec traffic.

Consider the following example. Two default routes exist - one in the main routing table and another in the routing table "backup". You must use the backup link for the IPsec site-to-site tunnel.

```ros
[admin@pair_r1] > /ip/route/print detail 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
0 A S dst-address=0.0.0.0/0 gateway=10.155.107.1 gateway-status=10.155.107.1 reachable via ether1 distance=1 scope=30 target-scope=10 routing-mark=backup 

1 A S dst-address=0.0.0.0/0 gateway=172.22.2.115 gateway-status=172.22.2.115 reachable via ether2 distance=1 scope=30 target-scope=10 

2 ADC dst-address=10.155.107.0/25 pref-src=10.155.107.8 gateway=ether1 gateway-status=ether1 reachable distance=0 scope=10 

3 ADC dst-address=172.22.2.0/24 pref-src=172.22.2.114 gateway=ether2 gateway-status=ether2 reachable distance=0 scope=10 

4 ADC dst-address=192.168.1.0/24 pref-src=192.168.1.1 gateway=bridge-local gateway-status=ether2 reachable distance=0 scope=10 

[admin@pair_r1] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 

1 chain=srcnat action=masquerade out-interface=ether2 log=no log-prefix="" 
```

IPsec peer and policy configurations, as well as the NAT bypass rule for IPsec tunnel traffic, are created using the backup link's source address.

```ros
/ip/ipsec/peer
add address=10.155.130.136/32 local-address=10.155.107.8 secret=test
/ip/ipsec/policy
add sa-src-address=10.155.107.8 src-address=192.168.1.0/24 dst-address=172.16.0.0/24 sa-dst-address=10.155.130.136 tunnel=yes
/ip/firewall/nat
add action=accept chain=srcnat src-address=192.168.1.0/24 dst-address=172.16.0.0/24 place-before=0
```

The log shows "phase1 negotiation failed due to time up" errors. This is because IPsec tries to reach the remote peer using the main routing table with an incorrect source address. You must mark UDP/500, UDP/4500, and ipsec-esp packets with Mangle:

```ros
/ip/firewall/mangle
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 dst-port=500,4500 new-connection-mark=ipsec passthrough=yes protocol=udp
add action=mark-connection chain=output connection-mark=no-mark dst-address=10.155.130.136 new-connection-mark=ipsec passthrough=yes protocol=ipsec-esp
add action=mark-routing chain=output connection-mark=ipsec new-routing-mark=backup passthrough=no
```

#### Using the same routing table with multiple IP addresses

Consider the following example. Multiple IP addresses from the same subnet exist on the public interface. Masquerade rule is configured on out-interface. You must use one of the IP addresses explicitly.

```ros
[admin@pair_r1] > /ip/address/print 
Flags: X - disabled, I - invalid, D - dynamic 
# ADDRESS NETWORK INTERFACE
0 192.168.1.1/24 192.168.1.0 bridge-local
1 172.22.2.1/24 172.22.2.0 ether1
2 172.22.2.2/24 172.22.2.0 ether1
3 172.22.2.3/24 172.22.2.0 ether1

[admin@pair_r1] > /ip/route/print 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
# DST-ADDRESS PREF-SRC GATEWAY DISTANCE
1 A S 0.0.0.0/0 172.22.2.115 1
3 ADC 172.22.2.0/24 172.22.2.1 ether1 0
4 ADC 192.168.1.0/24 192.168.1.1 bridge-local 0

[admin@pair_r1] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 
```

IPsec peer and policy configurations are created using one of the public IP addresses.

```ros
/ip/ipsec/peer
add address=10.155.130.136/32 local-address=172.22.2.3 secret=test
/ip/ipsec/policy
add sa-src-address=172.22.2.3 src-address=192.168.1.0/24 dst-address=172.16.0.0/24 sa-dst-address=10.155.130.136 tunnel=yes
/ip/firewall/nat
add action=accept chain=srcnat src-address=192.168.1.0/24 dst-address=172.16.0.0/24 place-before=0
```

The phase 1 connection uses a different source address than specified, and "phase1 negotiation failed due to time up" errors are shown in the logs. This is because masquerade is changing the source address of the connection to match the pref-src address of the connected route. Exclude connections from the public IP address from being masqueraded.

```ros
/ip/firewall/nat
add action=accept chain=srcnat protocol=udp src-port=500,4500 place-before=0
```

## Application examples

### Site to Site IPsec (IKEv1) tunnel

Consider the setup as illustrated below. Two remote office routers are connected to the internet and office workstations are behind NAT. Each office has its own local subnet, 10.1.202.0/24 for Office1 and 10.1.101.0/24 for Office2. Both remote offices need secure tunnels to local networks behind the routers.

![](./img/ipsec-04.webp)

#### **Site 1 configuration**

Start off by creating a new Phase 1 profile and Phase 2 proposal entries using stronger or weaker encryption parameters that suit your needs. You should create separate entries for each menu so that they are unique for each peer in case you need to adjust any settings later. These parameters must match between the sites or the connection does not establish.

```ros
/ip/ipsec/profile
add dh-group=modp2048 enc-algorithm=aes-128 name=ike1-site2
/ip/ipsec/proposal
add enc-algorithms=aes-128-cbc name=ike1-site2 pfs-group=modp2048
```

Continue by configuring a peer. Specify the address of the remote router. This address should be reachable through UDP/500 and UDP/4500 ports, so ensure appropriate actions are taken regarding the router's firewall. Specify the name for this peer as well as the newly created profile.

```ros
/ip/ipsec/peer
add address=192.168.80.1/32 name=ike1-site2 profile=ike1-site2
```

The next step is to create an identity. For a basic pre-shared key secured tunnel, you only need to set a **strong** secret and the peer to which this identity applies.

```ros
/ip/ipsec/identity
add peer=ike1-site2 secret=thisisnotasecurepsk
```

:::danger
If security matters, consider using IKEv2 and a different auth-method.
:::

Lastly, create a policy that controls the networks/hosts between which traffic should be encrypted.

```ros
/ip/ipsec/policy
add src-address=10.1.202.0/24 src-port=any dst-address=10.1.101.0/24 dst-port=any tunnel=yes action=encrypt proposal=ike1-site2 peer=ike1-site2
```

#### **Site 2 configuration**

Office 2 configuration is almost identical to Office 1 with proper IP address configuration. Start off by creating a new Phase 1 profile and Phase 2 proposal entries:

```ros
/ip/ipsec/profile
add dh-group=modp2048 enc-algorithm=aes-128 name=ike1-site1
/ip/ipsec/proposal
add enc-algorithms=aes-128-cbc name=ike1-site1 pfs-group=modp2048
```

Next is the peer and identity:

```ros
/ip/ipsec/peer
add address=192.168.90.1/32 name=ike1-site1 profile=ike1-site1
/ip/ipsec/identity
add peer=ike1-site1 secret=thisisnotasecurepsk
```

When it is done, create a policy:

```ros
/ip/ipsec/policy
add src-address=10.1.101.0/24 src-port=any dst-address=10.1.202.0/24 dst-port=any tunnel=yes action=encrypt proposal=ike1-site1 peer=ike1-site1
```

At this point, the tunnel should be established and two IPsec Security Associations should be created on both routers:

```ros
/ip/ipsec
active-peers print
installed-sa print
```

#### **NAT and Fasttrack Bypass**

At this point if you try to send traffic over the IPsec tunnel, it does not work; packets are lost. This is because both routers have NAT rules (masquerade) that are changing source addresses before a packet is encrypted. A router is unable to encrypt the packet because the source address does not match the address specified in the policy configuration. For more information see the IPsec packet flow example.

To fix this you need to set up an IP/Firewall/NAT bypass rule.

Office 1 router:

```ros
/ip/firewall/nat
add chain=srcnat action=accept place-before=0 src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

Office 2 router:

```ros
/ip/firewall/nat
add chain=srcnat action=accept place-before=0 src-address=10.1.101.0/24 dst-address=10.1.202.0/24
```

:::warning
If you previously tried to establish an IP connection before the NAT bypass rule was added, you have to clear the existing connection from the connection table or restart both routers.
:::

Ensure the bypass rule is placed at the top of all other NAT rules.

Another issue is if you have IP/Fasttrack enabled, the packet bypasses IPsec policies. So you need to add an accept rule before FastTrack.

```ros
/ip/firewall/filter
add chain=forward action=accept place-before=1
src-address=10.1.101.0/24 dst-address=10.1.202.0/24 connection-state=established,related
add chain=forward action=accept place-before=1
src-address=10.1.202.0/24 dst-address=10.1.101.0/24 connection-state=established,related
```

However, this can add a significant load to the router's CPU if there are a fair number of tunnels and significant traffic on each tunnel.

The solution is to use IP/Firewall/Raw to bypass connection tracking, thereby eliminating the need for filter rules listed above and reducing the load on CPU by approximately 30%.

```ros
/ip/firewall/raw
add action=notrack chain=prerouting src-address=10.1.101.0/24 dst-address=10.1.202.0/24
add action=notrack chain=prerouting src-address=10.1.202.0/24 dst-address=10.1.101.0/24
```

### Site to Site GRE tunnel over IPsec (IKEv2) using DNS

This example explains how to establish a secure and encrypted GRE tunnel between two RouterOS devices when one or both sites do not have a static IP address. Before this configuration is possible, you must have a DNS name assigned to one of the devices which acts as a responder (server). For simplicity, this example uses the RouterOS built-in DDNS service IP/Cloud.

![](./img/ipsec-05.webp)

#### Site 1 (server) configuration

This side listens for incoming connections and acts as a responder. Use mode config to provide an IP address for the second site. First, create a loopback (blank) bridge and assign an IP address to it that is used later for GRE tunnel establishment.

```ros
/interface/bridge 
add name=loopback
/ip/address
add address=192.168.99.1 interface=loopback
```

Continuing with the IPsec configuration, start off by creating a new Phase 1 profile and Phase 2 proposal entries using stronger or weaker encryption parameters that suit your needs. This configuration example listens for all incoming IKEv2 requests, meaning the profile configuration is shared between all other configurations (e.g. RoadWarrior).

```ros
/ip/ipsec/profile
add dh-group=ecp256,modp2048,modp1024 enc-algorithm=aes-256,aes-192,aes-128 name=ike2
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

Next, create a new mode config entry with responder=yes. This provides an IP configuration for the other site as well as the host (loopback address) for policy generation.

```ros
/ip/ipsec/mode-config
add address=192.168.99.2 address-prefix-length=32 name=ike2-gre split-include=192.168.99.1/32 system-dns=no
```

You should create a new policy group to separate this configuration from any existing or future IPsec configuration.

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

Now set up a new policy template that matches the remote peers' new dynamic address and the loopback address.

```ros
/ip/ipsec/policy
add dst-address=192.168.99.2/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.1/32 template=yes
```

The next step is to create a peer configuration that listens to all IKEv2 requests. If you already have such an entry, you can skip this step.

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

Lastly, set up an identity that matches the remote peer by pre-shared-key authentication with a specific secret.

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=ike2 policy-template-group=ike2-gre secret=test
```

The server side is now configured and listening to all IKEv2 requests. Ensure the firewall is not blocking the UDP/4500 port.

The last step is to create the GRE interface itself. This can also be done later when an IPsec connection is established from the client-side.

```ros
/interface/gre
add local-address=192.168.99.1 name=gre-tunnel1 remote-address=192.168.99.2
```

Configure IP address and route to remote network through GRE interface.

```ros
/ip/address
add address=172.16.1.1/30 interface=gre-tunnel1
/ip/route
add dst-address=10.1.202.0/24 gateway=172.16.1.2
```

#### Site 2 (client) configuration

Similarly to the server configuration, start off by creating a new Phase 1 profile and a Phase 2 proposal configuration. Since this site is the initiator, you can use a more specific profile configuration to control which exact encryption parameters are used, just ensure they overlap with what is configured on the server-side.

```ros
/ip/ipsec/profile
add dh-group=ecp256 enc-algorithm=aes-256 name=ike2-gre
/ip/ipsec/proposal
add auth-algorithms=null enc-algorithms=aes-128-gcm name=ike2-gre pfs-group=none
```

Next, create a new mode config entry with responder=no. This ensures the peer requests IP and split-network configuration from the server.

```ros
/ip/ipsec/mode-config
add name=ike2-gre responder=no
```

You should also create a new policy group to separate this configuration from any existing or future IPsec configuration.

```ros
/ip/ipsec/policy/group
add name=ike2-gre
```

Create a new policy template on the client-side as well.

```ros
/ip/ipsec/policy
add dst-address=192.168.99.1/32 group=ike2-gre proposal=ike2-gre src-address=192.168.99.2/32 template=yes
```

Move on to peer configuration. Specify the DNS name for the server under the address parameter. You can also use an IP address.

```ros
/ip/ipsec/peer
add address=n.mynetname.net exchange-mode=ike2 name=p1.ez profile=ike2-gre
```

Lastly, create an identity for the newly created peers.

```ros
/ip/ipsec/identity
add generate-policy=port-strict mode-config=ike2-gre peer=p1.ez policy-template-group=ike2-gre secret=test
```

If everything is configured properly, a new dynamic policy appears.

```ros
/ip/ipsec/policy/print 
Flags: T - template, X - disabled, D - dynamic, I - invalid, A - active, * - default 
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all proposal=default template=yes

1 T group=ike2-gre src-address=192.168.99.2/32 dst-address=192.168.99.1/32 protocol=all proposal=ike2-gre template=yes

2 DA src-address=192.168.99.2/32 src-port=any dst-address=192.168.99.1/32 dst-port=any protocol=all action=encrypt level=unique ipsec-protocols=esp 
tunnel=yes sa-src-address=192.168.90.1 sa-dst-address=(current IP of n.mynetname.net) proposal=ike2-gre ph2-count=1 
```

A secure tunnel is now established between both sites which encrypts all traffic between 192.168.99.2 \<=> 192.168.99.1 addresses. Use these addresses to create a GRE tunnel.

```ros
/interface/gre
add local-address=192.168.99.2 name=gre-tunnel1 remote-address=192.168.99.1
```

Configure an IP address and route to the remote network through the GRE interface.

```ros
/ip/address
add address=172.16.1.2/30 interface=gre-tunnel1
/ip/route
add dst-address=10.1.101.0/24 gateway=172.16.1.1
```

### Road Warrior setup using IKEv2 with RSA authentication

This example explains how to establish a secure IPsec connection between a device connected to the Internet (road warrior client) and a device running RouterOS acting as a server.

![](./img/ipsec-06.webp)

#### RouterOS server configuration

Before configuring IPsec, you must set up certificates. You can use a separate Certificate Authority for certificate management; however, in this example, self-signed certificates are generated in the RouterOS System/Certificates menu. Some certificate requirements must be met to connect various devices to the server:

- The common name must contain the IP or DNS name of the server.
- SAN (subject alternative name) must have the IP or DNS name of the server.
- EKU (extended key usage) tls-server and tls-client are required.

Considering the requirements above, generate CA and server certificates:

```ros
/certificate
add common-name=ca name=ca
sign ca ca-crl-host=2.2.2.2
add common-name=2.2.2.2 subject-alt-name=IP:2.2.2.2 key-usage=tls-server name=server1
sign server1 ca=ca
```

After valid certificates are created on the router, add a new Phase 1 profile and Phase 2 proposal entries with pfs-group=none:

```ros
/ip/ipsec/profile
add name=ike2
/ip/ipsec/proposal
add name=ike2 pfs-group=none
```

Mode config is used for address distribution from IP/Pools:

```ros
/ip/pool
add name=ike2-pool ranges=192.168.77.2-192.168.77.254
/ip/ipsec/mode-config
add address-pool=ike2-pool address-prefix-length=32 name=ike2-conf
```

Since the policy template must be adjusted to allow only specific network policies, you should create a separate policy group and template.

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

Create a new IPsec peer entry that listens to all incoming IKEv2 requests.

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

##### Identity configuration

The identity menu allows matching specific remote peers and assigning different configurations for each one. First, create a default identity that accepts all peers but verifies the peer's identity with its certificate.

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict mode-config=ike2-conf peer=ike2 policy-template-group=ike2-policies
```

:::warning
If the peer's ID (ID\_i) does not match the certificate it sends, the identity lookup fails. See remote-id in the identities section.
:::

For example, to assign a different mode config for user "A", who uses certificate "rw-client1" to authenticate to the server, first ensure a new mode config is created and ready for the specific user.

```ros
/ip/ipsec/mode-config
add address=192.168.66.2 address-prefix-length=32 name=usr_A split-include=192.168.55.0/24 system-dns=no
```

Apply this configuration for user "A" with match-by=certificate and specify the certificate with remote-certificate.

```ros
/ip/ipsec/identity
add auth-method=digital-signature certificate=server1 generate-policy=port-strict match-by=certificate mode-config=usr_A peer=ike2 policy-template-group=ike2-policies remote-certificate=rw-client1
```

##### (Optional) Split tunnel configuration

Split tunneling is a method that allows road warrior clients to only access a specific secured network and at the same time send the rest of the traffic based on their internal routing table (as opposed to sending all traffic over the tunnel). To configure split tunneling, change the mode config parameters.

For example, allow road warrior clients to only access the 10.5.8.0/24 network.

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

You can also send a specific DNS server for the client to use. By default, system-dns=yes is used, which sends DNS servers that are configured on the router itself in IP/DNS. Force the client to use a different DNS server with the static-dns parameter.

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] system-dns=no static-dns=10.5.8.1
```

While it is possible to adjust the IPsec policy template to only allow road warrior clients to generate policies to the network configured by the split-include parameter, this causes compatibility issues with different vendor implementations (see known limitations). Instead of adjusting the policy template, allow access to a secured network in the IP/Firewall/Filter and drop everything else.

```ros
/ip/firewall/filter
add action=drop chain=forward src-address=192.168.77.0/24 dst-address=!10.5.8.0/24
```

:::warning
Split networking is not a security measure. The client (initiator) can still request a different Phase 2 traffic selector.
:::

##### Generating client certificates

To generate a new certificate for the client and sign it with a previously created CA.

```ros
/certificate
add common-name=rw-client1 name=rw-client1 key-usage=tls-client
sign rw-client1 ca=ca
```

**PKCS12 format** is accepted by most client implementations, so when exporting the certificate, make sure PKCS12 is specified.

```ros
/certificate
export-certificate rw-client1 export-passphrase=1234567890 type=pkcs12
```

A file named *cert\_export\_rw-client1.p12* is now located in the router's System/File section. This file should be securely transported to the client's device.

A PKCS12 bundle also contains a CA certificate, but some vendors do not install this CA, so a self-signed CA certificate must be exported separately in PEM format.

```ros
/certificate
export-certificate ca type=pem
```

A file named *cert\_export\_ca.crt* is now located in the router's System/File section. This file should also be securely transported to the client's device.

**PEM** is another certificate format for use in client software that does not support PKCS12. The principle is pretty much the same.

```ros
/certificate
export-certificate ca
export-certificate rw-client1 export-passphrase=1234567890
```

Three files are now located in the router's Files section: *cert\_export\_ca.crt*, *cert\_export\_rw-client1.crt* and *cert\_export\_rw-client1.key* which should be securely transported to the client device.

##### Known limitations

Here is a list of known limitations by popular client software IKEv2 implementations.

- Windows always ignores networks received by split-include and requests policy with destination 0.0.0.0/0 (TSr). When IPsec-SA is generated, Windows requests DHCP option 249 to which RouterOS responds with configured split-include networks automatically.

- Both Apple macOS and iOS only accept the first split-include network.

- Both Apple macOS and iOS use the DNS servers from system-dns and static-dns parameters only when 0.0.0.0/0 split-include is used.

- While some implementations can make use of a different PFS group for phase 2, use pfs-group=none under proposals to avoid any compatibility issues.

#### RouterOS client configuration

Import a PKCS12 format certificate in RouterOS.

```ros
/certificate/import file-name=cert_export_RouterOS_client.p12 passphrase=1234567890
```

The self-signed CA certificate and the client certificate now appear in the Certificate menu. Find the name of the client certificate.

```ros
/certificate/print
```

**cert\_export\_RouterOS\_client.p12\_0** is the client certificate.

You should create a separate Phase 1 profile and Phase 2 proposal configurations to not interfere with any existing IPsec configuration.

```ros
/ip/ipsec/profile
add name=ike2-rw
/ip/ipsec/proposal
add name=ike2-rw pfs-group=none
```

While you can use the default policy template for policy generation, create a new policy group and template to separate this configuration from any other IPsec configuration.

```ros
/ip/ipsec/policy/group
add name=ike2-rw
/ip/ipsec/policy
add group=ike2-rw proposal=ike2-rw template=yes
```

Create a new mode config entry with responder=no that requests configuration parameters from the server.

```ros
/ip/ipsec/mode-config
add name=ike2-rw responder=no
```

Lastly, create peer and identity configurations.

```ros
/ip/ipsec/peer
add address=2.2.2.2/32 exchange-mode=ike2 name=ike2-rw-client
/ip/ipsec/identity
add auth-method=digital-signature certificate=cert_export_RouterOS_client.p12_0 generate-policy=port-strict mode-config=ike2-rw peer=ike2-rw-client policy-template-group=ike2-rw
```

Verify that the connection is successfully established.

```ros
/ip/ipsec
active-peers print
installed-sa print
```

##### Enabling dynamic source NAT rule generation

The generated dynamic policies show that only traffic with a specific (received by mode config) source address is sent through the tunnel. In most cases a router needs to route a specific device or network through the tunnel. In such a case, use source NAT to change the source address of packets to match the mode config address. Since the mode config address is dynamic, you cannot create a static source NAT rule. In RouterOS, you can generate dynamic source NAT rules for mode config clients.

![](./img/ipsec-07.webp)

For example, a local network 192.168.88.0/24 is behind the router and all traffic from this network should be sent over the tunnel. First, create a new IP/Firewall/Address list that consists of the local network.

```ros
/ip/firewall/address-list
add address=192.168.88.0/24 list=local
```

When it is done, assign the newly created IP/Firewall/Address list to the mode config configuration.

```ros
/ip/ipsec/mode-config
set [ find name=ike2-rw ] src-address-list=local
```

Verify the correct source NAT rule is dynamically generated when the tunnel is established.

```ros
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 D ;;; ipsec mode-config
chain=srcnat action=src-nat to-addresses=192.168.77.254 src-address-list=local dst-address-list=!local
```

:::danger
Ensure the dynamic mode config address is not a part of a local network.
:::

#### Windows client configuration

Open the PKCS12 format certificate file on the Windows computer. Install the certificate by following the instructions. Select the Local Machine store location.![](./img/ipsec-08.webp) You can now proceed to Network and Internet settings -> VPN and add a new configuration. Fill in the Connection name, Server name, or address parameters. Select IKEv2 under VPN type. When it is done, select "Use machine certificates". This can be done in Network and Sharing Center by clicking the Properties menu for the VPN connection. The setting is located under the Security tab.

![](./img/ipsec-09.webp)

Windows 10 is compatible with the following Phase 1 (profiles) and Phase 2 (proposals) proposal sets:

| Phase 1 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | DH Group |
| SHA1 | 3DES | modp1024 |
| SHA256 | 3DES | modp1024 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA256 | AES-128-CBC | modp1024 |
| SHA1 | AES-192-CBC | modp1024 |
| SHA256 | AES-192-CBC | modp1024 |
| SHA1 | AES-256-CBC | modp1024 |
| SHA256 | AES-256-CBC | modp1024 |
| SHA1 | AES-128-GCM | modp1024 |
| SHA256 | AES-128-GCM | modp1024 |
| SHA1 | AES-256-GCM | modp1024 |
| SHA256 | AES-256-GCM | modp1024 |

| Phase 2 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | PFS Group |
| SHA1 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |
| SHA1 | DES | none |
| SHA1 | none | none |

#### macOS client configuration

Open the PKCS12 format certificate file on the macOS computer and install the certificate in the "System" keychain. Mark the CA certificate as trusted manually since it is self-signed. Locate the certificate in the macOS Keychain Access app under the System tab and mark it as Always Trust.

![](./img/ipsec-10.webp)

You can now proceed to System Preferences -> Network and add a new configuration by clicking the + button. Select Interface: VPN, VPN Type: IKEv2 and name your connection. Remote ID must be set equal to the common-name or subjAltName of the server's certificate. Local ID can be left blank. Under Authentication Settings select None and choose the client certificate. You can now test the connectivity.

![](./img/ipsec-11.webp)

macOS is compatible with the following Phase 1 ( profiles) and Phase 2 ( proposals) proposal sets:

| Phase 1 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | DH Group |
| SHA256 | AES-256-CBC | modp2048 |
| SHA256 | AES-256-CBC | ecp256 |
| SHA256 | AES-256-CBC | modp1536 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA1 | 3DES | modp1024 |

| Phase 2 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | PFS Group |
| SHA256 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |

#### iOS client configuration

Typically, a PKCS12 bundle also contains a CA certificate, but iOS does not install this CA, so a self-signed CA certificate must be installed separately in PEM format. Open these files on the iOS device and install both certificates by following the instructions. Mark the self-signed CA certificate as trusted on the iOS device. This can be done in the Settings -> General -> About -> Certificate Trust Settings menu. When it is done, check whether both certificates are marked as "verified" under the Settings -> General -> Profiles menu.

![](./img/ipsec-12.webp)

You can now proceed to Settings -> General -> VPN menu and add a new configuration. Remote ID must be set equal to common-name or subjAltName of the server's certificate. Local ID can be left blank.

![](./img/ipsec-13.webp)

iOS is compatible with the following Phase 1 (profiles) and Phase 2 (proposals) proposal sets:

| Phase 1 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | DH Group |
| SHA256 | AES-256-CBC | modp2048 |
| SHA256 | AES-256-CBC | ecp256 |
| SHA256 | AES-256-CBC | modp1536 |
| SHA1 | AES-128-CBC | modp1024 |
| SHA1 | 3DES | modp1024 |

| Phase 2 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | PFS Group |
| SHA256 | AES-256-CBC | none |
| SHA1 | AES-128-CBC | none |
| SHA1 | 3DES | none |

:::warning
If you are connected to the VPN over WiFi, the iOS device can go into sleep mode and disconnect from the network.
:::

#### Android (strongSwan) client configuration

Android has no native IKEv2 support, but you can use strongSwan from the Google Play Store which brings IKEv2 to Android. StrongSwan accepts PKCS12 format certificates, so before setting up the VPN connection in strongSwan, download the PKCS12 bundle to your Android device. When it is done, create a new VPN profile in strongSwan, type in the server IP, and choose "IKEv2 Certificate" as VPN Type. When selecting a User certificate, press Install and follow the certificate extraction procedure by specifying the PKCS12 bundle. Save the profile and test the connection by pressing on the VPN profile.

![](./img/ipsec-14.webp)

You can specify custom encryption settings in strongSwan by ticking the "Show advanced settings" checkbox. StrongSwan by default is compatible with the following Phase 1 (profiles) and Phase 2 (proposals) proposal sets:

| Phase 1 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | DH Group |
| SHA\* | AES-\*-CBC | modp2048 |
| SHA\* | AES-\*-CBC | ecp256 |
| SHA\* | AES-\*-CBC | ecp384 |
| SHA\* | AES-\*-CBC | ecp521 |
| SHA\* | AES-\*-CBC | modp3072 |
| SHA\* | AES-\*-CBC | modp4096 |
| SHA\* | AES-\*-CBC | modp6144 |
| SHA\* | AES-\*-CBC | modp8192 |
| SHA\* | AES-\*-GCM | modp2048 |
| SHA\* | AES-\*-GCM | ecp256 |
| SHA\* | AES-\*-GCM | ecp384 |
| SHA\* | AES-\*-GCM | ecp521 |
| SHA\* | AES-\*-GCM | modp3072 |
| SHA\* | AES-\*-GCM | modp4096 |
| SHA\* | AES-\*-GCM | modp6144 |
| SHA\* | AES-\*-GCM | modp8192 |

| Phase 2 |  |  |
| :-- | :-- | :-- |
| Hash Algorithm | Encryption Algorithm | PFS Group |
| none | AES-256-GCM | none |
| none | AES-128-GCM | none |
| SHA256 | AES-256-CBC | none |
| SHA512 | AES-256-CBC | none |
| SHA1 | AES-256-CBC | none |
| SHA256 | AES-192-CBC | none |
| SHA512 | AES-192-CBC | none |
| SHA1 | AES-192-CBC | none |
| SHA256 | AES-128-CBC | none |
| SHA512 | AES-128-CBC | none |
| SHA1 | AES-128-CBC | none |

#### Linux (strongSwan) client configuration

Download the PKCS12 certificate bundle and move it to the `/etc/ipsec`.d/private directory.

Add the exported passphrase for the private key to the `/etc/ipsec`.secrets file where "strongSwan\_client.p12" is the file name and "1234567890" is the passphrase.

```bash
: P12 strongSwan_client.p12 "1234567890"
```

Add a new connection to the `/etc/ipsec`.conf file

```bash
conn "ikev2"
keyexchange=ikev2
ike=aes128-sha1-modp2048
esp=aes128-sha1
leftsourceip=%modeconfig
leftcert=strongSwan_client.p12
leftfirewall=yes
right=2.2.2.2
rightid="CN=2.2.2.2"
rightsubnet=0.0.0.0/0
auto=add
```

You can now restart (or start) the ipsec daemon and initialize the connection.

```bash
ipsec restart
ipsec up ikev2
```

### Road Warrior setup using IKEv2 with EAP-MSCHAPv2 authentication handled by User Manager (RouterOS v7)

This example explains how to establish a secure IPsec connection between a device connected to the Internet (road warrior client) and a device running RouterOS acting as an IKEv2 server and User Manager. You can run User Manager on a separate device in the network, however in this example both User Manager and IKEv2 server are configured on the same device (Office).

![](./img/ipsec-06.webp)

#### RouterOS server configuration

##### Requirements

For this setup to work, the following prerequisites must be met:

1. The router's IP address must have a valid public DNS record - IP Cloud can provide this.
2. The router must be reachable through port TCP/80 over the Internet - if the server is behind NAT, configure port forwarding.
3. The User Manager package must be installed on the router.

##### Generating Let's Encrypt certificate

EAP-MSCHAPv2 authentication requires a TLS handshake, so the server must have a certificate the client can validate. To simplify this step, use a Let's Encrypt certificate which most operating systems can validate without user intervention. To generate the certificate, enable an SSL certificate under the Certificates menu. By default the command uses the dynamic DNS record provided by IP Cloud, however a custom DNS name can also be specified. The DNS record should point to the router.

```ros
/certificate/enable-ssl-certificate
```

If the certificate generation succeeded, the Let's Encrypt certificate appears installed under the Certificates menu.

```ros
/certificate/print detail where name~"letsencrypt"
```

##### Configuring User Manager

First, allow RADIUS requests from the localhost (the router itself):

```ros
/user-manager/router
add address=127.0.0.1 comment=localhost name=local shared-secret=test
```

Enable the User Manager and specify the Let's Encrypt certificate (replace the name of the certificate with the one installed on your device) that is used to authenticate the users.

```ros
/user-manager
set certificate="letsencrypt_2021-04-09T07:10:55Z" enabled=yes
```

Lastly add users and their credentials that clients use to authenticate to the server.

```ros
/user-manager/user
add name=user1 password=password
```

##### Configuring RADIUS client

For the router to use a RADIUS server for user authentication, you must add a new RADIUS client that has the same shared secret already configured on User Manager.

```ros
/radius
add address=127.0.0.1 secret=test service=ipsec
```

##### IPsec (IKEv2) server configuration

Add a new Phase 1 profile and Phase 2 proposal entries with pfs-group=none:

```ros
/ip/ipsec/profile
add name=ike2
/ip/ipsec/proposal
add name=ike2 pfs-group=none
```

Mode config is used for address distribution from IP/Pools.

```ros
/ip/pool
add name=ike2-pool ranges=192.168.77.2-192.168.77.254
/ip/ipsec/mode-config
add address-pool=ike2-pool address-prefix-length=32 name=ike2-conf
```

Since the policy template must be adjusted to allow only specific network policies, you should create a separate policy group and template.

```ros
/ip/ipsec/policy/group
add name=ike2-policies
/ip/ipsec/policy
add dst-address=192.168.77.0/24 group=ike2-policies proposal=ike2 src-address=0.0.0.0/0 template=yes
```

Create a new IPsec peer entry that listens to all incoming IKEv2 requests.

```ros
/ip/ipsec/peer
add exchange-mode=ike2 name=ike2 passive=yes profile=ike2
```

Lastly, create a new IPsec identity entry that matches all clients trying to authenticate with EAP. The generated Let's Encrypt certificate must be specified.

```ros
/ip/ipsec/identity
add auth-method=eap-radius certificate="letsencrypt_2021-04-09T07:10:55Z" generate-policy=port-strict mode-config=ike2-conf peer=ike2 \
policy-template-group=ike2-policies
```

##### (Optional) Split tunnel configuration

Split tunneling is a method that allows road warrior clients to only access a specific secured network and at the same time send the rest of the traffic based on their internal routing table (as opposed to sending all traffic over the tunnel). To configure split tunneling, change the mode config parameters.

For example, allow road warrior clients to only access the 10.5.8.0/24 network.

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] split-include=10.5.8.0/24
```

You can also send a specific DNS server for the client to use. By default, system-dns=yes is used, which sends DNS servers that are configured on the router itself in IP/DNS. Force the client to use a different DNS server with the static-dns parameter.

```ros
/ip/ipsec/mode-conf
set [find name="rw-conf"] system-dns=no static-dns=10.5.8.1
```

:::warning
Split networking is not a security measure. The client (initiator) can still request a different Phase 2 traffic selector.
:::

##### (Optional) Assigning static IP address to user

A static IP address can be assigned to any user by use of the RADIUS Framed-IP-Address attribute.

```ros
/user-manager/user
set [find name="user1"] attributes=Framed-IP-Address:192.168.77.100 shared-users=1
```

:::danger
To avoid any conflicts, the static IP address should be excluded from the IP pool of other users, and shared-users should be set to 1 for the specific user.
:::

##### (Optional) Accounting configuration

To keep track of every user's uptime, download and upload statistics, RADIUS accounting can be used. By default RADIUS accounting is already enabled for IPsec, but you should configure the Interim Update timer that sends statistics to the RADIUS server regularly. If the router handles many simultaneous sessions, increase the update timer to avoid CPU usage.

```ros
/ip/ipsec/settings
set interim-update=1m
```

### Basic L2TP/IPsec setup

This example demonstrates how to easily set up an L2TP/IPsec server on RouterOS for road warrior connections (works with Windows, Android, iOS, macOS, and other vendor L2TP/IPsec implementations).

#### RouterOS server configuration

The first step is to enable the L2TP server:

```ros
/interface/l2tp-server/server
set enabled=yes use-ipsec=required ipsec-secret=mySecret default-profile=default
```

use-ipsec is set to **required** to ensure that only IPsec encapsulated L2TP connections are accepted.

This enables an L2TP server and creates a dynamic IPsec peer with a specified secret.

```ros
[admin@MikroTik] /ip/ipsec/peer> print 
0 D address=0.0.0.0/0 local-address=0.0.0.0 passive=yes port=500 
auth-method=pre-shared-key secret="123" generate-policy=port-strict 
exchange-mode=main-l2tp send-initial-contact=yes nat-traversal=yes 
hash-algorithm=sha1 enc-algorithm=3des,aes-128,aes-192,aes-256 
dh-group=modp1024 lifetime=1d dpd-interval=2m dpd-maximum-failures=5 
```

:::warning
Care must be taken if a static IPsec peer configuration exists.
:::

The next step is to create a VPN pool and add some users.

```ros
/ip/pool/add name=vpn-pool range=192.168.99.2-192.168.99.100

/ppp/profile
set default local-address=192.168.99.1 remote-address=vpn-pool

/ppp/secret
add name=user1 password=123
add name=user2 password=234
```

Now the router is ready to accept L2TP/IPsec client connections.

#### RouterOS client configuration

For RouterOS to work as an L2TP/IPsec client, it is as simple as adding a new L2TP client.

```ros
/interface/l2tp-client
add connect-to=1.1.1.1 disabled=no ipsec-secret=mySecret name=l2tp-out1 \
password=123 use-ipsec=yes user=user1
```

This automatically creates dynamic IPsec peer and policy configurations.

### Troubleshooting/FAQ

#### Phase 1 Failed to get a valid proposal

```ros
[admin@MikroTik] /log> print
(..)
17:12:32 ipsec,error no suitable proposal found. 
17:12:32 ipsec,error 10.5.107.112 failed to get valid proposal. 
17:12:32 ipsec,error 10.5.107.112 failed to pre-process ph1 packet (side: 1, status 1). 
17:12:32 ipsec,error 10.5.107.112 phase1 negotiation failed. 
(..)
```

Peers are unable to negotiate encryption parameters causing the connection to drop. To solve this issue, enable IPSec debug logs and find out which parameters are proposed by the remote peer, and adjust the configuration accordingly.

```ros
[admin@MikroTik] /system/logging> add topics=ipsec,!debug
```

```ros
[admin@MikroTik] /log> print
(..)
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#1):Peer(prop#1:trns#1) = MD5:SHA 
17:21:08 ipsec rejected enctype: DB(prop#1:trns#2):Peer(prop#1:trns#1) = 3DES-CBC:AES-CBC 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#2):Peer(prop#1:trns#1) = MD5:SHA 
17:21:08 ipsec rejected enctype: DB(prop#1:trns#1):Peer(prop#1:trns#2) = AES-CBC:3DES-CBC 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#1):Peer(prop#1:trns#2) = MD5:SHA 
17:21:08 ipsec rejected hashtype: DB(prop#1:trns#2):Peer(prop#1:trns#2) = MD5:SHA 
17:21:08 ipsec,error no suitable proposal found. 
17:21:08 ipsec,error 10.5.107.112 failed to get valid proposal. 
17:21:08 ipsec,error 10.5.107.112 failed to pre-process ph1 packet (side: 1, status 1). 
17:21:08 ipsec,error 10.5.107.112 phase1 negotiation failed. 
(..)
```

In this example, the remote end requires SHA1 to be used as a hash algorithm, but MD5 is configured on the local router. The Setting before the colon symbol (:) is configured on the local side, the parameter after the colon symbol (:) is configured on the remote side.

#### "phase1 negotiation failed due to time up" what does it mean?

Communication problems exist between the peers. Possible causes include - misconfigured Phase 1 IP addresses; firewall blocking UDP ports 500 and 4500; NAT between peers not properly translating IPsec negotiation packets. This error message can also appear when a local-address parameter is not used properly.

#### Random packet drops or connections over the tunnel are very slow, enabling packet sniffer/torch fixes the problem?

The problem is that before encapsulation packets are sent to Fasttrack/FastPath, thus bypassing IPsec policy checking. The solution is to exclude traffic that needs to be encapsulated/decapsulated from Fasttrack.

#### How to enable ike2?

To enable ike2 for basic configuration, change exchange-mode in peer settings to ike2.

#### fatal NO-PROPOSAL-CHOSEN notify message?

Remote peer sent a notify that it cannot accept proposed algorithms, to find the exact cause of the problem, look at remote peer's debug logs or configuration and verify that both client and server have the same set of algorithms.

#### I can ping only in one direction?

A typical problem in such cases is a strict firewall: firewall rules allow the creation of new connections only in one direction. The solution is to recheck firewall rules, or explicitly accept all traffic that should be encapsulated/decapsulated.

#### Can I allow only encrypted traffic?

Yes, you can, see "Allow only IPsec encapsulated traffic" examples.

#### I enable IKEv2 REAUTH on StrongSwan and got the error 'initiator did not reauthenticate as requested'

RouterOS does not support rfc4478, reauth must be disabled on StrongSwan.
