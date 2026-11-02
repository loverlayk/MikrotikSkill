# TG-LR Setup

> This page is the setup guide for MikroTik TG-LR82 and TG-LR92 LoRaWAN sensor tags, covering activation, network join, telemetry and sensor configuration, magnet switch commands, command encoding for downlinks, data...

# TG-LR Setup

<Anchor id="tg-lr" />

## Quickstart Guide

- Register device on LoRaWAN network server. Use [`tg-lrx2-2.0-ul-dec.js`](pathname:///assets/tg-lrx2-2.0-ul-dec.js) paylaod decoder script if device model not supported.

- Optionally deploy Grafana + Influx ([`telemetry_hub.zip`](pathname:///assets/telemetry_hub.zip)) docker services for device capability evaluation.

- Activate device by holding magnet near reed switch and wait for 2x LED blinks (~1.5s).

## Functionality

:::note

New device is in [SHUTDOWN](#shutdown) mode. To activate use [magnet switch commands](#mag-sw-cmd).

:::

<Anchor id="id42" />

**Models**

| <Anchor id="model" />Model | Description | Sensors |
| --- | --- | --- |
| <Anchor id="tg-lr82" />TG-LR82 | LoRaWAN 1.0.4 Class A, B, 863.0 - 869.0 MHz band. | TMP116N, HDC2010, LIS2DW12 |
| <Anchor id="tg-lr92" />TG-LR92 | LoRaWAN 1.0.4 Class A, B, 900.0 - 928.0 MHz band. | TMP116N, HDC2010, LIS2DW12 |

<Anchor id="id43" />

**Bands**

| Numeric code | Name | Description |
| --- | --- | --- |
| 1 | <Anchor id="band-1ghz" />BAND_1GHz | Sub-GHz operating band. Frequency range is based on device [Model](#model). |
| 2 | <Anchor id="band-2ghz" />BAND_2GHz | 2.4GHz ISM band. |

<Anchor id="id44" />

**Operating modes**

| Numeric code | Mode | Description |
| --- | --- | --- |
| 0 | <Anchor id="shutdown" />SHUTDOWN | Device in low power mode with all functionality disabled. |
| 1 | <Anchor id="run" />RUN | Device joins network and sends uplinks based on current profile and configuration. |

<Anchor id="id45" />

**<Anchor id="supported-regions" />Supported regions**

| [X-Y](#x-y) Code | [downlink](#lora-set-region) | Common Name | [TG-LR82](#tg-lr82) | [TG-LR92](#tg-lr92) |
| --- | --- | --- | --- | --- |
| 1-1 | 1 | <Anchor id="eu868" />EU868 | Yes |  |
| 2-1 | 2 | <Anchor id="as923-grp1" />AS923_GRP1 |  | Yes |
| 3-1 | 3 | <Anchor id="us915" />US915 |  | Yes |
| 4-1 | 4 | <Anchor id="au915" />AU915 |  | Yes |
|  |  | <Anchor id="ww2g4" />WW2G4 | Yes | Yes |
| 6-1 | 7 | <Anchor id="as923-grp2" />AS923_GRP2 |  | Yes |
| 7-1 | 8 | <Anchor id="as923-grp3" />AS923_GRP3 |  | Yes |
| 8-1 | 9 | <Anchor id="in865" />IN865 | Yes |  |
| 9-1 | 10 | <Anchor id="kr920" />KR920 |  | Yes |

### LoRaWAN

Device supports Class A and B, and can operate in two frequency bands: [BAND_1GHz](#band-1ghz) and [BAND_2GHz](#band-2ghz).
User can configure periodic link check, MAC time synchronization (DeviceTimeReq) and network ADR.

#### Join Procedure

Once activated ([RUN](#run)) device will attempt to join network. Device sends Join-Request on primary band
and if Join-Accept is not received it will wait back-off interval and send next Join-Request on secondary
band if enabled, otherwise primary-band again.

:::note

Join attempt interval depends on time on air for last Join-Request and total join time.
See [1](#id40) section 7. If last join request used slower data rate - expect longer interval.

:::

Join configuration commands: [lora primary-band](#lora-primary-band), [lora second-band](#lora-second-band), [lora join-cfg](#lora-join-cfg).
See [Command Encoding](#command-encoding) on how to convert text commands to binary encoding for downlink.

#### Link Check

Once device has joined network optional periodic link check can be performed. Link check can be configured
specifically for each band using [lora link-chk](#lora-link-chk). If link check fails device leaves network and restarts
join procedure.

:::note

Any network downlink will restart link check timer to prevent unnecessary LinkCheckReq.

:::

#### Time Synchronization

Device supports optional time synchronization using DeviceTimeReq MAC command. See command [lora clk-sync](#lora-clk-sync)
for configuration parameters or to request immediate synchronization.

#### Class B

Device supports Class B operation. Class B operation can be either manually requested using
[lora class](#lora-class) or device can be configured to automatically switch to class B on network join using
[lora cfg-class-b](#lora-cfg-class-b).

#### ADR Configuration

It is possible to disable network ADR and set fixed data rate using [lora adr-cfg](#lora-adr-cfg).

#### Leaving Network

In case of [Link Check](#link-check) or confirmed uplink failure device leaves network and restarts join procedure.

#### Credentials

Device has factory configured default credentials that come with each device: [DevEUI](#deveui), [JoinEUI](#joineui), [AppKey](#appkey).

<Anchor id="deveui" />DevEUI and <Anchor id="joineui" />JoinEUI are IEEE 64-bit EUI ([2](#id41)) written MSB first.
On air byte order is LSB first. See [1](#id40) section 6.2.5.

<Anchor id="appkey" />AppKey is 16 byte AES128 encryption key and is written as stored in device memory. AppKey must be kept secret!

To change [JoinEUI](#joineui) and [AppKey](#appkey) use commands: [lora join-eui](#lora-join-eui), [lora net-key](#lora-net-key) and [lora cred](#lora-cred).
Commands [lora join-eui](#lora-join-eui) and [lora net-key](#lora-net-key) can be issued in any order and multiple times to write new pending
join credentials.

Once new pending credentials are written “[lora cred](#lora-cred) 600,1” or “[app reset](#app-reset) 0” can be executed to attempt join
with new credentials. If new credentials are not confirmed by join accept device will revert to previous.
See [LORA-275](#lora-275), [LORA-276](#lora-276) for know issues!

Example sequence where JoinEUI and AppKey are written and join is attempted:

```none
lora join-eui 87904163,0x00,0x16,0xC0,0x01,0xFF,0xFE,0x00,0x00
lora net-key 87904163,0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F
lora cred 600
app reset 0
// device reboots and attempts join using new credentials with 600s timeout
```

JoinEUI from previous example can be copy/pasted as is 00 16 C0 01 FF FE 00 00 to register new device.
[lora join-eui](#lora-join-eui) parameters are MSB first.

:::warning

Executing *lora cred &lt;confirm-timeout-s&gt;,87904163* will force confirm credentials without
verification join attempt! You may loose access to device!

:::

### Uplink Messages

Each LoRaWAN uplink message is formed by placing pending [Data Frames](#data-frames) ID and its contents in FPort and
FRMPayload fields. All pending frames are packed in ascending order and differential encoding is
used for IDs.

:::note

See [`tg-lrx2-2.0-ul-dec.js`](pathname:///assets/tg-lrx2-2.0-ul-dec.js) script for frame encoding details. This script can be used as is in
application server payload decoders.

:::

### Telemetry

#### Device Profiles

Device has 6 configurable profiles. Each profile stores independent sensor and uplink send configuration.
This allows device to quickly change operating characteristics without requiring costly downlink configuration messages.
Profile can be switched using [Device Commands](#device-commands), [magnet](#mag-sw-cmd) or even based on evaluated [Data Rules](#data-rules).
For instance switching between periodic keepalive mode with uplinks few times per day to more rapid telemetry every few minutes.

:::note

MikroTik can support your specific use case, new devices with custom default configuration are available.

:::

Devices come preconfigured with evaluation configuration to showcase some of possible use case:

<Anchor id="id46" />

**Default profile configuration**

| <Anchor id="profile-number" />Profile Number | Name | Description |
| --- | --- | --- |
| 0 | Sensor Telemetry | Send [current-state](#current-state), [device-orientation](#device-orientation) every 5 minutes. Send remaining telemetry every 60 minutes. |
| 1 | Activity Monitor | Send [activity](#activity), [full-activity](#full-activity), [current-state](#current-state) every 60 min and send [activity_state](#activity-state) events on activity idle transition. |
| 2 | Magnet Switch | Send [mag-switch](#mag-switch), [current-state](#current-state), [device-events](#device-events) every 60 minutes and send [mag_sw_cnt](#mag-sw-cnt) event when magnet is removed for at least 15 seconds. Save up to 10 events. |
| 3 | Orientation | Send [current-state](#current-state), [device-events](#device-events), [device-orientation](#device-orientation) every 60 minutes. Send [device-orientation](#device-orientation) frame in case of fast rotation by 30 degrees after idle ~30 seconds. Send [angle_1](#angle-1) event in case of specific orientation: V=(0,1,1). Save up to 3 events. |
| 4 | Asset Monitor | Send asset healt info every 3h with different frames based on events. |
| 5 | Empty |  |

See [`default-cfg.txt`](pathname:///assets/tg-lrx2-default-cfg.txt) for exact factory default configuration commands.

#### Configuring Sensors

##### Sampling Intervals

Periodic temperature, humidity and battery voltage sampling can be configured for specific use cases using [data poll-cfg](#data-poll-cfg) command.
Device can sample data at a higher rate than uplink frames are sent. This gives opportunity to send average values or to perform
rule based decisions. Since sampling interval influences device power consumption this can be leveraged to improve lifetime.

##### Averaging

Device also tracks average of sampled values in: [temperature_ema](#temperature-ema), [humidity_ema](#humidity-ema), [battery_mv_ema](#battery-mv-ema), [angle_ema](#angle-ema). Command
[data ema-cfg](#data-ema-cfg) configures exponential moving average (<Anchor id="ema" />EMA) period and optionally can send [EMA](#ema) values in [current-state](#current-state),
[dev-health](#dev-health), [device-orientation](#device-orientation) if *send-ema-** is enabled.

Count parameters *temp-cnt*, *humid-cnt*, *bat-cnt*, *orient-cnt* in [data ema-cfg](#data-ema-cfg) determine coefficient *a* used for moving
average calculation. Moving EMA is calculated based on previous value *ema* and new value *sample* as:

```none
ema(t) = sample(t) * a + ema(t-1) * (1 - a)
```

To get approximate time constant *t* of EMA you need to use sampling intervals configured by [data poll-cfg](#data-poll-cfg) and [data orient-cfg](#data-orient-cfg)
(*interval*) and respective count parameter (*N*):

```none
t ~ (N + 1) * interval / 2
```

To get required count parameter value for [data ema-cfg](#data-ema-cfg):

```none
N ~ 2 * t / interval - 1
```

Example:

Temperature sampling interval *th-poll-int* is configured to 30s using [data poll-cfg](#data-poll-cfg). To configure EMA with time constant t ~ 60 minutes:

```none
temp-cnt = 2 * 3600 / 30 - 1 = 239
```

Assuming profile #0 is used and we don’t want to change other parameters we need to send command:

```none
data ema-cfg 1,239
```

##### Histogram

All periodic samples are added to temperature and humidity histograms. Histograms can be used in addition to regular telemetry
or simply stand alone to monitor temperature and humidity distribution. Configure bins and epoch intervals using [data temp-histo-cfg](#data-temp-histo-cfg),
[data humid-histo-cfg](#data-humid-histo-cfg) commands and/or enable [temp-histogram](#temp-histogram), [humid-histogram](#humid-histogram) frames. All histogram frames contain epoch
number to detect histogram counter reset. Since frame size is limited to 1B per bin, if internal bin counter value is above 255 histogram
will be normalized (probability type) for uplink.

Example configuration:

```none
data temp-histo-cfg 1,86400,0,0,1,1,-10,0,10,15,17.5,20,22.5,25.0,30
data humid-histo-cfg 1,86400,0,0,1,1,10,20,30,40,50,60,70,80,90
```

##### Orientation

![Device accelerometer axis.](./img/tg-lrx2-axis.png)

*Device accelerometer axis.*

Periodic device 3D orientation sampling relative to Earth can be configured using command: [data orient-cfg](#data-orient-cfg). In addition 3 user
orientation vectors ref-1, ref-2, ref-3 can be configured to detect specific device orientations. User variables [angle_1](#angle-1), [angle_2](#angle-2),
[angle_3](#angle-3) contain current angle between device last sampled orientation and user defined vector. These variables can be used
in [Data Rules](#data-rules) to trigger on specific orientation. [angle_ema](#angle-ema) is angle between last sampled device orientation and [EMA](#ema) value of
samples. In addition coarse orientation is also available with [major_axis_orientation](#major-axis-orientation) variable.

<Anchor id="id48" />

**[major_axis_orientation](#major-axis-orientation) description**

| Value | Numeric code | Description |
| --- | --- | --- |
| XH | 0 | X up |
| HL | 1 | X down |
| YH | 2 | Y up |
| YL | 3 | Y down |
| ZH | 4 | Z up |
| ZL | 5 | Z down |
| DISABLED | 7 | sensor disabled |

Coarse orientation has advantage that it is sent in [current-state](#current-state) frame.

##### Activity Monitor

Device has activity monitoring service based on accelerometer. This service will automatically manage simple state machine that
determines movement/activity. [activity_s](#activity-s), [high_activity_s](#high-activity-s), [total_activity_s](#total-activity-s) count accumulated time in each state
[activity_state](#activity-state), [activity_state_etm](#activity-state-etm) hold state information.

Command [data activity-cfg](#data-activity-cfg) can be used to configure mode and thresholds for activity monitoring. [data activity-cal](#data-activity-cal) can be used to
automatically perform calibration for specific mode.

*level1-th* and *level2-th* units are *1/64 * 2G* irrespective of other accelerometer settings (like in *data acc-cfg*).
*level2-cnt* is internally computed and not user configurable. *level2-cnt* is always in range 7..15 and calculated as:

```none
level2-cnt = 7 + round((1 - ((level2-th - level1-th - 1) / 61)) * 8)
```

<Anchor id="id49" />

**[activity_state](#activity-state) description**

| Numeric code | Value |
| --- | --- |
| 0 | IDLE |
| 1 | LOW |
| 2 | HIGH |
| 3 | DISABLED |

###### Single Mode

Mode in [data activity-cfg](#data-activity-cfg) is set to single.

- If accelerometer sample value in any axis is above *level1-th* device transitions from IDLE to LOW state.

- If all samples for at least 1.3s are below *level1-th* device transitions from LOW to IDLE state.

Example to set profile #0 single mode with threshold 0.25G:

```none
data activity-cfg 1,1,8,63
```

###### Dual Mode

Mode in [data activity-cfg](#data-activity-cfg) is set to dual.

In dual mode LOW state has two sub states: LOW1 and LOW2 that both represent LOW. Device will report LOW state during both of
these and actvity counter values are incremented as if in LOW state. Only difference is transition logic between these states.

<Anchor id="id50" />

**[activity_state](#activity-state) dual mode state transitions**

| Current | Next | Condition |
| --- | --- | --- |
| IDLE | LOW2 | sample &gt; *level1-th* |
| LOW2 | LOW1 | sample &lt; *level2-th* at least 5s |
| LOW1 | LOW2 | sample &gt; *level1-th* |
| LOW2 | HIGH | sample &gt; *level2-th* at least *level2-cnt* times |
| LOW1 | IDLE | sample &lt; *level1-th* at least 5s |
| HIGH | LOW1 | sample &lt; *level2-th* at least 5s |

Example to set profile #0 dual mode with thresholds 0.25G and 0.5G:

```none
data activity-cfg 1,2,8,16
```

###### Calibration

In addition to manually configuring *level1-th* and *level2-th* there is activity calibration functionality.
Executing command [data activity-cal](#data-activity-cal) will perform auto calibration of *cal-level*. *level-one* will calibrate *level1-th* and
*level-two* will calibrate *level2-th* for all profiles selected in *profile-mask*. For dual mode you can run *level-one* and
*level-two* in sequence. Calibration time is 15s. This functionality is mostly suited for periodic motion/vibration.

:::note

It may be useful to enable LED during calibration procedure or activity monitor testing to ensure correct operation.

:::

Example to calibrate profile #0 with single level activity monitor:

:::warning

Activity calibration with orientation enabled causes fault and device reboot.
Disable using [data orient-cfg](#data-orient-cfg) before calibration and re-enable after finished. See [LORA-279](#lora-279).

:::

- Place device in environment with periodic motion/activity to calibrate.

- Send commands:

  ```none
  data activity-cfg 1,1,,,1
  data activity-cal 1,1,1
  ```

- Observe LED periodic blink 2x/1.5s for ~ 15s.

- Test motion detection. During LOW activity device will blink LED 3x/1s.

- If calibration results are acceptable send command to disable LED:

  ```none
  data activity-cfg 1,,,,0
  ```

Example to calibrate profile #0 with dual level activity monitor:

- Place device in environment with periodic motion/activity for level 1 calibration.

- Send commands:

  ```none
  data activity-cfg 1,2,,,1
  data activity-cal 1,1,1
  ```

- Observe LED periodic blink 2x/1.5s for ~ 15s.

- Place device in environment for level 2 calibration.

- Send commands to calibrate level 2:

  ```none
  data activity-cal 1,2,1
  ```

- Observe LED periodic blink 2x/1.5s for ~ 15s.

- Test motion detection. During HIGH activity device will blink LED 6x/1s.

- If calibration results are acceptable send command to disable LED:

  ```none
  data activity-cfg 1,,,,0
  ```

:::note

After calibration *level1-th* and *level2-th* can be manually changed using command [data activity-cfg](#data-activity-cfg).

:::

##### Impact and Free fall

Command [data acc-cfg](#data-acc-cfg) can be used to configure device accelerometer for basic impact and free-fall detection.
Frames: [motion-events](#motion-events), [impact-count](#impact-count) contain relevant data fields. [current-state](#current-state) contains [impact_evnt](#impact-evnt),
[free_fall_evnt](#free-fall-evnt) flags that indicate new event. These can be used if explicit read is preferred.

Variables [impact_cnt](#impact-cnt), [impact_cnt_x](#impact-cnt-x), [impact_cnt_y](#impact-cnt-y), [impact_cnt_z](#impact-cnt-z), [impact_etm](#impact-etm), [free_fall_cnt](#free-fall-cnt),
[free_fall_etm](#free-fall-etm) allow rule based logic.

:::warning

If [Activity Monitor](#activity-monitor) is enabled impact and free fall detection can’t be used and will be ignored.

:::

#### Data Rules

Up to 32 custom user rules are configurable using commands: [data set-rule](#data-set-rule), [data del-rule](#data-del-rule). Rules have test
expression, optional input rules and actions to perform.

Command syntax to add or override rules:

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>], [<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

##### Test Expression

&lt;test-expr&gt;: [^] [variable-type](#variable-type) &lt;operator&gt; &lt;argument&gt;

| [^] | use variable absolute value in expression |
| --- | --- |
| [variable-type](#variable-type) | variable name or ID |
| &lt;operator&gt; | &gt;, &gt;=, &lt;, &lt;=, ==, !=, % |
| &lt;argument&gt; | numeric value |

Example:

```none
data set-rule 0,profile == 0
data set-rule 1,^temperature > 30.55
data set-rule 2,impact_etm < 60
```

Same rules can be given using [User Variables](#user-variables) numeric IDs:

```none
data set-rule 0,0 == 0
data set-rule 1,^8 > 30.55
data set-rule 2,24 < 60
```

##### Input Expression

Input expression is used if rule needs to depend on result of other rules. This allows constructing
sophisticated logic based on multiple test expressions.

`<input-expr>: [&][|][!]<input-rule>[<]`

| [&] | logical AND of &lt;rule-num&gt; and &lt;input-rule&gt; |
| --- | --- |
| [\|] | logical OR of &lt;rule-num&gt; and &lt;input-rule&gt; |
| [!] | logical NOT of input value |
| &lt;input-rule&gt; | rule number to add as a input |
| [&lt;] | use rule [combined state](#combined-state) as input value, otherwise [local state](#local-state). |

Following configuration will send [current-state](#current-state) data frame if magnet switch changed state less than 15s ago
and [temperature](#temperature) or [humidity](#humidity) are out of range (-5..55 and 10..90%):

```none
data del-rule
data set-rule 0,temperature < -5
data set-rule 1,temperature > 55
data set-rule 2,humidity < 10
data set-rule 3,humidity > 90,|0|1|2
data set-rule 4,mag_sw_etm < 15,&3<,,,,,,current-state
```

:::warning

Input rules are evaluated in numeric order irrespective of ordering in set-rule command.

:::

##### Actions

Rule [Test Expression](#test-expression) evaluated value represents data rule <Anchor id="local-state" />local state. Local state evaluated
with optional input rules represents <Anchor id="combined-state" />combined state.

If [combined state](#combined-state) changes to TRUE state optional rule actions are performed: profile switching,
event generation, frame scheduling, user timer reset.

If &lt;switch-profile&gt; parameter is given, current profile will be changed. For example if temperature
drops below 15 C device will switch to profile 5 ([Device Profiles](#device-profiles)):

```none
data set-rule 1,temperature < 15,,5
```

Up to 4 different [Data Frames](#data-frames) can be scheduled per rule:

```none
data set-rule 0,impact_cnt % 10,,,,,,,current-state,device-orientation,dev-health,ema-temp
```

:::note

Rule chaining can be used if more than 4 frames should be sent.

:::

Up to 4 different events can be generated per rule:

```none
data set-rule 0,impact_cnt % 10,,,temperature_ema,humidity_ema,activity_state,timer_1
```

##### Events

[Actions](#actions) can optionally generate events. Events are time stamped [User Variables](#user-variables) that are sent in
[device-events](#device-events) frame. Event storage can be configured using [data event-cfg](#data-event-cfg) command. If device
has received absolute time using [Time Synchronization](#time-synchronization) events will have POSIX time stamp. This allows
collecting specific historic data to report later. Event uplink can be triggered periodically,
based on some rule or manually using downlink command.

### Magnet Switch

Device has magnet switch that can be used for command input or as magnetic field sensor. If
unused, command input can be completely disabled or [PIN](#pin) protected using [mag svc](#mag-svc) command.

:::note

Unique <Anchor id="pin" />PIN code comes with each device.

:::

#### Command Input

User must apply command sequence of 1 to 4 digits. Each digit is entered consecutively. After 2.5s
idle, valid input command is executed and device indicates result using LED. Successfully
executed command is indicated with 3x 0.2s LED blinks and failure is 1s long LED pulse. Invalid
commands are ignored.

When magnetic field is applied to device, LED starts blinking with interval 500ms ON, 500ms OFF
(or according to [mag cfg](#mag-cfg) configured blink-mode). When LED is switched on, internal counter is incremented
starting from 0. When magnetic field is removed counter value is latched as user input digit. If magnetic
field is applied again, next digit in input sequence is started. If interval after applying digit is larger than
2.5s, sequence is evaluated.

:::note

When applying input code based on time, ensure to follow this equation: T = N - 0.5, where
N is input digit from 1 to 9 and T is time in seconds to apply magnetic field. The interval between digits
must be less than 2.5s, but more than 200ms.

:::

Some commands require [PIN](#pin) mode to be entered and some can be optionally protected by [PIN](#pin) mode. See table
[Magnet switch commands](#mag-sw-cmd). To enter [PIN](#pin) mode, user must apply sequence of [PIN](#pin) digits provided
with the device. Once [PIN](#pin) mode is entered it will expire after configurable time and device will return
back to normal mode.

:::warning

It is also possible to completely disable magnet commands. Only way to re-enable is using
LoRaWAN downlink command. This can be useful if magnet sensor is used only for detecting external signals
and no user commands are expected or allowed.

:::

<Anchor id="mag-sw-cmd" />

**Magnet switch commands**

| Sequence | PIN mode | Command description |
| --- | --- | --- |
| 2 | optional | Activate - enable [RUN](#run) mode. |
| 3-1 | optional | Trigger [current-state](#current-state) frame uplink. |
| 4-1-X | optional | Switch device profile, where X is [Profile Number](#profile-number) + 1 [1..6]. |
| 4-2-1 | optional | Set primary band to [BAND_1GHz](#band-1ghz). |
| 4-2-2 | optional | Set primary band to [BAND_2GHz](#band-2ghz). |
| 4-3-1 | optional | Enable secondary band. |
| 4-3-9 | optional | Disable secondary band. |
| 6-1 | optional | Device restart. |
| 6-2-9 | optional | Deactivate device - [SHUTDOWN](#shutdown) mode. |
| 9-<Anchor id="x-y" />X-Y | optional | Set region for sub GHz band as per [Supported regions](#supported-regions). |
| 6-9-9 | mandatory | Device factory reset. |
| 3-1-5 | mandatory | Exit PIN mode. |
| A-B-C-D | – | Enter PIN mode. A-B-C-D are digits of device factory [PIN](#pin) code. |
| 5-3-1 | optional | Reserved. |

:::note

LED indications during digit input can be changed based on device configuration. It is possible
to change or completely disable LED indications using [mag cfg](#mag-cfg).

:::

#### Magnet Sensor

Magnetic sensor is always operational (even when commands are applied). This sensor can be utilized to detect
switching events [mag_sw_flag](#mag-sw-flag) or to count number of these events [mag_sw_cnt](#mag-sw-cnt). Device can report current
switch state, number of state changes and last time stamp (UNIX/uptime) [mag_switch_ts](#mag-switch-ts).
Additionally you can create rules based on these attributes.

### Command Encoding

Device commands are binary encoded to reduce downlink message size. We provide Python utilities
to verify, encode and publish commands as LoRaWAN binary downlink messages.

Install from [PyPI](https://pypi.org/project/tg-lrx2-utils/) with *pip install tg-lrx2-utils*.

Example configuration to set [current-state](#current-state) and [activity](#activity) frame uplink every 600 seconds and
[mag-switch](#mag-switch) every 43200 seconds as confirmed message:

```none
# lora-script.txt
frame set-cfg 1,601,0,0,current-state,activity
frame set-cfg 1,43200,1,0,mag-switch
```

We can use *tg-lrx2-encode* to convert text commands to binary messages for downlink:

```none
tg-lrx2-encode --script ./lora-script.txt --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
```

:::note

[`tg-lrx2-2.0-desc.yml`](pathname:///assets/tg-lrx2-2.0-desc.yml) contains full device characterization and is used by other tools.
Make sure to use correct file for specific device and FW version!

:::

*lora-pub.yml* will contain serialized binary payloads to use for downlink. You can either manually
schedule them using available web tools or use *tg-lrx2-pub* to schedule them on The Things Network:

```none
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

Example TTN credential file:

```none
# ttn-app.yml
app-id: "ttn-tag-demo@ttn"
host: "eu1.cloud.thethings.industries"
port: 1883
user: "ttn-tag-demo@ttn"
password: "NNSXS.5G..."
```

*tg-lrx2-encode* accepts command strings on CLI as well. This can be used for single or few lines of commands:

```none
tg-lrx2-encode --cmd $'frame send device-orientation\napp profile 1,0' --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

### Device Commands

All device commands consist of *group-name* and *cmd-name*. Optional parameters are given in square brackets.
Parameters must be comma separated for *tg-lrx2-encode* script. *group-name* and *cmd-name* can also be comma
separated but spaces are also accepted.

Example:

```none
app factory-reset <key>,[<fw-def>],<delay-ms>
```

Parameters &lt;key&gt; and &lt;delay-ms&gt; are mandatory, but &lt;fw-def&gt; is optional and can be omitted:

```none
app factory-reset 984651411,,2500
```

Each parameters has valid input range and format. Some parameters allow only specific choice between parameters
or choice between ranges.

Most parameters accept integer values. *%f* indicates that parameter accepts fractional value. Use of these values
results in larger downlink payload so if possible integer values should be preferred. [variable-type](#variable-type) indicates
that parameter accepts either user variable name or respective integer ID. [frame-type](#frame-type) indicates that parameter
accepts either data frame name or integer ID. *tg-lrx2-encode* automatically converts these names to numeric ID.

#### app set-mode

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app set-mode &lt;mode&gt;
  
  
    Set device operating mode
  
  
    Parameter
    Range
    Description
  
  
    mode
    0
    SHUTDOWN
  
  
    
    1
    RUN
  

#### app profile

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app profile &lt;profile-num&gt;,&lt;make-default&gt;
  
  
    Switch active profile and optionally make default
  
  
    Parameter
    Range
    Description
  
  
    profile-num
    0..5
    
  
  
    make-default
    0
    no
  
  
    
    1
    yes
  

#### app reset

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app reset &lt;type&gt;
  
  
    System reset
  
  
    Parameter
    Range
    Description
  
  
    type
    0
    board
  
  
    
    1
    app only
  

#### app factory-reset

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app factory-reset &lt;key&gt;,[&lt;fw-def&gt;],&lt;delay-ms&gt;
  
  
    Reboot device, clear saved configuration and set to defaults (optional)
  
  
    Parameter
    Range
    Description
  
  
    key
    984651411
    
  
  
    fw-def
    784565141
    don’t apply default configuration
  
  
    delay-ms
    0..65535
    
  

#### app led

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app led [&lt;enable&gt;]
  
  
    Configure application LED signals
  
  
    Parameter
    Range
    Description
  
  
    enable
    0
    no
  
  
    
    1
    yes
  

#### app set-time

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    app set-time [&lt;unix-time-s&gt;],&lt;uptime-s&gt;
  
  
    Set UNIX time relative to device uptime
  
  
    Parameter
    Range
    Description
  
  
    unix-time-s
    0..4294967295
    
  
  
    uptime-s
    0..4294967295
    
  

#### lora set-region

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora set-region &lt;region-code&gt;
  
  
    Set LoRaWAN region for sub GHz band
  
  
    Parameter
    Range
    Description
  
  
    region-code
    1
    EU868
  
  
    
    2
    AS923-1
  
  
    
    3
    US915
  
  
    
    4
    AU915
  
  
    
    7
    AS923-2
  
  
    
    8
    AS923-3
  
  
    
    9
    IN868
  
  
    
    10
    KR920
  

#### lora primary-band

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora primary-band &lt;band&gt;
  
  
    Select primary band
  
  
    Parameter
    Range
    Description
  
  
    band
    1
    &lt;1GHz
  
  
    
    2
    2.45GHz
  

#### lora second-band

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora second-band &lt;mode&gt;
  
  
    Enable or disable secondary band
  
  
    Parameter
    Range
    Description
  
  
    mode
    0
    off
  
  
    
    1
    on
  

#### lora join-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora join-cfg &lt;band&gt;,&lt;duty&gt;
  
  
    Configure join duty cycle for band
  
  
    Parameter
    Range
    Description
  
  
    band
    1
    &lt;1GHz
  
  
    
    2
    2.45GHz
  
  
    duty
    0
    0.1%
  
  
    
    1..254
    
  
  
    
    255
    1%
  

#### lora link-chk

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora link-chk &lt;band&gt;,&lt;int-minutes&gt;
  
  
    Set band specific link check interval and timeout
  
  
    Parameter
    Range
    Description
  
  
    band
    1
    &lt;1GHz
  
  
    
    2
    2.45GHz
  
  
    int-minutes
    0
    off
  
  
    
    5..500000
    
  

#### lora adr-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora adr-cfg &lt;en-netw-adr&gt;,[&lt;fixed-data-rate&gt;]
  
  
    Enable network ADR or configure fixed data rate
  
  
    Parameter
    Range
    Description
  
  
    en-netw-adr
    0
    off
  
  
    
    1
    on
  
  
    fixed-data-rate
    0..6
    
  

#### lora clk-sync

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora clk-sync [&lt;int-minutes&gt;],[&lt;leap-sec&gt;],&lt;sync-now&gt;,[&lt;retry-s&gt;],[&lt;retry-cnt&gt;]
  
  
    Absolute time synchronization
  
  
    Parameter
    Range
    Description
  
  
    int-minutes
    0
    off
  
  
    
    1..65535
    
  
  
    leap-sec
    -128..127
    
  
  
    sync-now
    0
    no
  
  
    
    1
    yes
  
  
    retry-s
    0..255
    
  
  
    retry-cnt
    0..255
    
  

#### lora cfg-class-b

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora cfg-class-b [&lt;auto-en&gt;],[&lt;ping-slot-int-s&gt;]
  
  
    Configure LoRaWAN Class B
  
  
    Parameter
    Range
    Description
  
  
    auto-en
    0
    off
  
  
    
    1
    on
  
  
    ping-slot-int-s
    1
    
  
  
    
    2
    
  
  
    
    4
    
  
  
    
    8
    
  
  
    
    16
    
  
  
    
    32
    
  
  
    
    64
    
  
  
    
    128
    
  

#### lora class

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora class &lt;class&gt;
  
  
    Switch LoRaWAN class
  
  
    Parameter
    Range
    Description
  
  
    class
    0
    A
  
  
    
    1
    B
  

#### lora join-eui

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora join-eui &lt;cred-ch-key&gt;,&lt;eui-0&gt;,&lt;eui-1&gt;,&lt;eui-2&gt;,&lt;eui-3&gt;,&lt;eui-4&gt;,&lt;eui-5&gt;,&lt;eui-6&gt;,&lt;eui-7&gt;
  
  
    Override network JoinEUI
  
  
    Parameter
    Range
    Description
  
  
    cred-ch-key
    87904163
    
  
  
    eui-0
    0..255
    
  
  
    eui-1
    0..255
    
  
  
    eui-2
    0..255
    
  
  
    eui-3
    0..255
    
  
  
    eui-4
    0..255
    
  
  
    eui-5
    0..255
    
  
  
    eui-6
    0..255
    
  
  
    eui-7
    0..255
    
  

#### lora net-key

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora net-key &lt;cred-ch-key&gt;,&lt;key-0&gt;,&lt;key-1&gt;,&lt;key-2&gt;,&lt;key-3&gt;,&lt;key-4&gt;,&lt;key-5&gt;,&lt;key-6&gt;,&lt;key-7&gt;,&lt;key-8&gt;,&lt;key-9&gt;,&lt;key-10&gt;, &lt;key-11&gt;,&lt;key-12&gt;,&lt;key-13&gt;,&lt;key-14&gt;,&lt;key-15&gt;
  
  
    Override network AppKey
  
  
    Parameter
    Range
    Description
  
  
    cred-ch-key
    87904163
    
  
  
    key-0
    0..255
    
  
  
    key-1
    0..255
    
  
  
    key-2
    0..255
    
  
  
    key-3
    0..255
    
  
  
    key-4
    0..255
    
  
  
    key-5
    0..255
    
  
  
    key-6
    0..255
    
  
  
    key-7
    0..255
    
  
  
    key-8
    0..255
    
  
  
    key-9
    0..255
    
  
  
    key-10
    0..255
    
  
  
    key-11
    0..255
    
  
  
    key-12
    0..255
    
  
  
    key-13
    0..255
    
  
  
    key-14
    0..255
    
  
  
    key-15
    0..255
    
  

#### lora cred

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    lora cred [&lt;confirm-timeout-s&gt;],[&lt;action&gt;]
  
  
    User network credential management
  
  
    Parameter
    Range
    Description
  
  
    confirm-timeout-s
    60..65535
    revert if not joined
  
  
    action
    0
    clear pending
  
  
    
    1
    try now
  
  
    
    87904163
    force confirm
  

#### frame send

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    frame send &lt;frame-id&gt;,…
  
  
    Schedule uplink frames
  
  
    Parameter
    Range
    Description
  
  
    frame-id
    frame-type
    
  

#### frame set-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    frame set-cfg &lt;profile-mask&gt;,[&lt;ul-period-s&gt;],[&lt;confirmed&gt;],[&lt;on-join&gt;],&lt;frame-id&gt;,…
  
  
    Set uplink frame configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    ul-period-s
    0
    off
  
  
    
    1..65535
    
  
  
    confirmed
    0
    no
  
  
    
    1
    yes
  
  
    on-join
    0
    no
  
  
    
    1
    yes
  
  
    frame-id
    frame-type
    
  

#### frame clear-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    frame clear-cfg &lt;profile-mask&gt;
  
  
    Clear all frame config for specified profiles (as if ‘set-cfg profile-mask,0,0,0,…’)
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  

#### mag cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    mag cfg [&lt;pin-timeout&gt;],[&lt;pin-protect&gt;],[&lt;blink-mode&gt;]
  
  
    Set configuration
  
  
    Parameter
    Range
    Description
  
  
    pin-timeout
    0..65535
    
  
  
    pin-protect
    0
    off
  
  
    
    1
    on
  
  
    blink-mode
    0
    half duty
  
  
    
    1
    pulse
  
  
    
    2
    off
  

#### mag svc

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    mag svc &lt;new-state&gt;,&lt;key&gt;
  
  
    Enable or disable magnet command interface
  
  
    Parameter
    Range
    Description
  
  
    new-state
    0
    off
  
  
    
    1
    on
  
  
    key
    649864801
    
  

#### data sample

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data sample
  
  
    Force sensor polling
  

#### data next-epoch

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data next-epoch &lt;type&gt;
  
  
    Manually start next histogram epoch
  
  
    Parameter
    Range
    Description
  
  
    type
    
    
  

#### data poll-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data poll-cfg &lt;profile-mask&gt;,[&lt;th-poll-int&gt;],[&lt;sync-period&gt;],[&lt;on-mag-switch&gt;],[&lt;on-activity-change&gt;],[&lt;on-impact&gt;], [&lt;on-free-fall&gt;],[&lt;on-ul-stale&gt;],[&lt;bat-poll-int&gt;]
  
  
    Set data polling configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    th-poll-int
    1..4294967295
    temperature and humidity
  
  
    sync-period
    0
    no
  
  
    
    1
    yes
  
  
    on-mag-switch
    0
    no
  
  
    
    1
    yes
  
  
    on-activity-change
    0
    no
  
  
    
    1
    yes
  
  
    on-impact
    0
    no
  
  
    
    1
    yes
  
  
    on-free-fall
    0
    no
  
  
    
    1
    yes
  
  
    on-ul-stale
    0
    no
  
  
    
    1
    yes
  
  
    bat-poll-int
    1..4294967295
    battery voltage
  

#### data temp-histo-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data temp-histo-cfg &lt;profile-mask&gt;,[&lt;epoch-interval-s&gt;],[&lt;epoch-interval-cnt&gt;],[&lt;epoch-max-bin-cnt&gt;], [&lt;frame-on-new-epoch&gt;],[&lt;lim-divider&gt;],[&lt;bin-limit-0&gt;],[&lt;bin-limit-1&gt;],[&lt;bin-limit-2&gt;],[&lt;bin-limit-3&gt;],[&lt;bin-limit-4&gt;], [&lt;bin-limit-5&gt;],[&lt;bin-limit-6&gt;],[&lt;bin-limit-7&gt;],[&lt;bin-limit-8&gt;]
  
  
    Set temperature histogram configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    epoch-interval-s
    0
    off
  
  
    
    1..4294967295
    
  
  
    epoch-interval-cnt
    0
    off
  
  
    
    1..4294967295
    
  
  
    epoch-max-bin-cnt
    0
    off
  
  
    
    1..4294967295
    
  
  
    frame-on-new-epoch
    0
    no
  
  
    
    1
    yes
  
  
    lim-divider
    1..4294967295
    
  
  
    bin-limit-0
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-1
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-2
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-3
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-4
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-5
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-6
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-7
    -128..127
    °C
  
  
    
    %f
    
  
  
    bin-limit-8
    -128..127
    °C
  
  
    
    %f
    
  

#### data humid-histo-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data humid-histo-cfg &lt;profile-mask&gt;,[&lt;epoch-interval-s&gt;],[&lt;epoch-interval-cnt&gt;],[&lt;epoch-max-bin-cnt&gt;], [&lt;frame-on-new-epoch&gt;],[&lt;lim-divider&gt;],[&lt;bin-limit-0&gt;],[&lt;bin-limit-1&gt;],[&lt;bin-limit-2&gt;],[&lt;bin-limit-3&gt;],[&lt;bin-limit-4&gt;], [&lt;bin-limit-5&gt;],[&lt;bin-limit-6&gt;],[&lt;bin-limit-7&gt;],[&lt;bin-limit-8&gt;]
  
  
    Set humidity histogram configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    epoch-interval-s
    0
    off
  
  
    
    1..4294967295
    
  
  
    epoch-interval-cnt
    0
    off
  
  
    
    1..4294967295
    
  
  
    epoch-max-bin-cnt
    0
    off
  
  
    
    1..4294967295
    
  
  
    frame-on-new-epoch
    0
    no
  
  
    
    1
    yes
  
  
    lim-divider
    1..4294967295
    
  
  
    bin-limit-0
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-1
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-2
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-3
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-4
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-5
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-6
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-7
    0..99
    RH%
  
  
    
    %f
    
  
  
    bin-limit-8
    0..99
    RH%
  
  
    
    %f
    
  

#### data ema-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data ema-cfg &lt;profile-mask&gt;,[&lt;temp-cnt&gt;],[&lt;humid-cnt&gt;],[&lt;bat-cnt&gt;],[&lt;orient-cnt&gt;],[&lt;send-ema-temp&gt;],[&lt;send-ema-humid&gt;], [&lt;send-ema-bat&gt;],[&lt;send-ema-orient&gt;]
  
  
    Set exponential moving average (EMA) configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    temp-cnt
    1..32766
    a = 2 / (temp-cnt + 1)
  
  
    humid-cnt
    1..32766
    a = 2 / (humid-cnt + 1)
  
  
    bat-cnt
    1..32766
    a = 2 / (bat-cnt + 1)
  
  
    orient-cnt
    1..32766
    a = 2 / (orient-cnt + 1)
  
  
    send-ema-temp
    0
    no
  
  
    
    1
    yes
  
  
    send-ema-humid
    0
    no
  
  
    
    1
    yes
  
  
    send-ema-bat
    0
    no
  
  
    
    1
    yes
  
  
    send-ema-orient
    0
    no
  
  
    
    1
    yes
  

#### data activity-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data activity-cfg &lt;profile-mask&gt;,[&lt;mode&gt;],[&lt;level1-th&gt;],[&lt;level2-th&gt;],[&lt;en-led&gt;]
  
  
    Set activity monitor configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    mode
    0
    off
  
  
    
    1
    single
  
  
    
    2
    dual
  
  
    level1-th
    1..63
    
  
  
    level2-th
    1..63
    
  
  
    en-led
    0
    off
  
  
    
    1
    on
  

#### data acc-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data acc-cfg &lt;profile-mask&gt;,[&lt;full-scale&gt;],[&lt;en-impact-x&gt;],[&lt;en-impact-y&gt;],[&lt;en-impact-z&gt;],[&lt;impact-th&gt;],[&lt;impact-dur&gt;], [&lt;en-ff&gt;],[&lt;ff-th&gt;],[&lt;ff-dur&gt;],[&lt;data-rate&gt;],[&lt;filter&gt;],[&lt;lp-mode&gt;],[&lt;low-noise&gt;]
  
  
    Set accelerometer configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    full-scale
    0
    2G
  
  
    
    1
    4G
  
  
    
    2
    8G
  
  
    
    3
    16G
  
  
    en-impact-x
    0
    off
  
  
    
    1
    on
  
  
    en-impact-y
    0
    off
  
  
    
    1
    on
  
  
    en-impact-z
    0
    off
  
  
    
    1
    on
  
  
    impact-th
    1..63
    impact-th * full-scale / 64
  
  
    impact-dur
    0..3
    
  
  
    en-ff
    0
    off
  
  
    
    1
    on
  
  
    ff-th
    0..7
    
  
  
    ff-dur
    0..63
    
  
  
    data-rate
    2
    Hz
  
  
    
    13
    
  
  
    
    25
    
  
  
    
    500
    
  
  
    
    100
    
  
  
    
    200
    
  
  
    filter
    2
    cutoff = data-rate/filter
  
  
    
    4
    
  
  
    
    10
    
  
  
    
    20
    
  
  
    lp-mode
    0..3
    
  
  
    low-noise
    0
    no
  
  
    
    1
    yes
  

#### data orient-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data orient-cfg &lt;profile-mask&gt;,[&lt;enable&gt;],[&lt;max-1G-offset&gt;],[&lt;poll-interval-s&gt;],[&lt;ref-1-x&gt;],[&lt;ref-1-y&gt;],[&lt;ref-1-z&gt;], [&lt;ref-2-x&gt;],[&lt;ref-2-y&gt;],[&lt;ref-2-z&gt;],[&lt;ref-3-x&gt;],[&lt;ref-3-y&gt;],[&lt;ref-3-z&gt;]
  
  
    Set orientation sense configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    enable
    0
    off
  
  
    
    1
    on
  
  
    max-1G-offset
    1..20
    
  
  
    poll-interval-s
    1..4294967295
    
  
  
    ref-1-x
    -32768..32767
    
  
  
    ref-1-y
    -32768..32767
    
  
  
    ref-1-z
    -32768..32767
    
  
  
    ref-2-x
    -32768..32767
    
  
  
    ref-2-y
    -32768..32767
    
  
  
    ref-2-z
    -32768..32767
    
  
  
    ref-3-x
    -32768..32767
    
  
  
    ref-3-y
    -32768..32767
    
  
  
    ref-3-z
    -32768..32767
    
  

#### data event-cfg

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data event-cfg &lt;profile-mask&gt;,[&lt;max-count&gt;],[&lt;send-th&gt;],[&lt;discard&gt;],[&lt;send-all&gt;]
  
  
    Set event storage configuration
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    max-count
    0
    disabled
  
  
    
    1..100
    
  
  
    send-th
    0..65535
    if count &gt;= send-th: send(device-events)
  
  
    discard
    0
    oldest
    if no free space
  
  
    
    1
    newest
  
  
    send-all
    0
    off
  
  
    
    1
    on
  

#### data erase-events

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data erase-events [&lt;num-oldest&gt;]
  
  
    Erase &lt;num-oldest&gt; events if provided, otherwise all
  
  
    Parameter
    Range
    Description
  
  
    num-oldest
    0..65535
    
  

#### data del-rule

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data del-rule [&lt;rule-num&gt;]
  
  
    Delete &lt;rule-num&gt; rules if provided, otherwise delete all
  
  
    Parameter
    Range
    Description
  
  
    rule-num
    0..31
    
  

#### data set-rule

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data set-rule [&lt;rule-num&gt;],&lt;test-expr&gt;,[&lt;input-expr&gt;],[&lt;switch-profile&gt;],[&lt;make-event-0&gt;],[&lt;make-event-1&gt;], [&lt;make-event-2&gt;],[&lt;make-event-3&gt;],[&lt;send-frame-0&gt;],[&lt;send-frame-1&gt;],[&lt;send-frame-2&gt;],[&lt;send-frame-3&gt;],[&lt;clr-timer-mask&gt;]
  
  
    Set data rule &lt;rule-num&gt;
  
  
    Parameter
    Range
    Description
  
  
    rule-num
    0..31
    
  
  
    test-expr
    
    
  
  
    input-expr
    
    
  
  
    switch-profile
    0..5
    
  
  
    make-event-0
    variable-type
    
  
  
    make-event-1
    variable-type
    
  
  
    make-event-2
    variable-type
    
  
  
    make-event-3
    variable-type
    
  
  
    send-frame-0
    frame-type
    
  
  
    send-frame-1
    frame-type
    
  
  
    send-frame-2
    frame-type
    
  
  
    send-frame-3
    frame-type
    
  
  
    clr-timer-mask
    0..15
    
  

#### data timer

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data timer [&lt;timer_1&gt;],[&lt;timer_2&gt;],[&lt;timer_3&gt;],[&lt;timer_4&gt;]
  
  
    Set user timer value
  
  
    Parameter
    Range
    Description
  
  
    timer_1
    0..4294967295
    timer_1
  
  
    timer_2
    0..4294967295
    timer_2
  
  
    timer_3
    0..4294967295
    timer_3
  
  
    timer_4
    0..4294967295
    timer_4
  

#### data activity-cal

  <colgroup>
    <col style={{width: "20.8333%"}} />
    <col style={{width: "20.8333%"}} />
    <col style={{width: "12.5%"}} />
    <col style={{width: "45.8333%"}} />
  </colgroup>
  
    data activity-cal &lt;profile-mask&gt;,&lt;cal-level&gt;,&lt;cal-led&gt;
  
  
    Run activity monitor calibration and apply result to profiles
  
  
    Parameter
    Range
    Description
  
  
    profile-mask
    1..63
    bitfield
  
  
    cal-level
    1
    level-one
  
  
    
    2
    level-two
  
  
    cal-led
    0
    no
  
  
    
    1
    yes
  

### Data Frames

<Anchor id="frame-type" />

| ID | Size [B] | Name | Data Fields |
| --- | --- | --- | --- |
| 1 | 5 | <Anchor id="current-state" />current-state | [temperature](#temperature), [humidity](#humidity), [mag_sw_cnt_u8](#mag-sw-cnt-u8), [major_axis_orientation](#major-axis-orientation), [activity_state](#activity-state), [free_fall_evnt](#free-fall-evnt), [impact_evnt](#impact-evnt), [pending_evnt](#pending-evnt) |
| 2 | variable | <Anchor id="device-events" />device-events | [event-list](#event-list) |
| 3 | 11 | <Anchor id="temp-histogram" />temp-histogram | [temp_histo_epoch](#temp-histo-epoch), [temp_histo_bin[10]](#temp-histo-bin-10) |
| 4 | 11 | <Anchor id="humid-histogram" />humid-histogram | [humid_histo_epoch](#humid-histo-epoch), [humid_histo_bin[10]](#humid-histo-bin-10) |
| 5 | 3 | <Anchor id="device-orientation" />device-orientation | [orientation_x](#orientation-x), [orientation_y](#orientation-y), [orientation_z](#orientation-z) |
| 6 | 9 | <Anchor id="full-activity" />full-activity | [activity_state](#activity-state), [activity_s](#activity-s), [high_activity_s](#high-activity-s) |
| 7 | 8 | <Anchor id="motion-events" />motion-events | [impact_cnt](#impact-cnt), [free_fall_cnt](#free-fall-cnt) |
| 8 | 8 | <Anchor id="mag-switch" />mag-switch | [mag_sw_cnt](#mag-sw-cnt), [mag_switch_ts](#mag-switch-ts) |
| 9 | 8 | <Anchor id="impact-count" />impact-count | [impact_cnt_u16](#impact-cnt-u16), [impact_cnt_x_u16](#impact-cnt-x-u16), [impact_cnt_y_u16](#impact-cnt-y-u16), [impact_cnt_z_u16](#impact-cnt-z-u16) |
| 10 | 2 | <Anchor id="last-temp" />last-temp | [temperature](#temperature) |
| 11 | 2 | <Anchor id="ema-temp" />ema-temp | [temperature_ema](#temperature-ema) |
| 12 | 1 | <Anchor id="last-humid" />last-humid | [humidity](#humidity) |
| 13 | 1 | <Anchor id="ema-humid" />ema-humid | [humidity_ema](#humidity-ema) |
| 14 | 5 | <Anchor id="activity" />activity | [activity_state](#activity-state), [total_activity_s](#total-activity-s) |
| 20 | 8 | <Anchor id="dev-time" />dev-time | [uptime_s](#uptime-s), [unix_time](#unix-time) |
| 21 | 2 | <Anchor id="dev-health" />dev-health | [battery_mv](#battery-mv) |
| 22 | 11 | <Anchor id="version" />version | [version_pid](#version-pid), [version_maj](#version-maj), [version_min](#version-min), [version_rev](#version-rev), [version_hash[6]](#version-hash-6) |
| 23 | 11 | <Anchor id="serial-number" />serial-number | [serial_number[11]](#serial-number-11) |
| 24 | 10 | <Anchor id="cfg-state" />cfg-state | [cfg_app_crc](#cfg-app-crc), [cfg_net_crc](#cfg-net-crc), [cfg_frames_crc](#cfg-frames-crc), [cfg_data_crc](#cfg-data-crc), [cfg_rules_crc](#cfg-rules-crc) |
| 25 | variable | <Anchor id="full-cfg" />full-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 26 | variable | <Anchor id="app-cfg" />app-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 27 | variable | <Anchor id="net-cfg" />net-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 28 | variable | <Anchor id="frame-cfg" />frame-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 29 | variable | <Anchor id="data-cfg" />data-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 30 | variable | <Anchor id="rules-cfg" />rules-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |

### User Variables

<Anchor id="variable-type" />

| ID | Size [B] | Encoding | Name | Description |
| --- | --- | --- | --- | --- |
| 0 | 1 | u8 | <Anchor id="profile" />profile | current data profile (0..5) |
| 1 | 4 | u32 | <Anchor id="profile-etm" />profile_etm | elapsed time [s] since last profile switch |
| 2 | 4 | u32 | <Anchor id="daytime-tm" />daytime_tm | seconds since midnight 00:00 GMT or 0 if unknown |
| 3 | 4 | u32 | <Anchor id="unix-time" />unix_time | current UNIX time or device uptime if unknown |
| 4 | 4 | u32 | <Anchor id="net-frame-etm" />net_frame_etm | elapsed time since last network uplink |
| 5 | 1 | bool | <Anchor id="net-joined-flag" />net_joined_flag | network join state |
| 6 | 1 | u8 | <Anchor id="net-class" />net_class | currently selected LoRaWAN [class](#lora-class) |
| 7 | 1 | u8 | <Anchor id="net-region" />net_region | currently used LoRaWAN [region code](#lora-set-region) |
| 8 | 2 | f8.8 | <Anchor id="temperature" />temperature | last measured temperature |
| 9 | 2 | f8.8 | <Anchor id="temperature-ema" />temperature_ema | EMA of measured temperature |
| 10 | 1 | u8 | <Anchor id="humidity" />humidity | last measured humidity |
| 11 | 1 | u8 | <Anchor id="humidity-ema" />humidity_ema | EMA of measured humidity |
| 12 | 4 | u32 | <Anchor id="mag-sw-cnt" />mag_sw_cnt | magnetic switch state change counter |
| 13 | 4 | u32 | <Anchor id="mag-sw-etm" />mag_sw_etm | elapsed time since last magnetic switch change [s] |
| 14 | 1 | bool | <Anchor id="mag-sw-flag" />mag_sw_flag | current state of magnetic switch |
| 15 | 1 | activity | <Anchor id="activity-state" />activity_state | current device activity state |
| 16 | 4 | u32 | <Anchor id="activity-s" />activity_s | low activity (level 1) state counter [s] |
| 17 | 4 | u32 | <Anchor id="high-activity-s" />high_activity_s | high activity (level 2) state counter [s] |
| 18 | 1 | orient | <Anchor id="major-axis-orientation" />major_axis_orientation | coarse device orientation |
| 19 | 4 | u32 | <Anchor id="impact-cnt-x" />impact_cnt_x | X axis impact event counter |
| 20 | 4 | u32 | <Anchor id="impact-cnt-y" />impact_cnt_y | Y axis impact event counter |
| 21 | 4 | u32 | <Anchor id="impact-cnt-z" />impact_cnt_z | Z axis impact event counter |
| 22 | 4 | u32 | <Anchor id="impact-cnt" />impact_cnt | impact event counter |
| 23 | 1 | bool | <Anchor id="impact-evnt" />impact_evnt | impact event flag, cleared by [current-state](#current-state), [motion-events](#motion-events), [impact-count](#impact-count) frames |
| 24 | 4 | u32 | <Anchor id="impact-etm" />impact_etm | elapsed time since last impact event event [s] |
| 25 | 4 | u32 | <Anchor id="free-fall-cnt" />free_fall_cnt | free-fall event counter |
| 26 | 1 | bool | <Anchor id="free-fall-evnt" />free_fall_evnt | free-fall event flag, cleared by [current-state](#current-state), [motion-events](#motion-events) frames |
| 27 | 4 | u32 | <Anchor id="free-fall-etm" />free_fall_etm | elapsed time since last free-fall event [s] |
| 28 | 1 | u8 | <Anchor id="angle-1" />angle_1 | angle between current orientation and user ref-1 vector, see [data orient-cfg](#data-orient-cfg) |
| 29 | 1 | u8 | <Anchor id="angle-2" />angle_2 | angle between current orientation and user ref-2 vector, see [data orient-cfg](#data-orient-cfg) |
| 30 | 1 | u8 | <Anchor id="angle-3" />angle_3 | angle between current orientation and user ref-3 vector, see [data orient-cfg](#data-orient-cfg) |
| 31 | 1 | u8 | <Anchor id="angle-ema" />angle_ema | angle between current orientation and EMA of device orientation |
| 32 | 2 | u16 | <Anchor id="battery-mv" />battery_mv | last measured battery voltage [mV] |
| 33 | 2 | u16 | <Anchor id="battery-mv-ema" />battery_mv_ema | EMA of battery voltage [mV] |
| 34 | 2 | u16 | <Anchor id="meta-rule-id" />meta_rule_id | meta variable to send generate event with rule number |
| 35 | 4 | u32 | <Anchor id="timer-1" />timer_1 | resettable continues up counting timer [s] |
| 36 | 4 | u32 | <Anchor id="timer-2" />timer_2 | resettable continues up counting timer [s] |
| 37 | 4 | u32 | <Anchor id="timer-3" />timer_3 | resettable continues up counting timer [s] |
| 38 | 4 | u32 | <Anchor id="timer-4" />timer_4 | resettable continues up counting timer [s] |
| 39 | 4 | u32 | <Anchor id="activity-state-etm" />activity_state_etm | time since [activity_state](#activity-state) state change [s] |

### Frame Data Fields

| Size [B] | Encoding | Name | Description |
| --- | --- | --- | --- |
| 1 | u8 | <Anchor id="mag-sw-cnt-u8" />mag_sw_cnt_u8 | LSB of internal magnet switch counter [mag_sw_cnt](#mag-sw-cnt) |
| 1/8 | bool | <Anchor id="pending-evnt" />pending_evnt | indicates device has stored events |
| 0 |  | <Anchor id="event-list" />event-list | variable length list of: event time stamp, code and optional value |
| 1 | u8 | <Anchor id="temp-histo-epoch" />temp_histo_epoch | temperature histogram epoch number |
| 10 | u8[10] | <Anchor id="temp-histo-bin-10" />temp_histo_bin[10] | temperature histogram bin counter values |
| 1 | u8 | <Anchor id="humid-histo-epoch" />humid_histo_epoch | humidity histogram epoch number |
| 10 | u8[10] | <Anchor id="humid-histo-bin-10" />humid_histo_bin[10] | humidity histogram bin counter values |
| 1 | i8 | <Anchor id="orientation-x" />orientation_x | device orientation normal vector X axis |
| 1 | i8 | <Anchor id="orientation-y" />orientation_y | device orientation normal vector Y axis |
| 1 | i8 | <Anchor id="orientation-z" />orientation_z | device orientation normal vector Z axis |
| 4 | u32 | <Anchor id="mag-switch-ts" />mag_switch_ts | time stamp of last time magnetic switch state change |
| 2 | u16 | <Anchor id="impact-cnt-u16" />impact_cnt_u16 | impact event counter |
| 2 | u16 | <Anchor id="impact-cnt-x-u16" />impact_cnt_x_u16 | X axis impact event counter |
| 2 | u16 | <Anchor id="impact-cnt-y-u16" />impact_cnt_y_u16 | Y axis impact event counter |
| 2 | u16 | <Anchor id="impact-cnt-z-u16" />impact_cnt_z_u16 | Z axis impact event counter |
| 4 | u32 | <Anchor id="total-activity-s" />total_activity_s | total activity state time (level 1 + level 2) |
| 4 | u32 | <Anchor id="uptime-s" />uptime_s | device FW uptime |
| 2 | u16 | <Anchor id="version-pid" />version_pid | TG-LR82:0x0000, TG-LR92:0x0001 |
| 1 | u8 | <Anchor id="version-maj" />version_maj | FW version major number |
| 1 | u8 | <Anchor id="version-min" />version_min | FW version minor number |
| 1 | u8 | <Anchor id="version-rev" />version_rev | FW version patch number |
| 6 | u8[6] | <Anchor id="version-hash-6" />version_hash[6] | FW version hash |
| 11 | u8[11] | <Anchor id="serial-number-11" />serial_number[11] | last 11 characters of device serial number |
| 2 | u16 | <Anchor id="cfg-app-crc" />cfg_app_crc | app & mag configuration group 16 bit checksum |
| 2 | u16 | <Anchor id="cfg-net-crc" />cfg_net_crc | net configuration group 16 bit checksum |
| 2 | u16 | <Anchor id="cfg-frames-crc" />cfg_frames_crc | frame configuration group 16 bit checksum |
| 2 | u16 | <Anchor id="cfg-data-crc" />cfg_data_crc | data configuration group 16 bit checksum |
| 2 | u16 | <Anchor id="cfg-rules-crc" />cfg_rules_crc | data rule configuration 16 bit checksum |
| 1/8 | bool | <Anchor id="content-final" />content-final | flag indicating last chunk of content |
| 15/8 | u15 | <Anchor id="content-offset" />content-offset | byte offset of content data |
| 1 | u8 | <Anchor id="content-len" />content-len | length of content |
| 0 |  | <Anchor id="content-binary-blob" />content-binary-blob | binary data of content chunk |

### Known Issues

| ID | FW | Description |
| --- | --- | --- |
| [LORA-275](#lora-275) | 2.0.0 | No timeout changing credentials with secondary band disabled. |
| [LORA-276](#lora-276) | 2.0.0 | Incorrect credential change command timeout. |
| [LORA-279](#lora-279) | 2.0.0 | Activity calibration with orientation enabled causes fault. |
| [LORA-281](#lora-281) | 2.0.0 - 2.0.1 | New ADR configuration is not applied until device rejoins or restarts. |
| [LORA-282](#lora-282) | 2.0.0 - 2.0.1 | Only DR0 works as a configured fixed data rate. |

#### LORA-275

**Description:** If credential changes are initiated with secondary band disabled - device will not timeout join.
Device will be stuck attempting join until either it succeeds or is restarted.

**Workaround:** If new credentials are invalid restart device physically with [magnet switch command](#mag-sw-cmd).

#### LORA-276

**Description:** When [lora cred](#lora-cred) is executed device will timeout join procedure on next join attempt based on total
uptime instead of command execution time. If uptime is longer than *confirm-timeout-s* parameter device will timeout
exactly after single failed join attempt.

**Workaround:** Issue device reset command [app reset](#app-reset) before attempting to change credentials. Or manually retry credential
change multiple times.

#### LORA-279

**Description:** If activity calibration is performed while orientation detection is enabled device may fault and restart.

**Workaround:** Disable orientation detection with [data orient-cfg](#data-orient-cfg) before performing activity calibration and re-enable after.

#### LORA-281

**Description:** Changing the ADR setting with [lora adr-cfg](#lora-adr-cfg) while the device is joined may not take effect
until the device rejoins or restarts. Uplinks may continue using the previous ADR mode and data rate.

**Workaround:** Reset the device with [app reset](#app-reset) after changing the ADR setting.

#### LORA-282

**Description:** When network ADR is disabled, only DR0 works as a configured fixed data rate. Configuring any
other fixed data rate may not take effect.

**Workaround:** Enable network ADR with [lora adr-cfg](#lora-adr-cfg).

## Related Documents

| No | Name |
| --- | --- |
| <Anchor id="id40" />1 | TS001-1.0.4 LoRaWAN® L2 1.0.4 Specification |
| <Anchor id="id41" />2 | Guidelines for 64-bit Global Identifier (EUI-64) |

export const Anchor = ({id}) => {
  useBrokenLinks().collectAnchor(id);
  return ;
};
