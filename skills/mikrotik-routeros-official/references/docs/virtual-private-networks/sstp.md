# SSTP

> SSTP provides secure remote access over HTTPS using TLS encryption, enabling VPN connections through firewalls and NAT devices. The page details SSTP client and server properties including authentication, encryption...

# SSTP

Secure Socket Tunneling Protocol (SSTP) encapsulates Point-to-Point Protocol (PPP) traffic within a Transport Layer Security (TLS) session to provide secure remote access over the internet. SSTP uses HTTPS over TCP port 443, allowing VPN traffic to pass through most firewalls, network address translation (NAT) devices, and proxy servers that typically permit standard web traffic.

SSTP supports strong encryption, authentication, and data integrity through TLS, helping protect transmitted data from interception or tampering. Because it relies on TCP, SSTP can provide reliable connections in unstable network conditions, although it introduces additional overhead compared to VPN protocols based on UDP.

SSTP is commonly used in environments where other VPN protocols, such as PPTP, L2TP/IPsec, or OpenVPN on non-standard ports, are blocked by network restrictions.

## Introduction

The SSTP connection mechanism:

![](./img/sstp-01.webp)

1. A TCP connection is established from client to server (by default on port 443).
2. SSL validates the server certificate. If a certificate is valid, a connection is established; otherwise, the connection is turned down (see the note below).
3. The client sends SSTP control packets within the HTTPS session which establishes the SSTP state machine on both sides.
4. PPP negotiation over SSTP. The client authenticates to the server and binds IP addresses to the SSTP interface.

The SSTP tunnel is now established and packet encapsulation can begin.

:::warning
Starting from v5.0beta2, SSTP does not require certificates to operate and can use any available authentication type. This feature works only between two MikroTik routers, as it is not in accordance with Microsoft standards. Otherwise, to establish secure tunnels, **mschap** authentication and client/server certificates from the same chain should be used.

**Warning:** TLS SNI support has been added starting with the 7.15beta10 version, the extension is added to client hello packets if the "Add SNI" checkbox is checked or set in CLI:

`/interface/sstp-client/set` add-sni=yes
:::

## Certificates

To set up a secure SSTP tunnel, certificates are required. On the server, authentication is done only by username and password, but on the client the server is authenticated with a server certificate. It is also used by the client to cryptographically bind SSL and PPP authentication — the client sends a special value over the SSTP connection to the server, derived from the key data generated during PPP authentication and the server certificate. This allows the server to check if both channels are secure.

If SSTP clients are on Windows PCs, the only way to set up a secure SSTP tunnel with a self-signed certificate is by importing the "server" certificate on the SSTP server and adding a CA certificate on the Windows PC in the [trusted root](https://technet.microsoft.com/en-us/library/dd458982.aspx).

:::warning
If your server certificate is issued by a CA which is already known to Windows, the Windows client works without any additional certificate imports into a trusted root.

**Caution:** RSA key length must be at least 472 bits if a certificate is used by SSTP. Shorter keys are considered security threats.
:::

A similar configuration on a RouterOS client is to import the CA certificate and enable the verify-server-certificate option. In this scenario, Man-in-the-Middle attacks are not possible.

Between two MikroTik routers, it is also possible to set up an insecure tunnel without certificates. In this case, data going through the SSTP tunnel uses anonymous DH and Man-in-the-Middle attacks are easily accomplished. This scenario is not compatible with Windows clients.

It is also possible to make a secure SSTP tunnel by adding additional authorization with a client certificate. Configuration requirements are:

- Certificates on both server and client.
- Verification options enabled on server and client.

This scenario is not possible with Windows clients, because there is no way to set up a client certificate on Windows.

#### Certificate Error Messages

When the SSL handshake fails, you see one of the following certificate errors:

- **Certificate is not yet valid** - notBefore certificate date is after the current time.
- **Certificate has expired** - certificate expiry date is before the current time.
- **Invalid certificate purpose** - the supplied certificate cannot be used for the specified purpose.
- **Self signed certificate in a chain** - the certificate chain could be built up with the untrusted certificates but the root could not be found locally.
- **Unable to get issuer certificate locally** - CA certificate is not imported locally.
- **Server's IP address does not match certificate** - server address verification is enabled, but the address provided in certificate does not match the server's address.

## Quick Example

![](./img/sstp-02.webp)

### SSTP Client

This example creates a simple SSTP client without a certificate:

```ros
[admin@MikroTik] > /interface/sstp-client/add connect-to=192.168.62.2 disabled=no name=sstp-out1 password=StrongPass profile=default-encryption user=MT-User
[admin@MikroTik] > /interface/sstp-client/print
```

Flags: X - disabled; R - running
 0  R name="sstp-out1" max-mtu=1500 max-mru=1500 mrru=disabled connect-to=192.168.62.2:443
      http-proxy=0.0.0.0:443 certificate=none verify-server-certificate=no
      verify-server-address-from-certificate=yes user="MT-User" password="StrongPass"
      profile=default-encryption keepalive-timeout=60 add-default-route=no dial-on-demand=no
      authentication=pap,chap,mschap1,mschap2 pfs=no tls-version=any

```

### SSTP Server

Configure a PPP secret for a particular user, then enable the SSTP server:

```ros
[admin@MikroTik] > /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass remote-address=10.0.0.5 service=sstp
[admin@MikroTik] > /interface/sstp-server/server/set default-profile=default-encryption enabled=yes
[admin@MikroTik] > /interface/sstp-server/server/print
                    enabled: yes
                       port: 443
                    max-mtu: 1500
                    max-mru: 1500
                       mrru: disabled
          keepalive-timeout: 60
            default-profile: default-encryption
             authentication: pap,chap,mschap1,mschap2
                certificate: none
  verify-client-certificate: no
                        pfs: no
                tls-version: any
```

:::info
In P2P setups the network address is the same as the other endpoint's local address.

**Important:** As with any other PPP tunnel, SSTP also supports BCP which allows it to bridge the SSTP tunnel with a local interface. For example, in setups where routers are connected to the Internet through ether1 and workstations and laptops are connected to ether2, both local networks are routed through the SSTP client and they are not in the same broadcast domain. BCP is used.
:::
