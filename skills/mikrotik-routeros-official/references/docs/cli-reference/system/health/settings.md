# settings

> Configures the fan and temperature monitoring behavior of the device.

-----------

## system/health/settings 
**Conditions:** !i386
**Syscap:** health and health-settings
**Type:** Settings Directory

Configures the fan and temperature monitoring behavior of the device.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="fan-full-speed-temp" typ="num">Sets the temperature value at which the fan speed is increased to the maximum possible RPM. The fan controller reads the temperature from CPU, PHY, switch and SFP, and adjusts the fan speed based on the component with the highest temperature. Range: -273..65. Default: 65.</ArgTableRow>
<ArgTableRow arg="fan-target-temp" typ="num">Sets the target temperature for the hottest component. The fan controller adjusts the fan behavior to keep the temperature in the target range. Range: -273..65. Default: 58.</ArgTableRow>
<ArgTableRow arg="fan-min-speed-percent" typ="num">Sets the minimum percentage of the fan speed, so the fans do not drop below this value. The default varies by fan controller chip; current devices default to 12. Range: 0..100.</ArgTableRow>
<ArgTableRow arg="fan-control-interval" typ="time">Sets the interval for reading the temperature data from the CPU, PHY, switch and SFP. This setting directly affects CPU usage. Range: 5..30 seconds. Default: 30s.</ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto) { manual:0, auto:1 }">Selects the fan control mode. With `auto`, the device automatically switches to the auxiliary fan when the main fan fails. With `manual`, you select which fans run by using `use-fan` and `use-fan2`.</ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main) { auxiliary:0, main:1 }">Selects which fan to use in the manual fan-control mode.</ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main) { auxiliary:0, main:1 }">Selects which second fan to use in the manual fan-control mode.</ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off) { auto:0, on:1, off:2 }">Sets the fan state: `auto` follows the automatic temperature control, `on` forces the fan to run, and `off` forces the fan to stop.</ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num">Sets the temperature at which the fans are switched on.</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool">Enables or disables CPU overtemperature monitoring. Available on ARM and ARM64 devices. Default: no.</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num">Sets the maximum temperature before the overtemperature protection is triggered. Range: 0..105. Default: 105.</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time">Sets the delay after startup before overtemperature monitoring is enabled. Default: 1m.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }">Fan that is currently in use.</ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }">Second fan that is currently in use.</ArgTableRow>
</ArgTable>
