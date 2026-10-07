# Email notification on the MikroTik BLE tag's accelerometer triggers

> In this guide, we will show a quick step-by-step on how you can set up your KNOT to send an e-mail notification, whenever it detects a "triggered" condition reported by the TG-BT5-IN or TG-BT5-OUT tag.

### Introduction

In this guide, we will show a quick step-by-step on how you can set up your KNOT to send an e-mail notification, whenever it detects a "triggered" condition reported by the [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) or [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) tag.

Both tags have a built-in accelerometer that is able to detect free-falling, wakeup/movement, and tilted states. When the tag is set up to broadcast [MikroTik format](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-tag-advertisement-formats) payloads and accelerometer triggers are enabled (using the MikroTik Beacon Manager app) → the tag will instantly broadcast an advertising payload/report whenever the trigger is going to be detected.

For [iOS](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices), the trigger setting looks like this (in a disabled state/default settings):

![](../../img/image2022-8-12_8-26-32.webp)

For [Android](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices), the trigger setting looks like this (in a disabled state/default settings):

![](../../img/image2022-8-12_8-29-6.webp)

To active trigger detection, just enable the corresponding "checkbox".

After the Bluetooth payload is broadcasted by the tag →  the payload's 21st octet will indicate which exact trigger was detected. You can view the payloads under the **IoT>Bluetooth>Advertisng reports** tab:

![](../../img/image2022-8-12_9-24-4.webp)

As per the screenshot above, the 21st octet is "04", which indicates, that the payload was sent when a freefalling condition was detected by the tag (these payloads were broadcasted when we "accidentally" dropped or threw the tag).

Once everything is configured the following is going to happen:

- The KNOT will run a script on a schedule.
- The script will "read/scan" the payloads that are shown in the **IoT>Bluetooth>Advertising reports** tab.
- If the stored/captured payload's 21st octet value equals to any "triggered" value → email notification is going to be sent.

In other words, when the KNOT scans through the payloads and finds one where the 21st octet indicates that the trigger was activated → you will get an email notification that the trigger was detected.

### TG-BT5 tag configuration

In this specific example, we need to set up our tags to work in the **MikroTik format**. In the MikroTik format, the 21st octet of each payload will indicate the reason it was triggered.

You can find a manual on how to enable the triggers by following the [iOS](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices) and/or [Android](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices) guides (**"Advertisement"/Beacon settings** sections).

To easier "activate" the trigger, we can also alter the trigger's settings as per the iOS and/or Android guides (**Free Fall Threshold and Duration** sections). For the purpose of the test and to, basically, just "trigger" the detection much faster, we can change the "**Free Fall Duration**" parameter to "0" seconds (this will make sure that any acceleration that is within the threshold on all axis will be instantly detected as a "freefalling" event).

### RouterOS configuration

:::info
**iot** package is required. You can get it from our download page - under "Extra packages".
:::
The configuration can be completed in 4 steps:

- enable scanner (and, preferably, confirm that the tag is broadcasting payloads when the trigger is detected);
- set up an email server;
- import the script (and alter a few script lines depending on the requirement);
- set up the scheduler.

#### Bluetooth Scanner

Go to the [IoT>Bluetooth>Scanners](/docs/internet-of-things/bluetooth/) tab and make sure that it is enabled:

![](../../img/image2022-8-12_9-39-30.webp)

Go to the **Advertising reports** tab and filter the list using the MAC address filtering option (you can find the MAC address of the MikroTik tag printed on the label on the tag itself).

Try to "trigger" the configured detection and confirm it by checking the 21 octet's value.

In our example, we configured the "freefalling" detection for our tag and we **dropped it**. We got reports from the tag indicating the "falling" state (21st octet = **04**):

![](../../img/image2022-8-12_9-48-45.webp)

We have confirmed, that the tag is reporting the trigger properly.

#### Email

Navigate to the [Tools>Email](/docs/system-information-and-utilities/e-mail) section and set up an email server of your choice.

We will be using shown **GMAIL** example in this guide.

![](../../img/image2022-8-12_10-5-40.webp)

Try sending a test email to make sure that it is set up correctly.

#### Scripts

##### Option (a)

Navigate to [System>Scripts](/docs/developer-guides/scripting/) menu and add a new script there.

You can copy the script below. Copy the script below into a "notepad" and copy it again into the script "**Source:**" field.

```ros
## Input MAC address of the tag within ""
:local addressRegex "2C:C8:1B:E2:15:29"

#enter the subject for the email within the ""
:local emailsubject "RouterOS report!"

#enter the email address wthin the ""
:local emailaddress "YOUR_EMAIL@gmail.com"

#Script:
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## Find fresh Bluetooth advertisements
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local obj "$[$flagStr $flags]"

    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

#Message structure:
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--trigger(s) reported by the tag!"

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"} else={:put "21st octet does not have triggers detected!"}
```

The following 3 lines need to be taken into account:

```
:local addressRegex "2C:C8:1B:E2:15:29"
```

line, where we input the MAC address of the tag that you wish to monitor;

```
:local emailsubject "RouterOS report!"
```

line, where you can alter the subject for the email;

```
:local emailaddress "YOUR_EMAIL@gmail.com"
```

the email address line, where you need to input the email address. To where do you want to send the report.

You can also change the structure of the e-mail message using the lines:

```ros
#Message structure:
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--trigger(s) reported by the tag!"
```

Name the script however you like, for example, **triggernotification**. Click on **Apply** and **OK**.

:::info
AdditionallyIn this example, we are specifically showcasing an e-mail notification scenario. **But!** in case you want to use other methods for sending a notification, you can just alter the line below:

```
:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"}
```

You can change the `do={/tool e-mail...` part of the line to, for example, `do={/tool fetch...` or `do={/iot mqtt publish...`. That way, you can send out an HTTP post or MQTT publish message instead.

If you would like to get a phone notification when the trigger is detected, you can also utilize IFTTT services (HTTP post to IFTTT webhook) as described in our other guide over [here](/docs/internet-of-things/bluetooth/user-guides/ifttt-app-notifications-ble-tag).
:::
You can run the script manually via the command "**/system script run triggernotification**" or by clicking on the "**Run Script**" button under the **Script List** section.

You should make sure that the e-mail notification was received after manually initiating the script.

When script **(a)** is initiated, RouterOS is going to check every received/stored Bluetooth payload, and if any trigger is found in the payload's list → an e-mail message is structured and sent. This e-mail message will simply indicate which triggers were detected in the list with no additional information.

##### Option (b)

```ros
## Input MAC address of the tag within ""
:local addressRegex "2C:C8:1B:E2:15:29"

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold ""

#enter the subject for the email within the ""
:local emailsubject "RouterOS report!"

#enter the email address wthin the ""
:local emailaddress "YOUR_GMAIL@gmail.com"

#Script:
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## Find fresh Bluetooth advertisements
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local fflags "$[$flagStr $flags]"
    :if ($fflags="") do={:set $fflags "none - periodically broadcasted payload"}

    :local obj "# $advCount:
                             time: $rtime
                             trigger: $fflags

"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$triggerlist"} else={:put "21st octet does not have triggers detected!"}
```

When script **(b)** is initiated, RouterOS is going to check every received/stored Bluetooth payload, and if any trigger is found in the payload's list → an e-mail message is structured and sent. This e-mail message will have a bit more detailed information, compared to script **(a)**. The message, in this case, will indicate each payload's reception time.

#### Scheduler

To automate the process add a new scheduler under the **System>Scheduler** tab:

![](../../img/image2022-8-12_13-8-32.webp)

Type in "**/system script run triggernotification**" under the "**On Event:**" field and set up an **interval** with which you wish to run the script to check/scan advertising reports (to, for example, 10 seconds).

Click on **Apply** and **OK**.

#### Result verification

1) Confirm that the tag broadcasts advertising reports and that the tag's triggers get detected:

![](../../img/image2022-8-12_9-48-45.webp)

1) Confirm that your email server is set up correctly and that you are able to send emails from the KNOT (RouterOS).

2) After you manually run the script or apply a scheduler to the script, an email notification should go through, like so:

     Script **(a)**:

![](../../img/image2022-8-29_15-15-9.webp)

     Script **(b)**:

![](../../img/image2022-8-29_15-18-39.webp)
