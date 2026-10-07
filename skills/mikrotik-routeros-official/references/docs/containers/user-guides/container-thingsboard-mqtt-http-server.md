# Container - ThingsBoard MQTT/HTTP server

> This page introduces the container feature in MikroTik RouterOS, enabling users to run servers like ThingsBoard MQTT/HTTP IoT platform directly on the router. It explains how to configure container mode, networking...

# Container - ThingsBoard MQTT/HTTP server

The introduction of the container feature into RouterOS made it possible to run all kinds of servers for all sorts of tasks inside the router. This is especially relevant for people who want to reduce the number of devices in their network. Instead of running a server on a separate device/machine, why not run it inside the router?

A lot of users need a server that is able to gather the data, store it and display it in a way that it is easy to understand. This is where a platform like [ThingsBoard](https://thingsboard.io/) can come into play.

It is primarily positioned as an IoT platform and you can find all sorts of use cases for it that they demonstrate in the [link](https://thingsboard.io/iot-use-cases/).

The most appealing part, from the RouterOS user standpoint, is that it can be used as an MQTT server (MQTT broker) or an HTTP server, meaning, you can use [MQTT publish](../../internet-of-things/mqtt/index.md) or [HTTP post](../../system-information-and-utilities/fetch.md) to post the data. You can find the ThingsBoard MQTT API guide by using the link [here](https://thingsboard.io/docs/reference/mqtt-api/) and the HTTP API by using the link [here](https://thingsboard.io/docs/reference/http-api/).

In short, you can utilize [scripting](../../developer-guides/scripting/index.md) to collect RouterOS statistics (like uptime, GPS coordinates, packet statistics, and almost anything else that you print into the terminal), then store this information into variables and structure a JSON message out of those. You can then send this message using MQTT or HTTP post to the ThingsBoard via a [scheduler](../../system-information-and-utilities/scheduler.md) (that will run this script whenever you need it). You can find an example of a basic script that does it in [this guide](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md).

ThingsBoard will store and display the data with the help of [widgets](https://thingsboard.io/docs/user-guide/ui/widget-library/), which can be used to help you set up dashboards that visualize the data in graphs, tables, maps, and other ways.

For example, there are 2 below-mentioned options of the ThingsBoard instances available and each of them uses a different database:

- [thingsboard/tb-postgres](https://hub.docker.com/r/thingsboard/tb-postgres/)
- [thingsboard/tb-cassandra](https://hub.docker.com/r/thingsboard/tb-cassandra/)

You can find more information in the ThingsBoard/docker documentation.

In our example, we will showcase **tb-postgres** - a single instance of ThingsBoard with a PostgreSQL database for testing purposes.

The guide will showcase an "in-memory" queue type service, but for a production environment, consider using other service types. You can find more information [here](https://thingsboard.io/docs/user-guide/install/docker/).

## Summary

**Sub-menu:** `/container`

***note**:* **container** package is required.

RouterOS versions that are older than v7.8 will not be able to run this scenario.

Make sure to study our [container](../) guide before proceeding with the configuration. Make sure to check the [disclaimer](../#disclaimer) and [requirements](../#requirements) sections to understand all the risks and necessary steps you might be required to do.

In this example, we will run it on a [Cloud Hosted Router, CHR](../../getting-started/routeros-licensing/chr/index.md).

At the time when the guide was published, the **thingsboard/tb-postgres** image was available for linux/**arm64** and linux/**amd64** OS/architectures **only**. This means you are not able to run this scenario on our arm32-bit architecture RouterOS devices.

There are a couple of parameters to keep in mind:

- You need to understand that it is a **server** and that you will need to have additional space for the data that is stored there and the image itself. In our tests, 8 GB of disk space was plenty enough but! you might want to consider adding more for real-life applications, especially if you are planning on running more containers. Just remember → it might be better to have a reserve.
- Same as with disk space, RAM memory is also important. Per the ThingsBoard documentation, when using a single instance of ThingsBoard with a PostgreSQL database, it is recommended to allocate at least 1GB of RAM and use a minimum load (a few messages per second). 2-4GB RAM is recommended. In other words, if you want to run it on a RouterBoard device, please understand that you might not be able to achieve it on devices that have less than 1 GB RAM. That is why → consider having a device with more RAM memory to spare.

Go to the [tips and tricks](../#tips-and-tricks) section to understand how to limit RAM.

## Configuration

### Container mode

Enable container mode:

```ros
/system/device-mode/update container=yes
```

You will need to confirm the device-mode with a press of the reset button, or a cold reboot, if using a container on X86.

### Networking

Add veth interface for the container

```ros
/interface/veth/add name=veth1 address=172.18.0.2/24 gateway=172.18.0.1
```

Create a bridge for the container, assign an IP network to it, and add veth to the bridge

```ros
/interface/bridge/add name=dockertb
/ip/address/add address=172.18.0.1/24 interface=dockertb
/interface/bridge/port/add bridge=dockertb interface=veth1
```

Setup NAT for outgoing traffic

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.18.0.0/24
```

Forward TCP 9090 for HTTP management (the default HTTP port per ThingsBoard documentation)

:::warning

We suggest using HTTP access only when testing locally or through a VPN (when you are certain that the local network is safe).

When you want to access container WEB management from the internet (from the public network/WAN), please, instead, consider using **HTTPS**.

:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=9090 protocol=tcp to-addresses=172.18.0.2 to-ports=9090
```

In the `dst-address` field shown in the DNAT (dst-nat) rule above, we use the device's local IP address. First, **use local IPs** (local access) **to** **set everything up** **and** **confirm that everything is working**.

:::info

After going through the rest of the steps shown in this guide and verifying that the ThingsBoard management portal works locally →  **further secure the setup**:

- (a) make sure that all default ThingsBoard user credentials were changed/removed and strong passwords were implemented (reference ThingsBoard documentation);
- (b) **enable** **HTTPS** (the steps will be explained later on in the guide);
- (c) preferably change the HTTPS port to a non-standard one (reference ThingsBoard documentation).

Only when you increase the security and only then →  you can consider enabling remote access from WAN (by using your public IP address in the `dst-address` field instead of the local IP used in the example above). Additionally, to further increase security, use the `src-address` or `src-address-list` parameter, where you can input your trusted public source IP addresses (a list of known/trusted addresses that, for example, belong to your branch office from where you also want to have access to the server). Please understand that only you are responsible for the security. If you leave a door open, someone may exploit it. You need to have networking knowledge and understand the risks when setting up such scenarios.
:::

Forward TCP 1883 for non-SSL MQTT (the default MQTT port used per ThingsBoard documentation)

:::warning
We suggest using non-SSL MQTT (TCP 1883) communication only when testing locally or through a VPN (when you are certain that the local network is safe).
>
Please consider using **SSL MQTT (TCP port 8883)**, instead of non-SSL MQTT (TCP port 1883), for real-life application, when it comes to access from the internet (from the public network). If you use non-SSL MQTT, the communication between the client (MQTT publisher) and the server (MQTT broker) can be easily sniff/packet captured, and that will compromise authentication data (such as client-ids, usernames and passwords).
:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.18.0.2 to-ports=1883
```

Same as with HTTP access, in the `dst-address` field shown in the DNAT (dst-nat) rule above, we use the device's local IP address. First, **use local IPs** (local access) **to** **set everything up** **and** **confirm that everything is working**.

:::info
After going through the rest of the steps shown in this guide and verifying that the ThingsBoard non-SSL MQTT communication works locally →  **further secure the setup**:
>
- (a) consider removing template devices from the ThingsBoard installation;
- (b) **enable SSL MQTT** (the steps will be explained later on in the guide);
- (c) preferably change MQTT port to a non-standard one (reference ThingsBoard documentation).
>
When you enable SSL MQTT, you can consider opening TCP 8883 (which is the default SSL MQTT port) from WAN (by using your public IP address in the `dst-address` field instead of the local IP, and changing `dst-port` and `to-ports` from 1883 to 8883). Additionally, to further increase security, use `src-address` or `src-address-list` parameters, where you can set up your trusted public IP address list. As a result, only configured trusted IPs will be able to establish an MQTT connection with the ThingsBoard broker.
:::

### Environment variables and mounts

Check the [docker-thingsboard](https://hub.docker.com/r/thingsboard/tb-postgres) documentation for exact mounts and variables that need to be added.

#### Environment variables

```ros
/container/envs/add list=tb_envs key=TB_QUEUE_TYPE value="in-memory"
```

#### Mounts

```ros
/container/mounts/add list=mytb-data src=tb/mytb-data dst=/data
/container/mounts/add list=mytb-logs src=tb/mytb-logs dst=/var/log/thingsboard
```

### Getting image

To simplify the configuration, we will get the image from an external library, but you can also import it via the [.tar](../#option-b-import-image-from-pc) file.

Make sure that you have "Registry URL" set accordingly, limited RAM usage (if necessary), and set up a directory for the image.

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull ram-high=2048.0MiB
```

Pull image:

```ros
/container/add remote-image=thingsboard/tb-postgres:latest interface=veth1 root-dir=ThingsBoard mountlists=mytb-data,mytb-logs envlists=tb_envs logging=yes
```

After running the command, RouterOS should start "extracting" the package. Check "File System" for newly created folders and monitor container status with the command `/container/print`.

### Starting the container

After you make sure that the container has been added and the status has changed to `status=stopped` after using `/container/print`, you can initiate it:

```ros
/container/start 0
```

Wait for a couple of minutes for the container to fully load.

## Verification

### Management access

After the container is started and installed, access it using any browser, by going to → [http://192.168.88.1:9090](http://192.168.88.1:9090) (where the IP address is the address used in the DNAT rule):

![](./img/container-thingsboard-mqtt-http-server-01.webp)

By default, credentials are (Username/Password):

- **System Administrator**: sysadmin@thingsboard.org / sysadmin
- **Tenant Administrator**: tenant@thingsboard.org / tenant

The login prompt should confirm that the server is running.

### MQTT test

Log in with the **tenant** and create a new device. Go to the "**Devices**" menu, click on the "**+**" (Add Device) button and choose the "**Add new device**" option:

![](./img/container-thingsboard-mqtt-http-server-02.webp)

 Name it, however you like, and click on "**Add**":

![](./img/container-thingsboard-mqtt-http-server-03.webp)

Check your device access token by clicking on the device you've just created and selecting the "**Manage credentials**" setting (copy the access token generated or type in your own →  "YOUR\_TOKEN"):

![](./img/container-thingsboard-mqtt-http-server-04.webp)

After these steps, go to the RouterOS settings (back to CHR settings) and create a new [MQTT broker](../../internet-of-things/mqtt/index.md) (**make sure that you have the IoT package installed** because otherwise, you will not have this menu):

```ros
/iot/mqtt/brokers/add name=tb address=172.18.0.2 port=1883 username=YOUR_TOKEN
```

Publish a static test MQTT message in the JSON format:

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

Confirm that the message was posted:

![](./img/container-thingsboard-mqtt-http-server-05.webp)

## Enabling HTTPS and SSL MQTT

By default, HTTP and MQTT protocols are used. As mentioned previously in the "Networking" section, working with non-SSL HTTP and non-SSL MQTT is not very safe (unless they are used within heavily protected networks with a well-configured firewall/restricted access), and **we advise enabling HTTPS** and **SSL MQTT**.

Please check ThingsBoard documentation for more information → [HTTP over SSL](https://thingsboard.io/docs/user-guide/ssl/http-over-ssl/) and [MQTT over SSL](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) guides.

First of all, there is no SSL without a certificate, and one needs to be made (or purchased).

In short, this section will demonstrate how to generate self-signed certificates for HTTPS and SSL MQTT. Then, you will need to upload them to the correct folder within the ThingsBoard installation and alter the ThingsBoard configuration file accordingly.

In our guide, we will use RouterOS to generate both [certificates](../../authentication-authorization-accounting/certificates.md) (but you can also use OpenSSL or other tools you want).

### Create certificates

Create a certificate for HTTPS:

```ros
/certificate/add name=TBhttps common-name=172.18.0.2
/certificate/sign TBhttps
```

Create a certificate for MQTT:

```ros
/certificate/add name=TBmqtt common-name=172.18.0.2
/certificate/sign TBmqtt
```

Confirm that they were added with the help of the `/certificate/print` command:

```ros
[admin@MikroTik] > /certificate/print
Flags: K - PRIVATE-KEY; A - AUTHORITY; T - TRUSTED
Columns: NAME, COMMON-NAME, FINGERPRINT
#     NAME     COMMON-NAME  FINGERPRINT                                                     
0 KAT TBhttps  172.18.0.2   863f4547c74ce3ec70c3e82172502711517b52bbc055d18c24ba4aafec46152c
1 KAT TBmqtt   172.18.0.2   ebf3ff5d03ed4cc73546e058da9bc414cdaf24ce45da29b203348045fbbd21ae
```

Export the certificates using PKCS12 format and set up a password/passphrase for them:

```ros
/certificate/export-certificate file-name=keystore export-passphrase=thingsboard_cert_password type=pkcs12 numbers=0
/certificate/export-certificate file-name=mqttserver export-passphrase=thingsboard_mqttcert_password type=pkcs12 numbers=1
```

Use your own `export-passphrase` and remember it.

The output from the command above will create certificate files **keystore.p12** and **mqttserver.p12** that you can download from the "[File List](../../system-information-and-utilities/files.md)" menu:

```ros
[admin@MikroTik] > /file/print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
 #  NAME                 TYPE             SIZE       CREATION-TIME       
 0  tb/mytb-data         container store             2023-01-19 13:43:16
 1  container-log.0.txt  .txt file        2240.5KiB  2023-01-27 15:37:41
 2  skins                directory                   2023-01-18 15:12:22
 3  tb/mytb-logs         container store             2023-01-27 12:24:30
 4  pull                 directory                   2023-01-19 13:41:01
 5  pub                  directory                   2023-01-18 16:15:29
 6  tb                   directory                   2023-01-23 15:46:39
 7  tb/data              container store             2023-01-18 16:50:08
 8  tb/logs              container store             2023-01-18 16:50:08
 9  mqttserver.p12       .p12 file        2438       2023-01-27 15:36:26
10  keystore.p12         .p12 file        2448       2023-01-27 15:08:07
11  ThingsBoard          container store             2023-01-19 13:40:50
```

Download both files from the router into any directory on your PC. For example, we've downloaded them into `C:\Users\Admin\Desktop\ThingsBoard` folder.

### Download the ThingsBoard's configuration file

Open your command terminal ("CMD", as Administrator, for Windows users, or "Linux Shell or Command Terminal" for Linux users) and navigate to the directory where the certificates are:

```powershell
C:\Windows\System32>cd c:\Users\Admin\Desktop\ThingsBoard
C:\Users\Admin\Desktop\ThingsBoard>dir
Directory of C:\Users\Admin\Desktop\ThingsBoard

27.01.2023  15:36    <DIR>          .
27.01.2023  15:36    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
               2 File(s)          4 882 bytes
               2 Dir(s)  51 380 154 368 bytes free
```

From this directory, you will need to connect to the router's IP via SFTP (which allows you to transfer files using SSH protocol, so you need to make sure that [SSH service](../../system-information-and-utilities/services.md) is enabled beforehand):

```powershell
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:/WmmZErqWL51SOlS4EaGvSQ0i4HPnSIHCEjnc8AmP2c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp>
```

While the container is running, go to the ThingsBoard configuration file folder (use `dir` or `ls` command to see the content of the folder you are in and `cd` command to go to the folder of our choice). By default, it should be the folder with the "**thingsboard.yml**" configuration file in it. In our example, we could locate it under:

```powershell
sftp> cd ThingsBoard/usr/share/thingsboard/conf

sftp> dir

banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

Download the "**thingsboard.yml**" configuration using the `get` command. This will download the default ThingsBoard configuration file to your machine (to the directory from where you initiated SFTP):

```powershell
sftp> get thingsboard.yml
Fetching /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml to thingsboard.yml
/ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml                               100%   67KB   2.0MB/s   00:00
sftp> quit

c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
```

### Alter the ThingsBoard's settings

Open "**thingsboard.yml**" via your preferred text editor (notepad or any other), and alter a few lines. You can backup this file and save it with a different name to have a copy of the default settings, in case of misconfiguration.

#### HTTPS-related settings

1. Enable SSL →  Change "SSL\_ENABLED:**false**" to "SSL\_ENABLED:**true**".
2. Change credentials type → from "SSL\_CREDENTIALS\_TYPE:**PEM**" to "SSL\_CREDENTIALS\_TYPE:**KEYSTORE**".
3. Change the path → from "SSL\_KEY\_STORE:**classpath:keystore/keystore.p12**" to "SSL\_KEY\_STORE:**keystore.p12**" (optional).
4. Disable key alias setting → comment it → just put the "**#**" symbol in front of the `key_alias: "${SSL_KEY_ALIAS:tomcat}"` line.
5. Input your own certificate password that was used in RouterOS → from "SSL\_KEY\_STORE\_PASSWORD:**thingsboard**" to "SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_cert\_password**" and from "SSL\_KEY\_PASSWORD:**thingsboard**" to "SSL\_KEY\_PASSWORD:**thingsboard\_cert\_password**".

```js
  ssl:
    # Enable/disable SSL support
    enabled: "${SSL_ENABLED:true}"
    # Server SSL credentials
    credentials:
      # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
      type: "${SSL_CREDENTIALS_TYPE:KEYSTORE}"
      # Keystore server credentials
      keystore:
        # Type of the key store (JKS or PKCS12)
        type: "${SSL_KEY_STORE_TYPE:PKCS12}"
        # Path to the key store that holds the SSL certificate
        store_file: "${SSL_KEY_STORE:keystore.p12}"
        # Password used to access the key store
        store_password: "${SSL_KEY_STORE_PASSWORD:thingsboard_cert_password}"
        # Key alias
        #key_alias: "${SSL_KEY_ALIAS:tomcat}"
        # Password used to access the key
        key_password: "${SSL_KEY_PASSWORD:thingsboard_cert_password}"
```

#### MQTT-related settings

1. Enable SSL →  Change "MQTT\_SSL\_ENABLED:**false**" to "MQTT\_SSL\_ENABLED:**true**";
2. Change credential type → from "MQTT\_SSL\_CREDENTIALS\_TYPE:**PEM**" to "MQTT\_SSL\_CREDENTIALS\_TYPE:**KEYSTORE**";
3. Change the type of key → from "MQTT\_SSL\_KEY\_STORE\_TYPE:**JKS**" to "MQTT\_SSL\_KEY\_STORE\_TYPE:**PKCS12**";
4. Change the path (extension) → from "MQTT\_SSL\_KEY\_STORE:mqttserver**.jks**" to "MQTT\_SSL\_KEY\_STORE:mqttserver**.p12**".
5. Disable key alias setting → comment it → just put the "**#**" symbol in front of the `key_alias: "${MQTT_SSL_KEY_ALIAS:}"` line;
6. Input your own certificate password that was used in RouterOS → from "MQTT\_SSL\_KEY\_STORE\_PASSWORD:**server\_ks\_password**" to "MQTT\_SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_mqttcert\_password**" and from "MQTT\_SSL\_KEY\_PASSWORD:**server\_key\_password**" to "MQTT\_SSL\_KEY\_PASSWORD:**thingsboard\_mqttcert\_password**".

```js
    ssl:
      # Enable/disable SSL support
      enabled: "${MQTT_SSL_ENABLED:true}"
      # Server SSL credentials
      credentials:
        # Server credentials type (PEM - pem certificate file; KEYSTORE - java keystore)
        type: "${MQTT_SSL_CREDENTIALS_TYPE:KEYSTORE}"
        # Keystore server credentials
        keystore:
          # Type of the key store (JKS or PKCS12)
          type: "${MQTT_SSL_KEY_STORE_TYPE:PKCS12}"
          # Path to the key store that holds the SSL certificate
          store_file: "${MQTT_SSL_KEY_STORE:mqttserver.p12}"
          # Password used to access the key store
          store_password: "${MQTT_SSL_KEY_STORE_PASSWORD:thingsboard_mqttcert_password}"
          # Optional alias of the private key; If not set, the platform will load the first private key from the keystore;
          #key_alias: "${MQTT_SSL_KEY_ALIAS:}"
          # Optional password to access the private key. If not set, the platform will attempt to load the private keys that are not protected with the password;
          key_password: "${MQTT_SSL_KEY_PASSWORD:thingsboard_mqttcert_password}"
```

:::info
Leave the rest of the settings at default value. Do not delete/change lines that are not shown in the examples above unless you know what you are doing.
:::

Apply the changes to the "**thingsboard.yml**" file (re-save it after editing).

### Upload altered ThingsBoard configuration file

All that is left is to overwrite the current configuration file with an altered file and upload both certificates.

Once again, make sure your terminal is pointing to the right folder (where 3 files are located → both certificates and an altered "thingsboard.yml" file), and, from there, SFTP into the container's configuration file directory:

```powershell
c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp> cd ThingsBoard/usr/share/thingsboard/conf
sftp> dir
banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

Upload these files with the help of the `put` command:

```powershell
sftp> put thingsboard.yml
Uploading thingsboard.yml to /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml
thingsboard.yml                                                                       100%   67KB   2.2MB/s   00:00
sftp> put keystore.p12
Uploading keystore.p12 to /ThingsBoard/usr/share/thingsboard/conf/keystore.p12
keystore.p12                                                                          100% 2448     1.2MB/s   00:00
sftp> put mqttserver.p12
Uploading mqttserver.p12 to /ThingsBoard/usr/share/thingsboard/conf/mqttserver.p12
mqttserver.p12                                                                        100% 2434   608.5KB/s   00:00
sftp> dir
banner.txt          i18n                keystore.p12        logback.xml         mqttserver.p12      templates           
thingsboard.conf    thingsboard.yml
```

Restart the container:

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

Make sure to wait for the container to stop (`status=stopped` should be shown after using `/container/print` command) before initiating it again.

### Confirm HTTPS access

Now, you should be able to access [https://your\_IP:9090](https://192.168.88.1) (where the IP address is the address used in the DNAT rule):

![](./img/container-thingsboard-mqtt-http-server-06.webp)

:::info
Since we are using a self-signed certificate that was not issued by a trusted authority, an error indicating that the connection is not secure might appear but you can view the certificate through the browser (confirm it is the one), accept the risk, and continue.
:::

### Confirm SSL MQTT connection

:::info
**Do not forget to alter the port forwarding rule** that is shown in the "Networking" section by changing **`dst-port`** and **`to-ports`** from 1883 (standard non-SSL MQTT port) **to 8883** (**SSL MQTT port**).
:::

In this example, we will test a [one-way SSL communication access token scenario](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario).

#### Testing with the device that is running the container

:::info
The MQTT certificate should already be installed into the device's system (because it is the device that generated it).
:::

Add MQTT broker:

```ros
/iot/mqtt/brokers/add name=tbssl address=172.18.0.2 port=8883 username=YOUR_TOKEN ssl=yes
```

Publish a static test MQTT message in the JSON format:

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

Confirm that it was received by the MQTT broker:

![](./img/container-thingsboard-mqtt-http-server-07.webp)

#### Testing with another device

When you have two RouterOS devices, one that is running the container (and, in our example, is the same device that generated the certificate) and the other one that you wish to test the MQTT connection from (let's say, an [LTAP](https://mikrotik.com/product/ltap) or any other RouterOS device with IoT package installed) → you will need to import the certificate to the second device.

Drag and drop the exported certificate (**mqttserver.p12**) into the device's "File List":

```ros
[admin@LTAP] > /file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE  CREATION-TIME       
0  mqttserver.p12  .p12 file  2438  2023-01-30 13:28:11
1  flash           disk             2021-07-06 14:51:53
2  flash/pub       directory        2021-07-06 14:51:53
3  flash/skins     directory        1970-01-01 02:00:07
[admin@LTAP] > 
```

Import the certificate:

```ros
[admin@LTAP] > /certificate/import file-name=mqttserver.p12 passphrase=thingsboard_mqttcert_password
```

Add MQTT broker, where the address is the IP address `dst-address` that is used in the TCP 8883 port-forwarding rule on the ThingsBoard-container router:

```ros
/iot/mqtt/brokers/add name=tbssl address=192.168.88.1 port=8883 username=YOUR_TOKEN ssl=yes
```

Publish a static test MQTT message in the JSON format:

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

And confirm that the broker received it → under the "Latest Telemetry" section on ThingsBoard.
