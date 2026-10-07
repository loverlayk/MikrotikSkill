# CRS3xx and CSS3xx Series Manual

> SwOS is an operating system designed specifically for the administration of MikroTik switch products. It provides fundamental managed switch functionalities alongside advanced features such as port-to-port...

# CRS3xx and CSS3xx Series Manual

## Summary

SwOS is an operating system designed specifically for the administration of MikroTik switch products. It provides fundamental managed switch functionalities alongside advanced features such as port-to-port forwarding, broadcast storm control, MAC/IP/port filtering via ACL rules, VLAN configuration, traffic mirroring, and bandwidth limitation.

SwOS is managed exclusively through a web browser (HTTP) over IPv4. Console access, SSH, API, or other management interfaces are not supported.

---

## Connecting to the Switch

Open a web browser and enter the default management IP address.

![Swos login css326](./img/crs3-01.webp)

* **Default IP Address**: `192.168.88.1`
* **Default Username**: `admin`
* **Default Password**: *(blank)*

---

## System Tab

The System tab manages general configuration parameters, device discovery options, and administrative security.

![Swos system css326](./img/crs3-02.webp)

### System Management Settings

| Property | Description |
| :--- | :--- |
| **Address Acquisition** | Defines IP assignment via static settings, DHCP with fallback, or DHCP only. |
| **Static IP Address** | Specifies the static IPv4 address for management access. |
| **Identity** | Sets a customizable name for the switch identifier. |
| **Allow From** | Restricts management web access to specified IP ranges or subnets. |
| **Allow From Ports** | Limits web access to designated physical switch interfaces. |
| **Allow From VLAN** | Restricts access to a specific incoming VLAN ID profile. |

![SwOS Management](./img/crs3-03.webp)

### DHCP & PPPoE Snooping

SwOS features built-in security mechanics to block unauthorized or rogue DHCP servers and PPPoE discovery sequences on specified untrusted interfaces.

![CSS326 DHCP Snooping](./img/crs3-04.webp)

### Configuration Security and Maintenance

The lower section handles backups and administrative passwords.

![Swos system3 css326](./img/crs3-05.webp)

* **Change Password**: Updates the device access keys.
* **Backup Configuration**: Saves current settings to a local file.
* **Restore Configuration**: Uploads and applies existing configuration states.

---

## Link Tab

The Link tab configures physical link parameters and monitors active connection properties for each interface.

![Swos link css326](./img/crs3-06.webp)

* **Link Profiles**: Manage interface states, toggle speed/duplex auto-negotiation, and control flow control pause frames.

---

## PoE Tab

*(Available on devices supporting Power over Ethernet distribution features)*

![SwOS PoE](./img/crs3-07.webp)

* Supports configuring power delivery settings (`auto`, `on`, `off`) and establishing port prioritization during power constraint events.

---

## SFP Tab

Provides visual diagnostics for connected SFP/SFP+ optical transceivers.

![Swos sfp1 css326](./img/crs3-08.webp)

* Monitors internal diagnostics such as operating temperatures, laser supply voltages, TX/RX power levels, and hardware serialization strings.

---

## Forwarding and Port Isolation

Manages Layer 2 packet-forwarding tables across the switching architecture.

![Swos forw css326](./img/crs3-09.webp)
![Swos ivl system](./img/crs3-10.webp)

### Port Isolation and Isolated Groups

Port isolation splits broadcast domains internally, controlling client communications without adding subnet layers.

![SwOS Isolated Groups](./img/crs3-11.webp)
![SwO isolation example3](./img/crs3-12.webp)

---

## LAG (Link Aggregation)

Bundles physical interfaces into single high-throughput channels using either dynamic LACP links or static arrays.

![Swos lag css326](./img/crs3-13.webp)

---

## RSTP (Rapid Spanning Tree Protocol)

Provides loop avoidance architectures and structural redundancy parameters.

![Swos rstp css326](./img/crs3-14.webp)

* Supports configuring custom bridge path costs utilizing classic short or modern long path evaluation structures.

---

## VLAN & VLANs Matrix Configuration

VLAN routing rules split ingress packet sorting behavior from egress formatting tables.

### VLAN Tab (Ingress Control)

Handles port behaviors for incoming traffic streams.

![Swos vlan css326](./img/crs3-15.webp)

* **VLAN Modes**: Configures entry constraints across `disabled`, `optional`, `enabled`, and `strict` modes.

![Swos strict vlans](./img/crs3-16.webp)

* **Default VLAN ID**: Sets the Port VLAN ID (PVID) assigned to incoming untagged traffic.

![Default vlan id](./img/crs3-17.webp)

### VLANs Tab (Egress Mapping)

Defines broadcast memberships and handling across target trunk ports.

![Swos vlans css326](./img/crs3-18.webp)
![Swos vlans menu](./img/crs3-19.webp)

#### Traditional Mode Templates

* **Access Interfaces**: Pairs standard untagged endpoints to specific target VLAN tags.

  ![Access ports](./img/crs3-20.webp)

* **Trunk and Hybrid Options**: Blends multiple tagged streams with optional untagged native routing paths across primary core uplinks.

  ![Hybrid ports](./img/crs3-21.webp)
  ![Swos hybrid](./img/crs3-22.webp)
  ![Swos hybrid vlan](./img/crs3-23.webp)

---

## Private VLANs

Enforces secure structural port communication profiles across shared infrastructure spaces.

![SwOS Private VLAN](./img/crs3-24.webp)

---

## Hosts Tab

Exposes the active hardware Forwarding Database (FDB) dynamic entries discovered via incoming source addresses.

![Swos shost css326](./img/crs3-25.webp)

---

## IGMP Snooping

Filters multicast distributions, tracking active group subscriptions to block multicast flooding.

![IGMP snooping](./img/crs3-26.webp)
![CSSxx IGMP](./img/crs3-27.webp)
![IGMP vlantab](./img/crs3-28.webp)

---

## SNMP Tab

Enables monitoring via standard SNMP structures.

![Swos snmp2 1](./img/crs3-29.webp)

---

## ACL Tab (Access Control Lists)

Executes hardware-offloaded filtering rules matching patterns across L2/L3/L4 frame headers to drop or redirect packets.

![CRS326 ACL table](./img/crs3-30.webp)

---

## Diagnostics: Stats, Errors, and Histograms

Tracks interface counters, dropped frames, error patterns, and detailed structural link history diagnostics.

![Swos stat1 css326](./img/crs3-31.webp)
![Swos stat2 css326](./img/crs3-32.webp)
![Swos stat3 css326](./img/crs3-33.webp)

---

## Health Tab

Monitors hardware operating environments, tracking system core temperatures and operating input voltages.

![SwOS CRS328 health](./img/crs3-34.webp)

---

## Dual Boot Operation

Many CRS hardware units support a dual-boot design, allowing toggle operations between running RouterOS or SwOS.

![Router board settings](./img/crs3-35.webp)
![Router board settings webfig](./img/crs3-36.webp)
![Dual boot option](./img/crs3-37.webp)

Swapping operating systems toward SwOS using the RouterOS CLI interface utilizes the following system command structure:

```bash
/system routerboard settings set boot-os=swos
```

## Reset and Reinstall

It is possible to reset SwOS configuration using the "Reset Configuration" button in the System menu. In case SwOS web management is not available, the configuration can still be reset using other options.

The CSS326-24G-2S+ and CSS318-16G-2S+IN devices have built-in backup SwOS firmware which can be loaded in case standard firmware breaks or upgrade fails:

* Holding Reset button for few seconds while CSS326-24G-2S+ and CSS318-16G-2S+IN is booting resets configuration and loads backup firmware.
* After loading backup firmware, it is possible to connect to 192.168.88.1 (or leased address from a DHCP server) using web browser and install new SwOS firmware.

The Dual Boot devices can boot RouterOS using a reset button. Power the device while holding the reset button and wait till user LED starts flashing (around 5 seconds). This will reset the RouterOS configuration and the device will now boot into RouterOS. After device is accessible by RouterOS, it is possible to upgrade and reset SwOS configuration. See the article - Configuring SwOS using RouterOS.

CRS3xx devices with a serial console have additional options.

To change between RouterOS and SwOS follow these steps:

1. Connect to the device using a serial console
2. Enter RouterBOOT setup
3. Choose "j - boot os"
4. Choose either RouterOS or SwOS

It is possible to load a SwOS backup firmware in case standard firmware breaks or upgrade fails:

1. Connect to the device using a serial console
2. Boot SwOS
3. Choose "p - boot primary SwOS"
4. After loading backup firmware, it is possible to connect to 192.168.88.1 (or leased address from a DHCP server) using a web browser and install new SwOS firmware.

To reset SwOS configuration:

1. Connect to the device using a serial console
2. Boot SwOS
3. Choose "r - reset configuration"

![Swos reset](./img/crs3-38.webp)
