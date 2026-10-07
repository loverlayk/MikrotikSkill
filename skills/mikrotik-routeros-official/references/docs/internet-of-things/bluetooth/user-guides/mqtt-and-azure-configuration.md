# MQTT and Azure configuration

> Publish MikroTik MQTT data to Microsoft Azure IoT, covering Azure account setup, device credentials, and MQTT broker configuration.

### Introduction

One of the many cloud services that you can use to monitor information that is sent by an MQTT publisher is Microsoft [Azure](https://azure.microsoft.com/en-us). This article will demonstrate how to configure both Azure and RouterOS to publish the data using the MQTT protocol. RouterOS, in this scenario, is going to act as a gateway and publish the data that is broadcasted by the BLEtag to the cloud (Azure). Azure, in this scenario, will act as an MQTT broker and MQTT subscriber (server, where data will be posted/shown).

Before we proceed with the settings, you need to create an account in the Azure system. You can find more information on how to do that following this [link](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=azurefreeaccount).

Azure has many different options and services that they provide and many of those options/services have a pricelist. You can find more information about pricing following the [link](https://www.azure.cn/en-us/pricing/).

### Azure configuration

Once you have a subscription setup (Azure Portal>All Services>Subscriptions), you will need to configure a resource group, an IoT hub, a certificate, and a device.

#### Resource Group

Go to All Services>Resource groups and create one.

![](../../img/azure_resources.png)

Link your IoT Hub to the previously created resource group. Do not forget to check/set up "Networking" (Network connectivity) and Management (a [subscription tier](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-scaling)) tabs.

You can find more information over [here](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub).

#### IoT Hub

Navigate to All services>IoT Hub and create one.

![](../../img/azure_iothub.png)

Link your IoT Hub to the previously created resource group. Do not forget to check/set up "Networking" (Network connectivity) and Management (a subscription tier) tabs.

You can find more information over here.

#### Certificates

In this example, we will be focusing on [X.509 CA-signed](https://learn.microsoft.com/en-us/azure/iot-edge/how-to-authenticate-downstream-device?view=iotedge-2020-11#x509-ca-signed-authentication) authentication.

You can use [Microsoft-supplied scripts](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows)) or [open SSL](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows) to generate test certificates.

After generating RootCA, go to IoT Hub>Certificates and add the certificate there:

![](../../img/image2021-6-1_9-46-36.webp)

After successfully adding RootCA, you will need to [prove possession](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows) (verify it).

It is well described and shown in the [tutorial (step 3)](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-3---prove-possession) if you are using scripts or [tutorial (step 7)](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-7---demonstrate-proof-of-possession) if you are using open ssl.

Once the certificate is successfully verified, you will need to create the [device certificate](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-4---create-a-new-device) (or follow this [link](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub) if you are using open ssl).

#### Devices

Navigate to your IoT Hub>IoT Devices and add a new device:

![](../../img/image2021-6-1_10-1-41.webp)

Pay attention to the "Device ID" field. The Device ID should match the "Common name" for the device certificate.

Chose `Authentication type=X.509 CA Signed` and save the setting.

You can now generate the last required certificate - the [device certificate](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-4---create-a-new-device) (or follow this [link](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub) if you are using open ssl).

With this, the Azure part of the configuration is complete.

### RouterOS configuration

:::info
In order to configure MQTT, make sure that **iot** package is installed beforehand.
:::
In our example, we are using [KNOT](https://mikrotik.com/product/knot) as a gateway and a script (created specifically for the KNOT) to publish the data. In your specific application scenario, you can use any RouterOS device (with iot package installed) to post any data that you need.

#### Certificates

Since we are using an SSL connection, we will require the previously generated device certificate and its private key. We will also be using [Baltimore CyberTrust Root certificate](https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-certificate-authority-details?tabs=root-and-subordinate-cas-list).

Go to the "Files" menu and add there the following certificates - *Baltimore CyberTrust Root certificate, previously generated device certificate, and its private key*.

![](../../img/image2021-6-1_10-34-22.webp)

Go to System>Certificates and import all 3 files (via the "Import" button - one by one):

![](../../img/image2021-6-1_10-36-54.webp)

:::info
*Double-check that the "Common Name" matches the Device ID that was configured for the device on the Azure portal. In our case, the Device ID is "testor" and it matches the "Common Name" field.*
:::
Make sure that both certificates are trusted (T) and that the private key (K) was added to the device certificate.

#### MQTT Broker

Navigate to IoT>MQTT and add a new broker ("+" button):

![](../../img/image2021-6-1_10-44-13.webp)

- Name the broker in the "Name" field (for example, **Azure**).
- Type in/paste Azure hostname address into the "Address" field (you can find the hostname in the IoT Hub>Overview menu):

![](../../img/image2021-6-1_10-24-10.webp)

- Configure the port used by the broker in the "Port" field and enable SSL via SSL checkbox (Azure, in this case, uses **8883** and, since we use certificates, it requires to **enable SSL**).
- The "Username" field should be configured the following way - `{iothubhostname}/{device_id}/?api-version=2018-06-30`, where `{iothubhostname}` is the hostname for your IoT hub and `{device_id}` is the Device ID that was set up on the Azure portal (same as the "Common Name" for the certificate and in our example, it is "testor").
- "Password" field is not required in this scenario (this configuration depends on the broker's settings - skip this field).
- "Client Id" should be the same as the Device's ID (in our example, **testor**).
- Since SSL is used, the certificate must be selected in the "Certificate" field (select the device certificate).

You can find more information about the required settings over [here](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#using-the-mqtt-protocol-directly-as-a-device).

Click on "Apply" and "OK" to finish setting up the broker.

#### MQTT Publish with a script

In order to publish data from the Bluetooth tag (in our example, TG-BT5-IN) to Azure, we will be using the script. Script example is shown below.

Every line that begins with the symbol `#` is instructional and it describes the parameter that is going to be configured below the line. Change the parameters within quotation marks `""` that would apply to your specific case.

```ros
## Required packages: iot

################################ Configuration ################################
## Name of an existing MQTT broker that should be used for publishing
:local broker "Azure"

## MQTT topic where the message should be published
:local topic "devices/testor/messages/events/"

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

:set $btOldestAdvertisementTimestamp $lastAdvTimestamp
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

2 script lines should be taken into account:

```
:local broker "Azure"
```

line, where you should specify the broker's name within the quotation marks `""` (in our example, **Azure**).

```
:local topic "devices/testor/messages/events/"
```

line, where you should specify the correct topic within the quotation marks `""`. The topic `devices/{device_id}/messages/events/` is used for publishing by Azure by default (as described in the manual [here](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#for-azure-iot-tools)). Do not forget to change the `{device_id}` part to the "Device ID" that was configured on your Azure portal.

The rest of the script configuration depends on the overall requirements. The script explains which exact parameters are configured to be published.

Navigate to System>Scripts, add a new script there, and paste the script that is shown above (name it, for example, script1).

To run the script, you can use the command line:

```
/system script run script1
```

### Verification

There are many different ways to view the received/published message on the Azure portal. Please check Azure tutorials on the options you have.

In our example, we will verify the results using the [Visual Studio Code program](https://code.visualstudio.com/).

Download the program and connect it to your [IoT Hub](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit).

Once the IoT Hub is added, you can start monitoring the endpoint:

![](../../img/image2021-6-14_10-47-6.webp)

And you can view published messages in the "OUTPUT" section as shown in the screenshot below:

![](../../img/image2021-6-1_11-39-43.webp)
