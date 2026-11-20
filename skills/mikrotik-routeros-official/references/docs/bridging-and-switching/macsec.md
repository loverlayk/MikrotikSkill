# MACsec

> Configure MACsec on RouterOS with manual CAK/CKN keys, direct and bridged links, cipher selection, MTU planning, monitoring, and troubleshooting.

# MACsec

Media Access Control Security (MACsec), defined by IEEE 802.1AE, protects Ethernet traffic with confidentiality, integrity and authenticity. After negotiation, MACsec protects Layer 2 payloads, including ARP, DHCP, LLDP and higher-layer protocols.

RouterOS can run MACsec in software without special hardware. Hardware offload is available only on selected ports and modules; the `H` flag indicates that offload is active.

:::warning
RouterOS requires manually configured Connectivity Association Keys (CAKs) and Connectivity Association Names (CKNs). It does not provision or rotate these values automatically through dot1x. The software, CPSS and Alaska MACsec paths do not provide replay protection.
:::

## Secure a direct link

This example creates a routed MACsec link between two routers. Each router uses `ether5` as the physical parent and a MACsec interface for IP traffic. Use a different parent if it is already your management interface, and remove that parent from any bridge first. Only one MACsec interface can exist on a parent.

On Router1, create the MACsec interface without CAK or CKN to generate random values:

```ros
/interface/macsec/add name=macsec1 interface=ether5
/ip/address/add address=192.0.2.1/24 interface=macsec1
/interface/macsec/print show-sensitive
```

On Router2, create an interface with the same CAK and CKN. The following values belong to this example only; use the values generated on your own router:

```ros
/interface/macsec/add name=macsec1 interface=ether5 \
    cak=30E8EE41D1127D738016A22475AC6459 \
    ckn=F5032E94636D5B68F3D31A9BB17A1F689B9EC4AD0EC6EC2C6E4BEC652112FD59
/ip/address/add address=192.0.2.2/24 interface=macsec1
```

After negotiation, `print show-sensitive` displays the generated values and the open status:

```text
Flags: R - RUNNING
1  R name="macsec1" mtu=1468 interface=ether5 status="open-encrypted"
     cak=30E8EE41D1127D738016A22475AC6459
     ckn=F5032E94636D5B68F3D31A9BB17A1F689B9EC4AD0EC6EC2C6E4BEC652112FD59
     profile=default
```

The CAK is sensitive. Protect configuration exports and terminal output that includes it.

Check the negotiated role and cipher:

```ros
/interface/macsec/monitor [find name=macsec1] once
```

```text
    key-server: yes        
  cipher-suite: aes-gcm-128
```

In this example, Router1 is the key server. With equal priorities, the lower MAC address determines that role.

Confirm routed connectivity:

```ros
/ping 192.0.2.2 count=3
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 192.0.2.2                                  56  64 558us     
    1 192.0.2.2                                  56  64 407us     
    2 192.0.2.2                                  56  64 363us     
    sent=3 received=3 packet-loss=0% min-rtt=363us avg-rtt=442us 
   max-rtt=558us 
```

## Bridge two MACsec links

In this topology, Host1 connects to Switch `ether2` and Host2 connects to Switch `ether3`. The switch has one independently keyed MACsec interface for each host and adds those interfaces to `bridge1`. Do not add the physical parent interfaces to the same bridge.

On Host1 and Host2, create MACsec without keys to generate independent values, then use `print show-sensitive` to read them:

```ros
# Host1
/interface/macsec/add name=macsec1 interface=ether2
/ip/address/add address=10.255.10.10/24 interface=macsec1

# Host2
/interface/macsec/add name=macsec1 interface=ether2
/ip/address/add address=10.255.10.20/24 interface=macsec1
```

Copy each host's CAK and CKN to the corresponding switch interface. These example values are not suitable for a production deployment:

```ros
# Switch: link to Host1
/interface/macsec/add name=macsec1 interface=ether2 \
    comment=Host1 \
    cak=7A5DF27E34AA7CDDCE49663FEB43B12C \
    ckn=A682055203B82FF163026274E3127DFF5EBBE5F8E1EAD9ED8BC2D3A606EC26EE

# Switch: link to Host2
/interface/macsec/add name=macsec2 interface=ether3 \
    comment=Host2 \
    cak=9ECB5F80D68594B80C1039F01A7A4BC7 \
    ckn=C3CB27F1FB0AB62FEE848536A7F45C4B173FC3DC6320AF60C662DCF1A71B962C
```

After both links reach `open-encrypted`, add only the MACsec interfaces to the bridge:

```ros
/interface/bridge/add name=bridge1 protocol-mode=none
/interface/bridge/port/add bridge=bridge1 interface=macsec1
/interface/bridge/port/add bridge=bridge1 interface=macsec2
```

Host1 can then reach Host2 through the encrypted bridge:

```ros
# Host1
/ping 10.255.10.20 count=5
```

```text
  SEQ HOST                                     SIZE TTL TIME       STATUS      
    0 10.255.10.20                               56  64 981us     
    1 10.255.10.20                               56  64 571us     
    2 10.255.10.20                               56  64 605us     
    3 10.255.10.20                               56  64 953us     
    4 10.255.10.20                               56  64 855us     
    sent=5 received=5 packet-loss=0% min-rtt=571us avg-rtt=793us 
   max-rtt=981us 
```

## Manage keys and ciphers

The CAK is 16 bytes (32 hexadecimal characters), and the CKN is 32 bytes (64 hexadecimal characters). If you omit either value, RouterOS generates it. Both ends need the same CAK and CKN; a mismatch leaves the link negotiating and prevents forwarding.

The MACsec Key Agreement (MKA) protocol elects a key server for each point-to-point connection and maintains peer liveness. The key server generates and distributes the Secure Association Key (SAK). Packet-number exhaustion triggers SA replacement. `aes-gcm-xpn-128` extends the packet-number space and reduces exhaustion-driven replacements; it does not eliminate them.

Profiles control the election and cipher suites:

- `server-priority` defaults to 10. A lower numeric value wins. Equal priorities use the lowest MAC address as the key server.
- `ciphers` must be specified for custom profiles. The built-in default profile uses `aes-gcm-128`. The other supported suite is `aes-gcm-xpn-128`; AES-GCM-256 is not supported.
- The key server selects the first common suite in its own profile order. Peers with no common suite cannot forward traffic. Check both ends: one side can report `open-encrypted` while the other remains `negotiating`.

Create an XPN profile on both routers and assign it to the MACsec interface:

```ros
/interface/macsec/profile/add name=site-xpn \
    ciphers=aes-gcm-xpn-128 server-priority=20
/interface/macsec/set [find name=macsec1] profile=site-xpn
```

Use a single matching suite for a deterministic configuration. When you list multiple suites, check the selected value with `/interface/macsec/monitor`.

## Plan MTU

MACsec adds 32 bytes. The read-only L2MTU is the parent interface's L2MTU minus those 32 bytes, and it cannot be changed directly. The default MACsec MTU is 1468, which fits a 1500-byte parent MTU.

To carry a 1500-byte inner IP packet, increase the physical MTU to 1532 and set the MACsec MTU to 1500 on both routers. Ensure that the physical L2MTU also has enough headroom:

```ros
/interface/ethernet/set [find default-name=ether5] mtu=1532
/interface/macsec/set [find name=macsec1] mtu=1500
```

Wait for `open-encrypted` after changing MTU, then test the required packet size:

```ros
/ping 192.0.2.2 size=1500 do-not-fragment
```

Insufficient L2MTU can silently drop traffic even when ping or MACsec negotiation succeeds. Test application-sized packets and every bridge in the path rather than relying on negotiation status alone.

## Monitor and troubleshoot

Use these commands to inspect negotiation, roles and detailed counters:

```ros
/interface/macsec/print detail
/interface/macsec/monitor [find name=macsec1] once
/interface/macsec/print stats
```

`open-encrypted` indicates local encrypted state, not successful peer negotiation or end-to-end forwarding. Check both peers and then work through the path:

1. **Compare CAK and CKN.** Different values prevent negotiation. Use `print show-sensitive` when reading them.
2. **Compare profiles.** Both peers need a common cipher suite. Check `cipher-suite` and `key-server` on both monitors.
3. **Check the parent.** A parent already in a bridge produces an invalid interface with `Interface is already a slave`. A second MACsec on the same parent is rejected with `interface already used`.
4. **Check MTU and L2MTU.** Small packets can pass while larger application traffic is dropped. Increase physical headroom or reduce the MACsec MTU.
5. **Check forwarding.** Test routed traffic, bridge traffic and non-IP discovery protocols separately. `/ip/neighbor/print` can help verify CDP, LLDP and MNDP through a MACsec bridge.

The detailed statistics include aggregate Secure Channel (SC) counters and per-Secure Association (SA) values. They cover encrypted/decrypted traffic, validation failures and other error conditions defined by IEEE 802.1AE. Reset all detailed counters when starting a new measurement:

```ros
/interface/macsec/reset-counters [find name=macsec1]
```

## Hardware offload

Software MACsec consumes CPU but requires no special MACsec hardware. Offload is optional and depends on the Ethernet port, pluggable module, board revision and cipher suite. XPN support is not available on every MACsec-capable port or module.

The `H` flag indicates active hardware offload; its absence does not prevent software forwarding. Do not infer offload support from the device family alone or assume that offloaded forwarding is always faster.

For all interface, profile, monitor and counter-reset details, see the [MACsec CLI reference](../cli-reference/interface/macsec/).
