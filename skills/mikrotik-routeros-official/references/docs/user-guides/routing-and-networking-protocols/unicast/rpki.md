# RPKI

> RouterOS validates BGP prefix origin and AS paths with RPKI. It negotiates RTR protocol version 2 for ASPA data and falls back to version 1 for older validators.

# RPKI

RouterOS implements the Resource Public Key Infrastructure (RPKI) to Router Protocol (RTR) defined in [RFC 8210](https://tools.ietf.org/html/rfc8210). It also supports RTR protocol version 2 as defined in [draft-ietf-sidrops-8210bis](https://datatracker.ietf.org/doc/draft-ietf-sidrops-8210bis/), which adds ASPA data. RTR is a lightweight, low-memory protocol for retrieving prefix origin data and Autonomous System Provider Authorization (ASPA) data from RPKI validators. See a validator setup example on the [RIPE blog](https://blog.apnic.net/2019/10/28/how-to-installing-an-rpki-validator/).

Configuration is available under [`/routing/rpki`](../../../cli-reference/routing/rpki/rpki.md).

## RTR protocol version 2

RouterOS starts an RTR session with protocol version 2 (RTRv2). If the validator only supports version 1, RouterOS reconnects with version 1. The fallback is automatic; no parameter selects the protocol version.

After the session synchronizes, the negotiated version is shown in the [`version`](../../../cli-reference/routing/rpki/session.md#version) field of the `/routing/rpki/session` menu:

```ros
/routing/rpki/session print detail
```

A version 2 session can receive ASPA PDUs. A version 1 session provides only prefix origin data. To validate AS paths with ASPA, use a validator that supports RTR protocol version 2 and publishes ASPA objects.

## Prefix origin validation

Assume your network has an RTR server at IP address `192.168.1.1`:

```ros
/routing/rpki
add group=myRpkiGroup address=192.168.1.1 port=8282 refresh-interval=20
```

The [`group`](../../../cli-reference/routing/rpki/rpki.md#group), [`address`](../../../cli-reference/routing/rpki/rpki.md#address), [`port`](../../../cli-reference/routing/rpki/rpki.md#port), and [`refresh-interval`](../../../cli-reference/routing/rpki/rpki.md#refresh-interval) parameters configure the RTR connection. Additional parameters include [`vrf`](../../../cli-reference/routing/rpki/rpki.md#vrf), [`preference`](../../../cli-reference/routing/rpki/rpki.md#preference), [`retry-interval`](../../../cli-reference/routing/rpki/rpki.md#retry-interval), and [`expire-interval`](../../../cli-reference/routing/rpki/rpki.md#expire-interval).

After the connection is established and the validator database is received, check prefix validity using [`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md):

```text
[admin@MikroTik] /routing/rpki> rpki-check group=myRpkiGroup prefix=70.132.18.0/24 origin-as=16509
    valid
```

Use the cached database in [routing filters](../route-selection-and-filtering.md) to accept or reject prefixes based on RPKI validity. First set up a [`/routing/filter/rule`](../../../cli-reference/routing/filter/rule.md) that defines which RPKI group performs verification. After that, filters can match the status from the RPKI database. Status can have one of four values:

- **valid** - Database has a record and origin AS is valid.
- **invalid** - The database has a record and origin AS is invalid.
- **unknown** - The database does not have information about the prefix and origin AS.
- **unverified** - Set when none of the RPKI group's sessions has synced the database. Use this value to handle total RPKI failure.

```ros
/routing/filter/rule
add chain=bgp_in rule="rpki-verify myRpkiGroup"
add chain=bgp_in rule="if (rpki invalid) { reject } else { accept }"
```

## ASPA validation

An ASPA object authorizes a set of provider ASes for a customer AS. RouterOS validates the BGP AS path against ASPA objects to detect route leaks that prefix origin validation cannot detect. ASPA validation complements prefix origin validation; use both to detect invalid origins and route leaks. The validation follows [draft-ietf-sidrops-aspa-verification](https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/).

ASPA validation requires:

- A validator that supports RTR protocol version 2 and publishes ASPA objects.
- An RFC 9234 role configured with [`local.role`](../../../cli-reference/routing/bgp/connection.md#local.role) on the eBGP connection. The `ibgp`, `ibgp-rr`, and `ebgp` roles do not provide the role information ASPA validation needs, so ASPA validation does not run for sessions that use them. See [Route leak prevention](bgp/route-leak-prevention.md).
- ASPA verification enabled in the routing filter chain with the `rpki-aspa-verify` command.

The following example validates both the prefix origin and the AS path for routes received from a provider. The example assumes an existing BGP connection named `to-provider`:

```ros
/routing/rpki
add group=rpki1 address=192.0.2.10 port=8282

/routing/bgp/connection
set [find where name=to-provider] local.role=ebgp-customer

/routing/filter/rule
add chain=bgp_in rule="rpki-verify rpki1"
add chain=bgp_in rule="rpki-aspa-verify rpki1"
add chain=bgp_in rule="if (rpki invalid || rpki-aspa invalid) { reject } else { accept }"
```

The `rpki-verify` command selects the group for prefix origin validation. The `rpki-aspa-verify` command selects the group for ASPA validation. Both commands can use the same group.

### ASPA validation states

The `rpki-aspa` filter property and the [`rpki-aspa`](../../../cli-reference/routing/route.md#rpki-aspa) route attribute have the following values:

- `valid` - The AS path is consistent with the ASPA data.
- `invalid` - The AS path contains an unauthorized AS pair. The route is likely a route leak.
- `unknown` - The ASPA data does not cover at least one AS pair in the path.
- `unverified` - ASPA validation did not run, for example because the BGP session has no RFC 9234 role or the filter chain does not select an RPKI group for ASPA. The `/routing/route` output does not show the `rpki-aspa` attribute in this state.

Use the status in filters to accept or reject routes:

```ros
/routing/filter/rule
add chain=bgp_in rule="rpki-aspa-verify rpki1"
add chain=bgp_in rule="if (rpki-aspa invalid) { reject } else { accept }"
```

ASPA validation only provides the status. The filter rules define the action. The `else` branch accepts routes with the `valid`, `unknown`, and `unverified` status. Add stricter rules to handle those states according to your routing policy.

### Verify ASPA validation

Check the negotiated RTR version:

```ros
/routing/rpki/session print detail
```

Check the ASPA status of routes:

```ros
/routing/route print detail where rpki-aspa=invalid
```

The [`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md) and [`rpki-query`](../../../cli-reference/routing/rpki/rpki-query.md) commands check prefix origin data only. ASPA status depends on the complete AS path and the BGP role, so use the `rpki-aspa` route attribute or a filter rule to check it.
