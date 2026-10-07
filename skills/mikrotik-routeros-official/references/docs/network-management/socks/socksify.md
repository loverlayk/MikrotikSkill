# Socksify

> Socksify forwards traffic chosen by firewall NAT rules through an upstream SOCKS5 server, so applications without SOCKS support can use a SOCKS proxy. Includes a Tor proxy example.

# Socksify

Socksify forwards traffic selected by firewall rules through an upstream SOCKS5 server, for applications that do not support SOCKS themselves. A destination NAT rule with `action=socksify` redirects the matching connections to the service, and the service asks the SOCKS server to connect to the connection's original destination.

Multiple socksify services can be configured at once, each forwarding to its own upstream server, so different traffic classes can use different proxies.

Prerequisites:

- The upstream server must speak SOCKS5. The RouterOS SOCKS server works when set to `version=5`; with the default `version=4` a SOCKS5 client is refused.
- `socks5-server` accepts IPv4 addresses only.
- New records are created disabled. Changes to a record's settings apply after you disable and re-enable the record, not while it is running.
- The upstream credentials are visible as plain text in `print detail` output.

The service refuses to proxy connections to LAN destinations (RFC 1918 private addresses); the log shows `cannot socksify LAN destination` under the `socksify` topic.

:::warning
Select traffic for redirection carefully with the NAT rule matchers. Always exclude the router's own addresses with `dst-address-type=!local`: without it, a rule that matches too much redirects the router's own services (for example SSH or WebFig) to the proxy and cuts off management access.
:::

## Use in combination with a Tor proxy

Socksify can forward traffic through Tor for privacy. The configuration forwards HTTP and HTTPS traffic through the Tor SOCKS5 proxy server.

First create the socksify service:

```ros
/ip/socksify
add connection-timeout=10 disabled=no name=Tor_socksify socks5-port=9050 socks5-server=<TOR_SOCKS_PROXY_IP>
```

Then configure the firewall to socksify the selected traffic and allow it to the service:

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=952 protocol=tcp src-address=<SOCKS_CLIENT_IP>
/ip/firewall/nat
add action=socksify chain=dstnat dst-address-type=!local dst-port=80,443 protocol=tcp socksify-service=Tor_socksify src-address=<SOCKS_CLIENT_IP>
```

The input accept rule is needed because the redirected connections arrive at the router itself (port 952 of the socksify service); when the input filter drops traffic from clients, the service never sees them. The `dst-address-type=!local` matcher keeps traffic to the router's own addresses out of the proxy.

## Tor container and secure DNS tutorial

RouterOS can also run the Tor proxy in a container. When you use Tor for browsing the web, consider protecting your DNS requests as well.

For detailed, step-by-step instructions watch the [Tor container and secure DNS tutorial video](https://www.youtube.com/watch?v=ECRjxpb5IgE&lc=Ugy6V6EEAwyu2UC8ZJB4AaABAg).
