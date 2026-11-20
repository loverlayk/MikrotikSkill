# TG-LR82 / TG-LR92 User Manual

> User manual for MikroTik TG-LR82 and TG-LR92 LoRaWAN sensor tags, covering FW 2.0.1 activation, network join, telemetry and sensor configuration, data rules, magnet switch commands, command encoding for downlinks,...

# TG-LR82 / TG-LR92 User Manual

<Anchor id="tg-lr" />

## Quickstart Guide

- Register device on LoRaWAN network server. Use [`tg-lrx2-2.0-ul-dec.js`](pathname:///assets/tg-lrx2-2.0-ul-dec.js) payload decoder script if device model not supported.

- Activate the device: new devices start in [SHUTDOWN](#shutdown). Hold the magnet near the
switch for about 1.5 s to enter digit 2, then remove it. The device confirms
the command with short LED blinks and restarts in [RUN](#run) mode.

- Wait for network join. Default profile 0 sends [current-state](#current-state) and
[device-orientation](#device-orientation) every 5 minutes. The first uplink after join can also
contain [version](#version), [serial-number](#serial-number), [cfg-state](#cfg-state), and [dev-health](#dev-health) frames.

- Decode the first uplink to verify temperature, humidity, orientation, battery,
and device identity data. Use downlink commands as the primary method for
configuration and management; see [Device Commands](#device-commands) and [Command Encoding](#command-encoding).
Magnet switch commands remain available for activation and local operations
such as profile or region selection; see [Magnet Switch](#magnet-switch).

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

:::note

For safety warnings, hardware specifications, installation, and
regulatory information, see the [TG-LR82 hardware page](https://manual.mikrotik.com/hardware/tg-lr82) and [TG-LR92 hardware page](https://manual.mikrotik.com/hardware/tg-lr92).

:::

<Anchor id="id43" />

**Bands**

| Numeric code | Name | Description |
| --- | --- | --- |
| 1 | <Anchor id="band-1ghz" />BAND_1GHz | Sub-GHz operating band. Frequency range is based on device [Model](#model). |
| 2 | <Anchor id="band-2ghz" />BAND_2GHz | 2.4GHz ISM band. Supported by both models; uses the LoRaWAN ISM2400 region automatically when active. |

<Anchor id="id44" />

**Operating modes**

| Numeric code | Mode | Description |
| --- | --- | --- |
| 0 | <Anchor id="shutdown" />SHUTDOWN | Device in low power mode. Network and data services are stopped, but all magnet switch commands remain available. Settings can be changed in this mode and the device activated afterwards. |
| 1 | <Anchor id="run" />RUN | Device joins network and sends uplinks based on current profile and configuration. |

<Anchor id="id45" />

**<Anchor id="supported-regions" />Supported regions**

| [X-Y](#x-y) Code | [downlink](#lora-set-region) | Common Name | [TG-LR82](#tg-lr82) | [TG-LR92](#tg-lr92) |
| --- | --- | --- | --- | --- |
| 1-1 | 1 | <Anchor id="eu868" />EU868 | Yes |  |
| 2-1 | 2 | <Anchor id="as923-grp1" />AS923_GRP1 |  | Yes |
| 3-1 | 3 | <Anchor id="us915" />US915 |  | Yes |
| 4-1 | 4 | <Anchor id="au915" />AU915 |  | Yes |
|  |  | <Anchor id="ism2400" />ISM2400 | Yes | Yes |
| 6-1 | 7 | <Anchor id="as923-grp2" />AS923_GRP2 |  | Yes |
| 7-1 | 8 | <Anchor id="as923-grp3" />AS923_GRP3 |  | Yes |
| 8-1 | 9 | <Anchor id="in865" />IN865 | Yes |  |
| 9-1 | 10 | <Anchor id="kr920" />KR920 |  | Yes |

The *X-Y* code is the magnet switch sequence. The numeric *downlink* value is
used by [lora set-region](#lora-set-region).

*ISM2400* is the LoRaWAN 2.4 GHz region. It is supported by both models and is
used automatically whenever [BAND_2GHz](#band-2ghz) is active. [BAND_2GHz](#band-2ghz) can be the
primary or secondary band ([lora primary-band](#lora-primary-band), [lora second-band](#lora-second-band)).

[lora set-region](#lora-set-region) configures only the sub-GHz region. It cannot select
*ISM2400*, and *ISM2400* is not available while only [BAND_1GHz](#band-1ghz) is active.
There is currently no independent *ISM2400* region selection or runtime region
switch; change the active band to use it.

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

Link check lets the end device verify that the network is still reachable. Most uplinks can be non-confirmed,
so they do not prove that the network received them. Use periodic link check or confirmed uplinks when the
device must detect a lost network.

Link check can be configured specifically for each band using [lora link-chk](#lora-link-chk). If link check fails, the
device leaves the network and restarts the join procedure. A failed confirmed uplink has the same effect.

:::note

Any network downlink will restart link check timer to prevent unnecessary LinkCheckReq.

:::

#### Time Synchronization

Time synchronization gives stored events absolute timestamps instead of device uptime. Events and telemetry
can be stored locally and sent later, so absolute time lets the application know when an event actually
occurred. This is useful when the device is outside network coverage and reports the collected data after
it returns to coverage.

Device supports optional time synchronization using DeviceTimeReq MAC command. See command [lora clk-sync](#lora-clk-sync)
for configuration parameters or to request immediate synchronization.

#### Class B

Device supports Class B operation. Class B operation can be either manually requested using
[lora class](#lora-class) or device can be configured to automatically switch to class B on network join using
[lora cfg-class-b](#lora-cfg-class-b).

#### ADR Configuration

It is possible to disable network ADR and set fixed data rate using [lora adr-cfg](#lora-adr-cfg).

:::warning

In FW 2.0.1, ADR changes made while the device is joined may not
take effect until the device rejoins or restarts ([LORA-281](#lora-281)). With network
ADR disabled, only DR0 works as a fixed data rate ([LORA-282](#lora-282)). Reset the
device after changing ADR; when network ADR is disabled, use DR0.

:::

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
See [LORA-275](#lora-275), [LORA-276](#lora-276) for known issues!

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
verification join attempt! You may lose access to device!

:::

### Uplink Messages

Each LoRaWAN uplink can carry one or more pending [Data Frames](#data-frames). Frames are added in ascending
frame-ID order. The first frame-type delta is encoded in the FPort field; additional type deltas
are encoded at the start of FRMPayload, followed by the frame contents. The FPort value therefore
depends on the first frame type and is not a fixed application port.

The device packs only frames that fit in the current payload. Frames that do not fit remain
pending for the next uplink. If any packed frame is configured as confirmed, the whole uplink is
sent as confirmed. A failed confirmed uplink causes the device to leave the network and restart
the join procedure.

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
| 1 | Activity Monitor | Send [activity](#activity), [full-activity](#full-activity), [current-state](#current-state) every 60 min and generate [activity_state](#activity-state) events on LOW and IDLE state changes. |
| 2 | Magnet Switch | Send [mag-switch](#mag-switch), [current-state](#current-state), [device-events](#device-events) every 60 minutes and generate a [mag_sw_cnt](#mag-sw-cnt) event when the magnet has been removed for at least 20 seconds. Save up to 10 events. |
| 3 | Orientation | Send [current-state](#current-state), [device-events](#device-events), [device-orientation](#device-orientation) every 60 minutes. Generate a [device-orientation](#device-orientation) frame when the rotation angle exceeds 30 degrees. Generate [angle_1](#angle-1) and [meta_rule_id](#meta-rule-id) events when the device is close to reference vector V=(0,1,1). Save up to 3 events. |
| 4 | Asset Monitor | Send [dev-health](#dev-health), [device-orientation](#device-orientation), histograms, [ema-temp](#ema-temp), [ema-humid](#ema-humid), [motion-events](#motion-events), [impact-count](#impact-count), and *device-events* every 3 hours. Additional frames and events are generated by the factory rules for orientation, impact, free fall, temperature, humidity, and magnet removal. Save up to 10 events. |
| 5 | Empty |  |

See [`default-cfg.txt`](pathname:///assets/tg-lrx2-default-cfg.txt) for exact factory default configuration commands.

##### Factory Defaults and Custom Configuration

The device ships with a complete factory configuration. When creating a custom
configuration, send only the commands needed to change the factory values.
Settings that are not changed keep their factory values. Reusing factory
settings reduces both the number and size of downlink messages.

Factory profiles 1-4 also contain example rules. If a custom use case does not
need those rules, remove all rules at once before adding the new ones:

```none
data del-rule
```

[data del-rule](#data-del-rule) without a rule number removes every rule, including the
factory rules. Rule numbers can then be used for the new configuration without
mixing it with the factory examples.

To return to a known test state, restore the factory configuration:

```none
app factory-reset 984651411,,2500
```

This returns the device to the exact factory state, including the factory rules,
and resets the join nonces. The device must join the network again, and custom
credentials or settings that were written after production are lost. Use this
command when you need a repeatable baseline before experimenting with new
configurations.

#### Configuring Sensors

##### Sampling Intervals

Periodic temperature, humidity and battery voltage sampling can be configured for specific use cases using [data poll-cfg](#data-poll-cfg) command.
Device can sample data at a higher rate than uplink frames are sent. This gives opportunity to send average values or to perform
rule based decisions. Since sampling interval influences device power consumption this can be leveraged to improve lifetime.

##### Frame-Triggered Sensor Refresh

[data poll-cfg](#data-poll-cfg) includes the *on-ul-stale* option. It is enabled by default in
the factory configuration. Its intended use is to keep sensor data reasonably
fresh and aligned with uplink timing when the normal polling interval is longer
than the frame interval. In that configuration, frame scheduling acts as an
additional sensor-polling trigger.

When *on-ul-stale* is enabled, scheduling [current-state](#current-state),
[device-orientation](#device-orientation), [last-temp](#last-temp), [ema-temp](#ema-temp), [last-humid](#last-humid), [ema-humid](#ema-humid),
or [dev-health](#dev-health) causes the device to check the age of the temperature/humidity,
battery, and orientation samples. Any sensor group older than the stale timeout
is flagged for a forced sample.
The request is handled asynchronously by the data service and does not block
frame scheduling. The check covers all three groups regardless of which fields
the scheduled frame contains. For example, scheduling [current-state](#current-state) can also
refresh battery and orientation data, and scheduling [dev-health](#dev-health) can refresh
temperature, humidity, and orientation.

The current stale timeout is 15 seconds. It is a fixed firmware value and is not
configurable through [data poll-cfg](#data-poll-cfg). The device uses a strict “older than”
comparison, so a sample that is exactly 15 seconds old is not refreshed. A
forced sample does not shift the normal periodic sampling schedule. If frames
are scheduled less than 15 seconds apart, not every frame triggers a new sample.

Frame scheduling as a polling trigger can be configured without changing the
normal periodic intervals:

```none
data poll-cfg 32,3600,0,0,0,0,0,1,21600
frame set-cfg 32,300,0,0,current-state
```

In this example temperature/humidity have a one-hour periodic interval and
battery has a six-hour interval, while [current-state](#current-state) is scheduled every five
minutes. Each scheduled frame refreshes any of the three sensor groups that is
older than 15 seconds. Because all groups are checked, a frequent [current-state](#current-state)
frame can also keep battery and orientation sampling active; include this in the
power budget.

Set *on-ul-stale* to 0 to disable frame-triggered refresh. Frames then use the
most recent samples even when they are old.

:::warning

*on-ul-stale* is checked when the frame is scheduled, not when it
is transmitted. If the uplink is delayed by the duty-cycle limit, the frame
can be transmitted with sensor data older than the stale timeout. The check
is not repeated while the frame is pending.

:::

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

:::note

The 1.3 s LOW-to-IDLE timing applies to single-level mode. In dual
mode the accelerometer and state machine use different timing; use the 5 s
transitions in the [Dual Mode](#dual-mode) table only for dual mode.

:::

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

1. Place device in environment with periodic motion/activity to calibrate.

2. Send commands:

   ```none
   data activity-cfg 1,1,,,1
   data activity-cal 1,1,1
   ```

3. Observe LED periodic blink 2x/1.5s for ~ 15s.

4. Test motion detection. During LOW activity device will blink LED 3x/1s.

5. If calibration results are acceptable send command to disable LED:

   ```none
   data activity-cfg 1,,,,0
   ```

Example to calibrate profile #0 with dual level activity monitor:

1. Place device in environment with periodic motion/activity for level 1 calibration.

2. Send commands:

   ```none
   data activity-cfg 1,2,,,1
   data activity-cal 1,1,1
   ```

3. Observe LED periodic blink 2x/1.5s for ~ 15s.

4. Place device in environment for level 2 calibration.

5. Send commands to calibrate level 2:

   ```none
   data activity-cal 1,2,1
   ```

6. Observe LED periodic blink 2x/1.5s for ~ 15s.

7. Test motion detection. During HIGH activity device will blink LED 6x/1s.

8. If calibration results are acceptable send command to disable LED:

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

Up to 32 user rules can be stored using [data set-rule](#data-set-rule) and [data del-rule](#data-del-rule).
A rule contains a test expression, optional input expressions, and optional actions.
If &lt;rule-num&gt; is omitted, the first free rule slot is used. [data del-rule](#data-del-rule)
without a rule number deletes all rules; with a rule number it deletes one rule.
Rule configuration persists across reboots; rule evaluation state is reset on
reboot.

:::note

When building a different use case, [data del-rule](#data-del-rule) without a rule
number removes all factory example rules at once. See [Factory Defaults and
Custom Configuration](#factory-defaults-and-custom-configuration).

:::

Command syntax to add or override rules:

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>], [<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

##### Rule Model

The test expression is evaluated against one value from [User Variables](#user-variables) and
produces the rule <Anchor id="local-state" />local state. The local state combined with optional input
rules produces the rule <Anchor id="combined-state" />combined state.

An action is executed only when [combined state](#combined-state) changes from false to true.
While it remains true, actions are not repeated. When it changes back to false,
no action is executed.

Rules are evaluated in dependency order. Rules without inputs are evaluated first,
then rules whose input rules have already been evaluated. Rule numbers identify
rules and input references; they do not define evaluation order. A rule that
depends on itself directly or through other rules is not evaluated.

##### Test Expression

`<test-expr>: [^] <variable-type> <operator> <argument>`

| Element | Description |
| --- | --- |
| [^] | use the absolute value of the variable in the expression |
| [variable-type](#variable-type) | variable name or numeric ID from [User Variables](#user-variables) |
| &lt;operator&gt; | &gt;, &gt;=, &lt;, &lt;=, ==, !=, % |
| &lt;argument&gt; | numeric value |

The *%* operator is true when the integer part of
`abs(variable) % abs(argument)` is zero. &lt;argument&gt; must not be zero.

Fractional arguments are supported and use fixed-point encoding. Prefer integer
arguments where possible because fractional values increase rule encoding size.
Use *==* and *!=* only for exact-value variables; for measured analog values,
prefer threshold comparisons.

Time values such as [mag_sw_etm](#mag-sw-etm), [impact_etm](#impact-etm), [timer_1](#timer-1), [profile_etm](#profile-etm),
and [activity_state_etm](#activity-state-etm) are in seconds. [daytime_tm](#daytime-tm) and [unix_time](#unix-time) are
only useful after [Time Synchronization](#time-synchronization).

Example:

```none
data set-rule 0,profile == 0
data set-rule 1,^temperature > 30.55
data set-rule 2,impact_etm < 60
```

Use variable names in rule commands. The *tg-lrx2-encode* utility converts
variable and frame names to numeric IDs and encodes the commands into the
compact binary downlink format.

##### Input Expression

Input expression is used if a rule needs to depend on the result of other rules.
This allows constructing logic based on multiple test expressions.

`<input-expr>: [&][|][!]<input-rule>[<]...`

| Term | Description |
| --- | --- |
| [&] | AND input with the current combined value |
| [\|] | OR input with the current combined value |
| [!] | invert the input value |
| &lt;input-rule&gt; | rule number whose state is used |
| [&lt;] | use the input rule [combined state](#combined-state), otherwise its [local state](#local-state). |

The first input term is combined with the rule local state. Each additional term
is applied to the result. There are no parentheses and no operator precedence.

:::warning

Terms are applied in ascending input-rule number order, regardless
of the order written in the command. This is easy to miss when composing
expressions.

:::

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

Rule 3 combines its own result with rules 0, 1, and 2 using OR. Rule 4 combines
its own result with the combined state of rule 3 using AND. The action of rule 4
therefore runs when the magnet switch changed recently and any temperature or
humidity threshold is true.

:::warning

Rule numbers are not evaluation order. Rules are evaluated in
dependency order. Avoid circular dependencies: rules in a cycle are not
evaluated. Input rules must be enabled; disabled input rules are not part of
the evaluation order.

:::

##### Actions

If [combined state](#combined-state) changes to true, actions are executed once for that
transition. Actions execute in this order: generate events, schedule frames, reset
user timers. The optional profile switch is applied after all rules in the current
evaluation pass. Rules in the same pass therefore still see the previous profile;
the new profile is used from the next evaluation pass.

If &lt;switch-profile&gt; parameter is given, the active profile is changed. The value
range is 0..5. This does not make the profile the default; use [app profile](#app-profile)
with *make-default* or a magnet profile command to persist it. For example if
temperature drops below 15 C device will switch to profile 5 ([Device Profiles](#device-profiles)):

```none
data set-rule 1,temperature < 15,,5
```

Up to 4 different [Data Frames](#data-frames) can be scheduled per rule. Scheduled frames
are sent as soon as the network stack has air time; they do not wait for the
configured periodic uplink interval:

```none
data set-rule 0,impact_cnt % 10,,,,,,,current-state,device-orientation,dev-health,ema-temp
```

:::note

Rule chaining can be used if more than 4 frames should be sent.

:::

Up to 4 different events can be generated per rule. Events are captured when the
action executes and are described in [Events](#events):

```none
data set-rule 0,impact_cnt % 10,,,temperature_ema,humidity_ema,activity_state,timer_1
```

The optional &lt;clr-timer-mask&gt; resets user timers when the action executes. See
[Timers and Rule ID Events](#timers-and-rule-id-events).

##### Events

[Actions](#actions) can optionally generate events. Events are stored in device memory and
sent in the [device-events](#device-events) frame. Event storage is configured per profile using
[data event-cfg](#data-event-cfg):

| Option | Description |
| --- | --- |
| max-count | Maximum stored events (0 disables event storage, range 1..100). |
| send-th | Schedule [device-events](#device-events) when the pending count is at least this value. 0 schedules a frame after every new event. |
| discard | Select oldest or newest event when storage is full. |
| send-all | After a [device-events](#device-events) frame is sent, schedule another frame while events remain. |

Events are sent when the [device-events](#device-events) frame is scheduled periodically using
[frame set-cfg](#frame-set-cfg), immediately using [frame send](#frame-send), by a rule send-frame
action, or automatically by the send-th threshold. Use [data erase-events](#data-erase-events) to
erase all events or a selected number of oldest events.

Each event record in the [device-events](#device-events) frame contains:

- a length byte; bit 7 set means more records follow;

- a 4-byte timestamp;

- a 1-byte event code;

- an optional value.

The timestamp is UNIX time after [Time Synchronization](#time-synchronization), otherwise device uptime.
Event codes 0..99 are user-variable events and carry the variable value. Event
codes 100..229 are reserved for rule events; [meta_rule_id](#meta-rule-id) uses code
*100 + rule-number* and carries no value. The supplied payload decoder
interprets these records.

Example commands:

```none
data event-cfg 1,50,10,0,1
data erase-events
data erase-events 10
```

The first command configures profile 0 to store at most 50 events, schedule
[device-events](#device-events) when at least 10 events are pending, discard the oldest event
when full, and keep sending while events remain. The second command erases all
events; the third erases the 10 oldest events.

##### Timers and Rule ID Events

[timer_1](#timer-1), [timer_2](#timer-2), [timer_3](#timer-3), and [timer_4](#timer-4) are free-running user timers.
They count seconds from the last reset and are reset on device reboot.

[data timer](#data-timer) sets the elapsed value of selected timers. Omitted parameters are
left unchanged:

```none
data timer 0
data timer ,0
data timer ,,,0
```

The first command resets [timer_1](#timer-1), the second resets [timer_2](#timer-2), and the third
resets [timer_4](#timer-4).

The &lt;clr-timer-mask&gt; action parameter is a 4-bit mask: bit 0 resets [timer_1](#timer-1),
bit 1 resets [timer_2](#timer-2), bit 2 resets [timer_3](#timer-3), and bit 3 resets [timer_4](#timer-4).

[meta_rule_id](#meta-rule-id) is a special event-action value. It cannot be used as a normal
test variable. When an action generates an event for [meta_rule_id](#meta-rule-id), the event
code is *100 + rule-number* and the event has no value. The decoder reports this
event as *data_rule*. This identifies which rule fired when several rules send
the same frame. For example:

```none
data set-rule 0,temperature > 30,,,temperature,meta_rule_id,,,current-state
data set-rule 1,humidity > 90,,,humidity,meta_rule_id,,,current-state
```

When either rule fires, [current-state](#current-state) is scheduled and the event identifies
the rule that triggered it.

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

#### Downlink Ports

| Port | Purpose |
| --- | --- |
| 2 | Binary command message. After the commands are processed, the device schedules a [cfg-state](#cfg-state) uplink with the current configuration checksums. |
| 3 | Binary command message. |

*tg-lrx2-encode* places all encoded messages on the command port except the last
message, which is placed on the configuration port to trigger the [cfg-state](#cfg-state)
response. Send all generated messages in file order. If *–max-len* splits a
script into several messages, the order is required.

Example configuration to set [current-state](#current-state) and [activity](#activity) frame uplink every 600 seconds and
[mag-switch](#mag-switch) every 43200 seconds as confirmed message:

```none
# lora-script.txt
frame set-cfg 1,601,0,0,current-state,activity
frame set-cfg 1,43200,1,0,mag-switch
```

We can use *tg-lrx2-encode* to convert text commands to binary messages for downlink:

```none
tg-lrx2-encode --script ./lora-script.txt --max-len=50 --out ./lora-pub.yml
```

:::note

*tg-lrx2-utils* includes a device descriptor and uses it by default.
Pass *–dev-desc* only when you need to override it, for example to use the
[`2.0 descriptor`](pathname:///assets/tg-lrx2-2.0-desc.yml) supplied with
this manual. Make sure the descriptor matches the device and FW version.

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

:::warning

*ttn-app.yml* contains an access key. Keep it out of source control
and do not publish it.

:::

*tg-lrx2-encode* accepts command strings on CLI as well. This can be used for single or few lines of commands:

```none
tg-lrx2-encode --cmd $'frame send device-orientation\napp profile 1,0' --max-len=50 --out ./lora-pub.yml
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

Each parameter has a valid input range and format. Some parameters allow only a specific choice between
values or a choice between ranges.

Most parameters accept integer values. *%f* indicates that parameter accepts fractional value. Use of these values
results in larger downlink payload so if possible integer values should be preferred. [variable-type](#variable-type) indicates
that parameter accepts either user variable name or respective integer ID. [frame-type](#frame-type) indicates that parameter
accepts either data frame name or integer ID. *tg-lrx2-encode* automatically converts these names to numeric ID.

The reference includes advanced manual commands such as [data sample](#data-sample) and
[data next-epoch](#data-next-epoch). See [Advanced Operations](#advanced-operations).

[frame set-cfg](#frame-set-cfg) accepts multiple frame IDs after the shared period, confirmed,
and on-join settings. If several frames use the same settings, list them in one
command instead of repeating the command:

```none
frame set-cfg 32,900,0,0,current-state,dev-health
```

The profile mask in the first parameter can also select multiple profiles. Only
the listed frames and profiles are changed; other configuration remains as it
was.

#### app set-mode

Set device operating mode

**Syntax**

```none
app set-mode <mode>
```

| Parameter | Range | Description |
| --- | --- | --- |
| mode | 0 | [SHUTDOWN](#shutdown) |
|  | 1 | [RUN](#run) |

#### app profile

Switch active profile and optionally make default

**Syntax**

```none
app profile <profile-num>,<make-default>
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-num | 0..5 |  |
| make-default | 0 | no |
|  | 1 | yes |

#### app reset

System reset

**Syntax**

```none
app reset <type>
```

| Parameter | Range | Description |
| --- | --- | --- |
| type | 0 | board |
|  | 1 | app only |

#### app factory-reset

Reboot device, clear saved configuration and set to defaults (optional)

**Syntax**

```none
app factory-reset <key>,[<fw-def>],<delay-ms>
```

| Parameter | Range | Description |
| --- | --- | --- |
| key | 984651411 |  |
| fw-def | 784565141 | don’t apply default configuration |
| delay-ms | 0..65535 |  |

#### app led

Configure application LED signals

**Syntax**

```none
app led [<enable>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| enable | 0 | no |
|  | 1 | yes |

#### app set-time

Set UNIX time relative to device uptime

**Syntax**

```none
app set-time [<unix-time-s>],<uptime-s>
```

| Parameter | Range | Description |
| --- | --- | --- |
| unix-time-s | 0..4294967295 |  |
| uptime-s | 0..4294967295 |  |

#### lora set-region

Set LoRaWAN region for sub GHz band

**Syntax**

```none
lora set-region <region-code>
```

| Parameter | Range | Description |
| --- | --- | --- |
| region-code | 1 | EU868 |
|  | 2 | AS923-1 |
|  | 3 | US915 |
|  | 4 | AU915 |
|  | 7 | AS923-2 |
|  | 8 | AS923-3 |
|  | 9 | IN865 |
|  | 10 | KR920 |

#### lora primary-band

Select primary band

**Syntax**

```none
lora primary-band <band>
```

| Parameter | Range | Description |
| --- | --- | --- |
| band | 1 | &lt;1GHz |
|  | 2 | 2.45GHz |

#### lora second-band

Enable or disable secondary band

**Syntax**

```none
lora second-band <mode>
```

| Parameter | Range | Description |
| --- | --- | --- |
| mode | 0 | off |
|  | 1 | on |

#### lora join-cfg

Configure join duty cycle for band

**Syntax**

```none
lora join-cfg <band>,<duty>
```

| Parameter | Range | Description |
| --- | --- | --- |
| band | 1 | &lt;1GHz |
|  | 2 | 2.45GHz |
| duty | 0 | 0.1% |
|  | 1..254 |  |
|  | 255 | 1% |

#### lora link-chk

Set band specific link check interval and timeout

**Syntax**

```none
lora link-chk <band>,<int-minutes>
```

| Parameter | Range | Description |
| --- | --- | --- |
| band | 1 | &lt;1GHz |
|  | 2 | 2.45GHz |
| int-minutes | 0 | off |
|  | 5..500000 |  |

#### lora adr-cfg

Enable network ADR or configure fixed data rate

**Syntax**

```none
lora adr-cfg <en-netw-adr>,[<fixed-data-rate>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| en-netw-adr | 0 | off |
|  | 1 | on |
| fixed-data-rate | 0..6 |  |

#### lora clk-sync

Absolute time synchronization

**Syntax**

```none
lora clk-sync [<int-minutes>],[<leap-sec>],<sync-now>,[<retry-s>],[<retry-cnt>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| int-minutes | 0 | off |
|  | 1..65535 |  |
| leap-sec | -128..127 |  |
| sync-now | 0 | no |
|  | 1 | yes |
| retry-s | 0..255 |  |
| retry-cnt | 0..255 |  |

#### lora cfg-class-b

Configure LoRaWAN Class B

**Syntax**

```none
lora cfg-class-b [<auto-en>],[<ping-slot-int-s>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| auto-en | 0 | off |
|  | 1 | on |
| ping-slot-int-s | 1 |  |
|  | 2 |  |
|  | 4 |  |
|  | 8 |  |
|  | 16 |  |
|  | 32 |  |
|  | 64 |  |
|  | 128 |  |

#### lora class

Switch LoRaWAN class

**Syntax**

```none
lora class <class>
```

| Parameter | Range | Description |
| --- | --- | --- |
| class | 0 | A |
|  | 1 | B |

#### lora join-eui

Override network JoinEUI

**Syntax**

```none
lora join-eui <cred-ch-key>,<eui-0>,<eui-1>,<eui-2>,<eui-3>,<eui-4>,<eui-5>,<eui-6>,<eui-7>
```

| Parameter | Range | Description |
| --- | --- | --- |
| cred-ch-key | 87904163 |  |
| eui-0 | 0..255 |  |
| eui-1 | 0..255 |  |
| eui-2 | 0..255 |  |
| eui-3 | 0..255 |  |
| eui-4 | 0..255 |  |
| eui-5 | 0..255 |  |
| eui-6 | 0..255 |  |
| eui-7 | 0..255 |  |

#### lora net-key

Override network AppKey

**Syntax**

```none
lora net-key <cred-ch-key>,<key-0>,<key-1>,<key-2>,<key-3>,<key-4>,<key-5>,<key-6>,<key-7>,<key-8>,<key-9>,<key-10>,<key-11>,<key-12>,<key-13>,<key-14>,<key-15>
```

| Parameter | Range | Description |
| --- | --- | --- |
| cred-ch-key | 87904163 |  |
| key-0 | 0..255 |  |
| key-1 | 0..255 |  |
| key-2 | 0..255 |  |
| key-3 | 0..255 |  |
| key-4 | 0..255 |  |
| key-5 | 0..255 |  |
| key-6 | 0..255 |  |
| key-7 | 0..255 |  |
| key-8 | 0..255 |  |
| key-9 | 0..255 |  |
| key-10 | 0..255 |  |
| key-11 | 0..255 |  |
| key-12 | 0..255 |  |
| key-13 | 0..255 |  |
| key-14 | 0..255 |  |
| key-15 | 0..255 |  |

#### lora cred

User network credential management

**Syntax**

```none
lora cred [<confirm-timeout-s>],[<action>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| confirm-timeout-s | 60..65535 | revert if not joined |
| action | 0 | clear pending |
|  | 1 | try now |
|  | 87904163 | force confirm |

#### frame send

Schedule uplink frames

**Syntax**

```none
frame send <frame-id>,...
```

| Parameter | Range | Description |
| --- | --- | --- |
| frame-id | [frame-type](#frame-type) |  |

#### frame set-cfg

Set uplink frame configuration

**Syntax**

```none
frame set-cfg <profile-mask>,[],[<confirmed>],[<on-join>],<frame-id>,...
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| ul-period-s | 0 | off |
|  | 1..65535 |  |
| confirmed | 0 | no |
|  | 1 | yes |
| on-join | 0 | no |
|  | 1 | yes |
| frame-id | [frame-type](#frame-type) |  |

#### frame clear-cfg

Clear all frame config for specified profiles (as if ‘set-cfg profile-mask,0,0,0,…’)

**Syntax**

```none
frame clear-cfg <profile-mask>
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |

#### mag cfg

Set configuration

**Syntax**

```none
mag cfg [<pin-timeout>],[<pin-protect>],[<blink-mode>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| pin-timeout | 0..65535 |  |
| pin-protect | 0 | off |
|  | 1 | on |
| blink-mode | 0 | half duty |
|  | 1 | pulse |
|  | 2 | off |

#### mag svc

Enable or disable magnet command interface

**Syntax**

```none
mag svc <new-state>,<key>
```

| Parameter | Range | Description |
| --- | --- | --- |
| new-state | 0 | off |
|  | 1 | on |
| key | 649864801 |  |

#### data sample

Force sensor polling

**Syntax**

```none
data sample
```

#### data next-epoch

Manually start next histogram epoch

**Syntax**

```none
data next-epoch <type>
```

| Parameter | Range | Description |
| --- | --- | --- |
| type | all |  |
|  | temp |  |
|  | humid |  |

#### data poll-cfg

Set data polling configuration

**Syntax**

```none
data poll-cfg <profile-mask>,[],[<sync-period>],[<on-mag-switch>],[<on-activity-change>],[<on-impact>],[<on-free-fall>],[<on-ul-stale>],[<bat-poll-int>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| th-poll-int | 1..4294967295 | temperature and humidity |
| sync-period | 0 | no |
|  | 1 | yes |
| on-mag-switch | 0 | no |
|  | 1 | yes |
| on-activity-change | 0 | no |
|  | 1 | yes |
| on-impact | 0 | no |
|  | 1 | yes |
| on-free-fall | 0 | no |
|  | 1 | yes |
| on-ul-stale | 0 | no |
|  | 1 | yes |
| bat-poll-int | 1..4294967295 | battery voltage |

#### data temp-histo-cfg

Set temperature histogram configuration

**Syntax**

```none
data temp-histo-cfg <profile-mask>,[<epoch-interval-s>],[<epoch-interval-cnt>],[<epoch-max-bin-cnt>],[<frame-on-new-epoch>],[<lim-divider>],[<bin-limit-0>],[<bin-limit-1>],[<bin-limit-2>],[<bin-limit-3>],[<bin-limit-4>],[<bin-limit-5>],[<bin-limit-6>],[<bin-limit-7>],[<bin-limit-8>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| epoch-interval-s | 0 | off |
|  | 1..4294967295 |  |
| epoch-interval-cnt | 0 | off |
|  | 1..4294967295 |  |
| epoch-max-bin-cnt | 0 | off |
|  | 1..4294967295 |  |
| frame-on-new-epoch | 0 | no |
|  | 1 | yes |
| lim-divider | 1..4294967295 |  |
| bin-limit-0 | -128..127 | °C |
|  | %f |  |
| bin-limit-1 | -128..127 | °C |
|  | %f |  |
| bin-limit-2 | -128..127 | °C |
|  | %f |  |
| bin-limit-3 | -128..127 | °C |
|  | %f |  |
| bin-limit-4 | -128..127 | °C |
|  | %f |  |
| bin-limit-5 | -128..127 | °C |
|  | %f |  |
| bin-limit-6 | -128..127 | °C |
|  | %f |  |
| bin-limit-7 | -128..127 | °C |
|  | %f |  |
| bin-limit-8 | -128..127 | °C |
|  | %f |  |

#### data humid-histo-cfg

Set humidity histogram configuration

**Syntax**

```none
data humid-histo-cfg <profile-mask>,[<epoch-interval-s>],[<epoch-interval-cnt>],[<epoch-max-bin-cnt>],[<frame-on-new-epoch>],[<lim-divider>],[<bin-limit-0>],[<bin-limit-1>],[<bin-limit-2>],[<bin-limit-3>],[<bin-limit-4>],[<bin-limit-5>],[<bin-limit-6>],[<bin-limit-7>],[<bin-limit-8>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| epoch-interval-s | 0 | off |
|  | 1..4294967295 |  |
| epoch-interval-cnt | 0 | off |
|  | 1..4294967295 |  |
| epoch-max-bin-cnt | 0 | off |
|  | 1..4294967295 |  |
| frame-on-new-epoch | 0 | no |
|  | 1 | yes |
| lim-divider | 1..4294967295 |  |
| bin-limit-0 | 0..99 | RH% |
|  | %f |  |
| bin-limit-1 | 0..99 | RH% |
|  | %f |  |
| bin-limit-2 | 0..99 | RH% |
|  | %f |  |
| bin-limit-3 | 0..99 | RH% |
|  | %f |  |
| bin-limit-4 | 0..99 | RH% |
|  | %f |  |
| bin-limit-5 | 0..99 | RH% |
|  | %f |  |
| bin-limit-6 | 0..99 | RH% |
|  | %f |  |
| bin-limit-7 | 0..99 | RH% |
|  | %f |  |
| bin-limit-8 | 0..99 | RH% |
|  | %f |  |

#### data ema-cfg

Set exponential moving average (EMA) configuration

**Syntax**

```none
data ema-cfg <profile-mask>,[<temp-cnt>],[<humid-cnt>],[<bat-cnt>],[<orient-cnt>],[<send-ema-temp>],[<send-ema-humid>],[<send-ema-bat>],[<send-ema-orient>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| temp-cnt | 1..32766 | a = 2 / (temp-cnt + 1) |
| humid-cnt | 1..32766 | a = 2 / (humid-cnt + 1) |
| bat-cnt | 1..32766 | a = 2 / (bat-cnt + 1) |
| orient-cnt | 1..32766 | a = 2 / (orient-cnt + 1) |
| send-ema-temp | 0 | no |
|  | 1 | yes |
| send-ema-humid | 0 | no |
|  | 1 | yes |
| send-ema-bat | 0 | no |
|  | 1 | yes |
| send-ema-orient | 0 | no |
|  | 1 | yes |

#### data activity-cfg

Set activity monitor configuration

**Syntax**

```none
data activity-cfg <profile-mask>,[<mode>],[<level1-th>],[<level2-th>],[<en-led>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| mode | 0 | off |
|  | 1 | single |
|  | 2 | dual |
| level1-th | 1..63 |  |
| level2-th | 1..63 |  |
| en-led | 0 | off |
|  | 1 | on |

#### data acc-cfg

Set accelerometer configuration

**Syntax**

```none
data acc-cfg <profile-mask>,[<full-scale>],[<en-impact-x>],[<en-impact-y>],[<en-impact-z>],[<impact-th>],[<impact-dur>],[<en-ff>],[<ff-th>],[<ff-dur>],[<data-rate>],[<filter>],[<lp-mode>],[<low-noise>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| full-scale | 0 | 2G |
|  | 1 | 4G |
|  | 2 | 8G |
|  | 3 | 16G |
| en-impact-x | 0 | off |
|  | 1 | on |
| en-impact-y | 0 | off |
|  | 1 | on |
| en-impact-z | 0 | off |
|  | 1 | on |
| impact-th | 1..63 | impact-th * full-scale / 64 |
| impact-dur | 0..3 |  |
| en-ff | 0 | off |
|  | 1 | on |
| ff-th | 0..7 |  |
| ff-dur | 0..63 |  |
| data-rate | 2 | Hz |
|  | 13 |  |
|  | 25 |  |
|  | 50 |  |
|  | 100 |  |
|  | 200 |  |
| filter | 2 | cutoff = data-rate/filter |
|  | 4 |  |
|  | 10 |  |
|  | 20 |  |
| lp-mode | 0..3 |  |
| low-noise | 0 | no |
|  | 1 | yes |

#### data orient-cfg

Set orientation sense configuration

**Syntax**

```none
data orient-cfg <profile-mask>,[<enable>],[<max-1G-offset>],[<poll-interval-s>],[<ref-1-x>],[<ref-1-y>],[<ref-1-z>],[<ref-2-x>],[<ref-2-y>],[<ref-2-z>],[<ref-3-x>],[<ref-3-y>],[<ref-3-z>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| enable | 0 | off |
|  | 1 | on |
| max-1G-offset | 1..20 |  |
| poll-interval-s | 1..4294967295 |  |
| ref-1-x | -32768..32767 |  |
| ref-1-y | -32768..32767 |  |
| ref-1-z | -32768..32767 |  |
| ref-2-x | -32768..32767 |  |
| ref-2-y | -32768..32767 |  |
| ref-2-z | -32768..32767 |  |
| ref-3-x | -32768..32767 |  |
| ref-3-y | -32768..32767 |  |
| ref-3-z | -32768..32767 |  |

#### data event-cfg

Set event storage configuration

**Syntax**

```none
data event-cfg <profile-mask>,[<max-count>],[<send-th>],[<discard>],[<send-all>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| max-count | 0 | disabled |
|  | 1..100 |  |
| send-th | 0..65535 | if count &gt;= send-th: send(device-events); 0 sends on every event |
| discard | 0 | oldest (if no free space) |
|  | 1 | newest |
| send-all | 0 | off (send remaining events after device-events frame) |
|  | 1 | on |

#### data erase-events

Erase &lt;num-oldest&gt; events if provided, otherwise all

**Syntax**

```none
data erase-events [<num-oldest>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| num-oldest | 0..65535 |  |

#### data del-rule

Delete &lt;rule-num&gt; rules if provided, otherwise delete all

**Syntax**

```none
data del-rule [<rule-num>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| rule-num | 0..31 |  |

#### data set-rule

Set data rule &lt;rule-num&gt;

**Syntax**

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>],[<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| rule-num | 0..31 |  |
| test-expr | test expression |  |
| input-expr | input expression |  |
| switch-profile | 0..5 |  |
| make-event-0 | [variable-type](#variable-type) |  |
| make-event-1 | [variable-type](#variable-type) |  |
| make-event-2 | [variable-type](#variable-type) |  |
| make-event-3 | [variable-type](#variable-type) |  |
| send-frame-0 | [frame-type](#frame-type) |  |
| send-frame-1 | [frame-type](#frame-type) |  |
| send-frame-2 | [frame-type](#frame-type) |  |
| send-frame-3 | [frame-type](#frame-type) |  |
| clr-timer-mask | 0..15 | bit0=timer_1 bit1=timer_2 bit2=timer_3 bit3=timer_4 |

#### data timer

Set user timer value

**Syntax**

```none
data timer [<timer_1>],[<timer_2>],[<timer_3>],[<timer_4>]
```

| Parameter | Range | Description |
| --- | --- | --- |
| timer_1 | 0..4294967295 | [timer_1](#timer-1) |
| timer_2 | 0..4294967295 | [timer_2](#timer-2) |
| timer_3 | 0..4294967295 | [timer_3](#timer-3) |
| timer_4 | 0..4294967295 | [timer_4](#timer-4) |

#### data activity-cal

Run activity monitor calibration and apply result to profiles

**Syntax**

```none
data activity-cal <profile-mask>,<cal-level>,<cal-led>
```

| Parameter | Range | Description |
| --- | --- | --- |
| profile-mask | 1..63 | bitfield |
| cal-level | 1 | level-one |
|  | 2 | level-two |
| cal-led | 0 | no |
|  | 1 | yes |

### Data Frames

Frames are packed into LoRaWAN uplinks as described in [Uplink Messages](#uplink-messages).
Configuration export frames 25-30 are described in [Advanced Operations](#advanced-operations).

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
| 24 | 4 | u32 | <Anchor id="impact-etm" />impact_etm | elapsed time since last impact event [s] |
| 25 | 4 | u32 | <Anchor id="free-fall-cnt" />free_fall_cnt | free-fall event counter |
| 26 | 1 | bool | <Anchor id="free-fall-evnt" />free_fall_evnt | free-fall event flag, cleared by [current-state](#current-state), [motion-events](#motion-events) frames |
| 27 | 4 | u32 | <Anchor id="free-fall-etm" />free_fall_etm | elapsed time since last free-fall event [s] |
| 28 | 1 | u8 | <Anchor id="angle-1" />angle_1 | angle between current orientation and user ref-1 vector, see [data orient-cfg](#data-orient-cfg) |
| 29 | 1 | u8 | <Anchor id="angle-2" />angle_2 | angle between current orientation and user ref-2 vector, see [data orient-cfg](#data-orient-cfg) |
| 30 | 1 | u8 | <Anchor id="angle-3" />angle_3 | angle between current orientation and user ref-3 vector, see [data orient-cfg](#data-orient-cfg) |
| 31 | 1 | u8 | <Anchor id="angle-ema" />angle_ema | angle between current orientation and EMA of device orientation |
| 32 | 2 | u16 | <Anchor id="battery-mv" />battery_mv | last measured battery voltage [mV] |
| 33 | 2 | u16 | <Anchor id="battery-mv-ema" />battery_mv_ema | EMA of battery voltage [mV] |
| 34 | 2 | u16 | <Anchor id="meta-rule-id" />meta_rule_id | special event action value: emits rule number as event code 100 + rule ID |
| 35 | 4 | u32 | <Anchor id="timer-1" />timer_1 | user timer elapsed time [s], reset by rule action or data timer |
| 36 | 4 | u32 | <Anchor id="timer-2" />timer_2 | user timer elapsed time [s], reset by rule action or data timer |
| 37 | 4 | u32 | <Anchor id="timer-3" />timer_3 | user timer elapsed time [s], reset by rule action or data timer |
| 38 | 4 | u32 | <Anchor id="timer-4" />timer_4 | user timer elapsed time [s], reset by rule action or data timer |
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

### Example Configurations

The examples below are downlink configuration scripts and assume the device is
joined. Most examples use profile 5, which is empty by default, so existing
profile settings remain unchanged. The day/night example also uses the factory
default profile 0 and leaves profile 0 unchanged.

#### Temperature and Humidity Reporting

Configure profile 5 to report temperature and humidity every 15 minutes and
battery voltage every 6 hours:

```none
data poll-cfg 32,900,0,0,0,0,0,0,21600
frame set-cfg 32,900,0,0,current-state
frame set-cfg 32,21600,0,0,dev-health
app profile 5,1
```

The [current-state](#current-state) frame carries temperature, humidity, and the remaining
device state fields. Battery voltage is sent in the [dev-health](#dev-health) frame. Profile
5 is empty by default, so orientation and activity monitoring are not needed.

<Anchor id="door-window-switch" />

#### Door/Window Switch

Use profile 5. The device sends [current-state](#current-state) every 6 hours and reports
immediately when the magnet switch changes state:

```none
mag cfg 600,1,1
frame set-cfg 32,21600,0,0,current-state
data del-rule
data set-rule 0,mag_sw_etm < 2,,,,,,,current-state,mag-switch
app profile 5,1
```

*mag cfg 600,1,1* enables PIN protection for normal magnet commands with a
600-second PIN-mode timeout and selects pulse LED blink mode. Magnet switch
events continue to work normally; the PIN is supplied with the device.

The rule uses the elapsed time since the last magnet switch change, so either
opening or closing triggers [current-state](#current-state) and [mag-switch](#mag-switch). The latter
contains the full counter and last-change timestamp. Bit 0 of [mag_sw_cnt_u8](#mag-sw-cnt-u8)
is the current switch state.

#### Threshold Alarm With Cooldown

Use profile 5. Rule 0 is a five-minute cooldown gate. Rule 1 sends an alarm and
resets the gate when temperature exceeds 30 C. The event contains both the
temperature value and the rule ID:

```none
data poll-cfg 32,30
data event-cfg 32,20,0,0,1
data timer 300
data del-rule
data set-rule 0,timer_1 >= 300
data set-rule 1,temperature > 30,&0,,temperature,meta_rule_id,,,current-state,,,,1
app profile 5,1
```

The timer is preset so the first alarm can trigger immediately. After each
alarm, [timer_1](#timer-1) is reset and the gate closes for five minutes. The expected uplink
is [current-state](#current-state) plus a [device-events](#device-events) frame containing the temperature and
*data_rule* 1.

#### Impact and Free Fall Profile Switch

Use profile 5 and configure impact and free-fall detection for it. The
*app profile 5,1* command at the end activates profile 5 and makes it the
default:

```none
data acc-cfg 32,0,1,1,1,8,0,1,7,0,13,2,0,1
data del-rule
data set-rule 0,impact_etm < 20,,,meta_rule_id,,,,impact-count
data set-rule 1,free_fall_etm < 15,,,meta_rule_id,,,,motion-events
app profile 5,1
```

The expected uplink is [impact-count](#impact-count) or [motion-events](#motion-events) plus a
[device-events](#device-events) frame that identifies rule 0 or 1.

:::warning

Impact and free-fall detection cannot be used while [Activity
Monitor](#activity-monitor) is enabled.

:::

#### Orientation Change Event

Use the last profile, profile 5, and orientation EMA; no reference vectors are
needed. A change of at least 20 degrees relative to the orientation EMA
generates an event:

```none
data orient-cfg 32,1,2,3
data ema-cfg 32,6,6,6,20
data del-rule
data set-rule 0,angle_ema >= 20,,,angle_ema,meta_rule_id,,,device-orientation
app profile 5,1
```

The expected uplink is [device-orientation](#device-orientation) plus a [device-events](#device-events) frame with
the measured [angle_ema](#angle-ema) and *data_rule* 1. *orient-cnt* 20 sets the EMA time
constant to approximately 30 seconds at the 3-second orientation polling
interval. The example makes profile 5 the default.

#### Magnet-Only Setup

Use case: prepare a TG-LR device for a door/window installation without any
downlinks. The device starts in [SHUTDOWN](#shutdown), so the settings are applied first
and the device is activated last.

<Anchor id="id52" />

**Magnet-only setup for profile 2**

| Step | Sequence | Action |
| --- | --- | --- |
| 1 | `4-3-9` | Disable the secondary band (2.4 GHz). The device will use the 1 GHz band only. |
| 2 | `4-1-3` | Switch to profile 2 (Magnet Switch) and make it the default. |
| 3 | `2` | Activate the device and start it in [RUN](#run) mode. The device restarts and joins the network. |

After the device joins, it uses profile 2 by default and sends
[current-state](#current-state), [mag-switch](#mag-switch), and [device-events](#device-events) every 60 minutes. A
[mag_sw_cnt](#mag-sw-cnt) event is generated when the magnet has been removed for at least
20 seconds. The secondary band remains disabled and profile 2 remains the
default after reboot.

#### Confirmed Event Journal

Use profile 5 to store temperature, humidity, and battery voltage as events. The
event frame is sent as a confirmed message in batches:

```none
data poll-cfg 32,60,0,0,0,0,0,1,120
data event-cfg 32,100,101,0,1
data del-rule
data set-rule 0,timer_1 >= 60,,,temperature,humidity,,,,,,,1
data set-rule 1,timer_2 >= 120,,,battery_mv,,,,,,,,2
data timer 0,0
frame set-cfg 32,360,1,1,device-events
app profile 5,1
```

Temperature and humidity are sampled and stored every 60 seconds. Battery
voltage is sampled and stored every 120 seconds. The first rule uses [timer_1](#timer-1)
and resets it; the second rule uses [timer_2](#timer-2) and resets it. *data timer 0,0*
clears both timers, so the first temperature/humidity event is generated after
60 seconds and the first battery event after 120 seconds.

[data event-cfg](#data-event-cfg) stores up to 100 events. The send threshold is set to 101,
which is above the maximum stored event count, so automatic event flushing is
effectively disabled. Events are sent when the [device-events](#device-events) frame is
scheduled by [frame set-cfg](#frame-set-cfg) every six minutes or on network join. *send-all*
drains the remaining events after a frame. The [device-events](#device-events) frame is
confirmed, so pending events are sent after a normal leave/rejoin recovery.
Event timestamps become absolute after the default time synchronization
completes.

:::note

Event storage is a finite buffer, not a permanent archive. A long
outage can fill the 100-record buffer and discard the oldest events.

:::

<Anchor id="day-night-profiles" />

#### Day/Night Profiles

Use the factory default profile 0 for daytime telemetry and profile 5 for
sparse nighttime telemetry:

```none
frame set-cfg 32,3600,0,0,current-state,dev-health
data del-rule
data set-rule 0,daytime_tm >= 28800,,0
data set-rule 1,daytime_tm >= 64800,,5
data set-rule 2,daytime_tm < 28800,,5
```

Profile 0 is not reconfigured and keeps its factory polling and frame settings.
Profile 5 sends [current-state](#current-state) and [dev-health](#dev-health) every hour. Profile selection
is what changes the daytime and nighttime uplink rate.

The third rule handles the midnight boundary. At 00:00, rules 0 and 1 become
false and rule 2 becomes true, so profile 5 is selected even when this
configuration is applied at midnight. At 08:00, rule 0 switches back to profile
0; at 18:00, rule 1 selects profile 5 again.

*data del-rule* removes all user and factory rules, which is required so the
existing profile rules do not override this schedule. Profile 0 frame
configuration remains at its factory defaults. Profile 5 is not made the
default; profile switching is performed only by these rules. [daytime_tm](#daytime-tm) is
seconds since midnight GMT, and this example does not distinguish weekdays.
Time synchronization is already enabled in the default configuration.

#### Vehicle Activity Tracking

Use profile 5 to report movement start and stop events for a car or other
vehicle, together with the accumulated activity time. The [activity](#activity) and
[device-events](#device-events) frames are confirmed; [dev-health](#dev-health) is a periodic unconfirmed
uplink.

```none
data del-rule
data activity-cfg 32,1,4,63,1
frame set-cfg 32,0,1,0,activity,device-events
frame set-cfg 32,3600,0,0,dev-health
data set-rule 0,timer_1 >= 60
data set-rule 1,activity_state_etm >= 60
data set-rule 2,activity_state == 0,,,,,,,,,,,1
data set-rule 3,activity_state == 0, &1,,activity_state,,,,activity
data set-rule 4,activity_state != 0, &0,,activity_state,,,,activity
data timer 500
app profile 5,1
```

The final *1* in *data activity-cfg* enables the activity indication LED. After
testing is complete, disable the LED with:

```none
data activity-cfg 32,,,,0
```

Rule 2 resets [timer_1](#timer-1) when the activity state becomes idle. Rule 0 then
requires [timer_1](#timer-1) to be at least 60 seconds, so rule 4 generates a start event
only when movement resumes after at least 60 seconds of idle. Rule 1 requires the
idle state to have lasted 60 seconds, after which rule 3 generates the stop
event. This suppresses start/stop flapping for short state changes.

*data timer 500* presets [timer_1](#timer-1) so a tag that starts in motion can generate
an initial start event immediately. If it starts idle, rule 2 clears the timer
and the first stop event is generated after 60 seconds of idle.

Both transitions schedule the [activity](#activity) frame, which contains the accumulated
[total_activity_s](#total-activity-s). The event carries [activity_state](#activity-state), which identifies
whether the transition is a start or a stop. [dev-health](#dev-health) reports battery
voltage every hour.

### Known Issues

Issue IDs are internal support references. The description and workaround are
the user-facing contract.

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

### Advanced Operations

The operations below are public but not required for normal end-device operation.

#### Manual Sampling

[data sample](#data-sample) forces one temperature, humidity, battery, and orientation
sampling cycle. Forced samples update the last measured values and event flags,
but do not update EMA or histogram counters except for the first sample. Use it
for diagnostics or to refresh data before a manual read.

#### Manual Histogram Epoch

[data next-epoch](#data-next-epoch) immediately starts a new temperature and humidity histogram
epoch. Use *data next-epoch temp* or *data next-epoch humid* to reset only one
histogram. The next histogram frame reports the new epoch number.

#### Configuration Export Frames

Frames [full-cfg](#full-cfg), [app-cfg](#app-cfg), [net-cfg](#net-cfg), [frame-cfg](#frame-cfg), [data-cfg](#data-cfg), and
[rules-cfg](#rules-cfg) carry fragmented configuration data. They are intended for
configuration backup and verification tooling, not for normal telemetry. The
[cfg-state](#cfg-state) frame is the normal automatic checksum response after a
configuration downlink.

#### Optional Evaluation Stack

[`telemetry_hub.zip`](pathname:///assets/telemetry_hub.zip) contains optional
Grafana and Influx docker services for device capability evaluation. It is not
required for device operation. Follow the instructions included in the archive.

export const Anchor = ({id}) => {
  useBrokenLinks().collectAnchor(id);
  return ;
};
