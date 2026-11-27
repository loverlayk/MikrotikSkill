# Enterprise Wi-Fi and MAC authentication with User Manager

> Log Wi-Fi users in with their own user name and password (WPA2/WPA3-Enterprise) and let devices without a login in by MAC address, with User Manager on the CAPsMAN router: certificates, User Manager users and...

# Enterprise Wi-Fi and MAC authentication with User Manager

**Packages:** `wifi-qcom`, `wifi-qcom-ac`, `user-manager`

With one shared Wi-Fi passphrase, everybody who leaves the company still knows it. With WPA2/WPA3-Enterprise each person logs in with their own user name and password, which User Manager checks. Devices that cannot log in this way, such as printers and sensors, join a separate SSID with a passphrase, and only the devices whose MAC address is on the list are let in.

This guide sets up both on a CAPsMAN network, with [User Manager](../../authentication-authorization-accounting/user-manager) on the CAPsMAN router as the RADIUS server:

- the `Staff` SSID with WPA2/WPA3-Enterprise and the users `mario` and `normie`;
- the `IoT` SSID with a passphrase and MAC address authentication.

## Before you begin

- The access points are CAPs of a CAPsMAN router, set up as in [Steering clients between access points](./configuring-steering). This guide uses the channel profiles `ch-5g` and `ch-2g` and the steering profile `steer-office` from that guide, and replaces its provisioning rules.
- The CAPsMAN router has the address `192.168.99.1` and the `user-manager` package installed.

When an access point is a CAP, the CAPsMAN router sends the RADIUS requests for all access points. The access points need no RADIUS configuration, and User Manager needs only the CAPsMAN router as its client.

## Create the certificates

User Manager shows a server certificate to the clients when they log in. On the CAPsMAN router, create a certificate authority and a server certificate signed by it:

```ros
/certificate
add name=office-ca common-name=office-ca days-valid=3650 \
    key-usage=key-cert-sign,crl-sign
sign office-ca
add name=radius common-name=radius.office.lan \
    subject-alt-name=DNS:radius.office.lan days-valid=825 \
    key-usage=digital-signature,key-encipherment,tls-server
sign radius ca=office-ca
export-certificate office-ca file-name=office-ca
```

The last line saves the certificate of `office-ca`, without its private key, as the file `office-ca.crt`. The clients use it to check that they talk to your server.

## Set up User Manager

Turn User Manager on with the server certificate and add the CAPsMAN router as its client. Create two groups: people log in only with PEAP, devices only with the MAC address check. Add the users and the devices. A device is a user named after its MAC address, in the format that the access points send (see the next section), and has no password; add one line for each device. Then point the RADIUS client of the router for Wi-Fi to User Manager:

```ros
/user-manager
set enabled=yes certificate=radius
/user-manager/router
add name=capsman address=192.168.99.1 shared-secret=change-this-secret
/user-manager/user/group
add name=staff outer-auths=eap-peap inner-auths=peap-mschap2
add name=devices outer-auths=pap
/user-manager/user
add name=mario password=Mario-Pass-1 group=staff
add name=normie password=Normie-Pass-1 group=staff
add name=48a98ae02ca8 group=devices comment="IoT sensor"
/radius
add service=wireless address=192.168.99.1 src-address=192.168.99.1 \
    secret=change-this-secret
```

## Configure the SSIDs

First, on each access point, add the datapath to the virtual interfaces too, so that `IoT` clients reach the LAN:

```ros
/interface/wifi/cap
set slaves-datapath=capdp
```

On the CAPsMAN router, create the security profiles of both SSIDs and an AAA profile that sets the format of the MAC address in the requests. The access list sends every client of the `IoT` SSID to RADIUS before it can connect. The provisioning rules put `Staff` on each radio and `IoT` next to it as a virtual interface. The new rules replace those of the steering guide, so its `Office` SSID goes away, and its clients have to join `Staff`. The last line applies the rules to the access points that are already connected.

```ros
/interface/wifi/security
add name=sec-staff authentication-types=wpa2-eap,wpa3-eap ft=yes
add name=sec-iot authentication-types=wpa2-psk,wpa3-psk \
    passphrase="change-this-passphrase"
/interface/wifi/aaa
add name=aaa-iot username-format=aaaaaaaaaaaa
/interface/wifi/configuration
add name=cfg-staff-5g ssid=Staff country=Latvia security=sec-staff \
    channel=ch-5g
add name=cfg-staff-2g ssid=Staff country=Latvia security=sec-staff \
    channel=ch-2g
add name=cfg-iot ssid=IoT country=Latvia security=sec-iot aaa=aaa-iot
/interface/wifi/access-list
add ssid-regexp="^IoT\$" action=query-radius
/interface/wifi/provisioning
remove [find]
add action=create-dynamic-enabled supported-bands=5ghz-ax \
    master-configuration=cfg-staff-5g slave-configurations=cfg-iot \
    name-format=%I-5g slave-name-format=%m-iot
add action=create-dynamic-enabled supported-bands=5ghz-ac \
    master-configuration=cfg-staff-5g slave-configurations=cfg-iot \
    name-format=%I-5g slave-name-format=%m-iot
add action=create-dynamic-enabled supported-bands=2ghz-ax \
    master-configuration=cfg-staff-2g slave-configurations=cfg-iot \
    name-format=%I-2g slave-name-format=%m-iot
add action=create-dynamic-enabled supported-bands=2ghz-n \
    master-configuration=cfg-staff-2g slave-configurations=cfg-iot \
    name-format=%I-2g slave-name-format=%m-iot
/interface/wifi/capsman/remote-cap
provision [find]
```

What the settings do:

- `wpa2-eap,wpa3-eap` makes `Staff` an Enterprise SSID. The client logs in with a user name and password, and User Manager checks them.
- `username-format=aaaaaaaaaaaa` sends the MAC address of the client as 12 lowercase hexadecimal digits, for example `48a98ae02ca8`. The default format is `AA:AA:AA:AA:AA:AA`. The device users in User Manager have to use the same format.
- `action=query-radius` asks RADIUS about each client of `IoT`. A client whose MAC address User Manager does not know cannot connect, even with the right passphrase. Phones and laptops often use a private MAC address for each network; a device on the list has to use its own address.
- `slave-name-format=%m-iot` names the `IoT` interface after the `Staff` interface of the same radio, for example `ap-meeting-5g-iot`.
- `IoT` clients are in the same LAN as `Staff` clients. To put them in a network of their own, use a VLAN as in [CAPsMAN](./capsman).
- `Staff` has no steering profile. The access points do not build a neighbor group for an SSID with EAP; see [Steering properties](./#steering-properties).

The format characters of `username-format` are described in [AAA properties](./#aaa-properties).

## Connect a client

Copy `office-ca.crt` from the router's files to the client and install it as a certificate authority for Wi-Fi. Then choose `Staff` and enter the user name and password. Where the device asks, choose PEAP with MSCHAPv2, the CA certificate `office-ca`, and the domain `radius.office.lan`. A device that does not have the CA certificate shows the server certificate `radius.office.lan`, issued by `office-ca`, and asks whether to trust it. The notes for Windows, Android and iOS in [Enterprise wireless security with User Manager](../user-guides/enterprise-wireless-security-user) apply.

## Check that it works

The registration table shows each client with its SSID and the interface, and so the access point, it is connected to:

```ros
/interface/wifi/registration-table/print
```

```text
Flags: A - AUTHORIZED
Columns: INTERFACE, SSID, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL
#   INTERFACE          SSID   MAC-ADDRESS        UPTIME  LAST-AC  SIGNAL
0 A ap-reception-5g    Staff  F2:EB:8E:EB:A2:53  45s     0ms      -68   
1 A ap-meeting-5g-iot  IoT    48:A9:8A:E0:2C:A8  23s     15s20ms  -35
```

User Manager shows the active sessions of the users. `nas-port-id` is the interface, and so the access point, the user is connected to, and `calling-station-id` is the MAC address of the client in the registration table. Devices that connect by MAC address have no session:

```ros
/user-manager/session/print where active
```

```text
Flags: A - ACTIVE
0  A user=normie acct-session-id="82000030" nas-port-type=wireless-802.11
     nas-port-id="ap-reception-5g" nas-ip-address=192.168.99.1
     nas-identifier="CCR2116" calling-station-id="F2-EB-8E-EB-A2-53"
     status=start started=2026-11-26 13:42:42 uptime=0s download=0 upload=0
     last-accounting-packet=2026-11-26 13:42:42
```

To see refused logins, log the User Manager messages and print the refusals. In this output a user logged in with a wrong password:

```ros
/system/logging/add topics=manager
/log/print where topics~"manager" and message~"reject"
```

```text
 2026-11-26 13:43:41 manager,debug EAP rejected for user: <normie> 
 2026-11-26 13:43:49 manager,debug EAP rejected for user: <normie>
```

The log then holds every RADIUS request and reply. Remove the logging rule when you are done:

```ros
/system/logging/remove [find topics=manager]
```

The counters of the RADIUS client show how many logins were accepted and refused. `0` is the number of the RADIUS client entry in `/radius`. A PEAP login takes several requests, and `challenges` counts the replies between them:

```ros
/radius/monitor 0 once
```

```text
               pending: 0   
              requests: 71  
               accepts: 5   
               rejects: 6   
            challenges: 56  
  accounting-responses: 4   
         other-replies: 0   
               resends: 0   
              timeouts: 0   
           bad-replies: 0   
      last-request-rtt: 10ms
```
