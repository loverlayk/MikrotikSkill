# MikroTik Beacon Manager for iOS devices

> MikroTik Beacon Manager application is designed for Bluetooth tag (TG-BT5-XX) configuration. Since the tags are Bluetooth-based devices, you have to enable Bluetooth on the phone before proceeding with the configuration.

##

## Overview

MikroTik Beacon Manager application is designed for Bluetooth tag (TG-BT5-XX) configuration. Since the tags are Bluetooth-based devices, you have to enable Bluetooth on the phone before proceeding with the configuration.

For iOS devices, you can find the app following the [link](https://apps.apple.com/id/app/mikrotik-beacon-manager/id1561796698).

![](./img/app_qr_ios.png)

## My devices

The first screen you see when you launch the app is the "My devices" screen where all the nearby Bluetooth tags are shown.

![](./img/image2021-11-29_14-3-16.webp)

If the list is empty, it means that all the nearby tags are in factory-sleep mode. Once the tag is in advertising or configuration mode, it will show up on the list. To wake up the tag from the factory sleep mode, put the magnet over the tag (activate the reed-switch) for 3-10 seconds.

At the bottom of the screen, there are 2 options - to stay on the "My devices" tab or to alter the app's settings under the "Settings" tab.

## Settings

If you choose to alter the application's "Settings", you will see the following screen:

![](./img/image2021-11-29_14-12-45.webp)

The "Settings" tab is divided into "Discovery", Miscellaneous" and "About" sections.

In the "Discovery" section, you can enable the "MirkoTik packets only" checkbox, which will make sure that only MikroTik devices are displayed on the "My device" list. When disabled, all Bluetooth devices will show up on the "My device" list.

In the "Miscellaneous" section, it is possible to change the language of the app (English, Russian, Latvian and Portuguese) and the appearance (System, Dark, and Light).

The "About" section just shows the version of the app.

## Tag Management

When the tag is on the list, you can click on it and you will enter the tag's individual overview page:

![](./img/image2021-11-29_15-6-9.webp)

![](./img/image2021-11-29_15-6-25.webp)

The first thing you should notice is the signal strength indication (RSSI signal for the tag - how far the tag is). When all circles are filled/completed, it means the signal strength is about -60 RSSI. When only 2 circles are filled, it means the signal strength is about -70 RSSI. When only one circle is filled, it means that the signal strength is at -80 RSSI. When no circles are filled, it means that the signal strength is at -90 RSSI or more.

Under the signal strength indication, you can check the tag's battery level, temperature, and acceleration.

:::info
TG-BT5-IN model does not have a temperature sensor!
:::

In the "Sensor Triggers" field, you can check triggers that were reported by the tag (whether the device was tilted, thrown, or fell):

![](./img/image2021-11-29_15-16-10.webp)

In the "Display Name" field, you can change the tag's name.

In the "Device icon" field, you can assign an icon to the tag.

If you select the "Remove device" button →  you can unpair the device and remove it from the device list.

## Tag Configuration

In order to access the tag's configuration menu, you need to put the tag into the "Configuration mode":

![](./img/image2021-11-29_15-23-12.webp)

To enter device configuration, hold a magnet over the reed switch until its LED stops blinking.

After successfully entering the configuration mode, the "settings/gear" icon (in the upper right corner) will turn orange and you should see a message "Configuration mode enabled" in the bottom part of the screen, as shown in the screenshot below:

![](./img/image2021-11-29_15-24-28.webp)

Click on the orange "settings/gear" icon in the right upper corner of the screen and you will enter the tag's configuration page:

![](./img/image2021-11-29_15-33-20.webp)

This page is going to ask you to sync the time and date for the tag.

![](./img/image2021-11-29_15-37-31.webp)

The app will show general information about the tag under the "Device status" tab (as shown in the screenshot above).

:::info
TG-BT5-IN model does not have a temperature sensor!
:::

Settings can be altered in the "Configuration" tab:

![](./img/image2022-2-2_9-16-40.webp)

![](./img/image2022-2-2_9-16-57.webp)

### "Accelerometer" settings

This section allows you to alter "Power mode", "Measurements", "Wakeup Threshold and Duration", "Free Fall Threshold and Duration", "Angle Threshold", and "Low noise filter" settings.

#### Power Mode

![](./img/image2021-11-29_15-56-11.webp)

This menu allows you to choose between 2 modes: "Low power" and "High power". In "Low power" mode, you will get lower precision but also lower power consumption. In "High power" mode, you will get higher precision but also higher power consumption.

The "scale factor" is a measurement range (the lower the scale factor, the better the accuracy is, but, keep in mind, that larger acceleration peaks cannot be measured).

#### Measurements

![](./img/image2021-11-30_9-31-0.webp)

"Data Rate" setting represents the number of acceleration measurements during a 1-second window (measurement frequency). The fewer packets per second are sent → the lower the power consumption is.

"Bandwith filter" is a digital filtering cutoff (a high pass filter bandwidth).

If the bandwidth = "x" Hz, then the tag will filter out changes to acceleration that happen less frequently than "x" times a second.

For example, if the device is laying on the table, the acceleration will show 0g (instead of 1g), even though the earth's gravity is present → (because the earth's gravity is constant - its frequency of change is 0 Hz, which is &lt; "x" Hz) it gets filtered out.

#### Wakeup Threshold and Duration

![](./img/image2022-2-2_9-33-8.webp)

The "Wakeup Threshold" defines a wakeup zone/acceleration range. The "Wakeup Duration" defines the time during which the acceleration is over the configured wakeup threshold. A wakeup event will be generated (a wakeup condition will be triggered) when the acceleration on any axis (X, Y, or Z) exceeds a threshold for the configured wakeup duration. To better understand what is meant by "acceleration on any axis (X, Y, or Z)", imagine a 3-D Cartesian coordinate system and in the origin point (common point) the tag's accelerometer or the tag itself:

![](./img/intagaxis.png) ![](./img/outtagaxis.png)

For example, the wakeup threshold is set to 1.0g (it means that any acceleration between -1.0g to +1.0g falls under the configured threshold/acceleration range) and the wakeup duration is set to 0.12s. As a result, as soon as the device is pushed/thrown against any of the axis (the device begins moving in any direction) with the acceleration exceeding the configured threshold (acceleration> +1.0g or acceleration&lt; -1.0g) for longer than 0.12s → wakeup condition is triggered.

#### Free Fall Threshold and Duration

![](./img/image2022-2-2_9-39-14.webp)

The "Free Fall Threshold" defines a free-fall zone/acceleration range. The "Free Fall Duration" defines the time during which the acceleration is going to be within the configured free-fall threshold. The free-fall event will be generated (free-falling condition will be triggered) when the acceleration on all 3 axes (X, Y, and Z) is within the free-fall zone/threshold for the configured free-fall duration. To better understand what is meant by "acceleration on all axis (X, Y, and Z)", check the device photos above in the "Wakeup Threshold and Duration" section.

For example, the freefall threshold is set to 156.25g (it means that any acceleration between -156.25g to +156.25g falls under the configured threshold/acceleration range) and the freefall duration is set to 0.2s. As a result, as soon as the device is in a freefalling state with acceleration on all axis within the configured threshold (-156.25g&lt;acceleration&lt;+156.25g) for longer than 0.2s → a freefalling condition is triggered.

#### Angle Threshold

![](./img/image2022-2-2_9-19-46.webp)

Can vary between 50°...80°. It is the threshold for a tilt function. When the trigger is set to, for example, 60° and the device is tilted by that degree - the tilt action is triggered and the advertisement packet is sent.

#### Low noise filter

![](./img/image2021-11-30_11-55-41.webp)

An option to enable or disable a low noise filter. A low noise filter is used to reduce noise density in the measurements. Enabling this feature will slightly increase power consumption.

### "Transmission" settings

This section allows you to configure the "Tx power level" of the tag.

#### Tx power level

![](./img/image2021-11-30_11-56-42.webp)

The transmit power level in decibel-milliwatts. Can vary between -28dBm...6dBm. Tx Power is simply used to increase/decrease transmit power of the tag.

### "Advertismenet" settings

In advertising mode, the tag broadcasts information about itself in Bluetooth advertising packets. Information depends on the advertising packet type (the type can be changed in the settings).

At the moment, these are all the supported types:

MikroTik, [Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1), [Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) and [iBeacon](https://developer.apple.com/ibeacon/).

Eddystone-TLM, Eddystone-UID and iBeacon formats have an option to configure 4 parameters. MikroTik format has an option to configure an additional parameter called "encrypt packets":

![](./img/image2021-11-30_12-4-16.webp)

Once the checkbox "Enable advertising" is enabled, you will be able to configure the following parameters:

| Property | Description |
| --- | --- |
| Advertisement interval (20ms...10s or disable) | the interval in milliseconds after which an advertisement packet will be broadcasted by the tag |
| Freefall detection (on/off) | whether to send an advertisement packet when the accelerometer (the tag) detects a freefall trigger |
| Tilt detection (on/off) | whether to send an advertisement when the accelerometer (the tag) detects a tilt trigger |
| Impact detection (on/off) | whether to send an advertisement when the accelerometer (the tag) detects an impact/wake up trigger |
| Encrypt packets (on/off) - only available for MikroTik format | whether to encrypt acceleration, temperature, uptime, trigger action, and battery percentage parameters in the hex payload |

- When you have only advertisement interval configured without any triggers enabled - advertisement packets will be broadcasted based on the interval time set (each **x** seconds).
- When the tilt trigger is enabled and the device is tilted - the advertisement packet will be broadcasted immediately.
- When the freefall trigger is enabled and freefall is detected, as soon as the tag detects the freefalling condition -  the packet is sent.
- When the impact trigger is enabled and the device is pushed/moved - the advertisement packet is sent at once.
- When encrypt parameter is enabled, the hex payload data (like acceleration, temperature, uptime, trigger action, and battery percentage) is encrypted with a private key. This key is known only to the tag's owner (it is obtained with the purchase).

### "System" settings

The system section allows you to reset the tag's settings and put the tag into a factory sleep mode.

#### Reset device

This option puts the tag into advertising mode (to close the settings):

![](./img/image2022-2-2_9-43-25.webp)

#### Factory sleep

The option sets the device into a factory sleep mode:

![](./img/image2022-2-2_9-44-42.webp)
