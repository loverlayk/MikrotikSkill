# OpenVPN

> OpenVPN in RouterOS: set up an OpenVPN server with a certificate, connect a RouterOS client, choose the cipher and the transport, require client certificates, push routes, export and import .ovpn files, open the...

# OpenVPN

OpenVPN is a VPN protocol that uses TLS. Clients exist for Linux, Windows, macOS and other systems, which makes it a common choice for remote access from computers and phones. RouterOS has its own implementation of an OpenVPN server and client.

- A tunnel carries routed IP traffic (`mode=ip`, known as `tun`) or Ethernet frames (`mode=ethernet`, known as `tap`).
- It runs over TCP or UDP, on port 1194 by default, with IPv4 and IPv6.
- The users and their settings are in the PPP user database or on a RADIUS server: see [PPP AAA](../authentication-authorization-accounting/ppp-aaa).

![Two remote clients connect to the office router and reach a host and a network behind it](./img/openvpn-01.webp)

## Limitations

RouterOS does not support all features of OpenVPN, and not all unsupported features are listed here. The most important ones:

- LZO compression. Compression is deprecated in OpenVPN and not recommended: tunnels with compression are open to the VORACLE attack.
- Cipher negotiation (NCP). The cipher must be set in the `.ovpn` file of a client that connects to a RouterOS server. The file that RouterOS exports has it.
- `tls-auth`, `tls-crypt` and `tls-crypt v2` work only in the RouterOS client, and only when the configuration is imported from a `.ovpn` file.

A password can have up to 1000 characters.

## Set up a server

The server needs a certificate. [Certificates](../authentication-authorization-accounting/certificates) explains how to create and sign one. In this example the certificate has the name `ovpn-server` and contains the address of the router, 203.0.113.1.

Add a pool, a profile and a user, and then the server:

```ros
/ip/pool/add name=vpn-pool ranges=10.0.0.10-10.0.0.100
/ppp/profile/add name=vpn local-address=10.0.0.1 \
    remote-address=vpn-pool
/ppp/secret/add name=alice password=Example-pass-1 profile=vpn \
    service=ovpn
/interface/ovpn-server/server/add name=ovpn-server1 \
    certificate=ovpn-server default-profile=vpn protocol=udp \
    auth=sha256 cipher=aes256-gcm disabled=no
```

- A new server allows only the ciphers `blowfish128` and `aes128-cbc`, and a RouterOS client uses `blowfish128` with `sha1` by default. These are old algorithms: set `cipher` and `auth` as in the example.
- A new server uses TCP. UDP has less overhead and is the usual choice.
- The certificates have dates. Set the [clock](../system-information-and-utilities/clock) of the server and of the clients correctly, for example with NTP, or the certificate check fails.

## Connect a RouterOS client

Add a client with the same protocol, cipher and authentication as the server:

```ros
/interface/ovpn-client/add name=ovpn-office connect-to=203.0.113.1 \
    protocol=udp auth=sha256 cipher=aes256-gcm \
    user=alice password=Example-pass-1 disabled=no
```

`/interface/ovpn-client/monitor ovpn-office once` shows `status: connected` and the algorithms in `encoding`, here `AES-256-GCM/SHA256`. The server adds a dynamic interface `<ovpn-alice>` for the user, and `/ppp/active` lists the user with the service `ovpn`.

- When the cipher or the authentication of the client is not allowed on the server, the client shows `terminating... - peer disconnected`.
- With a GCM cipher, `auth=null` also works, because the cipher authenticates the packets itself.
- To reach the networks behind the server, add routes on the client with the client interface as the gateway, or let the server push them.

## Check the server certificate and require client certificates

Without more settings, the client does not check the certificate of the server. To check it, import the certificate authority (CA) that signed it on the client as a trusted certificate and set:

```ros
/interface/ovpn-client/set ovpn-office verify-server-certificate=yes
```

The client then also checks that the address or name in `connect-to` is in the certificate.

The server can ask each client for a certificate. The client certificate must be signed by a CA that the server trusts:

```ros
/interface/ovpn-server/server/set [find name=ovpn-server1] \
    require-client-certificate=yes
```

```ros
/interface/ovpn-client/set ovpn-office certificate=ovpn-client
```

A client without a certificate is then refused with `TLS error: ssl: unknown certificate`.

## Push routes to the clients

The server can send routes to the clients, so that they do not need static routes. Each route is `network netmask gateway`, and several routes are separated with commas:

```ros
/interface/ovpn-server/server/set [find name=ovpn-server1] \
    push-routes="192.168.88.0 255.255.255.0 10.0.0.1"
```

The client adds the route when it connects:

```ros
[admin@Client] > /ip/route/print where gateway~"ovpn|10.0.0.1"
Flags: D - DYNAMIC; A - ACTIVE; c - CONNECT, v - VPN
Columns: DST-ADDRESS, GATEWAY, ROUTING-TABLE, DISTANCE
    DST-ADDRESS      GATEWAY      ROUTING-TABLE  DISTANCE
DAc 10.0.0.0/24      ovpn-office  main                  0
DAv 192.168.88.0/24  10.0.0.1     main                  1
```

- `push-routes` can have up to 1400 characters or 37 routes. `push-routes-ipv6` has the IPv6 routes, for example `push-routes-ipv6="fdaa::/64,2001:db8::/32"`.
- `redirect-gateway=def1` sends all traffic of the clients through the tunnel. The client adds the routes 0.0.0.0/1 and 128.0.0.0/1, which take precedence over its default route.
- `route-nopull=yes` on a RouterOS client ignores the routes of the server.

## Export a configuration file for other clients

`export-client-configuration` writes a `.ovpn` file that OpenVPN clients on computers and phones can import. It needs the CA certificate, a client certificate and its key as files, and the server must have `require-client-certificate=yes`. In this example `vpn-ca` is the CA that signed the server certificate and `ovpn-client` is a client certificate that this CA signed; make one client certificate for each user. Export the client certificate with its key first:

```ros
/certificate/export-certificate ovpn-client file-name=client1 \
    export-passphrase=Example-key-pass-1
/certificate/export-certificate vpn-ca file-name=vpn-ca
/interface/ovpn-server/server/export-client-configuration \
    server=ovpn-server1 server-address=203.0.113.1 \
    ca-certificate=vpn-ca.crt client-certificate=client1.crt \
    client-cert-key=client1.key
```

The command writes a file with a name such as `client1795166484.ovpn`. It has the address, the port, the protocol and the cipher of the server, and the three certificates. The users also need their user name and password: the file asks for them (`auth-user-pass`). Copy the file from the [files](../system-information-and-utilities/files) of the router.

The file has the private key of the client. Send it to the user in a safe way, and give the passphrase of the key in another way.

Two more example files, for a client and for an OpenVPN server on another system: [client-1.ovpn](pathname:///assets/291241994_client-1.ovpn), [server-1.conf](pathname:///assets/291241995_server-1.conf).

## Import a configuration file on a RouterOS client

A RouterOS client can be made from a `.ovpn` file. Copy the file to the router and import it with the user name, the password and the passphrase of the key:

```ros
/interface/ovpn-client/import-ovpn-configuration \
    file-name=office.ovpn ovpn-user=alice \
    ovpn-password=Example-pass-1 key-passphrase=Example-key-pass-1
```

- The command adds a disabled client interface with a name such as `ovpn-import1795166676`, and imports the certificates of the file. Check the settings and enable the interface.
- Import the file on a router that does not have its certificates yet. `skip-cert-import=yes` imports the settings without the certificates.
- A RouterOS client always sends a user name and a password. A server that authenticates with certificates only ignores them.

### TLS authentication keys

`tls-auth` and `tls-crypt` add a shared key that protects the TLS handshake. The RouterOS client supports them only through the import of a `.ovpn` file that has the key:

```text
key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
-----END OpenVPN Static key V1-----
</tls-auth>
```

For `tls-crypt` and `tls-crypt v2`, the other system needs `auth SHA256` and no `key-direction` in the server configuration, and `auth SHA256` with `key-direction 1` in the client configuration.

## Carry Ethernet frames

With `mode=ethernet` on the server and on the client, the tunnel carries Ethernet frames. The client gets an address with the netmask set in `netmask` of the server (24 by default).

## Allow OpenVPN in the firewall

The default firewall drops connections that come from the internet. Accept the port of the server before the default drop rule, with the protocol that the server uses:

```ros
/ip/firewall/filter/add chain=input action=accept protocol=udp \
    dst-port=1194 in-interface-list=WAN comment="accept OpenVPN" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

## Use a VRF

`vrf` of a server sets the VRF in which it listens for connections. The default is `main`.

```ros
/interface/ovpn-server/server/set [find name=ovpn-server1] vrf=vrf1
```

## Troubleshoot

`monitor` on the client shows the reason of a failed connection in `status`, and the log has the same text under the topic `ovpn`.

| Status of the client | What to check |
| :-- | :-- |
| `disconnected`, or it stays at `link established` | The server is not reached. Check the address, the port, that the client and the server use the same `protocol`, and the firewall of the server. With `verify-server-certificate=yes`, also check that the address in `connect-to` is in the certificate of the server. |
| `terminating... - peer disconnected` | The cipher or the authentication of the client is not allowed on the server. |
| `TLS error: ssl: no trusted CA certificate found` | `verify-server-certificate=yes` is set and the CA of the server is not a trusted certificate on the client. |
| `TLS error: ssl: unknown certificate` | The server requires a client certificate and the client has none. |

## Read more

- [`/interface/ovpn-server/server`](../cli-reference/interface/ovpn-server/server/), [`/interface/ovpn-server`](../cli-reference/interface/ovpn-server/), [`/interface/ovpn-client`](../cli-reference/interface/ovpn-client/)
- [PPP AAA](../authentication-authorization-accounting/ppp-aaa)
- [Certificates](../authentication-authorization-accounting/certificates)
