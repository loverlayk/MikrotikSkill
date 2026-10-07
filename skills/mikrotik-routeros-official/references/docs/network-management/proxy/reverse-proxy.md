# Reverse Proxy

> The RouterOS reverse proxy accepts HTTPS connections, selects a rule by the TLS server name and forwards the requests as HTTP to a server or container app behind the router.

# Reverse Proxy

**Sub-menu:** `/ip/reverse-proxy`

The reverse proxy makes web servers behind the router reachable over HTTPS by host name, without a destination NAT rule for each server. The router accepts HTTPS connections on port 443 and selects a rule by the host name the client requests. It terminates TLS with the certificate of that rule and forwards the requests as HTTP to the server of the rule. Several servers can share one public address and port, each with its own host name and certificate.

RouterOS also adds rules for container apps automatically.

All rule properties are described in the [`/ip/reverse-proxy`](../../cli-reference/ip/reverse-proxy) CLI reference.

:::info
The reverse proxy is not supported on SMIPS devices (hAP lite, hAP lite TC and hAP mini).
:::

## Configuration example

This example makes a web server at `192.168.88.10`, port 8080, reachable as `https://nas.example.com`.

Prerequisites:

- The DNS name `nas.example.com` resolves to the public address of the router.
- You have a certificate and private key for `nas.example.com`, for example from a public certificate authority, in the files `nas.crt` and `nas.key`.
- The web server accepts plain HTTP on port 8080.

Upload the two files to the router and import them as a certificate named `nas`:

```ros
/certificate/import file-name=nas.crt name=nas passphrase=""
/certificate/import file-name=nas.key passphrase=""
```

Add the rule:

```ros
/ip/reverse-proxy/add sni=nas.example.com ip-address=192.168.88.10 port=8080 certificate=nas
```

The default firewall configuration drops connections to the router that do not come from the LAN. Accept HTTPS in the input chain, before the default drop rule:

```ros
/ip/firewall/filter/add chain=input protocol=tcp dst-port=443 in-interface-list=WAN action=accept comment="reverse proxy" place-before=[find comment="defconf: drop all not coming from LAN"]
```

For more about input rules, see [Filter](../../firewall-and-quality-of-service/firewall/filter).

## Rule selection

The router compares the server name the client sends in the TLS handshake (Server Name Indication, SNI) with the `sni` of each enabled rule. The name must match exactly: a wildcard such as `*.example.com` matches nothing. When no rule matches, the router closes the connection.

## Certificates

The router presents the certificate of the matching rule to the client. When a rule has `certificate=none`, the router presents the certificate of the `reverse-proxy` service in [`/ip/service`](../../system-information-and-utilities/services) instead. Set the service certificate when one certificate, for example a wildcard certificate, covers the host names of several rules. When neither the rule nor the service has a certificate, the TLS handshake fails.

## Requests to the server

The router connects to the server from its own address and forwards each request as HTTP/1.1. It uses plain HTTP also when the server port is 443, so the server must accept HTTP on that port.

The router keeps the `Host` header of the request and adds headers that tell the server about the original client:

- `X-Forwarded-For` and `X-Real-Ip` - The address of the client.
- `X-Forwarded-Proto` - `https`.
- `X-Forwarded-Host` - The host name the client requested.
- `Forwarded` - The address of the router, the address of the client, the protocol and the host name, in the format of RFC 7239.

## Service port

The reverse proxy listens on the port of the `reverse-proxy` service in [`/ip/service`](../../system-information-and-utilities/services), 443 by default. The port is open only while at least one enabled rule exists.

:::warning
The HTTPS web service `www-ssl` also uses port 443 by default. When both services are enabled on the same port, the one that starts first gets the port, and the other one shows `cannot bind to port 443: Address in use`. After a reboot, `www-ssl` gets the port, so the reverse proxy stops working even if it worked before the reboot.

Keep `www-ssl` disabled, which is the default, or move it to another port:

```ros
/ip/service/set www-ssl port=8443
```

:::

## Container apps

[Container apps](../../containers/apps) with `use-https=yes`, the default, and a web interface get a dynamic reverse proxy rule, shown with the `D` flag. The `sni` of the rule is the host name of the app URL (`ui-url`), and the rule forwards to the web port of the app. The rule uses the certificate set in `/app/settings`.

## Troubleshooting

The reverse proxy writes its messages to the log with the `rproxy` topic:

```ros
/log/print where topics~"rproxy"
```

- `no matching rule for <name>, client: <address>:<port>` - The client requested a host name that no enabled rule has as its `sni`.
- `certificate missing for rule <sni>` - Neither the rule nor the `reverse-proxy` service has a certificate.

When the reverse proxy does not accept connections at all, check that at least one rule is enabled. Then check the `reverse-proxy` service in `/ip/service/print` for a `cannot bind to port` comment, which means that another service, typically `www-ssl`, uses the same port.
