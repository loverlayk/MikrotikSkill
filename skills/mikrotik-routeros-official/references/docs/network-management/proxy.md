# Proxy

> RouterOS has two web proxies: the web proxy forwards, filters and caches the web requests of clients on your network, and the reverse proxy makes web servers behind the router reachable over HTTPS by host name.

# Proxy

A proxy accepts a request from a client and connects to the server on the client's behalf. RouterOS has two proxies for web traffic, and they work in opposite directions:

| Proxy | Menu | Clients | Servers | Use it to |
| :-- | :-- | :-- | :-- | :-- |
| [Web proxy](./web-proxy) | `/ip/proxy` | On your network | On the internet | Filter and cache the web requests of your users, or send them through another proxy. |
| [Reverse proxy](./reverse-proxy) | `/ip/reverse-proxy` | On the internet | Behind the router | Make web servers behind the router reachable over HTTPS by host name. |

For applications other than web browsers, RouterOS also has a [SOCKS proxy](../socks) in `/ip/socks`.
