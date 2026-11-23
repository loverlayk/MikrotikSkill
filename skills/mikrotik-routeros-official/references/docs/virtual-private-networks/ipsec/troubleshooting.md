# Troubleshooting

> Troubleshooting IPsec in RouterOS: where to look, what the log messages mean, and how to solve tunnels that do not come up, tunnels without traffic, slow connections and XFRM problems.

# Troubleshooting

## Where to look

Check a tunnel in this order:

1. `/ip/ipsec/active-peers/print` - is the IKE connection (phase 1) `established`? `PH2-TOTAL` shows the number of phase 2 SAs.
2. `/ip/ipsec/installed-sa/print` - are there SAs for both directions? The flag `S` shows that an SA has carried traffic.
3. `/ip/ipsec/policy/print detail` - does a policy exist for the traffic? A dynamic policy shows `ph2-state=established`.
4. `/ip/ipsec/statistics/print` - counters of the errors of the encryption itself.
5. `/log/print where topics~"ipsec"` - what happened and why.

The log has more detail when all messages of the `ipsec` topic except the debug messages are logged. Remove the rule when you are done:

```ros
/system/logging/add topics=ipsec,!debug
/system/logging/remove [find topics~"ipsec"]
```

## Messages in the log

| Message | Meaning |
| :-- | :-- |
| `got fatal error: AUTHENTICATION_FAILED` on one side, `peer failed to authorize` on the other | The pre-shared keys are different. |
| `no proposal chosen` | The algorithms of the two sides do not match. The peer is `established` and `PH2-TOTAL` is empty: compare the proposals (phase 2): encryption, authentication and PFS group. |
| No clear message, and the peer is never `established` | Compare the profiles (phase 1): encryption, hash and DH group must have a common value on both sides. |
| `can't get private key` | The certificate of the identity has no private key on this router. Check that the identity names the right certificate: after the import of a PKCS12 file, the client certificate and the CA certificate can have the same name. |
| `phase1 negotiation failed due to time up` | The two sides cannot talk to each other. See the section about it on this page. |
| `fatal NO-PROPOSAL-CHOSEN notify message` | The other side cannot accept the proposed algorithms. Look at the log or the configuration of the other side, and check that both have the same set of algorithms. |

### No valid proposal with IKEv1

With the exchange modes of IKEv1, a phase 1 mismatch looks like this:

```ros
[admin@MikroTik] /log> print
(..)
17:12:32 ipsec,error no suitable proposal found. 
17:12:32 ipsec,error 10.5.107.112 failed to get valid proposal. 
17:12:32 ipsec,error 10.5.107.112 failed to pre-process ph1 packet (side: 1, status 1). 
17:12:32 ipsec,error 10.5.107.112 phase1 negotiation failed. 
(..)
```

With the IPsec debug messages logged, the log shows which settings were refused:

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

In this example the other side requires SHA1 as the hash algorithm, but MD5 is configured on the local router. In each pair, the value before the colon (:) is the local setting and the value after it is the setting of the other side.

## The tunnel does not come up

### "phase1 negotiation failed due to time up"

The two sides cannot exchange IKE packets. Possible causes:

- The address of the peer is wrong.
- A firewall drops UDP port 500 or 4500: see [Firewall and routing for IPsec](firewall-and-routing).
- NAT between the two sides does not pass the IKE packets correctly.
- `local-address` of the peer does not fit the link that the packets leave on: see [Firewall and routing for IPsec](firewall-and-routing).

### How to use IKEv2

Set `exchange-mode=ike2` in the peer on both sides.

### strongSwan: "initiator did not reauthenticate as requested"

RouterOS does not support IKEv2 reauthentication (RFC 4478). Disable reauthentication in strongSwan.

## The tunnel is up, but traffic does not pass

### No traffic at all

Check that NAT does not change the packets before IPsec sees them. With a masquerade rule and no bypass rule, the peer is `established` but the packets do not match the policy: see [Site-to-site tunnel](site-to-site).

When you test from the router itself, ping from an address of the local network (`src-address`). A ping from the public address of the router does not match a policy between two local networks.

### Ping works in one direction only

A firewall accepts new connections in one direction only. Check the filter rules, or accept all traffic that comes out of and goes into the tunnel (`ipsec-policy=in,ipsec` and `ipsec-policy=out,ipsec`).

### Packets are lost or connections are very slow, and the packet sniffer or Torch makes the problem go away

FastTrack or FastPath takes the packets before they are encrypted, so they do not pass the IPsec policies. Leave the traffic of the tunnel out of FastTrack: see [Site-to-site tunnel](site-to-site).

### Only encrypted traffic must be accepted

See [Firewall and routing for IPsec](firewall-and-routing).

## XFRM interfaces

### The XFRM interface does not come up

The flag `R` appears only after an SA that uses the interface is made. If the SA is made but the interface stays down, re-create the interface or restart the router. An IP address on the interface is shown as invalid until the interface runs.

### The XFRM policy stays in no-phase2

Check that the policy group is bound to the XFRM interface, that the identity has the same group in `policy-template-group`, and that the traffic is routed through the XFRM interface. If you use the default policy group, check that no other policy of the group takes the traffic.

### OSPF over XFRM stays in ExStart

The XFRM interfaces of both routers must have the same MTU. Check `actual-mtu` with `/interface/print detail` on both routers and set `mtu` again if the values differ. With different values, the OSPF database description exchange cannot finish.

## Read more

- [IPsec](./): how IKE works, the menus, the algorithms
- [Site-to-site tunnel](site-to-site)
- [Firewall and routing for IPsec](firewall-and-routing)
- [Route-based IPsec with XFRM](route-based-ipsec-xfrm)
