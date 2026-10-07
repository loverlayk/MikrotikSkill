# Nexthop Selection

> BGP nexthop selection procedures on input and output.

# Nexthop Selection

RouterOS does not perform strict nexthop checks on BGP input; instead, it relies on [filter rules](../../../../cli-reference/routing/filter/rule) created by the user.

Actions performed on input:

- Read the nexthop from the BGP **NEXT_HOP** attribute.
- For multi-protocol NLRI, check whether the nexthop has a valid length:
  - Send an Update error notification and exit if the length is invalid.
  - Store the nexthop value.
  - If a link-local nexthop appears in the update message:
    - Determine the connection interface.
    - Store the link-local address and interface.
- Apply nexthop actions from input filter rules.
- Send the route to the main calc process, where nexthop reachability is determined.

## BGP Output

- If [`nexthop-choice`](../../../../cli-reference/routing/bgp/connection.md#nexthop-choice) is not `force-self` or the route AFI is not IPv4 or IPv6:
  - If the peer is a route reflector, or [`nexthop-choice`](../../../../cli-reference/routing/bgp/connection.md#nexthop-choice) is `propagate`, or the peer is not eBGP:
    - Check the nexthop AFI and try to set the outgoing link-local nexthop.
    - Check the nexthop AFI and try to set the outgoing nexthop.
  - If the outgoing nexthop is still unset and the BGP peer is not multihop:
    - Loop through available immediate nexthops and try to set the outgoing nexthop and the LL nexthop.
  - If the outgoing nexthop equals the remote [`router-id`](../../../../cli-reference/routing/bgp/instance.md#router-id), unset the outgoing nexthop.
  - If the outgoing nexthop equals the remote peer's address, unset the outgoing nexthop.
  - If the interface of the peer's address is not equal to the LL nexthop's interface, unset the outgoing LL nexthop.
  - If the outgoing LL nexthop equals the remote peer's address, unset the outgoing LL nexthop.
- If the outgoing nexthop is still not set, check the AFI and set the peer's local-address.
- If the outgoing nexthop is still unset and the route AFI is IPv6 or L2VPN:
  - If the peer's local address is IPv4, set the outgoing nexthop to the IPv6-mapped peer's local address.
