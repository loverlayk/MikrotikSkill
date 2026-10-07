# HotSpot - Captive portal

> The MikroTik HotSpot Gateway enables client authentication for public networks with features like DHCP address pools, multiple authentication methods, and walled-garden access. It requires IPv4 and has specific...

# HotSpot - Captive portal

The MikroTik HotSpot Gateway provides authentication for clients before access to public networks.

:::warning
HotSpot (captive portal) - uses web-proxy and it is capable of using only the default routing table, at the moment, making the PCC(per connection-classifier) not a valid method, due to the multiple routing tables used.
:::

:::warning
HotSpot functionality could be blocked by the device-mode. Prior to configuring HotSpot, make sure that it is enabled in `/system/device-mode` ([more info](../../system-information-and-utilities/device-mode.md).
:::

### HotSpot Properties

| Property | Description |
| :--- | :--- |
| **name** | Descriptive name for the HotSpot server instance. |
| **interface** | The specific local interface (physical or virtual) where the HotSpot service will listen for client requests. |
| **address-pool** | The IP address pool from which HotSpot clients will receive their IP addresses via DHCP. |
| **profile** | Reference to the HotSpot Server Profile containing common settings like login methods and HTML directory. |
| **idle-timeout** | The period of inactivity after which a client is automatically logged out if no traffic is detected. |
| **keepalive-timeout** | The time interval used to check if the client is still reachable; if the client does not respond, the session is terminated. |
| **login-timeout** | The maximum duration allowed for a client to complete the authentication process after the login page is displayed. |
| **addresses-per-mac** | Limits the number of IP addresses that can be associated with a single MAC address. |
| **proxy-status** | Indicates the current operational state of the internal web-proxy used by the HotSpot system. |

### HotSpot Gateway features

- Different authentication methods of clients, using a local client database on the router, or a remote RADIUS server.
- User accounting in a local database on the router, or on a remote RADIUS server.
- A walled-garden system, access to some web pages without authorization.
- Login page modification, where you can put information about the company.
- Automatic and transparent change of any IP address of a client to a valid address.
- HotSpot can inform DHCP clients that they are behind a captive portal (RFC7710).

A HotSpot can work reliably only when IPv4 is used. HotSpot relies on Firewall NAT rules which currently are not supported for IPv6.

## Example

```ros
[admin@MikroTik] /ip/hotspot> setup 
Select interface to run HotSpot on 

hotspot interface: ether3
Set HotSpot address for interface 

local address of network: 10.5.50.1/24
masquerade network: yes
Set pool for HotSpot addresses 

address pool of network: 10.5.50.2-10.5.50.254
Select hotspot SSL certificate 

select certificate: none
Select SMTP server 

ip address of smtp server: 0.0.0.0
Setup DNS configuration 

dns servers: 10.1.101.1
DNS name of local hotspot server 

dns name: myhotspot
Create local hotspot user 

name of local hotspot user: admin
password for the user: 
[admin@MikroTik] /ip/hotspot>
```

## Verify HotSpot configuration

```ros
[admin@MikroTik] /ip/hotspot> print 
Flags: X - disabled, I - invalid, S - HTTPS 
# NAME INTERFACE ADDRESS-POOL PROFILE IDLE-TIMEOUT
0 hotspot1 ether3 hs-pool-3 hsprof1 5m 
[admin@MikroTik] /ip/hotspot> 
[admin@MikroTik] /ip/pool> print 
# NAME RANGES 
0 hs-pool-3 10.5.50.2-10.5.50.254 
[admin@MikroTik] /ip/pool> /ip/dhcp-server 
[admin@MikroTik] /ip/dhcp-server> print 
Flags: X - disabled, I - invalid 
# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP
0 dhcp1 ether3 hs-pool-3 1h 
[admin@MikroTik] /ip/dhcp-server> /ip/firewall/nat 
[admin@MikroTik] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 X ;;; place hotspot rules here
chain=unused-hs-chain action=passthrough 

1 ;;; masquerade hotspot network
chain=srcnat action=masquerade src-address=10.5.50.0/24 
[admin@MikroTik] /ip/firewall/nat> 
```

### **Parameters asked during the setup process**

| Parameter | Description |
| :-- | :-- |
| **hotspot interface** (*string*; Default: **allow**) | Interface name on which to run HotSpot. To run HotSpot on a bridge interface, make sure public interfaces are not included in the bridge ports. |
| **local address of network** (*IP*; Default: **10.5.50.1/24**) | HotSpot gateway address |
| **masquerade network** (*yes \| no*; Default: **yes**) | Whether to masquerade HotSpot network, when **yes**, a rule is added to *`/ip/firewall/nat`* with *action=masquerade* |
| **address pool of network** (*string*; Default: **yes**) | Address pool for HotSpot network, which is used to change user IP address to a valid address. Useful if providing network access to mobile clients that are not willing to change their networking settings. |
| **select certificate** (*none \| import-other-certificate*; Default: ) | Choose an SSL certificate, when the HTTPS authorization method is required. |
| **ip address of smtp server** (*IP*; Default: **0.0.0.0**) | The IP address of the SMTP server, where to redirect HotSpot's network SMTP requests (TCP port 25) |
| **dns servers** (*IP*; Default: **0.0.0.0**) | DNS server addresses used for HotSpot clients, configuration is taken from *`/ip/dns`* menu of the HotSpot gateway |
| **dns name** (*string*; Default: **""**) | The domain name of the HotSpot server, a fully qualified domain name is required, for example, [www.example.com](http://www.example.com) |
| **name of local hotspot user** (*string*; Default: **"admin"**) | username of one automatically created HotSpot user, added to *`/ip/hotspot/user`* |
| **password for the user** (*string*; Default: ) | Password for automatically created HotSpot user |

## HotSpot

**Sub-menu:** `/ip/hotspot`

The menu is designed to manage the HotSpot servers of the router. It is possible to run HotSpot on Ethernet, wireless, VLAN, and bridge interfaces. One HotSpot server is allowed per interface. When HotSpot is configured on the bridge interface, set the HotSpot interface as the bridge interface, not as a bridge port, do not add public interfaces to bridge ports. You can add HotSpot servers manually to the *`/ip/hotspot`* menu, but it is advised to run *`/ip/hotspot/setup`*, which adds all necessary settings.

| Parameters | Description |
| :-- | :-- |
| **name** (text) | HotSpot server's name or identifier |
| **address-pool** (name/none; default: *none*) | address space used to change any HotSpot client IP address to a valid address. Useful for providing public network access to mobile clients that are not willing to change their networking settings |
| **idle-timeout** (time/none; default: *5m*) | period of inactivity for unauthorized clients. When there is no traffic from this client (literally, the client computer should be switched off), once the timeout is reached, a user is dropped from the HotSpot host list, its used address becomes available |
| **keepalive-timeout** (time/none; default: *none*) | Value of how long the host can stay out of reach to be removed from the HotSpot |
| **login-timeout** (time/none; default: *none*) | Period of time after which if a host hasn't been authorized with the system the host entry gets deleted from the host table. Loop repeats until the host logs in to the system. Enable if there are situations where a host cannot log in after being too long in the host table unauthorized. |
| **interface** (name of an interface) | Interface to run HotSpot on |
| **addresses-per-mac** (integer**/**unlimited; default: 2) | Number of IP addresses allowed to be bound with the MAC address, when multiple HotSpot clients are connected with one MAC-address |
| **profile** (name; default: ***default*)** | HotSpot server default HotSpot profile, which is located in *`/ip/hotspot/profile`* |

## Read-only

| Parameters | Description |
| :-- | :-- |
| keepalive-timeout (read-only; time) | The exact value of the keepalive-timeout that is applied to the user. The value shows how long the host can stay out of reach to be removed from the HotSpot |

## HotSpot Profile

This submenu contains a list of HotSpot server profiles. There may be various different HotSpot systems, defined as Server Profiles, on the same gateway machine. One or more interfaces can be grouped into one server profile. There are very few settings for the servers on particular interfaces - most of the configuration is set in the server profiles. For example, it is possible to make a completely different set of servlet pages for each server profile, and define different RADIUS servers for authentication.

| Property | Description |
| :-- | :-- |
| **dns-name** (*string*; Default: **""**) | DNS name of the HotSpot server. This is the DNS name used as the name of the HotSpot server (i.e., it appears as the location of the login page). This name will automatically be added as a static DNS entry in the DNS cache. |
| **hotspot-address** (*IP*; Default: **0.0.0.0**) | IP address of HotSpot service. |
| **html-directory** (*string*; Default: **hotspot**) | Directory name in which HotSpot HTML pages are stored (by default *hotspot* directory). It is possible to specify a different directory with modified HTML pages. To change the HotSpot login page, get HotSpot files from your router, change and upload them back to the same location. Full path must be typed in the html-directory field, including "/flash/(hotspot\_dir)" |
| **html-directory-override** (*string*; Default: **none**) | Alternative path for HotSpot HTML files. It should be used only when customized HotSpot HTML files are stored on external storage. |
| **http-cookie-lifetime** (*time*; Default: **3d**) | HTTP cookie validity time, the option is related to *cookie* HotSpot login method |
| **http-proxy** (*IP:Port*; Default: **0.0.0.0:0**) | Address and port of the proxy server for HotSpot service, when the default value is used all requests are resolved by the local `/ip/proxy` |
| **https-redirect** (*yes \| no*; Default: **yes**) | Whether to redirect the unauthenticated user to the HotSpot login page, if the user is visiting an https:// url. Since the certificate domain name will mismatch, often this leads to errors, so you can set this parameter to "no" and all https requests will simply be rejected and user will have to visit an http page. |
| **login-by** (*cookie\|http-chap\|http-pap\|https\|mac\|trial\|mac-cookie*; Default: **http-chap, cookie**) | The HotSpot authentication method usedmac-cookie - enables login by mac cookie methodcookie - may only be used with another HTTP authentication method. HTTP cookie is generated, when the user authenticates in HotSpot for the first time. User is not asked for the login/password and is authenticated automatically, until cookie-lifetime is activehttp-chap - login/password is required for the user to authenticate in HotSpot. CHAP challenge-response method with MD5 hashing algorithm is used for protecting passwords.http-pap - login/password is required for user to authenticate in HotSpot. Username and password are sent over network in plain text.https - login/password is required for user to authenticate in HotSpot. Client login/password exchange between client and server is encrypted with SSL tunnel. mac - client is authenticated without asking for a login form. Client MAC-address is added to `/ip/hotspot/user` database, client is authenticated as soon as connected to the HotSpottrial - client is allowed to use the internet without HotSpot login for the specified amount of time |
| **mac-auth-password** (*string*; Default: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Used together with MAC authentication, the field is used to specify password for the users to be authenticated by their MAC addresses. The following option is required, when a specific RADIUS server rejects authentication for the clients with a blank password |
| **name** (*string*; Default: ) | Descriptive name of the profile |
| **nas-port-type** (*string*; Default: **wireless-802.11**) | NAS-Port-Type value to be sent to RADIUS server, NAS-Port-Type values are described in the RADIUS RFC 2865. This optional value attribute indicates the type of the physical port of the HotSpot server. |
| **radius-accounting** (*yes \| no*; Default: **yes**) | Send RADIUS server accounting information for each user, when yes is used |
| **radius-default-domain** (*string*; Default: ) | Default domain to use for RADIUS requests. Allows using separate RADIUS server per *`/ip/hotspot/profile`*. If used, same domain name should be specified under /radius domain value. |
| **radius-interim-update** (*time \| received*; Default: **received**) | How often to send accounting updates. When *received* is set, interim-time from the RADIUS server is used. **0s** is the same as *received*. |
| **radius-location-name** (*string*; Default: ) | RADIUS-Location-Id to be sent to RADIUS server. Used to identify location of the HotSpot server during the communication with RADIUS server. Value is optional and used together with RADIUS server. |
| **radius-mac-format** (*"XX XX XX XX XX XX"\|XX:XX:XX:XX:XX:XX\|XXXXXX-XXXXXX\|XXXXXXXXXXXX\|XX-XX-XX-XX-XX-XX\|XXXX:XXXX:XXXX\|XXXXXX:XXXXXX*; Default: **XX:XX:XX:XX:XX:XX**) | Option to set format of user mac-address, that is sent to RADIUS server during AAA session. |
| **rate-limit** (*string*; Default: **""**) | Rate limitation in the form of **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]] [priority] [rx-rate-min[/tx-rate-min]]** from the point of view of the router (so "rx" is client upload, and "tx" is client download). All rates should be numbers with optional 'k' (1,000s) or 'M' (1,000,000s). If tx-rate is not specified, rx-rate is as tx-rate too. Same goes for tx-burst-rate and tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as the default. rx-rate-min and tx-rate min are the values of limit-at properties |
| **smtp-server** (*IP*; Default: **0.0.0.0**) | SMTP server address to be used to redirect HotSpot users' SMTP requests. |
| **split-user-domain** (*yes \| no*; Default: **no**) | Split username from domain name when the username is given in "user@domain" or in "domain\user" format from RADIUS server |
| **ssl-certificate** (*string \| none*; Default: **none**) | Name of the SSL certificate on the router to use only for HTTPS authentication. |
| **trial-uptime** (*time/time*; Default: **30m/1d**) | Used only with *trial* authentication method. First time value specifies how long trial user identified by MAC address can use access to public networks without HotSpot authentication. Second time value specifies the amount of time, that has to pass until the user is allowed to use trial again. |
| **trial-user-profile** (*string*; Default: **default**) | Specifies **HotSpot user profile** for trial users. |
| **use-radius** (*yes \| no*; Default: **no**) | Use RADIUS to authenticate HotSpot users. |

## HotSpot User Profiles

**Sub-menu:** `/ip/hotspot/user/profile`

User profile menu is used for common HotSpot client settings. Profiles are like User groups with the same set of settings, rate-limit, filter chain name, etc.

| Property | Description |
| :-- | :-- |
| **add-mac-cookie** (*yes\|no*; Default: **yes**) | Allows adding a mac cookie for users. |
| **address-list** (*string*; Default: ) | Name of the address list in which the user's IP address will be added. Useful to mark traffic per user group for queue tree configurations. |
| **address-pool** (*string \|none*; Default: **none**) | IP pool name from which the user will get an IP. When the user has improper network settings configuration on the computer, the HotSpot server makes a translation and assigns the correct IP address from the pool instead of the incorrect one |
| **advertise** (*yes \| no*; Default: **no**) | Enable forced advertisement popups. After a certain interval, a specific web-page is being displayed for HotSpot users. The advertisement page might be blocked by browser popup blockers. |
| **advertise-interval** (*time[,time[,..]]*; Default: **30m,10m**) | Set of intervals between advertisement popups. After the list is done, the last value is used for all further advertisements, 10 minutes |
| **advertise-timeout** (*time \| immediately \| never*; Default: **1m**) | How long the advertisement is shown, before blocking network access for the HotSpot client. Connection to the Internet is not allowed when the advertisement is not shown. |
| **advertise-url** (*string[,string[,..]]*; Default: ) | List of URLs that are shown for advertisement popups. After the last URL is used, the list starts from the beginning. |
| **idle-timeout** (*time \| none*; Default: **none**) | Maximal period of inactivity for authorized HotSpot clients. The timer counts when there is no traffic coming from that client and going through the router, for example, the computer is switched off. The user is logged out, dropped from the host list, and the address used by the user is freed when the timeout is reached. |
| **incoming-filter** (*string*; Default: ) | Name of the firewall chain applied to incoming packets from the users of this profile. A jump rule is required from the built-in chain (input, forward, output) to chain=hotspot |
| **incoming-packet-mark** (*string*; Default: ) | Packet mark put on incoming packets from every user of this profile |
| **keepalive-timeout** (*time \| none*; Default: ) | Keepalive timeout for authorized HotSpot clients. Used to detect that the computer of the client is alive and reachable. The user is logged out when the timeout value is reached |
| **mac-cookie-timeout** (*time*; Default: **3d**) | Selects the mac-cookie timeout from the last login or logout. |
| **name** (*string*; Default: ) | Descriptive name of the profile |
| **on-login** (*string*; Default: **""**) | Script name to be executed when the user logs in to the HotSpot from the particular profile. It is possible to get the username from internal **user** and **interface** variables. For example, *:log info "User $user logged in!"*. If the HotSpot is set on a bridge interface, then the **interface** variable will show the bridge as the actual interface unless **use-ip-firewall** is set in the bridge settings. List of available variables: $user$username (alternative var name for $user)$address$"mac-address"$interface |
| **on-logout** (*string*; Default: **""**) | Script name to be executed when the user logs out from the HotSpot. It is possible to get the username from internal **user** and **interface** variables. For example, *:log info "User $user logged in!"* . If the HotSpot is set on a bridge interface, then the **interface** variable will show the bridge as the actual interface unless **use-ip-firewall** is set in the bridge settings. List of available variables: $user$username (alternative var name for $user)$address$"mac-address"$interface$cause Starting with v6.34rc11 some additional variables are available: $uptime-secs - final session time in seconds$bytes-in - bytes uploaded$bytes-out - bytes downloaded$bytes-total - bytes up + bytes down$packets-in - packets uploaded$packets-out - packets downloaded$packets-total - packets up + packets down |
| **open-status-page** (*always \| http-login*; Default: **always**) | Option to show status page for a user authenticated with the mac login method. For example, to show advertisement on the status page (alogin.html)http-login - open the status page only for HTTP login (includes cookie and HTTPS)always - open the HTTP status page in case of mac login as well |
| **outgoing-filter** (*string*; Default: ) | Name of the firewall chain applied to outgoing packets from the users of this profile. A jump rule is required from the built-in chain (input, forward, output) to chain=hotspot |
| **outgoing-packet-mark** (*string*; Default: ) | Packet mark put on outgoing packets from every user of this profile |
| **rate-limit** (*string*; Default: **""**) | A simple dynamic queue is created for the user once the user logs in to the HotSpot. Rate-limitation is configured in the following form **[rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**. For example, to set 1M download, 512k upload for the client, rate-limit=512k/1M |
| **session-timeout** (*time*; Default: **0s**) | Allowed session time for the client. After this time, the user is logged out unconditionally |
| **shared-users** (*integer*; Default: **1**) | Allowed number of simultaneously logged-in users with the same HotSpot username |
| **status-autorefresh** (*time \| none*; Default: **none**) | HotSpot status page autorefresh interval |
| **transparent-proxy** (*yes \|*; Default: **yes**) | Use a transparent HTTP proxy for the authorized users of this profile |

## HotSpot Users

This is the menu, where client's user/password information is actually added. Additional configuration options for HotSpot users are configured here as well.

| Property | Description |
| :-- | :-- |
| **address** (*IP*; Default: **0.0.0.0**) | IP address, when specified, the client will get the address from the HotSpot one-to-one NAT translations. Address does not restrict HotSpot login only from this address |
| **comment** (*string*; Default: ) | descriptive information for the HotSpot user. It might be used for scripts to change parameters for specific clients |
| **email** (*string*; Default: ) | HotSpot client's e-mail, informational value for the HotSpot user |
| **limit-bytes-in** (*integer*; Default: **0**) | Maximal amount of bytes that can be received from the user. The user is disconnected from HotSpot after the limit is reached. |
| **limit-bytes-out** (*integer*; Default: **0**) | Maximal amount of bytes that can be transmitted from the user. The user is disconnected from HotSpot after the limit is reached. |
| **limit-bytes-total** (*integer*; Default: **0**) | (limit-bytes-in+limit-bytes-out). The user is disconnected from HotSpot after the limit is reached. |
| **limit-uptime** (*time*; Default: **0**) | Uptime limit for the HotSpot client. The user is disconnected from HotSpot as soon as the uptime is reached. |
| **mac-address** (*MAC*; Default: **00:00:00:00:00:00**) | The client is allowed to log in only from the specified MAC-address. If the value is *00:00:00:00:00:00*, any mac address is allowed. |
| **name** (*string*; Default: ) | HotSpot login page username. When MAC-address authentication is used, the name is configured as the client's MAC-address |
| **password** (*string*; Default: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | User password |
| **profile** (*string*; Default: **default**) | User profile configured in *`/ip/hotspot/user/profile`* |
| **routes** (*string*; Default: ) | Routes added to HotSpot gateway when the client is connected. The route format is **dst-address gateway metric** (for example, *192.168.1.0/24 192.168.0.1 1*) |
| **server** (*string \| all*; Default: **all**) | HotSpot server's name to which the user is allowed to log in |
| **otp-secret** (*string*; Default: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | A one-time password token that is used for HotSpot user authorization. It could be used as a separate "password" for HotSpot user authentication. |

## Read-only properties

| Property | Description |
| :-- | :-- |
| **bytes-in** (*integer*) | Total amount of data bytes received from the client. |
| **bytes-out** (*integer*) | Total amount of data bytes sent to the client. |
| **packets-in** (*integer*) | Total number of packets received from the client. |
| **packets-out** (*integer*) | Total number of packets sent to the client. |
| **uptime** (*time*) | Current session duration since the client was authenticated. |

## HotSpot Active

**Sub-menu:** `/ip/hotspot/active`

HotSpot active menu shows all clients authenticated in HotSpot, the menu is informational (read-only). It is not possible to change anything here, except the user can be logged out with the remove command.

| Parameters | Description |
| :-- | :-- |
| **server** (read-only; name) | HotSpot server name client is logged in |
| **user** (read-only; name) | name of the HotSpot user |
| **domain** (read-only; text) | the domain of the user (if split from the username), the parameter is used only with RADIUS authentication |
| **address** (read-only; IP address) | The IP address of the HotSpot user |
| **mac-address** (read-only; MAC-address) | MAC-address of the HotSpot user |
| **login-by** (read-only; multiple-choice: cookie **/** http-chap **/** http-pap **/** https **/** mac **/** mac-cookie **/** trial) | the authentication method used by the HotSpot client |
| **uptime** (read-only; time) | current session time of the user, it is showing how long the user has been logged in |
| **idle-time** (read-only; time) | the amount of time the user has been idle |
| **session-time-left** (read-only; time) | the exact value of session-time, that is applied for the user. Value shows how long user is allowed to be online to be logged off automatically by **uptime** reached |
| **idle-timeout** (read-only; time) | the exact value of the user's idle-timeout |
| **keepalive-timeout** (read-only; time) | the exact value of the keepalive-timeout, that is applied for the user. Value shows how long the host can stay out of reach to be removed from the HotSpot |
| **limit-bytes-in** (read-only; integer) | value shows how many bytes received from the client, the option is active when the appropriate parameter is configured for HotSpot user |
| **limit-bytes-out** (read-only; integer) | value shows how many bytes sent to the client, the option is active when the appropriate parameter is configured for HotSpot user |
| **limit-bytes-total** (read-only; integer) | value shows how many bytes total were sent/received from the client, the option is active when the appropriate parameter is configured for HotSpot user |

## HotSpot Host

**Sub-menu:** `/ip/hotspot/host`

The host table lists all computers connected to the HotSpot server. The host table is informational and it is not possible to change any value there:

| Parameters | Description |
| :-- | :-- |
| **mac-address** (read-only; MAC-address) | HotSpot user MAC-address |
| **address** (read-only; IP address) | HotSpot client's original IP address |
| **to-address** (read-only; IP address) | The new client address assigned by HotSpot might be the same as the original **address** |
| **server** (read-only; name) | HotSpot server name the client is connected to |
| **bridge-port** (read-only; name) | *`/interface/bridge/port`* the client is connected to, value is unknown when HotSpot is not configured on the bridge |
| **uptime** (read-only; time) | value shows how long the user is online (connected to the HotSpot) |
| **idle-time** (read-only; time) | time the user has been idle |
| **idle-timeout** (read-only; time) | value of the client idle-timeout (unauthorized client) |
| **keepalive-timeout** (read-only; time) | keepalive-timeout value of the unauthorized client |
| **bytes-in** (read-only; integer) | amount of bytes received from an unauthorized client |
| **packet-in** (read-only; integer) | amount of packets received from an unauthorized client |
| **bytes-out** (read-only; integer) | amount of bytes sent to an unauthorized client |
| **packet-out** (read-only; integer) | amount of packets sent to an unauthorized client |

## HotSpot walled-garden

A Walled garden is a system which allows unauthorized use of some resources, but requires authorization to access other resources. This is useful, for example, to give access to some general information about the HotSpot service provider or billing options.

The menu only manages Walled Garden for HTTP and HTTPs protocols. Other protocols can also be included in Walled Garden, but that is configured elsewhere (in `/ip/hotspot/walled-garden/ip`).

| Property | Description |
| :-- | :-- |
| **action** (*allow \| deny*; Default: **allow**) | Action to perform, when packet matches the ruleallow - allow access to the web-page without authorizationdeny - authorization is required to access the web-page |
| **server** (*string*; Default: ) | Name of the HotSpot server the rule is applied to. |
| **src-address** (*IP*; Default: ) | Source address of the user, usually the IP address of the HotSpot client |
| **method** (*string*; Default: ) | HTTP method of the request |
| **dst-host** (*string*; Default: ) | Domain name of the destination web-server |
| **dst-port** (*integer*; Default: ) | TCP port number the client sends request to |
| **path** (*string*; Default: ) | The path of the request. Path comes after '''http://dst\_host' |

# Read-only properties

| Property | Description |
| :-- | :-- |
| **dst-address** (*IP*) |  |
| **hits** (*integer*) |  |

Wildcard properties (dst-host and path) match a complete string (i.e., they will not match "[example.com](http://example.com)" if they are set to "example"). Available wildcards are '\*' (match any number of any characters) and '?' (match any one character). Regular expressions are also accepted here, but if the property should be treated as a regular expression, it should start with a colon (':'). To show that no symbols are allowed before the given pattern, we use the ^ symbol at the beginning of the pattern. To specify that no symbols are allowed after the given pattern, we use the $ symbol at the end of the pattern.

### Example

To only permit bypassed access in the walled garden to "[www.example.com/test](http://www.example.com/test)" but not to "[www.example.com/test/test.php](http://www.example.com/test/test.php)" :

```
/ip/hotspot/walled-garden
add dst-host=:^www.example.com path=":/test\$"
```

## HotSpot walled-garden ip

To bypass HotSpot authentication for other protocols and different src/dst addresses (or address-lists). Used for different services (Winbox, SSH, Telnet, SIP, etc.)

| Property | Description |
| :-- | :-- |
| **action** (*accept \|drop\|reject*; Default: **allow**) | Action to perform, when the packet matches the ruleallow - allow access to the opened service without authorizationdrop - the authorization is required to access the servicereject - the authorization is required to access the service, when the service is accessed, an ICMP reject message host-unreachable will be generated |
| **server** (*string*; Default: ) | Name of the HotSpot server, rule is applied to. |
| **src-address** (*IP*; Default: ) | Source address of the user, usually the IP address of the HotSpot client |
| **dst-address** (*IP*; Default: ) | Destination IP address, the IP address of the WEB-server. Ignored if **dst-host** is already specified. |
| **src-address-list** (*string*; Default: ) | Source address list name |
| **dst-address-list** (*string*; Default: ) | Destination address list. Ignored if **dst-host** is already specified. |
| **dst-host** (*string*; Default: ) | Domain name of the destination web-server. When this parameter is specified, a dynamic entry is added to Walled Garden |
| **dst-port** (*integer*; Default: ) | TCP port number, client sends request to |
| **protocol** (*integer \| string*; Default: ) | IP protocol |

## IP Binding

**Sub-menu:** `/ip/hotspot/ip-binding`

IP-Binding HotSpot menu allows the setup of static One-to-One NAT translations, allows bypassing specific HotSpot clients without any authentication, and also allows blocking specific hosts and subnets from the HotSpot network

| Property | Description |
| :-- | :-- |
| **address** (*IP Range*; Default: **""**) | The original IP address of the client |
| **mac-address** (*MAC*; Default: **""**) | MAC address of the client |
| **server** (*string \| all*; Default: **"all"**) | Name of the HotSpot server.all - will be applied to all HotSpot servers |
| **to-address** (*IP*; Default: **""**) | New IP address of the client, translation occurs on the router (client does not know anything about the translation) |
| **type** (*blocked \| bypassed \| regular*; Default: **""**) | Type of the IP-binding actionregular - performs One-to-One NAT according to the rule, translates the address to to-addressbypassed - performs the translation, but excludes the client from login to the HotSpotblocked - translation is not performed and packets from a host are dropped |

## Cookies

The menu contains all cookies sent to the HotSpot clients, which are authorized by the cookie method. All the entries are read-only.

**Sub-menu:** `/ip/hotspot/cookie`

| Property | Description |
| :-- | :-- |
| **domain** (*string*) | The domain name (if split from the username) |
| **expires-in** (*time*) | How long the cookie is valid |
| **mac-address** (*MAC*) | Client's MAC-address |
| **user** (*string*) | HotSpot username |

## MAC Cookie

MAC cookie is a HotSpot feature, designed to improve accessibility for smartphones, laptops and other mobile devices.

When the MAC cookie feature is enabled (**login-by**=mac-cookie, **add-mac-cookie**=yes set in user profile), the following actions are taken:

- **First successful login**. Mac cookie keeps a record of username and password for the MAC address if there is only one host with such a MAC. Cookie timeout is set to a value equal to mac-cookie-timeout.
- **New host appears**. HotSpot checks if there is a mac cookie record for the MAC address and logs in the host using the recorded username and password. If there is more than one host with the same MAC address, the user will not be logged in and the MAC cookie record for this address will be deleted.

When **a user logs out** mac cookie is removed in the following cases:

- user-request - User clicked on the logout button.
- admin-reset - Disconnected from the radius server or the user is removed from the HotSpot active menu.
- nas-request - Traffic limit reached.
- session-timeout.

To debug problems with mac-cookies you will need to enable HotSpot debug logs and look for reasons why mac-cookie login didn't work for a certain host.

### Reasons when mac cookie is removed by server

- `/ip/hotspot/cookie/remove [number]`.
- Radius server sends Disconnect-Request.
- End-User has logged out himself via HotSpot status page.
- End user has reached his data cap ("traffic limit reached").
- Session-Timeout.
- If mac-cookie login fails.
- If the server detects that in the host table there is more than one entry with the same mac-address.

### Properties of the HotSpot API JSON (RFC 7710)

Based on the `api.json` template provided in the documentation, here are the descriptions for each property used to communicate captive portal status to client devices:

- **captive**: A boolean value (`true` or `false`) that informs the client device whether it is currently restricted by the captive portal. If the user is already authenticated, it returns `false`.
- **user-portal-url**: The specific URL where the user can access the login page or manage their current session. In MikroTik RouterOS, this is dynamically populated by the `$(link-login-only)` variable.
- **seconds-remaining**: (Optional) An integer representing the number of seconds left before the current session expires. This is only included if a session timeout is configured.
- **bytes-remaining**: (Optional) An integer representing the remaining data quota in bytes available to the user. This is only included if data limits are applied to the HotSpot user.
- **can-extend-session**: A boolean value indicating whether the user has the ability to extend their current session or purchase/request more time/data via the portal.

## Load balancing with mangle on HotSpot server

In a multi-uplink HotSpot setup (for example, [PCC](../../high-availability-solutions/load-balancing/per-connection-classifier.md), default routing often might fail to work as expected because the router prioritises mangle rules over the local destination check.

To fix this, ensure traffic destined for the HotSpot server is routed via the **local** table before the **mangle** chain is evaluated. You can achieve this by:

1. Adjusting the "`/routing/settings"` ([Routing table lookup](../../user-guides/routing-and-networking-protocols/routing-decision.md#routing-table-lookup).
2. Or, adding specific "`/routing/rule"` entries to force the HotSpot server's traffic to use the local table first (including HTTP 80 traffic which is used to detect the HotSpot server).
