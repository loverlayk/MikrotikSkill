# IPsec

> IPsec in RouterOS: what the menus do, which setup to choose, how IKE and its two phases work, Diffie-Hellman groups, AH and ESP, tunnel and transport mode, the supported algorithms and hardware acceleration.

# IPsec

Internet Protocol Security (IPsec) is a set of protocols of the Internet Engineering Task Force (IETF) that protect IP packets on networks that are not trusted, such as the internet. It encrypts and authenticates the traffic between two routers, or between a router and a remote device, and it works with the devices of most vendors.

The protocols are in three groups:

- **Internet Key Exchange (IKE)** makes and renews the keys.
- **Encapsulating Security Payload (ESP)**, RFC 4303, encrypts and authenticates the packets.
- **Authentication Header (AH)**, RFC 4302, only authenticates the packets.

## Choose a setup

| You want to | See |
| :-- | :-- |
| Connect the networks of two offices | [Site-to-site tunnel](site-to-site) |
| Run dynamic routing over the tunnel, or route traffic into it | [Route-based IPsec with XFRM](route-based-ipsec-xfrm) |
| Let remote computers and phones connect with certificates | [Road warrior with certificates](road-warrior-ikev2-certificates) |
| Let remote users connect with a user name and a password | [Road warrior with EAP and User Manager](road-warrior-ikev2-eap) |
| Protect an L2TP, GRE, IPIP or EoIP tunnel with a shared key | `ipsec-secret` of the tunnel: see [L2TP](../l2tp/), [GRE](../gre), [IPIP](../ipip), [EoIP](../eoip) |
| Allow only encrypted traffic, or use a certain WAN address | [Firewall and routing for IPsec](firewall-and-routing) |
| Find why a tunnel does not work | [Troubleshooting](troubleshooting) |
| Connect to NordVPN | [IKEv2 EAP between NordVPN and RouterOS](ikev2-eap-between-nordvpn-and-routeros) |
| Add a post-quantum pre-shared key (PPK) with quantum key distribution | [QKD integration in RouterOS IPsec](qkd-integration-in-routeros-ipsec-ppk) |

## The configuration menus

An IPsec connection in RouterOS is built from several entries under `/ip/ipsec`:

| Menu | What it has |
| :-- | :-- |
| [`profile`](../../cli-reference/ip/ipsec/profile) | The algorithms and timers of the IKE connection (phase 1). |
| [`proposal`](../../cli-reference/ip/ipsec/proposal) | The algorithms and the lifetime of the encrypted traffic (phase 2). |
| [`peer`](../../cli-reference/ip/ipsec/peer) | The other side: its address, the IKE version (`exchange-mode`) and the profile. A peer with `passive=yes` waits for connections. |
| [`identity`](../../cli-reference/ip/ipsec/identity) | How the two sides authenticate each other: a pre-shared key, certificates or EAP. It also selects the mode config and the policy group for the peer. |
| [`policy`](../../cli-reference/ip/ipsec/policy/) | Which traffic is encrypted: source and destination addresses, and the peer. A policy with `template=yes` is a pattern for the policies that are made dynamically. |
| [`policy/group`](../../cli-reference/ip/ipsec/policy/group) | A name that connects policy templates to identities. |
| [`mode-config`](../../cli-reference/ip/ipsec/mode-config) | Addresses, DNS servers and networks that a server gives to remote clients, or that a client asks for. |
| [`active-peers`](../../cli-reference/ip/ipsec/active-peers/) | The IKE connections that exist now. |
| [`installed-sa`](../../cli-reference/ip/ipsec/installed-sa/) | The security associations (SAs) that encrypt traffic now. |

The entries `default` of the profile, the proposal and the policy template exist after installation. The examples add their own entries, so that a change for one connection does not affect another.

:::warning
IPsec is sensitive to time changes. If the clocks of the two sides change in different ways, tunnels break and must be made again. Use an NTP client on both sides.
:::

## How IKE works

IKE authenticates the two sides and manages the security associations automatically. The IKE service does nothing most of the time. It starts to work in two cases:

- Traffic matches a policy that has no SA yet. The router then connects to the peer of the policy.
- A remote peer connects.

In both cases the peers make a connection in two phases:

- **Phase 1.** The peers agree on the algorithms for the IKE messages and authenticate each other. They also make the keying material for all SAs. These settings must match on both sides:
  - authentication method
  - DH group
  - encryption algorithm
  - exchange mode
  - hash algorithm
  - NAT-T
  - DPD and lifetime (optional)
- **Phase 2.** The peers make one or more SAs that IPsec uses to encrypt data. These settings must match:
  - IPsec protocol
  - mode (tunnel or transport)
  - authentication method
  - PFS (DH) group
  - lifetime

Each SA has a lifetime: a time, an amount of data, or both. There are two limits. At the soft lifetime, the IKE service makes a new SA to replace the old one. At the hard lifetime, the SA is removed.

:::warning

- Phase 1 is not re-keyed when the lifetime ends if DPD is disabled; only phase 2 is re-keyed. To re-key phase 1, enable DPD.
- Authentication with a pre-shared key (PSK) is open to offline attacks. This was known for the `aggressive` exchange mode, and it is also possible in the `main` and `ike2` modes. Avoid pre-shared keys where you can and use certificates. If you use a key, make it long and random.

:::

IKE can provide Perfect Forward Secrecy (PFS): new keying material is made for each phase 2, so that someone who gets the long-term phase 1 key cannot read all the data of the SAs made with it. Making keying material is expensive for the CPU. A `modp8192` exchange can take several seconds even on a very fast computer. Without PFS this happens once for each phase 1; with PFS it happens for each phase 2 as well.

To avoid problems with IKE packets that would match a policy before its SA exists, packets that the router sends from UDP port 500, and packets to UDP port 500 of the router, are not checked against the policies.

### Diffie-Hellman groups

The Diffie-Hellman (DH) key exchange lets two sides without a shared secret make one securely. RouterOS supports these Modular Exponential (MODP) and ECP groups, also known as Oakley groups:

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

The profile also accepts `x25519`. The [IANA registry](https://www.iana.org/assignments/ipsec-registry/ipsec-registry.xhtml) has more about the standards.

Larger groups are more secure but need more CPU:

- **Group 19** (256-bit ECP, `ecp256`) is fast and secure. Use it when both sides support it.
- **Group 14** (2048-bit MODP) is a practical balance of security and CPU use and is widely supported.
- **Group 5** (1536-bit) is a little less secure than group 14 and needs less CPU.
- **Group 2** (1024-bit) is the least secure of the common groups. Do not use it for new setups; use it only where an old device needs it.

To choose algorithms for a required security level, see [https://www.keylength.com/en/4/](https://www.keylength.com/en/4/).

### EAP authentication methods

| Outer Auth | Inner Auth |
| :-- | :-- |
| EAP-GTC |  |
| EAP-MD5 |  |
| EAP-MSCHAPv2 |  |
| EAP-PEAPv0 | EAP-MSCHAPv2 EAP-GPSK EAP-GTC EAP-MD5 EAP-TLS |
| EAP-SIM |  |
| EAP-TLS |  |
| EAP-TTLS | PAP  CHAP  MS-CHAP  MS-CHAPv2  EAP-MSCHAPv2 EAP-GTC EAP-MD5 EAP-TLS |

EAP-TLS on Windows is called "Smart Card or other certificates".

:::info

- AES-GCM is not supported for the encryption of the IKEv2 connection itself (phase 1).
- A certificate for IPsec must be an X.509 version 3 certificate with the SubjectKeyIdentifier extension.
- Authentication with ed25519 is not supported.

:::

## Authentication Header (AH)

AH adds a header with a value that is calculated from the contents of the packet. The receiver can check that the packet was not changed, but the packet is not encrypted: AH gives authentication without privacy. ESP is usually the better choice, because it encrypts and can also authenticate.

RouterOS supports these authentication algorithms for AH: SHA2 (256, 512), SHA1 and MD5.

- In **transport mode**, the AH header is put after the IP header. The IP data and the header are used for the calculation. IP fields that can change on the way, such as the TTL, are set to zero for the calculation.
- In **tunnel mode**, the original IP packet is put into a new IP packet, and the whole original packet is authenticated.

## Encapsulating Security Payload (ESP)

ESP encrypts the data with a shared key, and it can authenticate the packet in the same way as AH. ESP adds three parts to a packet:

- **ESP header** - before the encrypted data. Its place depends on the mode.
- **ESP trailer** - after the encrypted data. It has the padding that aligns the data.
- **ESP authentication data** - the Integrity Check Value (ICV), when authentication is used.

In **transport mode**, the ESP header is put after the original IP header, and the trailer and the authentication value are added at the end. Only the IP payload is encrypted and authenticated; the IP header is not protected.

![An ESP packet in transport mode: the original IP header, the ESP header, the encrypted payload, the ESP trailer and the authentication data](./img/ipsec-01.webp)

In **tunnel mode**, the original IP packet is put into a new IP packet, so the payload and the original IP header are both protected.

![An ESP packet in tunnel mode: a new IP header, the ESP header, the encrypted original packet, the ESP trailer and the authentication data](./img/ipsec-02.webp)

### Algorithms

Authentication:

- MD5
- SHA1
- SHA2 (256-bit, 512-bit; also 384-bit for the IKE connection)

Encryption:

- **AES** - AES-CBC, AES-CTR and AES-GCM with 128-bit, 192-bit and 256-bit keys. AES-GCM authenticates the packets itself: a proposal with an AES-GCM algorithm needs `auth-algorithms=""`.
- **ChaCha20-Poly1305**
- **Blowfish**
- **Twofish**
- **Camellia** - 128-bit, 192-bit and 256-bit keys.
- **DES** - 56-bit DES-CBC.
- **3DES** - 168-bit (3 x 56-bit) DES.

DES, 3DES, Blowfish and MD5 are old algorithms. Use them only for devices that support nothing else.

## Hardware acceleration

Hardware acceleration enables faster encryption with a built-in encryption engine inside the CPU.

A list of devices with hardware acceleration is on the [MikroTik products page](https://mikrotik.com/products?filter&s=c&f=%5B%22ipsec%22%5D).

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

## In this section

<DocCardList />
