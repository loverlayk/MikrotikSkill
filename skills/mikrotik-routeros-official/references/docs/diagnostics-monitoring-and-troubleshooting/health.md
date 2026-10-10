# Health

> This page documents MikroTik RouterOS hardware health monitoring, covering temperature, voltage, current, power supply and power consumption readings, fan control settings, SNMP OIDs, and REST API and script examples...

# Health

Hardware that supports monitoring displays information about hardware status, such as temperature, voltage, current, fan speed, power supply state and power consumption. The same readings are also available in Winbox, on the **System → Health** tab. Devices without hardware sensors print nothing: this includes CHR and virtual machines, and boards that simply have no sensors (for example the hAP ax²).

Example on the CCR1072-1G-8S+ device:

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
 #  NAME                VALUE  TYPE
 0  power-consumption   50.8   W   
 1  cpu-temperature     43     C   
 2  fan1-speed          5654   RPM 
 3  fan2-speed          5825   RPM 
 4  fan3-speed          5800   RPM 
 5  fan4-speed          5750   RPM 
 6  board-temperature1  29     C   
 7  board-temperature2  28     C   
 8  psu1-voltage        0      V   
 9  psu2-voltage        12.1   V   
10  psu1-current        0      A   
11  psu2-current        4.2    A
```

The `TYPE` column shows the unit of the reading: `C` is degrees Celsius, `RPM` is fan speed, `V` is voltage, `A` is current and `W` is power consumption. Scripts see the same values as the CLI shows. SNMP uses deci-units for temperature, voltage and power (23.8 V → 238), and current in mA in the legacy OIDs or dA in the dynamic gauge table (see the SNMP section below).

To print a single reading, filter it by name:

```ros
[admin@MikroTik] > /system/health/print where name="cpu-temperature"
Columns: NAME, VALUE, TYPE
 #  NAME             VALUE  TYPE
 0  cpu-temperature  43     C   
```

To see what health data a specific RouterBOARD product supports, check the product specification at [mikrotik.com](https://mikrotik.com/products).

## Readings

| Reading | Unit | Description |
| :-- | :-- | :-- |
| `voltage` | V | Supplied voltage on devices with a single power input |
| `psuN-voltage` | V | Voltage of power supply N |
| `psuN-input-voltage` | V | Input (mains) voltage of power supply N |
| `jack-voltage`, `2pin-voltage`, `poe-in-voltage` | V | Voltage of a specific power input (on devices without PSUs) |
| `poe-outN-voltage` | V | Voltage on PoE-out port N |
| `psuN-current` | A | Current drawn by power supply N |
| `power-consumption` | W | Total power consumption |
| `poe-out-consumption` | W | Current PoE-out power consumption |
| `psuN-power` | W | Power of power supply N |
| `temperature` | C | Device temperature on devices with a single sensor |
| `cpu-temperature` | C | CPU temperature |
| `board-temperatureN` | C | Board temperature sensor N |
| `phy-temperature` | C | PHY temperature |
| `sfp-temperature` | C | SFP module temperature |
| `switch-temperature` | C | Switch chip temperature |
| `pcie-switch-temperature` | C | PCIe switch temperature |
| `psuN-temperature` | C | Temperature of power supply N |
| `fan-state` | — | Fan state: `ok` or `fail` |
| `fanN-speed` | RPM | Speed of fan N |
| `psuN-fan-speed` | RPM | Speed of the internal fan of power supply N |
| `psuN-state` | — | Power supply N state (see the state table below) |

Numbered names (`psuN`, `fanN`, `board-temperatureN`, `poe-outN`) use indexes starting from 1, and the count depends on the device. Which of the readings are present depends on the hardware sensors of the device.

A fan speed reading of 0 RPM when the device has a high temperature can mean the fan has stopped or failed.

### Voltage

Routers that support voltage monitoring display the supplied voltage value. In CLI, Winbox and scripts it is reported in volts; over SNMP it is in dV (the CLI value multiplied by 10).

Routers that have PEXT and PoE power input are calibrated using PEXT. As a result, the value shown over PoE can be lower than input voltage due to additional Ethernet protection chains.

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C 
```

### Temperature

Routers that support temperature monitoring display a temperature reading. In CLI, Winbox and scripts it is reported in degrees Celsius; over SNMP the value is multiplied by 10. Different devices use different temperature sensors, for example `cpu-temperature`, `board-temperature1`, `sfp-temperature`, `phy-temperature` or `switch-temperature`. Some readings appear only when the corresponding component is present, for example `sfp-temperature` shows only when an SFP module is installed. You can find the device tested ambient temperature range in the specification description at [mikrotik.com](https://mikrotik.com/products). The tested ambient temperature range is the temperature in which the device can be physically located. It is **not** the same as the temperature reported by the system health monitor.

### Power supply states

Devices with redundant power supplies report the state of each power supply. For battery-backed devices, see the [UPS](../system-information-and-utilities/ups) page. Possible values are:

| Value | Description |
| :-- | :-- |
| `ok` | The power supply works normally. |
| `fail` | The power supply has failed. |
| `not-present` | No power supply is detected in this slot. |
| `idle` | The power supply is present but idle. |
| `no-input` | The power supply has no input power. |

A value of `fail` or `no-input` indicates a problem with the power supply or its power source.

### Legacy devices

If the old revision CRS112, CRS210 and CRS109 devices are powered with PoE - Health will show correct voltage only up to 26.7 V. If higher voltage is used, Health will show a constant 16 V.

x86 (legacy PC hardware) based devices use a different set of reading names, for example `core`, `3.3v`, `5v`, `12v`, `lm87-temp`, `cpu-temp`, `board-temp`, `voltageN`, `tempN` and `fanN`.

## Fan control and behavior

The [/system/health/settings](../cli-reference/system/health/settings) menu controls fan behavior on devices with fans.

Three parameters can start the fans: PoE-out consumption, SFP temperature and CPU temperature. When one of the parameters exceeds the optimal value, the fans start.

### PoE-out consumption

If a device has PoE-out, then the fan RPM will change as described below:

| PoE-out load | RPM % of max fan speed |
| :-- | :-- |
| 0%..24% | Fan speed 0% |
| 25%..46% | Fan speed 25% |
| 47%..70% | Fan speed 50% |
| 71%..92% | Fan speed 75% |
| 93%.. | Fan speed 100% |

For devices with **PWM** fans, the speed will linearly increase or decrease from 9..88% (below 100 W the fan RPM is 0).

### Manual fan-control option

Manual fan-control is available for CRS3xx, CRS5xx and CCR2xxx devices, and for the revised CCR1036-8G-2S+-r2, CCR1036-12G-4S-r2 and CCR1016-12S-1S+-r2 devices.

Set them in [`/system/health/settings`](../cli-reference/system/health/settings) — every parameter, including the manual fan-control options `fan-mode`, `use-fan`, `use-fan2`, `fan-switch` and `fan-on-threshold`, and the read-only `active-fan`/`active-fan2` states, is described in the CLI reference. Devices with main and auxiliary fans, such as RB1100, CCR1016 and CCR1036 devices, also support manual fan-control.

For example, to keep the fans running at least at a quarter of their maximum speed:

```ros
/system/health/settings/set fan-min-speed-percent=25
```

When the main fan fails, the device automatically switches to the auxiliary fan and `active-fan` (or `active-fan2`) changes to `auxiliary`. Fan state changes are also written to the log on CRS3xx, CRS5xx, CCR2xxx, CCR1016r2 and CCR1036r2 devices.

Use the `/system/health/settings/detect-fans` command to detect the fans connected to the device, for example after installing or replacing a fan.

### Fan control in detail

If at least one of the internal measured temperatures (CPU, SFP, switch, board) exceeds **fan-target-temp**, the fans start spinning. The higher the temperature, the faster the fans spin.

- Devices with PWM fans: the fans increase their RPM linearly to keep the temperature at **fan-target-temp** if possible, and reach their maximum RPM when the temperature equals or exceeds **fan-full-speed-temp**.
- Devices with DC fans: the fans start spinning at a higher minimum RPM by default. This may cool the device so much that the fans turn off completely if **fan-min-speed-percent** is **0%**; with the default **12%** the fans never stop fully, which reduces the noise and on/off peaks. When the temperature rises back to **fan-target-temp**, the fans turn on again.

One exception: S+RJ10 modules have a temperature threshold of 65 C before they trigger the fans, so the fans start spinning at a higher initial speed to cool the device. All the previously mentioned functionality is directly related to the **fan-control-interval** parameter value, as it determines how often the fan controller monitors all sensor data and applies fan-control changes.

PWM and DC fans react to fan-control differently. PWM fans increase or decrease their RPM in a linear way. However, DC fans have only a few possible speed ratings at which they can operate.

All readings are approximate. Their purpose is to inform users about possible or upcoming failures.

## Monitor health and get alerts

### SNMP trap

For SNMP-based monitoring, enable the `temp-exception` trap generator. The router then sends an SNMP trap when the temperature reaches 100 C or the value set with `cpu-overtemp-threshold`. See the [SNMP](./snmp) page for details.

### SNMP OIDs

All health readings are exposed in the [MIKROTIK-MIB](https://mikrotik.com/download) under the `1.3.6.1.4.1.14988.1.1.3` sub-tree, in the form `.1.3.6.1.4.1.14988.1.1.3.<index>.0`:

| Index | Object name | Reading |
| :-- | :-- | :-- |
| 1 | `mtxrHlCoreVoltage` | Core voltage (V) |
| 2 | `mtxrHlThreeDotThreeVoltage` | 3.3 V rail voltage |
| 3 | `mtxrHlFiveVoltage` | 5 V rail voltage |
| 4 | `mtxrHlTwelveVoltage` | 12 V rail voltage |
| 5 | `mtxrHlSensorTemperature` | Temperature at the sensor chip (C) |
| 6 | `mtxrHlCpuTemperature` | CPU temperature |
| 7 | `mtxrHlBoardTemperature` | Board temperature |
| 8 | `mtxrHlVoltage` | Main voltage |
| 9 | `mtxrHlActiveFan` | Name of the active fan |
| 10 | `mtxrHlTemperature` | Temperature |
| 11 | `mtxrHlProcessorTemperature` | Processor temperature |
| 12 | `mtxrHlPower` | Power consumption (W) |
| 13 | `mtxrHlCurrent` | Current (mA) |
| 14 | `mtxrHlProcessorFrequency` | CPU frequency (MHz) |
| 15 | `mtxrHlPowerSupplyState` | PSU state (0 = not ok, 1 = ok) |
| 16 | `mtxrHlBackupPowerSupplyState` | Backup PSU state (0 = not ok, 1 = ok) |
| 17 | `mtxrHlFanSpeed1` | Fan 1 speed (RPM) |
| 18 | `mtxrHlFanSpeed2` | Fan 2 speed (RPM) |
| 19 | `mtxrAlarmSocketStatus` | Alarm socket status (0 = inactive, 1 = active) |

Temperature, voltage and power values are multiplied by 10 (divide by 10 to get the value). Current is reported in mA, frequency in MHz and fan speeds in RPM. Which indexes return a value depends on the hardware sensors of the device; run `/system/health/print oid` on a device to see its actual OID mapping.

The static OIDs in the table are the fixed legacy set. Newer readings — such as fan speeds beyond fan 2, the per-power-supply readings (`psuN-*`), `pcie-switch-temperature`, and PoE-out voltages — are available in a dynamic gauge table at `.1.3.6.1.4.1.14988.1.1.3.100`. Each row of this table lists a reading by name (`mtxrGaugeName`), together with its raw value (`mtxrGaugeValue`) and unit (`mtxrGaugeUnit`: `celsius(1)`, `rpm(2)`, `dV(3)`, `dA(4)`, `dW(5)` or `status(6)`). The `dV`, `dA` and `dW` units are deci-volts, deci-amperes and deci-watts, so divide the raw value by 10.

### REST API

With the REST API you can read the same readings as JSON:

```bash
curl -k -u admin https://192.168.88.1/rest/system/health
```

See the [REST API](../developer-guides/rest-api) page for details.

### Send an email alert

With a script you can check the readings periodically by using the scheduler and send an email when a limit is exceeded. First configure the [E-mail](../system-information-and-utilities/e-mail) settings, then add the script and a scheduler entry:

```ros
/system/script/add name=temp-alert source={
    :local t [/system/health/get [find name="cpu-temperature"] value]
    :if ($t > 65) do={/tool/e-mail/send to="admin@example.com"
        subject="Router overheating" body=("CPU temperature: " . $t)}
}
/system/scheduler/add name=temp-alert start-time=startup interval=5m on-event=temp-alert
```

In scripts the values are plain numbers as printed by the CLI (54 for 54 C), so the example compares against 65.

For all parameters, see the [`/system/health`](../cli-reference/system/health) and [`/system/health/settings`](../cli-reference/system/health/settings) CLI reference pages.
