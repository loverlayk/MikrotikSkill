# Virtual Private Networks

> The VPN and tunnel types of RouterOS and when to use each: WireGuard, IPsec, L2TP, SSTP, OpenVPN, PPPoE, GRE, IPIP, EoIP, 6to4, ZeroTier and PPTP.

# Virtual Private Networks

RouterOS has several ways to connect networks and remote users over another network. Some encrypt the traffic and some only carry it, so choose by what you need:

| You want to | Use |
| :-- | :-- |
| Connect two sites or remote users with strong encryption and little configuration | [WireGuard](wireguard) |
| Connect to devices and services of other vendors with a standard, encrypted VPN | [IPsec](ipsec/) |
| Give remote users access with a user name and a password, with clients that are built into Windows and other systems | [L2TP](l2tp/) with IPsec, or [SSTP](sstp) |
| Give remote users access where only web traffic passes the firewalls | [SSTP](sstp), or [OpenVPN](openvpn) over TCP |
| Serve or connect OpenVPN clients | [OpenVPN](openvpn) |
| Connect subscribers on an Ethernet network, or connect to an internet provider | [PPPoE](pppoe/) |
| Carry IP packets between two routers without encryption, or with IPsec added | [GRE](gre), [IPIP](ipip) |
| Carry Ethernet frames between two sites | [EoIP](eoip), or L2TP Ether on the [L2TP](l2tp/) page |
| Carry IPv6 over an IPv4 network | [6to4](6to4) |
| Join a ZeroTier network | [ZeroTier](zerotier) |
| Host your own ZeroTier network on a router | [Self-hosted ZeroTier controller](zerotier-controller) |

[PPTP](pptp) is an old protocol with weak encryption. Use it only for devices that have nothing else.

The users of the L2TP, SSTP, OpenVPN, PPPoE and PPTP servers are in one database: see [PPP AAA](../authentication-authorization-accounting/ppp-aaa).

<DocCardList />
