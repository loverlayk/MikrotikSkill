# PoE

> This page documents PoE (Power over Ethernet) on MikroTik devices: supported standards and power classes, configuring and monitoring PoE out (PSE) and PoE in (PD) ports in RouterOS and SwOS, logging, warnings,...

# PoE

## Summary

This page explains PoE (Power over Ethernet) on MikroTik devices: powering other devices with **PoE out** ports (the device acts as PSE, Power Sourcing Equipment) and, on some models, being powered with a **PoE in** port (the device acts as PD, Powered Device). MikroTik devices utilize an RJ45 mode B pinout for power delivery, with PoE supplied through pins 4 and 5 (+) and pins 7 and 8 (-).

## MikroTik supported PoE standards

MikroTik devices can support some or all of the following PoE standards - both for powering other devices (PoE out, the device acts as PSE) and, on some models, for being powered themselves (PoE in, the device acts as PD):

- **Passive PoE up to 30 V** - PoE without negotiation between the PSE (Power Sourcing Equipment) and the PD (Powered Device). A PoE out port delivers the same voltage that is supplied to the PSE itself. Applies to devices that support input voltage up to 30 V. (for example, [hEX PoE lite](https://mikrotik.com/product/RB750UPr2), [RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM), [RB2011iL-IN](https://mikrotik.com/product/RB2011iL-IN).)

- **Passive PoE up to 57 V** - Works the same as low-voltage (up to 30 V) passive PoE, but can also deliver or accept higher voltage over the PoE ports. For PoE out, the output voltage depends on the power source connected to the PSE. It can also power af/at compatible PDs that accept power over pairs 4,5 (+) and 7,8 (-) and do not require PoE negotiation. (for example, [cAP ac](https://mikrotik.com/product/cap_ac), [hAP ac](https://mikrotik.com/product/RB962UiGS-5HacT2HnT), [wsAP ac lite](https://mikrotik.com/product/wsap_ac_lite).)

- **IEEE Standards 802.3af/at** - Also known as PoE (802.3af, Type 1) and PoE+ (802.3at, Type 2), these IEEE standards ensure compatibility between vendors. PSEs that support these standards can power both Type 1 and Type 2 PDs, and PDs that support them can be powered from any compliant PSE. (for example, [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in), [CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm), [CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm).)

- **IEEE Standards 802.3bt** - The 802.3bt standard, also known as PoE++, extends the earlier PoE standards and introduces "Type 3" (Classes 5-6) and "Type 4" (Classes 7-8). This standard uses all four pairs of wires in a Gigabit Ethernet cable to deliver power, hence the name 4PPoE/802.3bt ("4-pair Power over Ethernet"). Depending on the model, 802.3bt is used for PoE out, PoE in, or both. (for example, [CRS320-8P-8B-4S+RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm))

Every PoE out implementation supports overload and short-circuit detection.

### Power classes

The 802.3 PoE standards define power classes which describe the maximum power a PSE provides to a PD:

| Class | Standard | PSE output power | PD available power |
| :-- | :-- | :-- | :-- |
| 0-3 | 802.3af (Type 1) | 15.4 W | 12.95 W |
| 4 | 802.3at (Type 2) | 30 W | 25.5 W |
| 5 | 802.3bt (Type 3) | 45 W | 40 W |
| 6 | 802.3bt (Type 3) | 60 W | 51 W |
| 7 | 802.3bt (Type 4) | 75 W | 62 W |
| 8 | 802.3bt (Type 4) | 90 W | 71.3 W |

The class is used by the PSE and the PD to agree on how much power can be delivered: the PD signals its class, the PSE then allocates the corresponding power budget.

You can tell which passive PoE standard a device supports from its specification page: a **`Low voltage PoE-Out current limit`** entry under the "PoE-OUT" section means the device supports **Passive PoE up to 30 V**, and an additional **`High voltage PoE-Out current limit`** entry means it also supports **Passive PoE up to 57 V**. The supported IEEE standards are listed directly on the specification page as `PoE out` (for example, 802.3af/at or 802.3bt).

As described in the previous list, **Passive PoE up to 57 V** can also power 802.3af/at-compatible devices (PDs) that do not require PoE negotiation - for MikroTik PDs this works reliably. Third-party PDs, however, may classify themselves into a lower PoE class when no negotiation takes place and request less power than they could otherwise use - this can show up as reduced radio output power, disabled peripherals, and similar symptoms. Behavior varies between PDs.

## Configuration

PoE configuration is supported on all MikroTik devices with PoE interfaces. It can be edited from the RouterOS and SwOS interfaces.

### RouterOS

**Sub-menu:** `/interface/ethernet/poe`

#### Usage

RouterOS provides an option to configure and monitor PoE over Winbox, Webfig, and CLI. Basic commands using the CLI are

| Property | Description |
| :-- | :-- |
| **print** () | Prints PoE related settings. |
| **export** () | PoE configuration is exported under the `/interface/ethernet` menu. |
| **monitor** (*string\| interface*) | Monitors the PoE status of a specified port - `poe-out-status`, voltage, current and power on PoE out ports, negotiated power-related information on PoE in ports. All ports can be monitored with `/interface/ethernet/poe/monitor [find]`. |
| **power-cycle** (*duration: 0..1m*; Default: **5s**) | Disables PoE out power on a PoE out port for a specified period of time. |

### SwOS

SwOS interface provides basic PoE out configuration and monitoring options, see more details in the [SwOS manual](https://manual.mikrotik.com/docs/bridging-and-switching/swos/).

## Monitoring

**Sub-menu:** `/interface/ethernet/poe/monitor`

| Property | Description |
| :-- | :-- |
| **name** () | Name of an interface. |
| **port-type** () | Shows whether the interface is capable of PoE out, PoE in, or both (**poe-out**, **poe-in**, **poe-in/poe-out**). |
| **poe-out** () | Shows PoE out state. |
| **poe-voltage** () | Shows PoE out voltage selection (**auto**, **low**, **high**). |
| **poe-out-status** () | Shows the current PoE out status on the port (see the [status list](#poe-out-statuses) below). |
| **poe-out-voltage** () | Displays the voltage which is applied to the PD. |
| **poe-out-current** () | Displays the port current (mA) drawn by the PD. |
| **poe-out-power** () | Displays PD power consumption. |
| **poe-out-power-pair()** | Displays on which power pairs the PSE delivers power to the PD: **a** - 1,2 (+) 3,6 (-); **b** - 4,5 (+) 7,8 (-); **bt** - all 4 pairs. |
| **power-cycle-host-alive** (*yes \| no*) | Shows if the monitored host is reachable (shown when the [power-cycle-ping](#power-cycle-settings) feature is enabled). Read-only. |
| **power-cycle-after** (*time*) | Shows the time, after which the port will be power-cycled (shown when the [power-cycle-ping](#power-cycle-settings) feature is enabled). Read-only. |

#### PoE out statuses

- **powered-on** - Power is applied to the port, and PoE out is operating normally.
- **waiting-for-load** - The PSE attempts to detect whether power can be applied to the port. For powering, there should be resistance in the range from 3kΩ to 26.5kΩ.
- **short-circuit** - A short circuit is detected on the PoE out port; power is switched off, and only detection with low voltage takes place. This can also mean that PoE is not supported on the connected device.
- **overload** - The PoE out current limit is exceeded, and power is switched off on the port. For port limits, see each model's specifications.
- **voltage-too-low** - The PD cannot be powered with the voltage provided from the PSE (for example, Vmin =>30V, but only 24V is provided).
- **voltage-too-high** - The connected device is detected as a PoE in device, but the output voltage from the PSE is higher than the range supported by the PD.
- **current-too-low** - The PD draws less current (below 10 mA) than a normal PoE out device should.
- **no-valid-PSU** - No valid power supply unit is detected: the PSE does not have a sufficient or power-capable power source to provide PoE out on the port, so power is not applied. See [Powering requirements](#powering-requirements) for the supported source combinations.
- **lldp-power-off** - The board is powered with PoE in and the LLDP-approved power budget received from the upstream PSE is insufficient to power the board's own PoE out ports.
- **low-voltage-pd-detected** - The connected PD supports only low voltage and cannot be powered from this PSE with the currently selected voltage. Power is not applied, to avoid damage to the PD. Power the PD from a low voltage PSE, or switch the port to low voltage (`poe-voltage=low`) on PSEs with switchable voltage modes.
- **voltage-on-poe-in** - Voltage is detected on the PoE out port unexpectedly, which can occur in two cases:
  - **External power source** - another device is supplying power to the port (PoE in voltage).
  - **Internal fault** - the PoE out circuitry on the port may be damaged.
- **low-voltage-too-low** - The low input voltage on the PSE is too low to power the PD; power is not applied.
- **disabled** - All detection and power is turned off for this port (`poe-out=off`).
- **power_reset** - The PSE controller is resetting the power, for example, during a PoE controller upgrade, or when executing the power cycle command or when pings fail (power-cycle-ping).
- **controller-init** - PSE controller initialization.
- **controller-upgrade** - The PSE controller is being upgraded.
- **controller-error** - The PSE controller does not respond.

### PoE in ports

:::note
PoE in monitoring is available only on devices that support PoE in with LLDP. Older devices do not show PoE in ports in the monitor.
:::

When monitoring a **PoE in** port (`port-type: poe-in`), the monitor shows information about the power the device receives with PoE, for example, on boards that support 802.3bt PoE in:

```ros
/interface/ethernet/poe/monitor ether1
```

```
              name: ether1
         port-type: poe-in
```

The monitor may also display a `power-limiting port` message. It means the PD (this device) is powered with limited power, because the power approved by LLDP negotiation is below the power requested by the PD.

### SNMP

It is possible to monitor PoE out values using the SNMP protocol. [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) must be enabled on the PSE.

Available SNMP OIDs:

| OID | Value |
| :-- | :-- |
| 1.3.6.1.4.1.14988.1.1.15.1.1.1 | interface ID |
| 1.3.6.1.4.1.14988.1.1.15.1.1.2 | interface name |
| 1.3.6.1.4.1.14988.1.1.15.1.1.3 | PoE out status (same values as shown by [monitor](#monitoring) `poe-out-status`) |
| 1.3.6.1.4.1.14988.1.1.15.1.1.4 | voltage in dV (decivolt) |
| 1.3.6.1.4.1.14988.1.1.15.1.1.5 | current in mA |
| 1.3.6.1.4.1.14988.1.1.15.1.1.6 | power usage in dW (deciwatt) |

SNMP values can be also requested from RouterOS, for example, `snmp-walk` will print current mA from all available PoE out ports:

```ros
/tool/snmp-walk address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5
```

To get a very specific OID value, use the `snmp-get` tool (displays current mA on ether3 interface):

```ros
/tool/snmp-get address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5.3
```

## Logging and notifications

### Logging

PoE events are [logged](../diagnostics-monitoring-and-troubleshooting/log/index.md) by default. PoE out state changes use the `poe-out` topic, PoE in events (for example, LLDP power negotiation on boards that are powered with PoE) use the `poe-in` topic. Important events (for example, overload or short-circuit) are logged with the "warning" topic, informational state changes with the "info" topic, for example:

```
2026-10-08 11:42:45 poe-out,info ether16 detected poe-out status: on
```

To avoid unnecessary logging in cases when PD is not powered because of current-too-low, RouterOS will filter such events, and add one log per 512 current-too-low events.

The `poe-out` and `poe-in` topics follow the standard [logging](../diagnostics-monitoring-and-troubleshooting/log/index.md) mechanism - they can be excluded, filtered by severity or sent to a separate log target like any other topic.

Detailed LLDP power negotiation messages use the "debug" topic, for example:

```
06:56:50 poe-out,debug ether4 LLDP TLV 25.0W request denied : hw-limit
```

Possible LLDP power request denial reasons:

| Reason | Description |
| :-- | :-- |
| **budget** | Requested power exceeds the total PSE budget. |
| **hw-limit** | Requested power is more than hardware supports (PSU affects this). |
| **low-voltage** | LLDP request made to a low-voltage port. |
| **off** | The port is shut down. |
| **class-limit** | LLDP requires more than the class can provide. |
| **cmd-failed** | RouterOS could not make a request to the controller. |

### GUI/CLI warnings

Important PoE related problems are shown as warnings: in the interface list in Winbox / WebFig (under Interfaces), as flag comments in the CLI interface printout, as the port status in [monitor](#monitoring), and in the [logs](#logging-and-notifications).

PoE out statuses that trigger a warning:

| Status | Description |
| :-- | :-- |
| **overload** | The PoE out current limit is exceeded. |
| **short-circuit** | Short-circuit detected on the port. |
| **current-too-low** | The connected PD draws less current than it should. |
| **voltage-on-poe-in** | Unexpected voltage detected on the port (for example, another device is supplying power to it). |

## PoE out

### How to choose your PoE PSE

This table can help you choose which PSE device is best suitable for your needs.

<WideTable>

| Device name | Software | PoE out port count | PoE type | Power input | Low voltage PoE out current limit, A | High voltage PoE out current limit, A | Max total output power, W |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **OmniTIK 5 PoE** | RouterOS | 4 | Passive | PoE in only (11-30 V) | 1 |  | 60 |
| **RB260GSP** | SwOS | 4 | Passive | DC jack / PoE in (11-30 V) | 1 |  | 60 |
| **hEX PoE lite / PowerBox** | RouterOS | 4 | Passive | DC jack / PoE in (8-30 V) | 1 | - | 60 |
| **OmniTIK 5 PoE ac** | RouterOS | 4 | Passive, af/at | PoE in only (12-57 V) | 1 | 0.45 | 102 |
| **hEX PoE / PowerBox Pro** | RouterOS | 4 | Passive, af/at | DC jack / PoE in (12-57 V) | 1 | 0.45 | 102 |
| **RB5009UPr+S+** | RouterOS | 8 | Passive, af/at | DC jack / 2-pin / PoE in (24-57 V) | 0.9 | 0.44 | 130 |
| **netPower Lite 8P** | SwOS | 8 | Passive, af/at | 3× 2-pin terminal (24-57 V) | 1 | 0.64 | 120 |
| **CRS112-8P-4S-IN** | RouterOS | 8 | Passive, af/at | 2× DC jack (18-28 V / 48-57 V) | 1 | 0.45 | 150 |
| **CRS418-8P-8G-2S+RM** | RouterOS | 8 | Passive, af/at | AC (2 PSU slots) | 1.1 | 0.56 | 150 |
| **CSS610-8P-2S+IN** | SwOS | 8 | Passive, af/at | AC &amp; DC 48-57 V | 1 | 0.625 | 140 |
| **CRS320-8P-8B-4S+RM** | RouterOS / SwOS | 16 | Passive, af/at, bt | AC (2 PSU slots) | - | 0.56 (af/at) / 1.67 (bt) | 963 |
| **netPower 16P** | RouterOS / SwOS | 16 | Passive, af/at | 2× DC jack (18-30 V / 48-57 V) | 1.1 | 0.6 | 160 |
| **CRS328-24P-4S+RM** | RouterOS / SwOS | 24 | Passive, af/at | AC | 1 | 0.45 | 450 |
| **CRS354-48P-4S+2Q+RM** | RouterOS / SwOS | 48 | Passive, af/at | AC | 1 | 0.57 | 700 |

</WideTable>

:::tip
When powering other devices with PoE out, use a minimum input voltage of 18V.
:::

### Settings

#### Global Settings

**Sub-menu:** `/interface/ethernet/poe/settings`

Some MikroTik PoE out devices support the global PoE settings

| Property | Description |
| :-- | :-- |
| **ether1-poe-in-long-cable** (*yes \| no*) | Set it to "yes" when the device itself is powered with PoE in through a long cable. It disables strict input current monitoring (short-circuit detection) so that a long cable is not incorrectly detected as a short-circuit. **This is a potentially dangerous setting and should be used with caution.** It can also affect PoE out behavior on a PSE which is powered using a DC connector |
| **psuX-max-power**  **jack-max-power**  **2pin-max-power** | Specifies the maximum power in watts that can be drawn from the given power source (PSU, DC jack or 2-pin terminal). Default: **96W** |
| **poe-in-max-power** | Specifies the maximum power in watts that the PoE injector (for example, 802.3bt) can deliver, when the device (PSE) itself is powered with PoE in |
| **routerboard-max-self-power** | Specifies how much power the device reserves for itself for powering. Read-only. |
| **routerboard-max-total-power** | Maximum power consumption of the board itself, without PoE out. It is used to calculate the PoE out budget on devices where the budget is determined by PSU power (PoE budget = PSU power − routerboard power). Read-only. |
| **poe-out-limit-power** | Total PoE out budget limit. Read-only. |
| **psuX-poe-out-max-power**  **jack-poe-out-max-power**  **2pin-poe-out-max-power**  **poe-in-poe-out-max-power** | PoE out limit in watts per power source (PSU, DC jack, 2-pin terminal or PoE in injector). Read-only. |
| **version** | PoE controller (ATtiny) firmware version. Read-only. |

#### Port Settings

**Sub-menu:** `/interface/ethernet/poe`

PoE out can be configured per port in this menu. Each port can be controlled independently.

| Property | Description |
| :-- | :-- |
| **name** () | Name of an interface. |
| **port-type** () | Shows whether the port is capable of PoE out, PoE in, or both (poe-out, poe-in, poe-in/poe-out). Read-only. |
| **poe-out** (*auto-on \| forced-on \| forced-on-a \| forced-on-bt \| off*; Default: **auto-on**) | Specifies PoE out stateauto-on - the resistance on the port is checked first, and power is applied only if it is in the range from 3kΩ to 26.5kΩforced-on - resistance detection is disabled and power is always provided on pair B (alt)off - all detection and power is turned off for this portAdditional states on PSEs that support 802.3bt PoE out:forced-on-a - same as forced-on, but power is provided on pair A (main)forced-on-bt - same as forced-on, but power is provided on all 4 pairs (available only from the CLI, this state cannot be selected in Winbox/WebFig)**Note:** Short-circuit and overload protection is always on, independently of the selected PoE out state. |
| **poe-priority** (*integer: 0..99*; Default: **10**) | poe-priority specifies the importance of PoE out ports, in cases when a total PoE out limit is reached, the interface with the lowest port priority will be powered off first. Highest priority is 0, the lowest priority is 99. If there are 2 or more ports with the same priority then the port with the smallest port number will have a higher priority. Every 6 seconds ports will be checked for a possibility to provide PoE out if it was turned off due to port priority. |
| **poe-voltage** (*auto \| low \| high*; Default: **auto**) | A feature that allows to manually switch between two voltage outputs on PoE out ports. It will take effect only on PSEs with switchable voltage modes ([CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in), [CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm), [netPower 16P](https://mikrotik.com/product/netpower_16p), [CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm)). |

Starting from RouterOS 7.15, the old **poe-lldp-enabled** port property was removed. LLDP power negotiation between a PSE and a PD is configured with the [Neighbor Discovery](../cli-reference/ip/neighbor/discovery-settings) `lldp-poe-power` property.

#### Power-cycle settings

RouterOS provides a possibility to monitor PD using a ping, and power-cycle a PoE out port when the host does not respond. The power-cycle-ping feature can be enabled under the `/interface/ethernet/poe` menu.

| Property | Description |
| :-- | :-- |
| **power-cycle-ping-enabled** (*yes \| no*; Default: **no**) | Enables ping watchdog, power-cycles port if a host does not respond to ICMP or MAC-Telnet packets. |
| **power-cycle-ping-address** (*IPv4 \| IPv6 \| MAC*) | An address which will be monitored. Since RouterOS 6.46beta16, an active route towards PD is required in case an IP address is configured, so make sure PSE can reach the PD. In case the MAC address is specified, PSE will send MAC-Telnet ping requests only from a specified ethernet interface. When configuring a [bridge vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) or some way of [VLAN switching](../bridging-and-switching/user-guides/basic-vlan-switching.md), it is recommended to use the IP address for monitoring your PD. |
| **power-cycle-ping-timeout** (*time: 0..1h*; Default: **5s**) | If the host does not respond for more than the timeout period of time, then PoE out port is switched off for 5s. |
| **power-cycle-interval** (*time \| none*; Default: **none**) | Periodically power-cycles the PoE out port (switches the power off for 5s and then on again) every specified interval. Not related to the power-cycle-ping feature. |

If the power-cycle-ping feature is enabled, [monitoring](#monitoring) will also show the status of the monitored host and the time until the next power cycle.

### LEDs

Most devices indicate the PoE out state with one LED per port - the same LED can light up in different colors:

| LED | PoE out state |
| :-- | :-- |
| Red | **Powered-on** - red regardless of voltage on models without voltage selection; on models with voltage selection and on 802.3bt models, the PD is powered with high voltage (802.3af/at) |
| Green | **Powered-on**, PD uses low voltage (models with selectable voltage output) |
| Purple | **Powered-on**, PD is powered with all 4 pairs (802.3bt) |
| Blinking (any color) | **Short-circuit** or **overload** |

#### Model-specific LED behavior

- [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in), [netPower 16P](https://mikrotik.com/product/netpower_16p) - All PoE LEDs flashing: wrong voltage PSU plugged into one of the ports.

### How it works

#### PoE out Modes

- **auto-on** - the board checks the resistance on the connected port and applies power only if it is in the range from 3kΩ to 26.5kΩ:
  - when power is applied, the PSE continuously checks for overload and short circuit;
  - if the cable is unplugged, the port returns to the detection state and remains off until a suitable PD is detected again.
- **forced-on** - resistance detection is disabled and power is applied even without a cable attached:
  - power is applied on the pairs depending on the configured `poe-out` state (`forced-on`, `forced-on-a` or `forced-on-bt`);
  - the PSE still continuously checks for overload and short circuit;
  - after the cable is unplugged, power remains enabled on the port.
- **off** - PoE out on the port is turned off, no detection takes place, and the interface behaves like a simple Ethernet port.

#### PoE out limits

The following PoE out characteristics differ between PSE models - check the specification page of the device:

- **Port limit** - PoE out ports are limited by the maximum current which is supported at a particular voltage. The maximum current usually differs for low voltage devices (up to 30 V) and for high voltage devices.
- **Total limit** - the PSE also has a total PoE out current limitation, which cannot be exceeded even if the individual port limit allows it. The total limit scope differs between models: on boards where the limit is per port group (for example, per 8-port section), power priorities also apply within that port group.
- **Polarity** - most MikroTik PSEs use the same PoE out pin polarity, [Mode B](https://en.wikipedia.org/wiki/Power_over_Ethernet#Pinouts) - 4,5 (+) and 7,8 (-). PSEs with 802.3bt capable ports use both polarities: 1,2 (+) and 3,6 (-) as Mode A, and 4,5 (+) and 7,8 (-) as Mode B.

#### Safety

PSE has the following safety features:

- **Compatibility detection** - in auto-on mode, the resistance on the port is checked first and power is applied only if it is within the allowed range of 3kΩ to 26.5kΩ. Non-standard PDs that are outside of this range are not powered.
- **Overload protection** - while a PoE out port is powered on, it is constantly checked for overload. If an overload is detected, PoE out is turned off on the port to avoid damage to the PD or PSE, and powered on again after a few seconds to check if the situation has changed.
- **Short circuit detection** - while power is applied on a PoE out port, the PSE continuously checks for a short circuit. If it is detected, power is turned off on that port to avoid additional damage to the PD and PSE, and the port continues to be checked until the environment returns to normal.

#### Model-specific features

Some PSEs have independent 8-port sections. On such devices PoE out works independently of RouterOS: you can reboot or upgrade RouterOS and the powered devices will not lose power. An exception is a PoE controller firmware upgrade, during which the power is interrupted - such upgrades are always mentioned in the RouterOS changelog.

The way the PoE budget is defined also differs between models: on some devices the budget limit is set for the whole board, on others it is set per 8-port section. In the same way, PoE out priorities work within the scope of the budget: on boards with a per-section budget, priorities are applied per section, on boards with a board-wide budget, they are applied globally.

## PoE in

MikroTik devices can also be powered over Ethernet themselves, acting as a PD (Powered Device). PoE in ports are managed in the same `/interface/ethernet/poe` menu and can be identified by `port-type: poe-in` in the monitor output.

### Configuration

PoE in related options are a part of the [Global Settings](#global-settings), for example:

- **poe-in-max-power** - informs the device about the maximum power of the PoE injector (for example, 802.3bt) powering it, so the PoE out budget can be calculated correctly;
- **ether1-poe-in-long-cable** - disables strict input/output current monitoring when the device is powered over a long cable.

### Powering requirements

When powering a device with PoE in, the power source must match the device input. Check the specification page of the device for the supported PoE in voltage range and standards:

- The PSU or PoE injector output voltage must be within the device input voltage range (for example, 8-30 V or 12-57 V on passive PoE models). Too low a voltage can prevent the device from starting or cause restarts under load, and too high a voltage can damage the device.
- The power source must deliver enough power for the device itself and, if the device powers other equipment, for the PoE out budget as well - see [PoE out limits](#poe-out-limits) and the [settings](#global-settings) for how the budget is calculated.
- Passive PoE in on MikroTik devices uses Mode B polarity (pins 4,5 (+) and 7,8 (-)), except devices with 802.3bt PoE in, which accept power over all four pairs.
- Powering devices that support PoE out and 802.3bt (PoE++) PoE in with an 802.3af/at PSE or a passive 2-pair injector is not considered a valid power source: PoE out will not work and the monitor shows the `no-valid-PSU` status on the PoE out ports. Use an 802.3bt PSE or a 4-pair passive injector instead.

When the device itself is powered with PoE and LLDP power negotiation is used (see [Neighbor Discovery](../cli-reference/ip/neighbor/discovery-settings) `lldp-poe-power`), the device communicates its requested power to the upstream PSE, which approves power accordingly. If the approved power is below the requested power, the monitor displays the `power-limiting port` message (see [PoE in ports](#poe-in-ports)) and some PoE out ports may not be powered.

## Examples

### PoE out

#### Powering non-standard PDs (forced-on)

PDs that do not present the required resistance (3kΩ to 26.5kΩ) are not powered in `auto-on` mode. Power them with `forced-on` instead:

```ros
/interface/ethernet/poe set ether5 poe-out=forced-on
```

On PSEs with 802.3bt, `forced-on-a` and `forced-on-bt` power the PD over pair A or all four pairs (CLI only, see [Port Settings](#port-settings)). To save power and improve safety, disable PoE out on unused ports with `poe-out=off`.

#### Port priorities

PoE out priorities define which ports lose power first when the total PoE out limit is reached. The priority of *0* is the highest, *99* is the lowest:

```ros
/interface/ethernet/poe set ether2 poe-priority=10
/interface/ethernet/poe set ether3 poe-priority=13
/interface/ethernet/poe set ether4 poe-priority=11
/interface/ethernet/poe set ether5 poe-priority=14
```

If the total limit is exceeded, the port with the lowest priority is disabled first (ether5, then ether3). Disabled ports are re-checked every few seconds and powered up again in the reverse order once the budget allows it.

When several ports have the same priority, the port with the lowest port number is favored: with equal priorities on all ports, ether5 is disabled first, then ether4, then ether3.

#### Scheduled power-cycle

Periodically power-cycle a PoE out port, for example, to reboot the connected device once a day, with [power-cycle-interval](#power-cycle-settings):

```ros
/interface/ethernet/poe set ether5 power-cycle-interval=1d
```

#### Power-cycle watchdog (power-cycle-ping)

Monitor the connected PD and power-cycle the port when the host does not respond:

```ros
/interface/ethernet/poe set ether1 power-cycle-ping-enabled=yes power-cycle-ping-address=192.168.88.10 power-cycle-ping-timeout=30s
```

The PD on ether1 is monitored with ICMP pings. If the host at 192.168.88.10 does not respond for more than 30s, PoE out on the port is switched off for 5s.

#### Monitoring PoE out

```ros
/interface/ethernet/poe/monitor ether9
```

```
                name: ether9
             poe-out: auto-on
      poe-out-status: powered-on
     poe-out-voltage: 54.2V
     poe-out-current: 449mA
       poe-out-power: 24.3W
  poe-out-power-pair: b
```

#### Checking the power limits

Review the PoE out budget and the read-only power limits of the device with the global settings:

```ros
/interface/ethernet/poe settings print
```

```
               jack-max-power: 96W
               2pin-max-power: 150W
   routerboard-max-self-power: 20W
  routerboard-max-total-power: 30W
          poe-out-limit-power: 240W
       jack-poe-out-max-power: 66W
       2pin-poe-out-max-power: 120W
```

In this example, the board itself reserves 20 W and the total budget for PoE out is 240 W, 66 W of which is available when powered through the DC jack, or 120 W when powered through the 2-pin terminal.

### PoE in

When the device itself is powered with a PoE injector (for example, 802.3bt), declare the power of the injector with the [poe-in-max-power](#global-settings) global setting so the PoE out budget is calculated correctly:

```ros
/interface/ethernet/poe settings set poe-in-max-power=144
```

## Troubleshooting

If a PD does not power up or restarts unexpectedly when powered with PoE out, work through this checklist:

1. **Check the port status first.** Run `/interface/ethernet/poe/monitor` on the port - the value of `poe-out-status` usually points directly at the problem, for example `overload`, `short-circuit`, `voltage-too-low` or `no-valid-PSU`. See the full [status list](#poe-out-statuses).
2. **Check the logs.** PoE state changes are recorded with the `poe-out` topic, see [Logging](#logging).
3. **Try a different cable.** Use a short, good-quality patch cable directly at the PSE to rule out cabling problems.
4. **Check the power supply of the PSE.** Review the limits with `/interface/ethernet/poe settings print`:
   - The PSU must cover the power consumption of the PSE itself, all powered PDs, and about 10% of headroom.
   - Too low an input voltage can cause the `voltage-too-low` status on the PDs (for example, with a long DC cable or an oversized load on the PSU).
   - On boards with 802.3bt PoE in, make sure the device is powered from a valid power source, otherwise the `no-valid-PSU` status occurs and PoE out stays off - see [Powering requirements](#powering-requirements).
5. **Check PD compatibility against its datasheet:**
   - Check the specifications of the PSE and the PD together: a passive PoE in device (for example, with input up to 30 V) cannot be powered from a higher voltage source. On passive PSEs the PoE out voltage matches the PSE input voltage, so a PSE powered with a 48 V PSU also outputs 48 V on its PoE out ports - use a low voltage PSU or a PSE with selectable voltage output for low voltage PDs.
   - The PD supported input voltage must match the PSE output voltage.
   - Pin polarity differences (Mode A or reversed) between the PSE and the PD.
6. **Try `forced-on`** for non-standard PDs, after verifying that the PD supports the PSE voltage and polarity (see [examples](#powering-non-standard-pds-forced-on)).
7. **Update RouterOS.** PoE functionality receives regular fixes and updates, make sure you are running the latest [RouterOS version](https://mikrotik.com/download).
8. **Isolate the PD.** Power it from a matching passive PoE injector. If it works from the injector but not from the PSE port, the problem is the port or its configuration.

If none of these steps solve the issue, collect the monitor output and logs, generate a [supout.rif file](../cli-reference/system/sup-output), and contact MikroTik support.
