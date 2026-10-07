# Health

> This page documents MikroTik RouterOS hardware health monitoring features, detailing metrics like temperature, voltage, fan speed, and CPU status for supported devices. It includes CLI examples, warnings about device...

# Health

Hardware that supports monitoring will display different information about hardware status, like temperature, voltage, current, fan-speed, etc.

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

:::info
For feature availability on RouterBOARD products check [mikrotik.com](https://mikrotik.com/products)
:::

Intensive health monitoring on the [CCR2004-16G-2S+PC](https://mikrotik.com/product/ccr2004_16g_2s_pc) device (from the console, winbox or SNMP) causes significant CPU load.

### Voltage

Routers that support voltage monitoring will display the supplied voltage value. In CLI/Winbox it will display volts. In scripts/API/SNMP this will be dV or the value shown in CLI/Winbox

**Note:** Routers that have PEXT and PoE power input are calibrated using PEXT, as a result, the value shown over PoE can be lower than input voltage due to additional Ethernet protection chains.

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C 
```

:::warning
If the old revision CRS112, CRS210 and CRS109 devices are powered with PoE - Health will show correct voltage only up to 26.7V. If higher voltage is used - Health will show constant 16V.
:::

### Temperature

Routers that support temperature monitoring will display a temperature reading. In CLI/Winbox it will display degrees Celsius. Using scripts/API/SNMP this value will be shown in CLI/Winbox multiplied by 10. There are various temperature sensors depending on the device. These sensors may refer to: cpu-temperature, pcb-temperature, sfp-temperature. You can find the device tested ambient temperature range in the specification description at [mikrotik.com](https://mikrotik.com/products). Tested ambient temperature range is the temperature in which the device can be physically located. It is **not** the same as the temperature reported by the system health monitor!

### Fan control and behavior

**Sub-menu:** `/system/health`

Using this menu users will be able to control fan behaviour on TILE architecture [devices](https://mikrotik.com/download).

:::info
Improved FAN stability starting from version 6.45.5.
:::

There are three parameters that may affect fan behaviour: PoE-out consumption, SFP temperature and CPU temperature. As soon as one of the parameters exceeds the optimal value, the fans are started.

#### PoE-out consumption

If a device has PoE-out, then the fan RPM will change as described below:

| PoE-out load | RPM % of max FAN speed |
| :-- | :-- |
| 0%..24% | FAN speed 0% |
| 25%..46% | FAN speed 25% |
| 47%..70% | FAN speed 50% |
| 71%..92% | FAN speed 75% |
| 93%.. | FAN speed 100% |

For devices with **PWM** fans, the speed will linearly increase or decrease from 9..88% (note: below 100W the fan RPM=0)

#### Limited manual fan-control option

:::info
Starting from RouterOS version 7.9 limited manual fan-control options have been added for CRS3xx, CRS5xx and CCR2xxx devices.

Starting from RouterOS version 7.14 limited manual fan-control is available for the CCR1036-8G-2S+-r2, CCR1036-12G-4S-r2 and CCR1016-12S-1S+-r2 devices.
:::

Fan behavior can be manipulated using the settings section of system health:

```
/system/health/settings/set 
```

Available properties are described below:

| Property | Description |
| :-- | :-- |
| **fan-full-speed-temp** (*integer* *[-273..65];* Default: **65**) | Sets the temperature value upon which the fan speed will be increased to the maximum possible rpm.  Reads temperature from CPU, PHY, SWITCH and SFP and adjusts fan speed based on the component with the highest temperature. |
| **fan-target-temp** (*integer* *[-273..65];* Default: **58**) | Sets the target temperature for the hottest component. Based on this setting, it adjusts fan behavior to hold temperatures in target range. |
| **fan-min-speed-percent** (*integer* *[0..100];* Default: **depends on FAN controller**) | Sets the minimum percentage of fan speed thus not allowing fans to have a lower rpm than this value. **\*NOTE:** the default value may vary based on FAN controller chip and/or specific model requirements. From RouterOS version 7.14, the default value is set to **12**, and all previous versions have **0.** |
| **fan-control-interval** (*integer* *[5..30];* Default: **30**) | Sets the actual temperature data read interval to get temperature values from CPU, PHY, SWITCH and SFP.  **\*NOTE:** THIS SETTING DIRECTLY AFFECTS CPU USAGE |
| **cpu-overtemp-check** *(yes \| no; Default: no)* | Enables/disables CPU overtemperature monitoring.  *(Available for ARM/ARM64 devices)* |
| **cpu-overtemp-threshold** *(integer [0..105]; Default: 105)* | Maximum temperature before triggering an overtemperature protection. |
| **cpu-overtemp-startup-delay** *(time; Default: 1m)* | Delay after startup before enabling overtemperature monitoring. |

#### Brief description of the fan-control

If at least one of the internal measured (CPU, SFP, Switch, Board etc.) temperatures exceeds **fan-target-temp**, the fans will start to spin. The higher the temperature, the faster the fans will spin. For devices with PWM fans, as the internal measured temperatures exceed **fan-target-temp**, the fans will linearly increase their RPM to try to keep the temperature at **fan-target-temp** if possible and will get to their Max RPM when the temperature is equal to or exceeds **fan-full-speed-temp**.  For devices with DC fans, as the internal measured temperatures exceed **fan-target-temp**, the fans will start spinning but at a higher minimum RPM by default. This may result in cooling the device to the point where the fans turn off completely if **fan-min-speed-percent** is set to **0%**, while with the default value of **12%** fans will never go to a full stop therefore reducing the noise and On/Off peaks that may occur. The temperature then may slowly increase to **fan-target-temp** and the fans will turn on again. Currently, there is one exception. The S+RJ10 modules have a temperature threshold of 65C before they trigger the fans. Since it's a higher temperature threshold, the fans will start spinning at a higher initial speed to cool the device. All the above mentioned functionality is directly related to the **fan-control-interval** parameter value as it will determine how often the FAN controller monitors all sensor data and triggers changes in fan-control.

:::warning
PWM and DC fans react to fan-control differently. While PWM fans will increase/decrease their RPM in a linear way the DC fans have only a few possible speed ratings at which they may operate.
All readings are approximate and may not be 100% precise. Their purpose is to ~inform users about possible/upcoming failures.
:::
