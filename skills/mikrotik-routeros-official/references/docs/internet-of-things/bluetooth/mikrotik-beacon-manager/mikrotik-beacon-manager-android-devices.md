# MikroTik Beacon Manager for Android devices

> MikroTik Beacon Manager application is designed for Bluetooth tag (TG-BT5-XX) configuration. Since the tags are Bluetooth-based devices, you have to enable Bluetooth on the phone before proceeding with the configuration.

##

## Overview

MikroTik Beacon Manager application is designed for Bluetooth tag (TG-BT5-XX) configuration. Since the tags are Bluetooth-based devices, you have to enable Bluetooth on the phone before proceeding with the configuration.

For Android devices, you can find the app following the [link](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1).

![](./img/app_qr.png)

## Beacon manager screen

The first screen you see when you launch the app is the "MikroTik Beacon Manager" screen where all the nearby Bluetooth tags are shown.

![](./img/image2021-6-10_8-16-34.webp)

If the list is empty, it means that all the nearby tags are in factory-sleep mode. Once the tag is in advertising or configuration mode, it will show up on the list. To wake up the tag from the factory sleep mode, put the magnet over the tag (activate the reed-switch) for 3-10 seconds.

:::info
If the list does not capture any tags even though you are certain there is a tag in the phone's range → try turning on "Location=ON" in the phone's GPS settings.
:::
In the right upper corner of the screen there are 3 buttons:

![](./img/image2021-6-10_8-17-49.webp)

### OR Code Reader

"QR Code reader" button which allows you to add the tag via QR code (MAC address is used as tag's ID):

![](./img/image2021-7-7_13-13-39.webp)

#### NFC support

:::info
This section is available only for the TG-BT5-OUT model
:::

You can also find the tag (similar to the QR code reader feature) using NFC (MAC address is used as tag's ID).

All you need to do is to enable NFC in your phone settings and open the MikroTik Beacon Manager app.

Once you see the initial screen (list of tags), position the tag near the phone's NFC antenna and you will be provided with an option to open device settings:

![](./img/image2021-7-7_13-6-34.webp)

If you press "YES", you will be redirected to the page shown below. In the menu, you have an option to delete the device from the list or to enter configuration mode via the "Configure" button.

![](./img/image2021-7-7_13-15-48.webp)

### Order by

The "Order by" button, which allows you to change the order of the device list or just filter the list to only show MikroTik beacons by checking the "Show only MikroTik beacons" checkbox:

![](./img/image2021-7-7_14-17-41.webp)

### Settings and Batch Configuration

The "⋮" tab is divided into 2 sub-tabs - "Settings" and "Batch Configuration".

#### Settings

The first option in this tab is to set up a "Discovery refresh interval", which is the interval for scanning for the nearby tags.

![](./img/image2021-7-7_14-18-17.webp)

The second option is to enable or disable the "Save triggers" setting. When enabled, the app saves detected triggers in the database. You can check the triggers in the "Sensor Triggers" menu (the "Sensor Triggers" menu is shown in the "**Tag Management**" section of this guide). If this option is disabled, "Sensor Triggers" data is erased as soon as the app is closed.

And, lastly, the "App version" field displays the current app version/build.

#### Batch Configuration

This option allows you to mass-configure multiple tags with the same settings.

In order to do that, you will need to export the configuration file from one of the tags. Tag's configuration exporting and importing is shown in the "**Tag Configuration**" section of this guide.

After you have saved the configuration file, just press the "Batch Configuration" button and it will take you to the file menu where you need to select the file. Choose the configuration file (that you wish to apply to multiple units) and the app will show you the screen with all the nearby-detected tags:

![](./img/image2021-7-7_13-16-53.webp)

The last step is to put those tags into the configuration mode (by putting the magnet over the tag for 5-10 seconds). After the device is put into configuration mode, you will see the "Uploading configuration" message. The message will change to "Configuration updated" when the configuration is successfully applied.

![](./img/image2021-7-7_13-17-19.webp)

## Tag Management

When the tag is on the list, you can click on its MAC address and you will be presented with the following options:

![](./img/image2021-7-7_13-40-36.webp)

To "SAVE" the tag or to immediately go to the tag's configuration menu via the "CONFIG ONLY" button.

First, we will explain the "SAVE" option in more detail. The tag's configuration menu is going to be explained later on in the "**Tag Configuration**" section.

When you click on the tag that was previously saved, you will see the following menu:

![](./img/image2021-6-9_10-39-56.webp)

The first thing you should notice is the signal strength indication (RSSI signal for the tag - how far the tag is). When all circles are green, it means the signal strength is about -60 RSSI. When only 2 circles are green, it means the signal strength is about -70 RSSI. When only one circle is green, it means that the signal strength is at -80 RSSI. When no circles are green, it means that the signal strength is at -90 RSSI or more.

Under the signal strength indicator, you have 2 options - to go to the tag's configuration menu ("Configure" button) or to delete the device ("Delete" button).

In the "Name/Display Name" field, you can change the tag's name:

![](./img/image2021-7-7_13-42-16.webp)

In the "Sensors" field, you can check the tag's battery level or temperature.

:::info
TG-BT5-IN model does not have a temperature sensor
:::

In the "Sensor Triggers" field, you can check triggers that were reported by the tag:

![](./img/image2021-7-7_13-44-46.webp)

## Tag Configuration

In order to access the tag's configuration menu, you need to either press the "CONFIG ONLY" button or the "Configure" button as shown below:

![](./img/image2021-7-7_13-45-49.webp)

![](./img/image2021-7-7_13-46-7.webp)

Right after that, you will need to put a magnet over the reed-switch for 5-10 seconds:

![](./img/image2021-7-7_13-47-1.webp)

After a short wind up time, the device should be in the configuration mode:

![](./img/image2021-6-30_10-33-30.webp)

The app will show general information about the tag in the "Status" tab (as shown in the screenshot above).

Configuration can be altered in the "Settings" tab:

![](./img/image2021-6-30_10-34-13.webp)

![](./img/image2021-6-30_10-34-50.webp)

![](./img/image2021-6-30_10-35-5.webp)

### Write Protection

This menu allows you to lock the settings of the tag with a 6-symbol long password:

![](./img/image-2023-9-8_12-2-12.webp)

Once the password is set, there is no way to remove password protection (you can only edit it).

The next time you try to configure the tag, you will be notified that it is "write protected" and you can choose either to stay in the "READ-ONLY" mode (which allows you to browse/read through the settings and restricts making configuration changes) or to "UNLOCK" the settings by inputting the configured password:

![](./img/image-2023-9-8_12-1-51.webp)

### Beacon settings

In advertising mode, the tag broadcasts information about itself in Bluetooth advertising packets. Information depends on the advertising packet type (the type can be changed in the settings).

At the moment, these are all the supported types:

DeviceName, MikroTik, [Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1), [Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) and [iBeacon](https://developer.apple.com/ibeacon/).

![](./img/image-2023-9-8_12-16-54.webp)

![](./img/image-2023-9-8_12-17-4.webp)

![](./img/image-2023-9-8_12-17-16.webp)

![](./img/image-2023-9-8_12-17-23.webp)

| Property | Description |
| --- | --- |
| **Advertisement interval** (20ms...24h or disable) | The interval in milliseconds after which an advertisement packet will be broadcasted by the tag. When you have only advertisement interval configured without any triggers enabled → advertisement packets are broadcasted based on the interval time set (each **x** seconds). |
| **Freefall detect** (on/off) | Whether to send an advertisement packet when the tag detects a freefall trigger. When the freefall trigger is enabled and the freefalling state is detected → the packet is sent. |
| **Tilt detect** (on/off) | Whether to send an advertisement when the tag detects a tilt trigger. When the tilt trigger is enabled and the device is tilted → the advertisement packet is broadcasted immediately. |
| **Impact detec**t (on/off) | Whether to send an advertisement when the tag detects an impact/wake up trigger. When the impact trigger is enabled and the device is pushed/moved → the advertisement packet is sent. |
| **Encrypt** (on/off) - only available for MikroTik format  | Whether to encrypt the broadcasted hex payload with an "AES" key. When the "Encrypt" parameter is enabled, the hex payload data (acceleration, temperature, uptime, trigger action, and battery percentage) is encrypted with a private key. This key is known only to the tag's owner (it is obtained with the purchase). |
| **Namespace** - only available for Eddystone-UID format  | Set up a unique 10-byte long beacon Namespace ID. |
| **Instance** - only available for Eddystone-UID format  | Set up a unique 6-byte long beacon Instance ID. |
| **UUID** - only available for iBeacon format  | Set up a universally unique identifier (UUID) in the following format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| **Major** - only available for iBeacon format  | Set up a 16-bit integer secondary identifier, in the hex format or a decimal number (from 0 to 65 535). |
| **Minor** - only available for iBeacon format  | Set up a 16-bit integer secondary identifier, in the hex format or a decimal number (from 0 to 65 535). |

### Advertisment properties

| Property | Description |
| --- | --- |
| **Connectable advertisements** (on/off) | Enables connectable advertisements. |
| **Channel 37** (on/off) | To enable advertising on the specific channel. |
| **Channel 38**(on/off) | To enable advertising on the specific channel. |
| **Channel 39** (on/off) | To enable advertising on the specific channel. |

### Estimated battery life

This section displays the estimated battery life:

![](./img/image2021-7-7_13-52-0.webp)

Estimated battery life is heavily dependant on the number of advertising packets sent (configured to be sent). The app calculates how many packets are estimated to be broadcasted daily, for how long the tag will be active, and the estimate for the average daily power consumption.

### Accelerometer settings

Accelerometer can be toggled (turned) off completey and can be turned on by using  "Use Accelerometer" toggle button.

This section allows you to change the parameters shown in the screenshot below:

![](./img/image2021-6-30_11-47-16.webp)

#### Mode and Data Rate

![](./img/image2021-7-7_13-53-8.webp)

This menu allows you to choose between 2 modes: "Low power" and "High power". In "Low power" mode, you will get lower precision but also lower power consumption. In "High power" mode, you will get higher precision but also higher power consumption.

"Data Rate" setting represents the number of acceleration measurements during a 1-second window (measurement frequency). The fewer packets per second are sent → the lower the power consumption is.

#### Full Scale

![](./img/image-2022-11-14_11-57-58.webp)

Can vary between (2g...16g). It is the measurement range that is used to calculate the wake-up threshold. Full scale defines the range of acceleration, that the accelerometer is capable of measuring (the bigger the range, the lower the accuracy of the measured acceleration).

#### Bandwith Filter

![](./img/image2021-7-7_13-53-53.webp)

Is a digital filtering cutoff (a high pass filter bandwidth).

If the bandwidth = "x" Hz, then the tag will filter out changes to acceleration that happen less frequently than "x" times a second.

For example, if the device is laying on the table, the acceleration will show 0g (instead of 1g), even though the earth's gravity is present → (because the earth's gravity is constant - its frequency of change is 0 Hz, which is &lt; "x" Hz) it gets filtered out.

#### Wakeup Threshold and Duration

![](./img/image2021-7-7_13-54-18.webp)

The "Wakeup Threshold" defines a wakeup zone/acceleration range. The "Wakeup Duration" defines the time during which the acceleration is over the configured wakeup threshold. A wakeup event will be generated (a wakeup condition will be triggered) when the acceleration on any axis (X, Y, or Z) exceeds a threshold for the configured wakeup duration. To better understand what is meant by "acceleration on any axis (X, Y, or Z)", imagine a 3-D Cartesian coordinate system and in the origin point (common point) the tag's accelerometer or the tag itself:

![](./img/intagaxis.png) ![](./img/outtagaxis.png)

For example, the wakeup threshold is set to 1.0g (it means that any acceleration between -1.0g to +1.0g falls under the configured threshold/acceleration range) and the wakeup duration is set to 0.12s. As a result, as soon as the device is pushed/thrown against any of the axis (the device begins moving in any direction) with the acceleration exceeding the configured threshold (acceleration> +1.0g or acceleration&lt; -1.0g) for longer than 0.12s → wakeup condition is triggered.

#### Free Fall Threshold and Duration

![](./img/image2021-7-7_13-54-38.webp)

The "Free Fall Threshold" defines a free-fall zone/acceleration range. The "Free Fall Duration" defines the time during which the acceleration is going to be within the configured free-fall threshold. The free-fall event will be generated (free-falling condition will be triggered) when the acceleration on all 3 axes (X, Y, and Z) is within the free-fall zone/threshold for the configured free-fall duration. To better understand what is meant by "acceleration on all axis (X, Y, and Z)", check the device photoes above in the "Wakeup Threshold and Duration" section.

For example, the freefall threshold is set to 156.25g (it means that any acceleration between -156.25g to +156.25g falls under the configured threshold/acceleration range) and the freefall duration is set to 0.2s. As a result, as soon as the device is in a freefalling state with acceleration on all axis within the configured threshold (-156.25g&lt;acceleration&lt;+156.25g) for longer than 0.2s → a freefalling condition is triggered.

#### Angle Threshold

![](./img/image2021-7-7_13-55-18.webp)

Can vary between 50°...80°. It is the threshold for a tilt function. When the threshold is set to, for example, 60° and the device is tilted by that degree - the tilt action is triggered and the advertisement packet is sent.

#### Low noise filter

![](./img/image2021-7-7_13-57-32.webp)

An option to enable or disable a low noise filter. A low noise filter is used to reduce noise density in the measurements. Enabling this feature will slightly increase power consumption.

#### Temperature Offset

:::info
TG-BT5-IN model does not have a temperature sensor!
:::

![](./img/image2021-7-7_13-57-5.webp)

Can vary between -10°C...+10°C. Offset in centicelsius to apply to raw temperature measurements.

#### Tx Power

![](./img/image2021-7-7_13-58-19.webp)

The transmit power level in decibel-milliwatts. Can vary between -28dBm...6dBm. Tx Power is simply used to increase/decrease transmit power of the tag.

### Data logs

:::info
This section is available only for the TG-BT5-OUT model.
:::

This section allows you to configure/view logs (that are only accessible using the app):

![](./img/image2021-7-7_14-0-8.webp)

#### Configure logging

In the "Configure logging" menu, you can set up logging settings:

![](./img/image2021-7-7_14-9-24.webp)

You have an option to set up "Periodic logging interval (s)" (or you can disable it). When enabled, the data logs will automatically get saved every "x" seconds:

![](./img/image2021-7-7_14-5-45.webp)

Another option is to enable "Log Triggers" (periodic logging and trigger logging can be used together). When log triggers are used - logs will be saved whenever the tilt, free fall, and/or impact action is detected.

For example, when a tilt trigger is enabled and is detected by the tag - the message is logged.

You can set up which parameters are going to be logged in the "Field config" section:

![](./img/image2021-6-9_15-5-2.webp)

![](./img/image2021-6-9_15-5-25.webp)

![](./img/image2021-6-9_15-5-53.webp)

You have an option to log 3 parameters: 1) Battery level; 2) Temperature; 3) Acceleration.

You can disable each parameter if you are not interested in it and you can also set up the thresholds for them.

If you are not interested in logging battery level unless it is less than 40%, you can set up a threshold from minimum=0% to maximum=40%, and, as a result, the battery level (battery level percentage) is going to be displayed in the log only when it is in-between the configured range. The same principle applies to the other 2 parameters.

#### Data Logs

The logged messages will be displayed in the "Data Logs" tab:

![](./img/image2021-7-7_14-10-30.webp)

You can export the log as a .csv file via "Export as .csv" button:

![](./img/image2021-7-7_14-10-58.webp)

### System

In the "System" tab you synchronize the time, view the system log, put the tag into a factory sleep mode, and upgrade the firmware:

![](./img/image2021-6-30_14-24-6.webp)

#### Unix Time

Using this setting, you can synchronize the current time and date for the tag:

![](./img/image2021-7-7_14-13-23.webp)

#### Logs

Menu, where you can view system log:

![](./img/image2021-7-7_14-14-10.webp)

#### Factory sleep

This option can initiate factory sleep mode for the tag:

![](./img/image2021-7-7_14-14-52.webp)

#### Upgrade Firmware

This menu allows you to upgrade the tag's firmware version:

![](./img/image2021-7-7_14-15-20.webp)

##### Automatic upgrade

Click "Download and install" and wait for the device to reboot.

##### Manual upgrade

In order to manually download the tag's firmware file, navigate to https://download.mikrotik.com/firmware/bt-tag/latest. It will allow you to download the "latest" file which can be opened in a notepad or any other text editor. The content of the file will indicate the latest available TG-BT5-XX versions:

```
2.3.1 1638358509
1326c554c18340a41e79fd88abbea193dc53b99931eddecd018e33cff577f6d3 bt-tag_HT_app_2.3.1-0rr.gbl
9dc21eb980e8bd36732ec4db8e4b03a8177885fccdbbd87122f7d9bf76410b8b bt-tag_HT_apploader_3.2.3-0rr.gbl
9e4f30d9006f24063ac96d0fb1181d135929d86d0e243d3b3985cc5e43d6b448 bt-tag_IN_app_2.3.1-0rr.gbl
e03fa2987b874463e9a5c686303f4d75fef0c0f8d89dde14f8c4b04be4838a93 bt-tag_IN_apploader_3.2.3-0rr.gbl
54e959dd9cc1da3a5408b5dc7c797c52ae1a1685122e14d966cbe433ec1d1b3c bt-tag_OUT_app_2.3.1-0rr.gbl
e0bc2e8a1a9de6a1974c201a48cfea2276465414e07efc07816400abca91aa14 bt-tag_OUT_apploader_3.2.3-0rr.gbl
5257a1b06cb8d57d06ae10ef2c87abf0df0a3ab8a9ac7f9229a9a421b8a0c0fc bt-tag_HT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_HT_apploader_3.2.3-000.gbl
0f6603d97df5fc4b3f260b410628b3c62fb2562f26e85e44b6cdfdf1b58d04f8 bt-tag_IN_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_IN_apploader_3.2.3-000.gbl
3235db7bb9a9cca0d5e59ae774c3cd004be4e58b44c1ae40e6e3bb84feb077a6 bt-tag_OUT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_OUT_apploader_3.2.3-000.gbl
```

Double-check current tag's firwmare version using the app:

![](./img/image2022-1-31_14-6-50.webp)

Knowing, that the tag, for example, is the **TG-BT5-IN** model and that the current version is **1.6.1-000**, we can conclude that the latest release is "bt-tag_IN_app_2.3.1-000.gbl".

Please note, that for the majority of the tags, the firmware version will be 1.6.1-**0rr** (instead of 1.6.1-**000**). You will need to use the x.x.x-**0rr** file instead.

To download the actual firmware file, change the "latest" part of the link to "bt-tag_IN_app_2.3.1-000.gbl".

So, in case your current version is, for example, "1.6.1-000" (TG-BT5-IN tag), the firmware can be downloaded using the link:

https://download.mikrotik.com/firmware/bt-tag/bt-tag_IN_app_2.3.1-000.gbl

In case your current version is, for example, "1.6.1-0rr" (TG-BT5-OUT tag), the firmware can be downloaded using the link:

https://download.mikrotik.com/firmware/bt-tag/bt-tag_OUT_app_2.3.1-0rr.gbl

##### Upgrade settings

:::warning
**If you have issues with the tag's update, where the tag stays in the OTA/update mode → try enabling "Reliable write"!**

When the tag is "stuck" in the OTA/upgrade mode, there are two scenarios that can happen:
a) The Beacon Manager tag list will still show the tag on the list but there will be no indication that the tag is "configurable". You are still able to click on the tag in the list (even without the "gear" icon present) and surf its settings without activating the magnetic switch;

b) The tag might disappear from the list of manageable tags. In that case, try to manually add the tag using QR code reader function and approve the "configuration".
:::

To enter the additional upgrade setting menu, click on the "Upgrade settings" button:

![](./img/image-2023-8-9_13-9-47.webp)

This will allow you to alter the "Reliable write" configuration:

![](./img/image-2023-8-9_13-11-7.webp)

When enabled, the checkbox allows you to make the Bluetooth upgrade process "slower" but more "reliable" (where additional exchange and verification steps take place between the phone and the tag).

### Import/Export

In the right upper corner of the screen, you have an option to import/export current settings:

![](./img/image2021-7-7_14-15-43.webp)

If you press the export button, the app will open the phone's file menu, where you can name the configuration file and save it.

If you press the import button, the app will open the phone's file menu, where you can select the configuration file and apply it.
