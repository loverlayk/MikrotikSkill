# MLPPP over single and multiple links

> Multilink PPP in RouterOS: use MRRU on a single PPP link to carry full-size packets without lowering the TCP MSS, and join several PPPoE links to one provider into a single connection.

# MLPPP over single and multiple links

Multilink PPP (MP, MLPPP, [RFC 1990](https://tools.ietf.org/html/rfc1990)) splits packets into fragments, sends them over one or more PPP links, and joins them again on the other side. Both sides must support it: they agree on it with an LCP option when the link starts. RouterOS uses it in two ways:

- On a single link, to carry packets that are larger than the MTU of the link.
- On several links to the same server, to use them as one connection.

## MLPPP over a single link

A PPP link has a lower MTU than Ethernet: 1492 bytes for PPPoE, for example. With the Maximum Received Reconstructed Unit (`mrru`) set on both sides, the link splits larger packets and the other side joins them, so full 1500-byte packets pass.

Set `mrru` on the server and on the client:

```ros
/interface/pppoe-server/server/set [find service-name=internet] \
    mrru=1600
```

```ros
/interface/pppoe-client/set pppoe-out1 mrru=1600
```

After the client connects again, `monitor` shows a larger MTU for the link (1596 with `mrru=1600`), and a 1500-byte packet that must not be fragmented passes.

- With MRRU on both sides, the TCP MSS does not have to be lowered with a firewall mangle rule, and MRRU needs less CPU than two mangle rules for each client.
- `mrru` can be up to 65535 bytes.
- Windows calls this "Negotiate multi-link for single link connections", in the settings of the Networking tab of the connection. Its MRRU is always 1614, so use `mrru=1614` on a server for Windows clients.
- With MPPE encryption, the MTU of the link is 4 bytes lower.

## MLPPP over multiple links

A PPPoE client can use several physical links to one provider as a single connection, for example two DSL lines. All links must end on the same server, the server must support MLPPP over multiple links, and all links use the same user name and password.

RouterOS supports this as a client only. A RouterOS PPPoE server does not join several links.

![A router is connected to the internet provider with two links](./img/mlppp-over-single-and-multiple-links-01.webp)

Name all the interfaces in `interface` of the client:

```ros
/interface/pppoe-client/add name=pppoe-out1 service-name=ISP \
    interface=ether1,ether2 user=alice password=Example-pass-1 \
    add-default-route=yes use-peer-dns=yes disabled=no
```

`active-links` in the output of `/interface/pppoe-client/monitor` shows how many links the connection uses. If it is 1 with two interfaces, the server does not support MLPPP over multiple links.

The rest of the configuration is the same as for a client on one link: the PPPoE client interface is the WAN interface of the router. See [PPPoE](./) and, for the firewall, [Filter](../../firewall-and-quality-of-service/firewall/filter).

## Read more

- [`/interface/pppoe-client`](../../cli-reference/interface/pppoe-client/), [`/interface/pppoe-server/server`](../../cli-reference/interface/pppoe-server/server)
- [PPPoE](./)
