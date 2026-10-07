# Route Leak Prevention

> Prevent and detect route leaks using BGP roles defined in RFC 9234.

# Route Leak Prevention

A route leak occurs when a BGP speaker announces routes to a peer that, according to the configured business relationship, should not receive them. For example, a transit customer that re-announces routes learned from one provider to another provider can cause traffic to be routed through the customer's network, potentially bypassing the intended path and creating routing loops or traffic interception.

[RFC 9234](https://datatracker.ietf.org/doc/rfc9234/) — *Route Leak Prevention and Detection Using Roles in UPDATE and OPEN Messages* — defines a mechanism to prevent and detect route leaks by assigning each eBGP session a role that describes the relationship between the two peers. RouterOS implements this mechanism through the `local.role` parameter, which is mandatory for every BGP connection and defines the role of the local router in a BGP session.

The `ibgp`, `ibgp-rr`, and `ebgp` roles do not participate in RFC 9234 role negotiation. The session is established as a traditional BGP session without exchanging the Role capability.

The remaining five roles participate in RFC 9234 role negotiation:

| Role | Description |
| :-- | :-- |
| `ebgp-provider` | Transit provider. |
| `ebgp-rs` | Route server. |
| `ebgp-rs-client` | Route server client. |
| `ebgp-customer` | Transit customer. |
| `ebgp-peer` | Lateral peer (peering relationship). |

### Relationship types

These roles describe the business relationship between two eBGP peers:

- **Transit provider—customer**: A provider sells transit to a customer, giving the customer access to the provider's full routing table (typically the entire Internet). The customer announces its own prefixes and those of its downstream customers to the provider. The provider announces all routes it has learned (including routes from other customers and peers) to the customer. In this relationship, the provider is the upstream and the customer is the downstream.
- **Route server—client**: A route server is a neutral BGP speaker typically deployed at Internet Exchange Points (IXPs). It does not forward traffic itself — it only reflects routing information between its clients. A route server client connects to the route server to exchange routes with other clients without needing direct peering sessions with each of them. The route server does not modify the AS_PATH or NEXT_HOP, and it does not appear in the data path.
- **Lateral peer**: Two networks with a peering relationship exchange only their own routes and the routes of their respective customers. Neither announces routes learned from other peers or providers. Peering is typically settlement-free, meaning no money is exchanged between the two networks.

Both peers must be configured with matching roles for the session to establish successfully.

## Role negotiation

When a BGP session is configured with an RFC 9234 role, the router sends the BGP Role capability (Capability Code 9) in the OPEN message. When the local router receives the remote peer's OPEN message, it checks the received role against the expected role based on the locally configured `local.role`:

| Local role | Expected remote role |
| :-- | :-- |
| `ebgp-provider` | `ebgp-customer` |
| `ebgp-customer` | `ebgp-provider` |
| `ebgp-rs` | `ebgp-rs-client` |
| `ebgp-rs-client` | `ebgp-rs` |
| `ebgp-peer` | `ebgp-peer` |

If the remote peer does not send the Role capability, or if the received role does not match the expected role, the router sends a NOTIFICATION message with Error Code 2 (OPEN Message Error), Error Subcode 8 (Role Mismatch), and the session is terminated.

The negotiated roles are visible in the session monitoring output:

- `remote.role` — the role received from the remote peer in the OPEN message.
- `local.role` — the locally configured role.

## Configuration

The `local.role` parameter is configured in the [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp/connection) menu.

If the session is established, negotiated capabilites and selected roles can be monitored in [`/rouring/bgp/session`](../../../../cli-reference/routing/bgp/session) menu.

The `remote.capabilities` field includes `role` when the remote peer supports the BGP Role capability. The `remote.role` field shows the actual role received from the remote peer.

If the session fails to establish due to a role mismatch, the `input.last-notification` field contains the hex-encoded NOTIFICATION message received from the peer.

### Example: Transit provider to customer

A transit provider connecting to a downstream customer:

```ros
# Provider side (AS 64500)
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=to-customer remote.address=198.51.100.1 instance=instance1 local.role=ebgp-provider

# Customer side (AS 64501)
/routing/bgp/instance
add name=instance1 as=64501
/routing/bgp/connection
add name=to-provider remote.address=192.0.2.1 instance=instance1 local.role=ebgp-customer
```

Both peers must be configured with matching roles. A peer configured as `ebgp-provider` expects the remote to be `ebgp-customer`, and vice versa.

### Example: Route server with multiple clients

An IXP route server connecting to multiple clients:

```ros
# Route server side (AS 65500)
/routing/bgp/instance
add name=instance1 as=65500
/routing/bgp/connection
add name=rs-client1 remote.address=203.0.113.1 instance=instance1 local.role=ebgp-rs
add name=rs-client2 remote.address=203.0.113.2 instance=instance1 local.role=ebgp-rs

# Route server client side (AS 64601)
/routing/bgp/instance
add name=instance1 as=64601
/routing/bgp/connection
add name=to-rs remote.address=203.0.113.254 instance=instance1 local.role=ebgp-rs-client
```

### Example: Peering between two networks

Two networks with a peering relationship:

```ros
# Network A (AS 64500)
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=to-peer-b remote.address=192.0.2.2 instance=instance1 local.role=ebgp-peer

# Network B (AS 64700)
/routing/bgp/instance
add name=instance1 as=64700
/routing/bgp/connection
add name=to-peer-a remote.address=192.0.2.1 instance=instance1 local.role=ebgp-peer
```

### Example: iBGP and route reflector

Internal BGP sessions do not use RFC 9234 role negotiation:

```ros
# iBGP peer
/routing/bgp/instance
add name=instance1 as=64500
/routing/bgp/connection
add name=ibgp-peer1 remote.address=10.0.0.2 instance=instance1 local.role=ibgp

# iBGP route reflector client
/routing/bgp/connection
add name=rr-client1 remote.address=10.0.0.3 instance=instance1 local.role=ibgp-rr
```
