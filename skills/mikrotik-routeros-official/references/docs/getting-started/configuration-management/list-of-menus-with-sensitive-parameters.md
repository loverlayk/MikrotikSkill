# List of menus with sensitive parameters

> This page lists MikroTik RouterOS menus where sensitive parameters such as passwords, keys, and secrets are configured, with links to detailed documentation for each.

# List of menus with sensitive parameters

Below you can find a list of menus where sensitive (shown only when [show-sensitive parameter](./index.md#configuration-export) is used or alternatively hidden when "Hide password" is enabled in WinBox settings) parameters can be configured. For more detailed information, please refer to the corresponding menu documentation pages.

| Menu | Parameter names | Page link |
| :-- | :-- | :-- |
| `/container` | password | [Container#Containerconfiguration](../../containers/index.md) |
| `/ip/hotspot` | mac-auth-password, password, otp-secret | [HotSpot - Captive portal#HotSpotUsers](../../authentication-authorization-accounting/hotspot-captive-portal/index.md) |
| `/iot` | password, key | password - [MQTT#Brokers](../../internet-of-things/mqtt/index.md)  key - [Lora#Servers](../../internet-of-things/lora/general-properties.md#servers)|
| `/interface/gre`  `/interface/gre6` | ipsec-secret | [GRE#Properties](../../virtual-private-networks/gre.md) |
| `/interface/ipip`  `/interface/ipipv6` | ipsec-secret | [IPIP#Properties](../../virtual-private-networks/ipip.md) |
| `/interface/eoip`  `/interface/eoipv6` | ipsec-secret | [EoIP#PropertyDescription](../../virtual-private-networks/eoip.md) |
| `/interface/6to4` | ipsec-secret | [6to4#6to4-PropertyDescription](../../virtual-private-networks/6to4.md) |
| `/interface/ppp-client` | password, pin | Work in Progress [PPP](../../mobile-networking/ppp.md) |
| `/interface/sstp-client` | password | [SSTP#Properties](../../virtual-private-networks/sstp.md) |
| `/interface/l2tp-server`  `/interface/l2tp-client`  `/interface/l2tp-ether` | ipsec-secret, password | ipsec-secret, password - [L2TP#L2TPClient](../../virtual-private-networks/l2tp/index.md#l2tp-client)  ipsec-secret - [L2TP#L2TPServer](../../virtual-private-networks/l2tp/index.md#l2tp-server)  ipsec-secret - [L2TP#L2TPEther](../../virtual-private-networks/l2tp/index.md#l2tp-ether)|
| `/interface/ovpn-client` | password | [OpenVPN#OVPNClient](../../virtual-private-networks/openvpn.md) |
| `/interface/pptp-client` | password | [PPTP#PPTPClient](../../virtual-private-networks/pptp.md) |
| `/interface/pppoe-client` | password | [PPPoE#PPPoEClient](../../virtual-private-networks/pppoe/index.md) |
| `/ppp/secret` | password | [PPP AAA#UserDatabase](../../authentication-authorization-accounting/ppp-aaa.md) |
| `/ppp/l2tp-secret` | secret | Work in Progress |
| `/ip/ssh/export-host-key`  `/ip/ssh/import-host-key` | passphrase | [SSH](../../management-tools/ssh#server-host-key) |
| `/ip/ipsec` | auth-key, enc-key, ppk-secret, secret, password, passphrase, key | auth-key, enc-key - [IPsec InstalledSA](../../cli-reference/ip/ipsec/installed-sa/installed-sa.md)  secret, password - [IPsec Identity](../../cli-reference/ip/ipsec/identity.md)  ppk-secret - Work in Progress [IPsec Peer](../../cli-reference/ip/ipsec/peer.md)  key, passphrase - Work in Progress IPsec Keys|
| `/system/ssh-exec` | password | [SSH](../../management-tools/ssh#run-remote-commands-from-scripts) |
| `/user` | password, passphrase | [User](../../authentication-authorization-accounting/user.md) |
| `/disk` | nvme-tcp-server-password, nvme-tcp-password, smb-server-password, smb-password, self-encryption-password, encryption-key, sshfs-password | nvme-tcp-server-password, nvme-tcp-password - [NVMe over TCP](../../storage/nvme-over-tcp.md)  sshfs-password - Work in Progress  smb-server-password, smb-password - [SMB](../../storage/smb.md)  self-encryption-password, encryption-key - [Self-Encrypting Drives](../../storage/self-encrypting-drives.md)|
| `/interface/vrrp` | password | [VRRP#Parameters](../../high-availability-solutions/vrrp.md) |
| `/interface/dot1x` | password | [Dot1X#Client](../../authentication-authorization-accounting/dot1x.md) |
| `/interface/macsec` | cak | [MACsec#PropertyReference](../../bridging-and-switching/macsec.md) |
| `/interface/wireguard` | private-key, preshared-key, \**show-client-config* | [WireGuard](../../virtual-private-networks/wireguard.md) |
| `/interface/lte` | pin, password | [LTE/5G#LTEClient](../../mobile-networking/lte-5g.md#lte-client) |
| `/ip/socks/users` | password | [SOCKS](../../network-management/socks/index.md) |
| `/ip/cloud` | vpn-private-key, vpn-peer-private-key, private-key | [Back To Home](../../network-management/cloud/back-to-home) |
| `/ip/smb` | password | [SMB#Usersetup](../../storage/smb.md) |
| `/password` | old-password, new-password, confirm-new-password | Password change command; no dedicated documentation page available. |
| `/radius` | secret | [RADIUS#RADIUSClient](../../authentication-authorization-accounting/radius.md) |
| `/routing` | password, tcp-md5-key, auth-key, key | password,key - [/routing/rip](../../cli-reference/routing/rip/instance)  tcp-md5-key - [/routing/bgp/connection](../../cli-reference/routing/bgp/connection.md)  auth-key - [/routing/ospf](../../cli-reference/routing/ospf/interface-template.md)|
| `/snmp/community` | authentication-password, encryption-password | [SNMP#CommunityProperties](../../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| `/system/backup` | password | [Backup](./backup.md) |
| `/system/ntp/key` | key-val | Work in Progress [NTP](../../system-information-and-utilities/ntp.md) |
| `/system/swos/password` | new-password, confirm-new-password | SwOS password change command; no dedicated documentation page available. |
| `/system/package/local-update` | password | [Packages#LocalUpdate](../installation-and-upgrade/packages.md) |
| `/system/license` | password | [RouterOS license keys#CHRLicenseLevels](../routeros-licensing/chr/chr-licensing.md#chr-license-levels) |
| `/tool/romon` | secrets | [RoMON#Configuration](../../management-tools/romon.md) |
| `/tool/sms` | sim-pin, secret | [SMS#Receiving](../../mobile-networking/sms.md) |
| `/tool/email` | password | [E-mail](../../system-information-and-utilities/e-mail.md) |
| `/tr069-client` | connection-request-password, password | [TR-069#ConfigurationSettings](../../management-tools/tr-069.md) |
| `/user-manager` | web-private-password, paypal-password, shared-secret, password, otp-secret | shared-secret - [User Manager#Routers](../../authentication-authorization-accounting/user-manager.md#routers)  paypal-password, web-private-password - [User Manager#Advanced](../../authentication-authorization-accounting/user-manager.md#advanced)  password, otp-secret - [User Manager#Users](../../authentication-authorization-accounting/user-manager.md#users)|
| `/interface/wifi` | passphrase, eap-password | [WiFi#SecurityProperties](../../wireless/wifi/index.md) |
| `/caps-man` | private-passphrase, passphrase | private-passphrase - [CAPsMAN#CAPsMANAccess-list](../../wireless/abgn/capsman/index.md#capsman-access-list)  passphrase - [CAPsMAN#CAPsMANconfiguration](../../wireless/abgn/capsman/index.md#capsman-configuration)|
| `/interface/wireless` | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key, management-protection-key, nv2-preshared-key, private-key, private-pre-shared-key, wpa-pre-shared-key, wpa2-pre-shared-key, mschapv2-password | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key - [Wireless Interface#WEPproperties](../../wireless/index.md)  management-protection-key, private-key, private-pre-shared-key - [Wireless Interface#Properties](../../wireless/index.md)  wpa-pre-shared-key, wpa2-pre-shared-key - [Wireless Interface#WPAproperties](../../wireless/index.md)  mschapv2-password - [Wireless Interface#WPAEAPproperties](../../wireless/index.md)  nv2-preshared-key - [Wireless Interface#Generalinterfaceproperties](../../wireless/index.md) |
| `/interface/w60g` | password | [W60G#Generalinterfaceproperties](../../wireless/w60g/index.md) |
| `/zerotier` | identity | [ZeroTier#Parameters](../../virtual-private-networks/zerotier.md) |
| `/certificate` | export-passphrase, passphrase, challenge-password, pin, key-passphrase, challenge-passphrase | pin - used for card-reinstall and card-verify commands, no dedicated documentation page available.  export-passphrase - [Certificates#ExportCertificate](../../authentication-authorization-accounting/certificates.md#export-certificate)  passphrase - [Certificates#ImportCertificate](../../authentication-authorization-accounting/certificates.md#import-certificate)  challenge-password, key-passphrase, challenge-passphrase - Work in progress |
