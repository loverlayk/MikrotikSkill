# RADIUS

> RADIUS enables centralized authentication and accounting for PPP, HotSpot, and other services in MikroTik RouterOS by connecting to a RADIUS server via UDP or RadSec protocol, with configurable ports, shared secrets,...

# RADIUS

RADIUS, short for Remote Authentication Dial-In User Service, is a remote server that provides authentication and accounting facilities to various network appliances. RADIUS authentication and accounting allows the ISP or network administrator to manage PPP user access and accounting from one server throughout a large network. The MikroTik RouterOS has a RADIUS client that can authenticate [router's local](./user.md) [users](./user.md), [HotSpot](./hotspot-captive-portal/index.md), [PPP](../mobile-networking/ppp.md) and ISDN connections. The attributes received from the RADIUS server override the ones set in the default profile, but if some parameters are not received they are taken from the respective default profile.

The RADIUS server database is consulted only if no matching user access record is found in the router's local database.

If RADIUS accounting is enabled, accounting information is also sent to the default RADIUS server for that service.

## RADIUS Client

**Sub-menu:** `/radius`

This sub-menu allows adding and removing RADIUS clients.

:::warning
The order of added items in this list is significant.

:::

### Properties

| Property | Description |
| :-- | :-- |
| **accounting-backup** (*yes \| no*; Default: **no**) | Whether the configuration is for the backup RADIUS server |
| **accounting-port** (*integer [1..65535]*; Default: **1813**) | RADIUS server port used for accounting |
| **address** (*IPv4/IPv6 address*; Default: **0.0.0.0**) | IPv4 or IPv6 address of RADIUS server.  The following formats are accepted:  - *ipv4* - *ipv4*`@`*vrf* - *ipv6* - *ipv6*`@`*vrf* |
| **authentication-port** (*integer [1..65535]*; Default: **1812**) | RADIUS server port used for authentication. |
| **called-id** (*string*; Default: ) | Value depends on Point-to-Point protocol: PPPoE - service name, PPTP - server's IP address, L2TP - server's IP address. |
| **certificate** (*string*; Default: ) | [Certificate from certificate store](../authentication-authorization-accounting/certificates.md) to use for communicating with RADIUS Server with RadSec enabled. |
| **comment** (*string*; Default: ) |  |
| **disabled** (*yes \| no*; Default: **no**) |  |
| **domain** (*string*; Default: ) | Microsoft Windows domain of client passed to RADIUS servers that require domain validation. |
| **protocol** (*radsec \| udp*; Default: **udp**) | Specifies the protocol to use when communicating with the RADIUS Server. |
| **radsec-timeout**(*time,* Default: **3300ms**) | Timeout after which the request should be resent over RadSec protocol. |
| **require-message-auth** (*no \| yes-for-request-resp* Default: **yes-for-request-resp**) | Specifies if Message-Authenticator attributes are required. |
| **realm** (*string*; Default: ) | Explicitly stated realm (user domain), so the users do not have to provide proper ISP domain name in the user name. |
| **secret** (*string*; Default: ) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | The shared secret used to access the RADIUS server. |
| **service** (*ppp\|login\|hotspot\|wireless\|dhcp\|ipsec\|dot1x*; Default: ) | Router services that will use this RADIUS server:hotspot - HotSpot authentication servicelogin - router's local user authenticationppp - Point-to-Point clients authenticationwireless - wireless client authenticationdhcp - DHCP protocol client authentication (client's MAC address is sent as User-Name)ipsec - ipsec client authenticationdot1x - dot1x authentication |
| **src-address** (*ipv4/ipv6 address*; Default: **0.0.0.0**) | Source IP/IPv6 address of the packets sent to the RADIUS server |
| **timeout** (*time*; Default: **1100ms**) | Timeout after which the request should be resent. |

:::warning
When the RADIUS server is authenticating the user with CHAP, MS-CHAPv1, MS-CHAPv2, it is not using a shared secret; the secret is used only in the authentication reply, and the router (RADIUS client) verifies it.So if you have the wrong shared secret, the RADIUS server will accept a request, but the router won't accept the reply. You can see that with the "*`/radius/monitor`*" command, the "bad-replies" number should increase whenever somebody tries to connect.

:::

:::danger
If RadSec is enabled, make sure your RADIUS Server is using "**radsec**" as the shared secret, otherwise, the RADIUS Server will not be able to decrypt data correctly (unprintable characters).With RadSec, RouterOS forces the shared secret to "radsec" regardless of what has been set manually.For more details see RFC6614.

:::

:::info
If RadSec is used, RouterOS will override to use TCP port 2083
:::

### Example

To set up a RADIUS Client for HotSpot and PPP services that will authenticate against a RADIUS Server (10.0.0.3), you need to do the following:

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=ex
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 
```

To set up a RADIUS Client with RadSec, you need to do the following:

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=radsec protocol=radsec certificate=client.crt
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 10.0.0.3 radsec
```

:::warning
Make sure the specified certificate is trusted and common-name verification on both ends will work properly.

:::

Here is a trivial example of certificates that can be used for RADIUS RadSec configuration:

```ros
On server:

#CN should be RADIUS server IP
/certificate/add name=radsec_server common-name=10.155.114.91
/certificate/sign radsec_server

#CN should be RADIUS client IP
/certificate/add name=radsec_client1 common-name=10.155.114.92
/certificate/sign radsec_client1
/user-manager/set radsec-certificate=radsec_server

#Export certificates on the server in order to apply them on client
/certificate/export-certificate type=pkcs12 export-passphrase=verystrongpassword radsec_client1
/certificate/export-certificate type=pkcs12 radsec_server

On client:

#Download both files and upload them to the client
/certificate/import file-name=cert_export_radsec_client1.p12 passphrase=verystrongpassword
/certificate/import file-name=cert_export_radsec_server.p12
/radius/set <radius_client_id_in_list> certificate=cert_export_radsec_client1.p12_0

#After that when RADIUS client tries to connect to the server you should see on status fileld: status="TLS connected".
```

To view RADIUS Client statistics, you need to do the following:

```ros
[admin@MikroTik] > /radius/monitor 0
pending: 0
requests: 10
accepts: 4
rejects: 1
resends: 15
timeouts: 5
bad-replies: 0
last-request-rtt: 0s
```

Make sure you enable RADIUS authentication for the desired services:

```ros
/ppp/aaa/set use-radius=yes
/ip/hotspot/profile/set default use-radius=yes
```

## Connection Terminating from RADIUS

**Sub-menu:** `/radius/incoming`

This facility supports unsolicited messages sent from the RADIUS server. Unsolicited messages extend RADIUS protocol commands that allow terminating a session that has already been connected from the RADIUS server. For this purpose, DM (Disconnect-Messages) is used. Disconnect messages cause a user session to be terminated immediately.

:::warning
RouterOS doesn't support POD (Packet of Disconnect), the other RADIUS access request packet that performs a similar function to Disconnect Messages

:::

### Properties

| Property | Description |
| :-- | :-- |
| **accept** (*yes \| no*; Default: **no**) | Whether to accept unsolicited messages |
| **port** (*integer*; Default: **1700**) | The port number to listen for the requests on |
| **vrf** (*VRF name*; default value: **main**) | Set VRF on which the service is listening for incoming connections |

## Supported RADIUS Attributes

Here you can download the [RADIUS reference dictionary.txt](pathname:///assets/319783010_RADIUS_reference_dictionary.txt), that includes all supported RADIUS attributes by MikroTik device. This file is designed for FreeRADIUS, but may also be used by other RADIUS servers. Note, it may conflict with the default configuration file of your RADIUS server. Correct the configuration, not the dictionary, as no other attributes are supported by MikroTik RouterOS. There is also the [MikroTik Vendor attributes.txt](pathname:///assets/319783011_MikroTik_Vendor_attributes.txt) that can be included in an existing dictionary to support MikroTik vendor-specific attributes.

Below you will find a description about attributes and how they are used on MikroTik devices during communication with RADIUS.

### Definitions

- **PPPs** - PPP, PPTP, PPPoE
- **default configuration** - settings in default profile (for PPPs) or HotSpot server settings (for HotSpot)

### Access-Request packet

- **Service-Type** - Always is "Framed" (only for PPPs).
- **Framed-Protocol** - Always is "PPP" (only for PPPs).
- **NAS-Identifier** - Router's identity name.
- **NAS-IP-Address** - IP address of the router itself.
- **NAS-Port** - This Attribute indicates the physical port number of the NAS which is authenticating the user.
- **Acct-Session-Id** - Unique session ID. The first two symbols of session ID represent service (PPP, Hotspot, etc.). The next symbol is incremented on each reboot. The last group of symbols is incremented on each new session. This means, that you can not get the same ID for 1 million re-connects on the same boot for the same RADIUS type service. If you lose the session stop message and RADIUS server does still keep the session open, but then receives another session start message, then it must be aware that the stop message was lost, close the old session and start a new session.
- **NAS-Port-Type** - Async PPP - "Async"; PPTP and L2TP - "Virtual"; PPPoE - "Ethernet"; ISDN - "ISDN Sync"; HotSpot - "Ethernet | Cable | Wireless-802.11" (according to the value of the nas-port-type parameter in `/ip/hotspot/profile`).
- **Calling-Station-Id** - PPPoE and HotSpot- client MAC address in capital letters; PPTP and L2TP - client public IP address.
- **Called-Station-Id** - PPPoE - service name; PPTP and L2TP - server IP address; HotSpot - name of the HotSpot server.
- **NAS-Port-Id** - Async PPP - serial port name; PPPoE - ethernet interface name on which server is running; HotSpot - name of the physical HotSpot interface (if bridged, the bridge port name is shown here); not present for ISDN, PPTP and L2TP.
- **Framed-IP-Address** - IP address of HotSpot client after Universal Client translation.
- **Mikrotik-Host-IP** - IP address of HotSpot client before Universal Client translation (the original IP address of the client).
- **User-Name** - Client login name.
- **MS-CHAP-Domain** - User domain, if present.
- **Mikrotik-Realm** - If it is set in /radius menu, it is included in every RADIUS request as the Mikrotik-Realm attribute. If it is not set, the same value is sent as in the MS-CHAP-Domain attribute (if MS-CHAP-Domain is missing, Realm is not included either).
- **WISPr-Location-ID** - Text string specified in the radius-location-id property of the HotSpot server.
- **WISPr-Location-Name** - Text string specified in the radius-location-name property of the HotSpot server.
- **WISPr-Logoff-URL** - Full link to the logout page (for example, **[](http://10.48.0.1/lv/logout)**).

Depending on authentication methods (NOTE: HotSpot uses CHAP by default and may also use PAP if unencrypted passwords are enabled, it cannot use MSCHAP):

- **User-Password** - Encrypted password (used with PAP authentication).
- **CHAP-Password**, **CHAP-Challenge** - Encrypted password and challenge (used with CHAP authentication).
- **MS-CHAP-Response**, MS-CHAP-Challenge - Encrypted password and challenge (used with MS-CHAPv1 authentication).
- **MS-CHAP2-Response**, **MS-CHAP-Challenge** - Encrypted password and challenge (used with MS-CHAPv2 authentication).

### Access-Accepts packet

- **Framed-IP-Address** - IP address given to the client. If the address belongs to 127.0.0.0/8 or 224.0.0.0/3 networks, IP pool is used from the default profile to allocate a client IP address. If Framed-IP-Address is specified, Framed-Pool is ignored.
- **Framed-IP-Netmask** - Client netmask. PPPs - if specified, a route will be created to the network Framed-IP-Address belongs to via the Framed-IP-Address gateway; HotSpot - ignored by HotSpot.
- **Framed-Pool** - IP pool name (on the router) from which to get an IP address for the client. If Framed-IP-Address is specified, this attribute is ignored.
- **Framed-IPv6-Prefix** - IPv6 prefix assigned to the client.
- **Mikrotik-Delegated-IPv6-Pool** - IPv6 pool used for Prefix Delegation.
- **Delegated-IPv6-Prefix** - IPv6 Prefix.
- **Delegated-IPv6-Prefix-Pool** - IPv6 Prefix pool used for Prefix Delegation.

NOTE: if Framed-IP-Address or Framed-Pool is specified, it overrides remote-address in the default configuration.

- **Idle-Timeout** - Overrides idle-timeout in the default configuration.
- **Session-Timeout** - Overrides session-timeout in the default configuration.
- **Port-Limit** - Maximal number of simultaneous connections using the same username (overrides the shared-users property of the HotSpot user profile).
- **Class** - Cookie. Will be included in Accounting-Request unchanged.
- **Framed-Route** - Routes to add on the server. Format is specified in RFC 2865 (Ch. 5.22). Can be specified as many times as needed.
- **Filter-Id** - Firewall filter chain name. It is used to make a dynamic firewall rule. Firewall chain name can have suffix .in or .out, that will install rule only for incoming or outgoing traffic. Multiple Filter-id can be provided, but only last ones for incoming and outgoing are used. For PPPs - filter rules in ppp chain that will jump to the specified chain, if a packet has come to/from the client (that means that you should first create a ppp chain and make jump rules that would put actual traffic to this chain). The same applies for HotSpot, but the rules will be created in hotspot chain.
- **Mikrotik-Mark-Id** - Firewall mangle chain name (HotSpot only). The MikroTik RADIUS client upon receiving this attribute creates a dynamic firewall mangle rule with action=jump chain=hotspot and jump-target equal to the attribute value. Mangle chain name can have suffixes .in or .out, that will install rule only for incoming or outgoing traffic. Multiple Mark-id attributes can be provided, but only last ones for incoming and outgoing is used.
- **Acct-Interim-Interval** - Interim-update for RADIUS client. PPP - if 0 uses the one specified in RADIUS client. HotSpot - only respected if radius-interim-update=received in HotSpot server profile.
- **MS-MPPE-Encryption-Policy** - Require-encryption property (PPPs only).
- **MS-MPPE-Encryption-Types** - Use-encryption property. Non-zero value means to use encryption (PPPs only).
- **Ascend-Data-Rate** - Tx/rx data rate limitation if multiple attributes are provided, first limits tx data rate, second - rx data rate. If used together with Ascend-Xmit-Rate, specifies rx rate. 0 if unlimited. Ignored if Rate-Limit attribute is present.
- **Ascend-Xmit-Rate** - Tx data rate limitation. It may be used to specify tx limit only instead of sending two sequential Ascend-Data-Rate attributes (in that case Ascend-Data-Rate will specify the receive rate). 0 if unlimited. Ignored if Rate-Limit attribute is present.
- **MS-CHAP2-Success** - Auth. response if MS-CHAPv2 was used (for PPPs only).
- **MS-MPPE-Send-Key, MS-MPPE-Recv-Key** - Encryption keys for encrypted PPPs provided by RADIUS server only if MS-CHAPv2 was used as authentication (for PPPs only).
- **Ascend-Client-Gateway** - Client gateway for DHCP-pool HotSpot login method (HotSpot only).
- **Mikrotik-Recv-Limit** - Total receive limit in bytes for the client.
- **Mikrotik-Recv-Limit-Gigawords** - 4G (2^32) bytes of total receive limit (bits 32..63, when bits 0..31 are delivered in Mikrotik-Recv-Limit).
- **Mikrotik-Xmit-Limit** - Total transmit limit in bytes for the client.
- **Mikrotik-Xmit-Limit-Gigawords** - 4G (2^32) bytes of total transmit limit (bits 32..63, when bits 0..31 are delivered in Mikrotik-Xmit-Limit).
- **Mikrotik-Wireless-Forward** - Does not forward the client's frames back to the wireless infrastructure if this attribute is set to "0" (Wireless only).
- **Mikrotik-Wireless-Skip-Dot1x** - Disables 802.1x authentication for the particular wireless client if set to non-zero value (Wireless only).
- **Mikrotik-Wireless-Enc-Algo** - WEP encryption algorithm: 0 - no encryption, 1 - 40-bit WEP, 2 - 104-bit WEP (Wireless only).
- **Mikrotik-Wireless-Enc-Key** - WEP encryption key for the client (Wireless only).
- **Mikrotik-Wireless-VLANID** - VLAN ID for the client (Wireless only).
- **Mikrotik-Wireless-VLANID-type** - VLAN ID type for the client. 0 - 802.1q tag and 1 - 802.1ad tag (Wireless only).
- **Mikrotik-Switching-Filter** - Allows creating dynamic switch rules, when authenticating clients with dot1x server.
- **Mikrotik-Rate-Limit** - Datarate limitation for clients. Format is: rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]] from the point of view of the router (so "rx" is client upload, and "tx" is client download). All rates should be numbers with optional 'k' (1,000s) or 'M' (1,000,000s). If tx-rate is not specified, rx-rate is as tx-rate too. Same goes for tx-burst-rate and tx-burst-threshold and tx-burst-time. If both rx-burst-threshold and tx-burst-threshold are not specified (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds. If both rx-burst-time and tx-burst-time are not specified, 1s is used as default. Priority takes values 1..8, where 1 implies the highest priority, but 8 - the lowest. If rx-rate-min and tx-rate-min are not specified rx-rate and tx-rate values are used. The rx-rate-min and tx-rate-min values can not exceed rx-rate and tx-rate values.
- **Mikrotik-Group** - Router local user group name (defined in `/user/group`) for local users; HotSpot default profile for HotSpot users; PPP default profile name for PPP users.
- **Mikrotik-Advertise-URL** - URL of the page with advertisements that should be displayed to clients. If this attribute is specified, advertisements are enabled automatically, including transparent proxy, even if they were explicitly disabled in the corresponding user profile. Multiple attribute instances may be sent by RADIUS server to specify additional URLs which are chosen in round robin fashion.
- **Mikrotik-Advertise-Interval** - Time interval between two adjacent advertisements. Multiple attribute instances may be sent by RADIUS server to specify additional intervals. All interval values are treated as a list and are taken one-by-one for each successful advertisement. If end of list is reached, the last value is continued to be used.
- **WISPr-Redirection-URL** - URL, which the clients will be redirected to after successful login.
- **WISPr-Bandwidth-Min-Up** - Minimal datarate (CIR) provided for the client upload.
- **WISPr-Bandwidth-Min-Down** - Minimal datarate (CIR) provided for the client download.
- **WISPr-Bandwidth-Max-Up** - Maximal datarate (MIR) provided for the client upload.
- **WISPr-Bandwidth-Max-Down** - Maximal datarate (MIR) provided for the client download.
- **WISPr-Session-Terminate-Time** - Time, when the user should be disconnected; in "YYYY-MM-DDThh:mm:ssTZD" form, where Y - year; M - month; D - day; T - separator symbol (must be written between date and time); h - hour (in 24 hour format); m - minute; s - second; TZD - time zone in one of these forms: "+hh:mm", "+hhmm", "-hh:mm", "-hhmm".

The received attributes override the default ones (set in the default profile), but if an attribute is not received from the RADIUS server, the default one is to be used.  Rate-Limit takes precedence over all other ways to specify data rate for the client. Ascend data rate attributes are considered second; and WISPr attributes take the last precedence.

Here are some Rate-Limit examples:

- **128k** - rx-rate=128000, tx-rate=128000 (no bursts).
- **64k/128M** - rx-rate=64000, tx-rate=128000000.
- **64k 256k** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=64000, rx/tx-burst-time=1s.
- **64k/64k 256k/256k 128k/128k 10/10** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=128000, rx/tx-burst-time=10s.

### Accounting-Request packet

The accounting request carries the same attributes as Access Request, plus these ones:

- **Acct-Status-Type** - Start, Stop, or Interim-Update.
- **Acct-Authentic** - Either authenticated by RADIUS or Local authority (PPPs only).
- **Class** - RADIUS server cookie, as received in Access-Accept.
- **Acct-Delay-Time** - How long the router tries to send this Accounting-Request packet.

### Stop and Interim-Update Accounting-Request packet

In addition to the accounting start request, the following messages will contain the following attributes:

- **Acct-Session-Time** - Connection uptime in seconds.
- **Acct-Input-Octets** - Bytes received from the client.
- **Acct-Input-Gigawords** - 4G (2^32) bytes received from the client (bits 32..63, when bits 0..31 are delivered in Acct-Input-Octets).
- **Acct-Input-Packets** - Number of packets received from the client.
- **Acct-Output-Octets** - Bytes sent to the client.
- **Acct-Output-Gigawords** - 4G (2^32) bytes sent to the client (bits 32..63, when bits 0..31 are delivered in Acct-Output-Octets).
- **Acct-Output-Packets** - Number of packets sent to the client.

:::warning
RADIUS accounting messages in RouterOS represent output as traffic from the client point of view, for example, for VPN user "test" output is user upload.

:::

### **Stop Accounting-Request packet**

These packets will, in addition to the Interim Update packets, have:

- **Acct-Terminate-Cause** - session termination cause (see RFC 2866 ch. 5.10)
  
  ### **Change of Authorization**

RADIUS disconnect and Change of Authorization (according to RFC3576) are supported as well. These attributes may be changed by a CoA request from the RADIUS server:

- **Mikrotik-Group**
- **Mikrotik-Recv-Limit**
- **Mikrotik-Xmit-Limit**
- **Mikrotik-Rate-Limit**
- **Ascend-Data-Rate** (only if Mikrotik-Rate-Limit is not present)
- **Ascend-XMit-Rate** (only if Mikrotik-Rate-Limit is not present)
- **Mikrotik-Mark-Id**
- **Filter-Id**
- **Mikrotik-Advertise-Url**
- **Mikrotik-Advertise-Interval**
- **Session-Timeout**
- **Idle-Timeout**
- **Port-Limit**

Note that it is not possible to change the IP address, the pool or routes that way - for such changes a user must be disconnected first.

## MikroTik Specific RADIUS Attribute Numeric Values

| Name                                    | VendorID | Value | RFC |
|:-- | --:| --:|:-- |
| **MIKROTIK\_RECV\_LIMIT**               | 14988    | 1     |     |
| **MIKROTIK\_XMIT\_LIMIT**               | 14988    | 2     |     |
| **MIKROTIK\_GROUP**                     | 14988    | 3     |     |
| **MIKROTIK\_WIRELESS\_FORWARD**         | 14988    | 4     |     |
| **MIKROTIK\_WIRELESS\_SKIPDOT1X**       | 14988    | 5     |     |
| **MIKROTIK\_WIRELESS\_ENCALGO**         | 14988    | 6     |     |
| **MIKROTIK\_WIRELESS\_ENCKEY**          | 14988    | 7     |     |
| **MIKROTIK\_RATE\_LIMIT**               | 14988    | 8     |     |
| **MIKROTIK\_REALM**                     | 14988    | 9     |     |
| **MIKROTIK\_HOST\_IP**                  | 14988    | 10    |     |
| **MIKROTIK\_MARK\_ID**                  | 14988    | 11    |     |
| **MIKROTIK\_ADVERTISE\_URL**            | 14988    | 12    |     |
| **MIKROTIK\_ADVERTISE\_INTERVAL**       | 14988    | 13    |     |
| **MIKROTIK\_RECV\_LIMIT\_GIGAWORDS**    | 14988    | 14    |     |
| **MIKROTIK\_XMIT\_LIMIT\_GIGAWORDS**    | 14988    | 15    |     |
| **MIKROTIK\_WIRELESS\_PSK**             | 14988    | 16    |     |
| **MIKROTIK\_TOTAL\_LIMIT**              | 14988    | 17    |     |
| **MIKROTIK\_TOTAL\_LIMIT\_GIGAWORDS**   | 14988    | 18    |     |
| **MIKROTIK\_ADDRESS\_LIST**             | 14988    | 19    |     |
| **MIKROTIK\_WIRELESS\_MPKEY**           | 14988    | 20    |     |
| **MIKROTIK\_WIRELESS\_COMMENT**         | 14988    | 21    |     |
| **MIKROTIK\_DELEGATED\_IPV6\_POOL**     | 14988    | 22    |     |
| **MIKROTIK\_DHCP\_OPTION\_SET**         | 14988    | 23    |     |
| **MIKROTIK\_DHCP\_OPTION\_PARAM\_STR1** | 14988    | 24    |     |
| **MIKROTIK\_DHCP\_OPTION\_PARAM\_STR2** | 14988    | 25    |     |
| **MIKROTIK\_WIRELESS\_VLANID**          | 14988    | 26    |     |
| **MIKROTIK\_WIRELESS\_VLANIDTYPE**      | 14988    | 27    |     |
| **MIKROTIK\_WIRELESS\_MINSIGNAL**       | 14988    | 28    |     |
| **MIKROTIK\_WIRELESS\_MAXSIGNAL**       | 14988    | 29    |     |
| **Mikrotik-Switching-Filter** | 14988 | 30 |

## All Supported Attribute Numeric Values

| Name                                   | VendorID | Value | RFC                           |
|:-- |:-- | --:|:-- |
| **Acct-Authentic**                     |          | 45    | RFC 2866                      |
| **Acct-Delay-Time**                    |          | 41    | RFC 2866                      |
| **Acct-Input-Gigawords**               |          | 52    | RFC 2869                      |
| **Acct-Input-Octets**                  |          | 42    | RFC 2866                      |
| **Acct-Input-Packets**                 |          | 47    | RFC 2866                      |
| **Acct-Interim-Interval**              |          | 85    | RFC 2869                      |
| **Acct-Output-Gigawords**              |          | 53    | RFC 2869                      |
| **Acct-Output-Octets**                 |          | 43    | RFC 2866                      |
| **Acct-Output-Packets**                |          | 48    | RFC 2866                      |
| **Acct-Session-Id**                    |          | 44    | RFC 2866                      |
| **Acct-Session-Time**                  |          | 46    | RFC 2866                      |
| **Acct-Status-Type**                   |          | 40    | RFC 2866                      |
| **Acct-Terminate-Cause**               |          | 49    | RFC 2866                      |
| **Ascend-Client-Gateway**              | 529      | 132   |                               |
| **Ascend-Data-Rate**                   | 529      | 197   |                               |
| **Ascend-Xmit-Rate**                   | 529      | 255   |                               |
| **Called-Station-Id**                  |          | 30    | RFC 2865                      |
| **Calling-Station-Id**                 |          | 31    | RFC 2865                      |
| **CHAP-Challenge**                     |          | 60    | RFC 2866                      |
| **CHAP-Password**                      |          | 3     | RFC 2865                      |
| **Class**                              |          | 25    | RFC 2865                      |
| **Filter-Id**                          |          | 11    | RFC 2865                      |
| **Framed-Compression**                 |          | 13    | RFC 2865                      |
| **Framed-IP-Address**                  |          | 8     | RFC 2865                      |
| **Framed-IP-Netmask**                  |          | 9     | RFC 2865                      |
| **Framed-IPv6-Prefix**                 |          | 97    | RFC 3162                      |
| **Framed-Mtu**                         |          | 12    | RFC 2865                      |
| **Framed-Pool**                        |          | 88    | RFC 2869                      |
| **Framed-Protocol**                    |          | 7     | RFC 2865                      |
| **Framed-Route**                       |          | 22    | RFC 2865                      |
| **Framed-Routing**                     |          | 10    | RFC 2865                      |
| **Idle-Timeout**                       |          | 28    | RFC 2865                      |
| **MS-CHAP-Challenge**                  | 311      | 11    | RFC 2548                      |
| **MS-CHAP-Domain**                     | 311      | 10    | RFC 2548                      |
| **MS-CHAP-Response**                   | 311      | 1     | RFC 2548                      |
| **MS-CHAP2-Response**                  | 311      | 25    | RFC 2548                      |
| **MS-CHAP2-Success**                   | 311      | 26    | RFC 2548                      |
| **MS-MPPE-Encryption-Policy**          | 311      | 7     | RFC 2548                      |
| **MS-MPPE-Encryption-Types**           | 311      | 8     | RFC 2548                      |
| **MS-MPPE-Recv-Key**                   | 311      | 17    | RFC 2548                      |
| **MS-MPPE-Send-Key**                   | 311      | 16    | RFC 2548                      |
| **NAS-Identifier**                     |          | 32    | RFC 2865                      |
| **NAS-Port**                           |          | 5     | RFC 2865                      |
| **NAS-IP-Address**                     |          | 4     | RFC 2865                      |
| **NAS-Port-Id**                        |          | 87    | RFC 2869                      |
| **NAS-Port-Type**                      |          | 61    | RFC 2865                      |
| **Port-Limit**                         |          | 62    | RFC 2865                      |
| **Redback-Agent-Remote-Id**            | 2352     | 96    |                               |
| **Redback-Agent-Circuit-Id**           | 2352     | 97    |                               |
| **Service-Type**                       |          | 6     | RFC 2865                      |
| **Session-Timeout**                    |          | 27    | RFC 2865                      |
| **User-Name**                          |          | 1     | RFC 2865                      |
| **User-Password**                      |          | 2     | RFC 2865                      |
| **WISPr-Bandwidth-Max-Down**           | 14122    | 8     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Max-Up**             | 14122    | 7     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Down**           | 14122    | 6     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Bandwidth-Min-Up**             | 14122    | 5     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Id**                  | 14122    | 1     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Location-Name**                | 14122    | 2     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Logoff-URL**                   | 14122    | 3     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Redirection-URL**              | 14122    | 4     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-Time**       | 14122    | 9     | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Session-Terminate-End-Of-Day** | 14122    | 10    | [wi-fi.org](https://www.wi-fi.org/) |
| **WISPr-Billing-Class-Of-Service**     | 14122    | 11    | [wi-fi.org](https://www.wi-fi.org/) |
|                      |          |       |                               |
