# Per-device passphrases and VLANs on one SSID

> Give groups of devices their own passphrase on one SSID (PPSK, multi-passphrase): staff laptops, IoT devices and guests share the SSID but use different passphrases, IoT devices and guests are put in their own VLANs...

# Per-device passphrases and VLANs on one SSID

**Package:** `wifi-qcom`

With one passphrase for the whole Wi-Fi network, changing it means entering the new passphrase on every laptop, printer and sensor. With per-device passphrases (PPSK, `multi-passphrase` in RouterOS), one SSID accepts several passphrases. A passphrase can belong to one device or to a group of devices, and the access point treats each client by the passphrase it used: it can put the client in a VLAN, isolate it from other clients, or stop accepting the passphrase on a given date.

This guide sets up one SSID, `Office`, with three passphrases:

- staff laptops, in the office LAN;
- printers and sensors, in VLAN 30;
- guests, in VLAN 40, isolated from each other, valid until a set date.

The router lets the IoT devices and the guests reach the router itself, but not the office LAN.

## Before you begin

- The CAPsMAN router has the LAN bridge `bridge` with the address `192.168.99.1`, and it is the router of the LAN.
- Each access point has its LAN port in a bridge named `bridge` and an address in the LAN. The access points become CAPs of the CAPsMAN router in this guide. For CAPsMAN in general, see [CAPsMAN](./capsman).
- The access points use the `wifi-qcom` package. They take the VLAN of a passphrase from CAPsMAN and need no VLAN configuration of their own. Access points with the `wifi-qcom-ac` package do not accept clients of a passphrase with a VLAN; see the caution at `vlan-id` in [Security multi-passphrase properties](./#security-multi-passphrase-properties).
- VLAN filtering is off on the bridges of the router and the access points, and the switches between them pass tagged frames. With VLAN filtering on, add the VLANs to the bridge VLAN table as in the VLAN example of [CAPsMAN](./capsman).

## Create the SSID and the passphrases

On the CAPsMAN router, add the passphrases to a group, create a security profile that uses the group, and create the `Office` SSID with it. The provisioning rules put the SSID on the 5 GHz and 2.4 GHz radios of the access points:

```ros
/interface/wifi/security/multi-passphrase
add group=office-keys passphrase="change-this-staff-passphrase" \
    comment=staff
add group=office-keys passphrase="change-this-iot-passphrase" \
    comment=iot
add group=office-keys passphrase="change-this-guest-passphrase" \
    comment=guest expires="2026-12-31 18:00:00"
/interface/wifi/security
add name=sec-ppsk authentication-types=wpa2-psk \
    multi-passphrase-group=office-keys
/interface/wifi/configuration
add name=cfg-office ssid=Office country=Latvia security=sec-ppsk
/interface/wifi/provisioning
add action=create-dynamic-enabled supported-bands=5ghz-ax \
    master-configuration=cfg-office name-format=%I-5g
add action=create-dynamic-enabled supported-bands=2ghz-ax \
    master-configuration=cfg-office name-format=%I-2g
/interface/wifi/capsman
set enabled=yes interfaces=bridge
```

On each access point, create a datapath that adds the Wi-Fi interfaces to the bridge, turn on the CAP service and hand the radios to CAPsMAN:

```ros
/interface/wifi/datapath
add name=capdp bridge=bridge
/interface/wifi/cap
set enabled=yes caps-man-addresses=192.168.99.1 \
    discovery-interfaces=none
/interface/wifi
set [find] configuration.manager=capsman datapath=capdp
```

What the settings do:

- Each entry of the group `office-keys` is a passphrase that the SSID accepts. The comment names the device or group of devices that uses it.
- `expires` sets the date and time, on the clock of the CAPsMAN router, after which the access point disconnects the clients of the passphrase and no longer accepts it. Keep the router clock correct, for example with NTP.
- `authentication-types=wpa2-psk`: the passphrases of a group work with WPA2-PSK, not with WPA3-PSK; see [Security multi-passphrase properties](./#security-multi-passphrase-properties). A client that allows only WPA3-PSK cannot connect.
- `country` sets the regulatory rules for the radios. Set it to the country where the access points are installed.
- When an SSID that already has clients changes to PPSK, use its old passphrase as the staff entry, so the staff laptops keep working.

## Check which passphrase a client uses

The registration table shows the comment of the passphrase entry above each client:

```ros
/interface/wifi/registration-table/print detail
```

```text
Flags: A - AUTHORIZED
0  A ;;; guest
     interface=ap-meeting-5g ssid="Office" mac-address=02:00:00:00:40:01
     uptime=3s signal=-35 auth-type=wpa2-psk mfp=yes band=5ghz-ac
 
1  A ;;; iot
     interface=ap-meeting-5g ssid="Office" mac-address=02:00:00:00:30:01
     uptime=1s signal=-23 auth-type=wpa2-psk mfp=yes band=5ghz-ax
```

## Put IoT devices and guests in their own VLANs

On the CAPsMAN router, create a VLAN interface on the LAN bridge for each VLAN, with an address, a DHCP server and the router as DNS server. Then give the IoT and guest passphrases their VLAN, and isolate the guests:

```ros
/interface/vlan
add name=vlan30-iot vlan-id=30 interface=bridge
add name=vlan40-guest vlan-id=40 interface=bridge
/ip/address
add address=192.168.30.1/24 interface=vlan30-iot
add address=192.168.40.1/24 interface=vlan40-guest
/ip/pool
add name=pool-iot ranges=192.168.30.100-192.168.30.200
add name=pool-guest ranges=192.168.40.100-192.168.40.200
/ip/dhcp-server
add name=dhcp-iot interface=vlan30-iot address-pool=pool-iot
add name=dhcp-guest interface=vlan40-guest address-pool=pool-guest
/ip/dhcp-server/network
add address=192.168.30.0/24 gateway=192.168.30.1 dns-server=192.168.30.1
add address=192.168.40.0/24 gateway=192.168.40.1 dns-server=192.168.40.1
/ip/dns
set allow-remote-requests=yes
/interface/wifi/security/multi-passphrase
set [find comment=iot] vlan-id=30
set [find comment=guest] vlan-id=40 isolation=yes
```

What the settings do:

- `vlan-id` puts the clients of the passphrase in that VLAN. The access point sends their traffic tagged to the router, and the router gives them an address from the DHCP server of the VLAN.
- `isolation=yes` stops the guests from reaching each other through the access point. It works between the clients of one access point; guests on different access points meet in VLAN 40 on the router.
- Clients without a VLAN, here the staff laptops, stay in the office LAN.
- Changing an entry disconnects the clients that use it; they connect again with the new settings.

## Keep the VLANs out of the office LAN

The router routes between its networks, so the IoT devices and the guests reach the office LAN through it. Drop that traffic in the forward chain, and keep the guests away from the IoT devices:

```ros
/ip/firewall/filter
add chain=forward in-interface=vlan30-iot out-interface=bridge \
    action=drop comment="IoT to office LAN"
add chain=forward in-interface=vlan40-guest out-interface=bridge \
    action=drop comment="guests to office LAN"
add chain=forward in-interface=vlan40-guest out-interface=vlan30-iot \
    action=drop comment="guests to IoT"
```

Put these rules before any rule in the forward chain that accepts the traffic. The rules do not block the traffic to the router itself, so the clients still get addresses and DNS from it.

## Check the VLANs

The DHCP leases show the VLAN, by its DHCP server, of each client:

```ros
/ip/dhcp-server/lease/print \
    proplist=address,mac-address,host-name,server
```

```text
Flags: D - DYNAMIC
Columns: ADDRESS, MAC-ADDRESS, HOST-NAME, SERVER
#   ADDRESS         MAC-ADDRESS        HOST-NAME     SERVER    
0 D 192.168.40.197  02:00:00:00:40:01  guest-tablet  dhcp-guest
1 D 192.168.30.101  02:00:00:00:30:01  iot-sensor    dhcp-iot
```

The counters of the firewall rules show the dropped connection attempts:

```ros
/ip/firewall/filter/print stats where chain=forward
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION  BYTES  PACKETS
;;; IoT to office LAN
0 forward  drop      168        3
;;; guests to office LAN
1 forward  drop      168        3
;;; guests to IoT
2 forward  drop      168        3
```

## Revoke or replace a passphrase

When a passphrase leaks, or a group of devices is retired, disable its entry. The access point disconnects the clients that use it immediately and does not let them connect again with it. The other passphrases keep working:

```ros
/interface/wifi/security/multi-passphrase
disable [find comment=guest]
```

The log of the CAPsMAN router shows the disconnected clients:

```ros
/log/print where message~"multi-passphrase changed"
```

```text
 2026-11-27 06:38:48 wireless,info 02:00:00:00:40:01@ap-meeting-5g(Office) disconnected, multi-passphrase changed, signal strength -34, channel 5700/ax/eeCe/D
```

To give the guests a new passphrase, set it on the same entry and enable the entry again:

```ros
/interface/wifi/security/multi-passphrase
set [find comment=guest] passphrase="change-this-new-guest-passphrase" \
    expires="2027-01-31 18:00:00" disabled=no
```

The passphrases, the 10000-passphrase limit and the use of passphrase groups in the access list are described in [Security multi-passphrase properties](./#security-multi-passphrase-properties).
