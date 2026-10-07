# OpenVPN

> OpenVPN is a secure VPN protocol offering Layer 2/3 tunneling, IPv4/IPv6 support, and flexible transport protocols (UDP/TCP). It supports client-server deployments with configurable authentication, encryption...

# OpenVPN

OpenVPN is a VPN protocol based on the SSL/TLS security model, widely used to provide secure remote access and site-to-site connectivity over untrusted networks. It supports both Layer 2 and Layer 3 tunneling modes, enabling the transport of Ethernet frames or routed IP traffic depending on deployment requirements.

OpenVPN supports both IPv4 and IPv6 traffic and can operate across a wide range of network topologies.

OpenVPN is available on multiple platforms, including Linux, Windows, macOS, and other operating systems. Its configuration structure is generally consistent across platforms, simplifying deployment, maintenance, and interoperability in mixed environments.

OpenVPN can operate over either User Datagram Protocol (UDP) or Transmission Control Protocol (TCP), allowing administrators to select the transport protocol best suited for their network requirements. Multiple VPN sessions can be multiplexed over a single TCP or UDP port.

OpenVPN can also operate through HTTP and SOCKS proxy servers, which can help in network environments with restricted outbound connectivity. Its flexibility, strong cryptographic support, and broad platform compatibility make OpenVPN a commonly deployed VPN solution.

## Limitations

ROS has its own OpenVPN implementation but not all features are supported, and not all unsupported features are listed. Notable unsupported features include:

- LZO compression (**deprecated**). Compression is generally not recommended. VPN tunnels that use compression are vulnerable to the VORACLE attack.
- NCP autonegotiation. The cipher must be specified in the `.ovpn` file when connecting to an ROS OpenVPN server.

OpenVPN usernames are limited to 27 characters, and passwords are limited to 1000 characters.

## tls-crypt, tls-crypt v2

To improve TLS authentication, `tls-crypt` support was added in version `7.17rc3`.

`tls-crypt` and `tls-crypt v2` are supported only by the OVPN client with the following settings:

- `auth SHA256` and no `key-direction` in the server configuration.
- `auth SHA256` and `key-direction 1` in the client configuration.

## Example configuration files

[client-1.ovpn](pathname:///assets/291241994_client-1.ovpn)
[server-1.conf](pathname:///assets/291241995_server-1.conf)

## Example

### Setup Overview

![](./img/openvpn-01.webp)

Assume that the office public IP address is `2.2.2.2`, and two remote OVPN clients need access to the `10.5.8.20` host and the `192.168.55.0/24` network located behind the office gateway.

### Creating Certificates

All certificates can be created on the RouterOS server with the certificate manager. [See example >>](../authentication-authorization-accounting/certificates.md)

For the simplest setup, only an OVPN server certificate is required.

### Server Config

The first step is to create an IP pool from which client addresses are assigned, then create user accounts.

```ros
/ip/pool/add name=ovpn-pool range=192.168.77.2-192.168.77.254

/ppp/profile/add name=ovpn local-address=192.168.77.1 remote-address=ovpn-pool
/ppp/secret
add name=client1 password=123 profile=ovpn
add name=client2 password=234 profile=ovpn
```

Assume that the server certificate has already been created and is named `server`.

```ros
/interface/ovpn-server/server/add disabled=no certificate=server name=myServer
```

It is also possible to prepare a `.ovpn` file for the OVPN client, which can be easily imported on the end device. **The server must have the required client certificate option enabled for export to work.**

```ros
/interface/ovpn-server/server/export-client-configuration ca-certificate=ca.crt  client-certificate=cert_e
xport_rw-client.crt  client-cert-key=cert_export_rw-client.key server-address=1.1.1.1 server=ovpn-server1 
```

:::info
Ensure that the router date is within the validity period of the installed certificate. To avoid certificate verification issues, enable **NTP** date synchronization on both the server and the client.
:::

### Client Config

Manually add which networks you want to access over the tunnel.

```ros
/interface/ovpn-client
add name=ovpn-client1 connect-to=2.2.2.2 user=client1 password=123 disabled=no
/ip/route 
add dst-address=10.5.8.20 gateway=ovpn-client1
add dst-address=192.168.55.0/24 gateway=ovpn-client1
/ip/firewall/nat/add chain=srcnat action=masquerade out-interface=ovpn-client1
```

It is also possible to import the OVPN client configuration from a `.ovpn` configuration file. This file is usually provided by the OVPN server and already contains the required configuration, so only a few parameters need to be configured manually.

```ros
/interface/ovpn-client/import-ovpn-configuration ovpn-password=securepassword \
key-passphrase=certificatekeypassphrase ovpn-user=myuserid skip-cert-import=no 
```

OVPN client supports TLS authentication. The `tls-auth` configuration can only be added by importing a `.ovpn` configuration file. tls-auth requires generating a shared secret key, which must be included in the client `.ovpn` configuration file.

ROS client requires a username and password. Authentication is managed by the server side. If the server supports TLS authentication, the username is ignored.

```ros
key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
-----END OpenVPN Static key V1-----
</tls-auth>
```

```
non-null auth in GCM mode is supported.
```

### Push Route

Push route support was added in version `7.14`. The maximum input is limited to 1400 characters or 37 routes. IPv6 support was added in version `7.21_ab220`.
Example: `route network/IP [netmask] [gateway] [metric]`.

```ros
/interface/ovpn-server/server/set 0 push-routes-ipv6="fdaa::/64,2001:db8::/32"
```

### VRF support

Support was added starting from version 7.17, and several configuration changes were introduced. If you are using the latest version, refer to this example:

```ros
      /interface/ovpn-server/server
        add disabled=no certificate=yourcert auth=sha1 cipher=aes128-cbc require-client-certificate=yes protocol=tcp name=ovpn-server1 vrf=main
```
