# MQTT/HTTPS and AWS configuration

> Forward MikroTik Bluetooth tag data to Amazon AWS using MQTT over HTTPS, covering AWS account setup, certificates, and broker configuration.

### Introduction

One of the options, that you can use to monitor information that is broadcasted by the Bluetooth tags is cloud systems, like AWS (Amazon WEB Services). In this article, we will show how to configure both AWS and RouterOS to publish the data using the MQTT and HTTPS protocols. RouterOS, in this scenario, is going to act as a gateway and publish the data that is broadcasted by the BLEtag to the cloud (AWS). AWS, in this scenario, will act as an MQTT broker and MQTT subscriber (server, where data will be posted/shown).

Before we proceed with the settings, you need to create an account in the AWS system. You can find more information on how to do that following this [link](https://repost.aws/knowledge-center/create-and-activate-aws-account).

After you have created an account, make sure that the payment card validates under **Your_Username>My account**, or else the account will not be active.

Go to **Services>Internet of Things>IoT Core**.

In the **Test** section, you can use a build-in MQTT test client so you can test publishing and subscribe to topics. You have **Subscribe to a topic** and **Publish to a topic** tabs which allows you to check both processes. MQTT test client section can also display HTTPS posts.

### AWS IoT configuration

:::info
Configuration shown in this section is meant for MQTT publish/subscribe scenario but you can also test HTTPS posting using the same AWS settings.
:::

#### Things

Step 1: Navigate to **Manage>Things**. This is the menu where configuration begins (Things menu is the representation of a device or logical entity).

**

![](../../img/image2021-3-31_11-20-55.webp)

**

Press **Create>Create a single thing>**choose a name**>Next>Create certificate.**

Step 2: Download "AmazonRootCA1.pem" certificate (Root CA for AWS), "xxxx.cert.pem" certificate (a certificate for the "thing") and "xxxx.private.key" key (a private key) - the "xxxx"part is unique for each newly created certificate.

![](../../img/image2021-3-31_11-40-45.webp)

Step 3: You have an option to either finish the setting (by choosing **Done**) or set up a policy (by choosing **Attach a policy**). You need to add policies to the created "thing" but if you are doing it with a fresh account, you might not have any policies to choose from. Do not worry, you can create them manually later.

There are two other menus that are important - **Secure>Certificates** and **Secure>Policies**.

#### Certificates

In the **Certificates** menu, you can create certificates, activate them and attach them to policies. The "Things" configuration should have already created the certificate. Just make sure that the certificate is "activated". To do that, select the certificate, click on "**Actions**" and click "**Activate**".

![](../../img/image2021-3-31_11-41-18.webp)

#### Policies

![](../../img/image2021-3-31_11-45-14.webp)

Step 1: Create a new policy. Click on "**Create**" and type in the name for the policy. In the "**Create a policy**" tab you have an option to set up "actions". We will be using 4 actions in this example (`iot:Publish`, `iot:Receive`, `iot:Subscribe` and `iot:Connect`). You can find more information on policies with examples following the [link](https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html).

Step 2: Navigate to the "**Add statements**" section. In the "**Action**" field, choose **iot:Publish** and **iot:Receive** actions and separate them with a comma ",". In the "**Resource ARN**" field replace the text "`replaceWithATopic`" with an actual relevant topic (for example "`my/test/topic`"). In the "**Effect**" checkbox mark "**Allow**".

![](../../img/image2021-3-31_11-48-20.webp)

Step 3: Add a new statement by clicking "**Add statement**". Add an action to the statement by choosing **iot:Subscribe** and replace the text in the "**Resource ARN**" field "`replaceWithATopicFilter`" with an actual relevant topic (for example "`my/test/topic`"). In the "**Effect**" checkbox mark "**Allow**".

![](../../img/image2021-3-31_11-51-18.webp)

Step 4: Add the last statement and setup **iot:Connect** action. Change only the "`replaceWithAClientId`" part with a proper client-id (for example "`test-client`") and mark the "**Allow**" checkbox. To finish the setup, click "**Create**".

Step 5: You need to attach the certificate to the newly created policy. In order to do that, go to **Secure>Certificates**, select the certificate, click on "**Actions**" and "**Attach policy**".

![](../../img/image2021-3-31_11-56-52.webp)

Select the policy and click "**Attach**".

![](../../img/image2021-3-31_11-57-29.webp)

And with that, the AWS settings are done.

#### Endpoint Address (Broker's address)

You can find the **Endpoint** address in the "**Settings**" section (Settings>Device data endpoint). This address should be configured as the broker's IP/FQDN address in the RouterOS settings.

![](../../img/image2021-3-31_12-0-54.webp)

### RouterOS configuration

:::info
In order to configure MQTT, make sure that **iot** package is installed beforehand.
:::
In our example, we are using [KNOT](https://mikrotik.com/product/knot) as a gateway and a script (created specifically for the KNOT) to publish the data. In your specific application scenario, you can use any RouterOS device (with iot package installed) to post any data that you need.

#### Certificates

Since AWS uses an SSL connection, we will require previously downloaded certificates and the key.

Go to the "Files" menu and add to the "File list" *AmazonRootCA1.pem*, *xxxx.cert.pem.crt* and *xxxx.private.pem.crt*.

![](../../img/image2021-3-24_16-11-43.webp)

Go to System>Certificates and import all 3 files (via the "Import" button - one by one):

![](../../img/image2021-3-24_16-4-55.webp)

Make sure that both certificates are trusted (T) and that "xxxx.certificate.pem.crt" is with a private key (K).

#### MQTT Broker

Navigate to IoT>MQTT and add a new broker ("+" button).

![](../../img/image2021-4-27_9-9-32.webp)

Name the broker in the "Name" field (for example, **AWS**).

Type in/paste AWS address into the "Address" field (you can find it in the AWS settings "**Settings>Device data endpoint**" - **Endpoint address**).

Configure the port used by the broker in the "Port" field and enable SSL via SSL checkbox (AWS, in this case, uses **8883** and, since we use certificates, it requires to **enable SSL**).

"Username" and "Password" fields are not required in this scenario (depends on the broker's configuration - skip both fields).

Set up a client-id in the "Client Id" field (it is the ID that was configured in the AWS policies - in this example, **`test-client`**).

Since SSL is used, the certificate must be selected in the "Certificate" field (select ***xxxx.certificate.pem.crt***).

Click on "Apply" and "OK" to finish setting up the broker.

#### MQTT Publish with a script

In order to publish data from the Bluetooth tag (in our example, TG-BT5-IN) to AWS, we will be using the script. Script example is shown below.

Every line that begins with a symbol `#` is instructional and it describes the parameter that is going to be configured below the line. Change the parameters within quotation marks `""` that would apply to your specific case.

```ros
## Required packages: iot

################################ Configuration ################################
## Name of an existing MQTT broker that should be used for publishing
:local broker "AWS"

## MQTT topic where the message should be published
:local topic "my/test/topic"

## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"clientId\":\"$[/iot mqtt brokers get value-name=client-id \
            [/iot mqtt brokers find name=$broker]]\",\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
:put ("[*] Sending message to MQTT broker...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] Done")
```

2 script lines should be taken into account.

```
:local broker "AWS"
```

line, where you should specify the broker's name within the quotation marks `""` (in our example, **AWS**).

```
:local topic "my/test/topic"
```

line, where you should specify the correct topic within the quotation marks `""`. The topic is configured in AWS policies (in our example, **my/test/topic**).

The rest of the script configuration depends on the overall requirements. The script explains which exact parameters are configured to be published.

Navigate to System>Scripts, add a new script there, and paste the script that is shown above (name it, for example, script1).

To run the script, you can use the command line:

```
/system script run script1
```

#### HTTPS post with a script

Another protocol that can be used to post the data from the gateway to the cloud is - HTTPS. This can be achieved using the [fetch tool](/docs/system-information-and-utilities/fetch). Until 7.1beta6 RouterOS version, fetch did not have an option to select a client certificate for the authentication (meaning HTTPS posting with client certificate was not supported) and in 7.1beta6 a new feature was added that enables this setting/support. HTTPS post examples using CURL and Python (as well as other useful information) are shown in the [AWS HTTPS manual](https://docs.aws.amazon.com/iot/latest/developerguide/http.html).

In order to post the data from the Bluetooth tag (in our example, TG-BT5-IN) to AWS, we will be using the script. Script example is shown below.

Every line that begins with a symbol `#` is instructional and it describes the parameter that is going to be configured below the line. Change the parameters within quotation marks `""` that would apply to your specific case.

```ros
################################ Configuration ################################
## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"

:put ("[*] Done")
```

1 script line should be taken into account:

```
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"
```

Change the certificate name and the URL accordingly to your specific case:

`url="https://xxxx:8443/topics/yyyy"`, where "xxxx" is AWS endpoint address and "yyyy" is the topic that was configured in the AWS policies - steps 2 and 3 (in our example, my/test/topic).

The rest of the script configuration depends on the overall requirements. The script explains which exact parameters are configured to be published.

Navigate to System>Scripts, add a new script there, and paste the script that is shown above (name it, for example, script2).

To run the script, you can use the command line:

`/system script run script2`

### Verification

To verify that AWS gets the data, go back to the AWS portal. Navigate to the **Test** page. Use **Subscribe to a topic** option. Type in the topic that was configured in the AWS policies (in our example, **my/test/topic**) in the **Topic filter** field and press **Subscribe**. Below, you should see the **Subscriptions** section where the data is going to be shown. Run the script (in RouterOS) and you should see the collected data in the "**Subscriptions**" tab.

![](../../img/image2021-3-31_12-47-14.webp)

The same page/tab should display HTTPS posted packets as well.
