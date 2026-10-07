# RPKI

> RouterOS supports RPKI for BGP prefix validation using the Resource Public Key Infrastructure, enabling secure route origin verification via RTR protocol. Configuration includes setting up RTR servers and applying...

# RPKI

RouterOS implements the Resource Public Key Infrastructure (RPKI) to Router Protocol defined in [`RFC 8210`](https://tools.ietf.org/html/rfc8210). RTR is a lightweight, low-memory protocol for retrieving prefix validation data from RPKI validators. See a validator setup example on the [RIPE blog](https://blog.apnic.net/2019/10/28/how-to-installing-an-rpki-validator/).

Configuration is available under [`/routing/rpki`](../../../cli-reference/routing/rpki/rpki.md).

## Basic Example

Assume your network has an RTR server at IP address `192.168.1.1`:

```ros
/routing/rpki
add group=myRpkiGroup address=192.168.1.1 port=8282 refresh-interval=20
```

The [`group`](../../../cli-reference/routing/rpki/rpki.md#group), [`address`](../../../cli-reference/routing/rpki/rpki.md#address), [`port`](../../../cli-reference/routing/rpki/rpki.md#port), and [`refresh-interval`](../../../cli-reference/routing/rpki/rpki.md#refresh-interval) parameters configure the RTR connection. Additional parameters include [`vrf`](../../../cli-reference/routing/rpki/rpki.md#vrf), [`preference`](../../../cli-reference/routing/rpki/rpki.md#preference), [`retry-interval`](../../../cli-reference/routing/rpki/rpki.md#retry-interval), and [`expire-interval`](../../../cli-reference/routing/rpki/rpki.md#expire-interval).

After the connection is established and the validator database is received, check prefix validity using [`rpki-check`](../../../cli-reference/routing/rpki/rpki-check.md):

```text
[admin@rack1_b33_CCR1036] /routing/rpki> rpki-check group=myRpkiGroup prfx=70.132.18.0/24 origin-as=16509
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
