# PPTP

> This page documents the PPTP (Point-to-Point Tunneling Protocol) implementation in MikroTik RouterOS, covering client and server configuration options including authentication methods, MTU/MRRU settings, and TCP port...

# PPTP

Point-to-Point Tunneling Protocol (PPTP) is a legacy VPN protocol designed to encapsulate PPP traffic for remote access connections. PPTP is widely supported by many operating systems and network devices, making it simple to deploy and configure in environments where compatibility is a priority.

Due to multiple known cryptographic and protocol-level vulnerabilities, PPTP is not considered secure for protecting sensitive or untrusted network traffic. Its use is generally limited to compatibility scenarios, testing environments, or networks where encryption strength is not a primary requirement.

PPTP does not support IPv6 transport or IPv6 traffic forwarding.

PPTP uses TCP port 1723 for tunnel management and Generic Routing Encapsulation (GRE, IP protocol 47) for data transport, as assigned by the Internet Assigned Numbers Authority (IANA). For PPTP to operate correctly through firewalls or routers, TCP port 1723 and GRE traffic must be permitted and properly forwarded.

PPTP supports PPP authentication, encryption, and accounting mechanisms for each client session. Authentication and accounting can be performed locally or through an external RADIUS server.

## Static and dynamic interfaces

An interface is created for each tunnel established to the server. There are two types of interfaces in the PPTP server's configuration:

- Static interfaces are added administratively when you need to reference a particular interface name (in firewall rules or elsewhere) created for a specific user.
- Dynamic interfaces are added to this list automatically when a user connects and their username does not match any existing static entry (or if the entry is already active, as there cannot be two separate tunnel interfaces referenced by the same name).

Dynamic interfaces appear when a user connects and disappear when the user disconnects, so it is impossible to reference the tunnel created for that user in router configuration (for example, in the firewall). If you need persistent rules for that user, create a static entry for that user. Otherwise, it is safe to use a dynamic configuration.

:::warning
In both cases PPP users must be configured properly — static entries do not replace PPP configuration.
:::

## Example

![](./img/pptp-01.webp)

### PPTP Client

The following example demonstrates how to set up a PPTP client with username "MT-User", password "StrongPass" and server 192.168.62.2:

```ros
[admin@MikroTik] > /interface/pptp-client/add connect-to=192.168.62.2 disabled=no name=pptp-out1 password=StrongPass user=MT-User
[admin@MikroTik] > /interface/pptp-client/print 
Flags: X - disabled; R - running 
 0  R name="pptp-out1" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.62.2 user="MT-User" 
      password="StrongPass" profile=default-encryption keepalive-timeout=60 add-default-route=no 
      dial-on-demand=no allow=pap,chap,mschap1,mschap2 
```

### PPTP Server

On the other side, enable the PPTP server and create a PPP secret for a particular user:

```ros
[admin@MikroTik] >  /interface/pptp-server/server/set enabled=yes
[admin@MikroTik] >  /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.5 service=pptp
[admin@MikroTik] >  interface pptp-server print
Flags: D - dynamic; R - running
Columns: NAME, USER, MTU, CLIENT-ADDRESS, UPTIME, ENCODING
#      NAME            USER     MTU  CLIENT-ADDRESS  UPTIM  ENCODING         
0  DR  <pptp-MT-User>  MT-User  1450  192.168.51.3   44m8s  MPPE128 stateless
```
