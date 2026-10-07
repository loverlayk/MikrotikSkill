# SOCKS

> The SOCKS proxy server in RouterOS: enable the server, restrict who can use it with the access list, authenticate clients with users, and monitor active proxied connections.

# SOCKS

SOCKS is a proxy protocol for TCP connections. A SOCKS-aware application connects to the proxy, names the destination it wants, and the proxy opens the connection and relays the data. Because the proxy makes the connection, applications that can reach the proxy can use destinations that firewall rules would otherwise block, and you control in one place which clients and destinations are allowed. SOCKS works with any TCP-based protocol, for example HTTP, FTP or SSH.

RouterOS includes a SOCKS server (in `/ip/socks`, this page) and the [Socksify](socksify) service for the opposite direction: forwarding traffic chosen by firewall rules through an upstream SOCKS server.

<DocCardList />

## Enable the server

The server is disabled by default. Set the protocol `version` and enable it:

```ros
/ip/socks/set version=5 enabled=yes
```

The default `version=4` accepts only SOCKS4 clients; SOCKS5 clients are refused. Choose `5` for SOCKS5 clients; password authentication also requires version 5.

With these settings the server listens on TCP port 1080 on all addresses of the router. Until you add access list rules, anyone who can reach this port can use the proxy.

## Access list

**Sub-menu:** `/ip/socks/access`

The access list controls which requests the server accepts. Rules are checked in order and the first matching rule decides. A request that matches no rule is **allowed**; an empty list allows everything. For a restrictive list, finish with a `deny` rule:

```ros
/ip/socks/access/add src-address=192.168.0.0/24 action=allow
/ip/socks/access/add action=deny
```

Besides addresses and ports, `dst-address` accepts a domain name, which matches only clients that request the destination by name.

:::warning
Secure the proxy with the access list or firewall rules. An open SOCKS proxy lets anyone route connections through the router, for example to abuse it for spam.
:::

## Users and authentication

**Sub-menu:** `/ip/socks/users`

With `/ip/socks/set auth-method=password`, clients must authenticate with a username and password of a user in the list; the connection is rejected when no users exist. Authentication uses the SOCKS5 username/password method:

```ros
/ip/socks/set version=5 auth-method=password
/ip/socks/users/add name=alice password=s3cret
```

New users are created enabled. Passwords are not shown in `print` output:

```ros
[admin@MikroTik] /ip/socks/users> print
Columns: NAME, ONLY-ONE
# NAME      ONLY-ONE
0 alice     no
```

## Monitor connections

**Sub-menu:** `/ip/socks/connections`

This read-only list shows the connections currently relayed by the server, with the client address, the requested destination and the byte counters. The `user` column shows the authenticated user, if any:

```ros
[admin@MikroTik] /ip/socks/connections> print detail
0  src-address=192.168.0.2:59264 dst-address=198.51.100.8:21 type=out
   tx=103 rx=737 user=alice
```

## Application example: FTP through the SOCKS server

Your network 192.168.0.0/24 is masqueraded behind a router with the addresses 203.0.113.104 and 192.168.0.1, and the firewall blocks direct FTP access:

```ros
[admin@MikroTik] /ip/firewall/nat> print
0   chain=srcnat action=masquerade src-address=192.168.0.0/24
[admin@MikroTik] /ip/firewall/filter> print
0   chain=forward action=drop protocol=tcp src-address=192.168.0.0/24
    dst-port=21
```

To allow the client 192.168.0.2 to reach an FTP server at 198.51.100.8 through the proxy, enable the server and add access rules: allow the client to connect to the FTP server's port 21 and to open passive data connections to it (high ports), then deny everything else:

```ros
[admin@MikroTik] /ip/socks> set enabled=yes version=5
[admin@MikroTik] /ip/socks> print
                  enabled: yes
                     port: 1080
  connection-idle-timeout: 2m
          max-connections: 200
                      vrf: main
                  version: 5
              auth-method: none
[admin@MikroTik] /ip/socks> access/add src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=21 action=allow
[admin@MikroTik] /ip/socks> access/add src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=1024-65535 action=allow
[admin@MikroTik] /ip/socks> access/add action=deny
[admin@MikroTik] /ip/socks> access/print
0   src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=21 action=allow

1   src-address=192.168.0.2 dst-address=198.51.100.8 dst-port=1024-65535 action=allow

2   action=deny
```

While the transfer runs, the control and the passive-data connections show in the connection list described in the previous section.

Configure the FTP client to use SOCKS with the router's address 192.168.0.1 and TCP port 1080.
