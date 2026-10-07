# MikroTik Bluetooth TG-BT5-XX tag changelog

> MikroTik Bluetooth TG-BT5-XX tag changelog: documentation and related topics.

## 2.5.0

- Added new advertisement type "Device Name".
- Reduce device power consumption during activities. For short-interval advertisements will result in a noticeable reduction.
- Reduce power consumption if beacons with temperature data are enabled.
- Reduce WDT (watchdog timer) power consumption. This will have an effect if any beacon with advertising interval less than 7s is enabled.

## 2.4.0

- Include ad flags field in all advertisements.
- Added functionality to disable password protection.
- Added possibility to disable accelerometer.
- Added an option for MikroTik format payload to detect disabled accelerometer (flags field now can indicate disabled accelerometer state).
- Allow setting non-standard advertising intervals.
- Added configuration option to disable an advertising channel.
- Implemented configurable connectable advertisements, allowing to connect to the tag in a configurable state, without holding the magnet.
- Add configuration option for accelerometer to set filter type: HPF, LPF (high pass or low pass filters).
- Improvements to logging.

## 2.3.1

- Improved device performance.

## 2.3.0

- Upgraded Bluetooth stack version.
- Improved device performance.

## 2.2.0

- Added support for non-standard advertising intervals.

## 2.1.0

- Fixed timing inconsistencies after wake-up from the factory sleep mode.
- Improved LED behavior before the device enters the configuration mode.

## 2.0.0

- Restriction to set the wake-up threshold to 0g.
- Added Write Protection feature.
- Increase the minimal valid value of the wake-up threshold.
- Upgraded Bluetooth stack version.

## 1.6.0

- Improved Data Log stability.
- Added an option to allow users to manually calibrate the sensor's temperature (offset).

## 1.5.0

- Added a new trigger Impact.
- Added Data Logs.

## 1.4.0

- Added an option to reset the device back into the advertising mode.
- Added an option to clear saved log messages.
- Added a Unix Time parameter.
