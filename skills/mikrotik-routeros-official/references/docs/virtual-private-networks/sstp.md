# SSTP

> SSTP in RouterOS: set up an SSTP server and client, secure the tunnel with a server certificate, require client certificates, choose the TLS settings, open the firewall, and find why a client does not connect.

# SSTP

The Secure Socket Tunneling Protocol (SSTP) carries a PPP link inside a TLS session. It uses TCP port 443, the port of HTTPS, so it passes most firewalls, NAT devices and web proxies. Use SSTP where networks block other VPN protocols.

- The users and their settings are in the PPP user database or on a RADIUS server: see [PPP AAA](../authentication-authorization-accounting/ppp-aaa).
- SSTP runs over TCP. It is reliable on a bad link, but it has more overhead than a VPN protocol that uses UDP.
- Microsoft Windows has an SSTP client.

A connection is made in four steps:

![The four steps of an SSTP connection between a client and a server](./img/sstp-01.webp)

1. The client opens a TCP connection to the server, to port 443 by default.
2. TLS starts, and the client checks the certificate of the server if it is set to do so.
3. The client sends SSTP control packets inside the HTTPS session, and both sides set up the SSTP connection.
4. PPP starts over SSTP: the client authenticates and the link gets its addresses.

## Set up a server and a client

![An SSTP client connects to an SSTP server over the internet](./img/sstp-02.webp)

On the server, add a pool, a profile and a user, and enable the SSTP server:

```ros
/ip/pool/add name=vpn-pool ranges=10.0.0.10-10.0.0.100
/ppp/profile/add name=vpn local-address=10.0.0.1 \
    remote-address=vpn-pool
/ppp/secret/add name=alice password=Example-pass-1 profile=vpn \
    service=sstp
/interface/sstp-server/server/set enabled=yes default-profile=vpn
```

On a RouterOS client, add an SSTP client with the address of the server:

```ros
/interface/sstp-client/add name=sstp-office connect-to=203.0.113.1 \
    user=alice password=Example-pass-1 disabled=no
```

```ros
[admin@Client] > /interface/sstp-client/monitor sstp-office once
               status: connected            
               uptime: 11s                  
             encoding: AES256-CBC           
                  mtu: 1500                 
        local-address: 10.0.0.99            
       remote-address: 10.0.0.1             
   local-ipv6-address: fe80::885c:c65:0:8   
  remote-ipv6-address: fe80::c17c:122c:f0:18
```

The server adds a dynamic interface for the user:

```ros
[admin@Server] > /interface/sstp-server/print detail
Flags: D - DYNAMIC; R - RUNNING
0 DR name="<sstp-alice>" user="alice" mtu=1500 client-address="203.0.113.2"
     uptime=12s encoding="AES256-CBC"
```

:::warning
This tunnel has no certificates. It works only between two RouterOS devices, and it is encrypted but not protected against an attacker in the path, who can pretend to be the server. Use a server certificate for a tunnel over the internet.
:::

## Secure the tunnel with a server certificate

With a certificate, the client can check that it talks to the right server. The server needs a certificate with its address or DNS name, and the client needs the certificate authority (CA) that signed it. [Certificates](../authentication-authorization-accounting/certificates) explains how to create, sign, export and import certificates. In this example the server certificate has the name `sstp-server` and contains the address 203.0.113.1.

On the server, set the certificate:

```ros
/interface/sstp-server/server/set certificate=sstp-server
```

On the client, import the CA certificate as a trusted certificate and turn the check on:

```ros
/interface/sstp-client/set sstp-office verify-server-certificate=yes
```

- The client connects only when a trusted CA signed the certificate of the server.
- With `verify-server-address-from-certificate=yes` (the default), the address or name in `connect-to` must also be in the certificate.
- The client uses the certificate to bind the TLS session to the PPP authentication, and this lets the server check that both are secure. For this, use MS-CHAPv2 authentication.
- A Windows client always checks the server certificate. A certificate from a CA that Windows already trusts works at once. For your own CA, import the CA certificate into the trusted root store of the Windows computer.
- The RSA key of a certificate for SSTP must have at least 472 bits.
- `add-sni=yes` on the client adds the server name (TLS SNI) to the first TLS packet.

## Require a client certificate

The server can also ask each client for a certificate. Give the client a certificate that the CA of the server trusts, with its private key:

```ros
/interface/sstp-client/set sstp-office certificate=sstp-client
```

On the server, the CA must be a trusted certificate. Turn the check on:

```ros
/interface/sstp-server/server/set verify-client-certificate=yes
```

A client without a certificate is then refused, and the log of the server has `ssl: empty certificate chain received`. A Windows client cannot send a client certificate, so this setup is for RouterOS clients.

## Choose the TLS settings

- `tls-version` on the server and on the client: `any`, `only-1.2`, `only-1.3`, `min-1.2` or `min-1.3`.
- `pfs` selects the key exchange. `yes` uses ECDHE-RSA and DHE-RSA, which give perfect forward secrecy, and `required` uses only ECDHE.
- `ciphers` selects the encryption algorithms.
- `port` of the server and of the client changes the TCP port.
- `http-proxy` and `proxy-port` of the client connect through a web proxy.

Use settings that both sides allow, for example `tls-version=only-1.2 pfs=yes` on the server and on the client.

## Allow SSTP in the firewall

The default firewall drops connections that come from the internet. Accept the port of the SSTP server before the default drop rule:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=tcp \
    dst-port=443 in-interface-list=WAN comment="accept SSTP" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

## Bridge Ethernet over the tunnel

As other PPP tunnels, SSTP can carry Ethernet frames with the Bridge Control Protocol (BCP), so that the networks on both sides are one layer 2 network. Set `bridge` in the PPP profile on both sides: see [L2TP](l2tp/) for the steps.

## Troubleshoot

A RouterOS client writes the reason of a failed connection to its log. In this output the client connected to another address of the server than the one in the certificate:

```ros
[admin@Client] > /log/print where topics~"sstp"
 2026-11-20 09:11:23 sstp,ppp,info sstp-office: terminating... - ssl: name verification failed for: "CN=203.0.113.1" (6)
 2026-11-20 09:11:23 sstp,ppp,info sstp-office: disconnected
```

| Message | Meaning |
| :-- | :-- |
| `name verification failed` | The address or name in `connect-to` is not in the certificate of the server. Connect by the name in the certificate, or set `verify-server-address-from-certificate=no`. |
| `empty certificate chain received` (on the server) | The server asks for a client certificate and the client has none. |
| `Certificate is not yet valid` | The start date of the certificate is in the future. Check the clock of the router. |
| `Certificate has expired` | The end date of the certificate is in the past. Check the clock of the router. |
| `Invalid certificate purpose` | The certificate cannot be used for this purpose. |
| `Self signed certificate in a chain` | The certificate chain has no trusted root on this router. |
| `Unable to get issuer certificate locally` | The CA certificate is not imported on this router. |

When the client stays `disconnected` without a message, check that the CA certificate on the client is trusted, that the firewall of the server accepts the port, and that the user name and the password are right.

## Read more

- [`/interface/sstp-server/server`](../cli-reference/interface/sstp-server/server), [`/interface/sstp-server`](../cli-reference/interface/sstp-server/), [`/interface/sstp-client`](../cli-reference/interface/sstp-client/)
- [PPP AAA](../authentication-authorization-accounting/ppp-aaa)
- [Certificates](../authentication-authorization-accounting/certificates)
- [L2TP](l2tp/)
