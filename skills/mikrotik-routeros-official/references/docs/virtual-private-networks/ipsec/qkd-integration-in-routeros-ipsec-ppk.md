# QKD Integration in RouterOS IPsec (PPK)

> This page introduces RouterOS IPsec's Post-Quantum Pre-shared Key (PPK) feature, detailing its integration with Quantum Key Distribution (QKD), supported key sources (static, PSK, QKD), security recommendations, and...

# QKD Integration in RouterOS IPsec (PPK)

### 1. Introduction

This manual describes the Post-Quantum Pre-shared Key (RFC9867) feature in RouterOS IPsec and its integration with Quantum Key Distribution (QKD).

PPK provides forward security against quantum attacks by using keys that are either dynamically distributed or statically configured. All PPK types (static, PSK, QKD) benefit from RFC 8784 recommendations: keys should have at least 256 bits of entropy to provide ~128 bits of post-quantum security.

RouterOS supports three PPK sources:

- Static PPK — manually configured per-peer secret.
- PSK (Pre-shared Key) — one-time generated keys, optionally usable only for initial IKE SA.
- QKD — dynamically distributed keys from a QKD server.

Dynamic keys (PSK/QKD) are consumed and invalidated after use. Static keys remain valid across sessions but offer weaker security if reused.

### ![](./img/qkd-integration-in-routeros-ipsec-ppk-01.webp)

### 2. Concepts

- **PPK (Post-Quantum Pre-shared Key):** An additional secret shared during IKE negotiation to resist quantum attacks.
- **QKD:** Quantum-based key distribution providing fresh symmetric keys via a Key Management Entity (KME).

#### IKE SA vs ESP SA

- IKE SA: Controls tunnel negotiation.
- ESP SA: Carries encrypted user data.

#### Static vs Dynamic keys

- Dynamic: ephemeral PSK or QKD-distributed secrets, used once and discarded.
- Static: manually set per peer, persistent across sessions.

#### 2.1 RouterOS PPK Sources

| PPK Source | Description |
| :-- | :-- |
| Static | Persistent, manually configured secret. |
| PSK | One-time dynamically generated pre-shared keys. Can optionally be used only for initial IKE SA (`psk-ike-initial`). |
| QKD | Keys pulled dynamically from a QKD server, consumed after use. |

### 3. Security Recommendations

- All PPK keys should meet RFC 8784 recommendations: ≥256 bits of entropy.
- Static PPK keys improve post-quantum protection if sufficiently long, but re-use reduces security.
- Dynamic keys (PSK/QKD) offer stronger security since they are one-time use. Synchronization failure may cause key desynchronization.

### 4. Two-Device Setup Overview

This manual focuses on a minimal setup with two devices:

| Role | Device | Function |
| :-- | :-- | :-- |
| Server | RouterOS | Hosts an IPsec tunnel; provides a QKD/PPK key |
| Client | ROS/LibreSwan | Connects to the server using QKD/PPK |

The RouterOS server may act as a QKD client to a KME, so no third device is required.

```routeros
# Example of pushing a configuration to a remote peer (IPsec)
/ip ipsec peer
add address=192.168.88.1/32 name=Server exchange-mode=ike2
/ip ipsec proposal
set [ find default=yes ] auth-algorithms=sha256 enc-algorithms=aes-256-gcm
```

### 5. Configuration Objects

#### 5.1 Certificates

QKD requires:

- CA certificate (to validate the server).
- SAE client certificate (for authentication to the QKD server).

```
/certificate/import file-name=ca.crt.pem
/certificate/import file-name=sae-server.crt.pem
/certificate/import file-name=sae-server.key.pem

```

#### 5.2 PSK Example

Generate one-time PSKs for PPK use:

```
/ip/ipsec/key/psk/generate count=10 key-size=32

```

- **count** → number of PSKs to generate.
- **key-size** → size of each key in bytes (32 bytes = 256 bits).

#### 5.3 QKD Key Manager

RouterOS server can act as a QKD client:

```
/ip/ipsec/key/qkd/set address=10.2.3.4:8020 \
    cache-size=1 \
    certificate=sae-server \
    key-size=32 \
    kme-id=server-kme-id \
    peer-sae-id=client-sae-id

```

Parameter descriptions:

| Parameter | Description |
| :-- | :-- |
| cache-size | Number of keys IPsec will prefetch from the QKD server. |
| cache-state | Current number of keys cached and available. |
| key-size | Requested size of each key in bytes (e.g., 32 bytes = 256 bits). |
| kme-id | Used for certificate validation. If not specified, the KME identity will not be validated. |
| peer-sae-id | Identifier for the peer SAE. |

#### 5.4 Profiles and Peers

```
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 \
    name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile

```

PPK options for profiles:

| Option | Description |
| :-- | :-- |
| no | PPK disabled. |
| psk | One-time PSK used for IKE and ESP rekey. |
| psk-ike-initial | PSK used only for the initial IKE SA (renamed from `psk-ike-only`). |
| qkd | Keys retrieved from a QKD server. |

#### 5.5 Proposal / Policy

```
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 \
    enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 \
    peer=peer-client proposal=qkd-proposal tunnel=yes

```

### 6. Behaviour

- Dynamic keys: Pulled from `/ip/ipsec/key/psk/` or QKD server, consumed once, then deleted.
- Static key: Configured per peer, used repeatedly.
- One-time dynamic keys ensure the strongest protection but require synchronization.
- Static fallback guarantees tunnel establishment but should be long enough (≥256 bits entropy).
- PPK usage can optionally be restricted to IKE SA only (`psk-ike-initial`) to reduce key consumption.

### 7. Debugging and Troubleshooting

To verify QKD integration and key retrieval, enable IPsec debug logging:

```
/system/logging/add topics=ipsec,debug action=memory

```

Sample debug output showing QKD key retrieval:

```
2025-10-11 17:32:38 ipsec,debug,packet POST
2025-10-11 17:32:38 ipsec,debug,packet Host: 10.2.3.4\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"number":1,"size":16}
2025-10-11 17:32:38 ipsec,debug,packet HTTP/1.1 200 OK\r\n
2025-10-11 17:32:38 ipsec,debug,packet {"keys":[{"key_ID":"37f4c842-dd82-4c49-8dfc-52a3793e5331","key":"m/JIEIUCzAE="}]}
2025-10-11 17:32:38 ipsec,debug,packet qkd: add to cache key 37f4c842-dd82-4c49-8dfc-52a3793e5331: 9bf24
```

If keys are not being added to the cache, check network connectivity to the KME, certificate validation, and correct `kme-id` and `peer-sae-id` configuration.

### 8. Example Export (Two-Device Setup)

#### RouterOS Server

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-server key-size=32 \
    kme-id=server-kme-id peer-sae-id=client-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.2 exchange-mode=ike2 name=peer-client profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-client profile=qkd-profile
/ip/ipsec/policy/add src-address=10.1.0.0/24 dst-address=10.2.0.0/24 peer=peer-client proposal=qkd-proposal tunnel=yes

```

#### Client Device

```
/ip/ipsec/key/qkd
set address=10.2.3.4:8020 cache-size=1 certificate=sae-client key-size=32 \
    kme-id=client-kme-id peer-sae-id=server-sae-id
/ip/ipsec/profile/add name=qkd-profile ppk=qkd
/ip/ipsec/proposal/add name=qkd-proposal auth-algorithms=sha256 enc-algorithms=aes-256-gcm pfs-group=modp2048
/ip/ipsec/peer/add address=10.2.1.1 exchange-mode=ike2 name=peer-server profile=qkd-profile proposal-check=obey
/ip/ipsec/identity/add peer=peer-server profile=qkd-profile
/ip/ipsec/policy/add src-address=10.2.0.0/24 dst-address=10.1.0.0/24 peer=peer-server proposal=qkd-proposal tunnel=yes

```

### 9. References

- IETF Draft: IKEv2 Post-Quantum PPK: [https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-qr-alt/)
- [https://datatracker.ietf.org/doc/html/rfc9867](https://datatracker.ietf.org/doc/html/rfc9867)

### Notes

#### QKD as a Distribution Mechanism

- QKD in RouterOS is not a new encryption method itself - it’s a **key distribution mechanism**.
- It provides dynamically generated keys via the **Key Management Entity (KME)**, which both peers retrieve securely.

#### Dynamic vs Static Sources

- *Dynamic sources*: QKD-distributed keys, one-time PSKs from `/ip/ipsec/key/psk/`.
- *Static sources*: Per-peer configured static PPK secret.
- Recommendation: prefer **dynamic keys** for long-term security; keep a **static fallback** to prevent tunnel drops if dynamic keys run out.

#### Security Guidelines (RFC 8784)

- Post-quantum preshared keys should contain **at least 256 bits of entropy** to provide 128-bit post-quantum security.
- Using only one static key for IKE SA protection is possible, but carries risk if reused.

#### Operational Considerations

- **Key exhaustion**: one-time PSKs are consumed quickly during aggressive rekeying (IKE + ESP). QKD avoids this by continuously providing fresh keys.
- **Hub-and-spoke topologies**: dynamic PSKs need peer association to avoid desynchronization between spokes.
- **Fallback behavior**: ensure the system can gracefully switch to static PPK if dynamic keys are unavailable.

#### Compatibility Notes

- **RouterOS - RouterOS**: supports both PSK and QKD PPK.
- **RouterOS - LibreSwan**: works with static PPK; dynamic PSK may require custom builds.
- **RouterOS - StrongSwan**: requires adaptation, as identifiers differ between draft versions.
