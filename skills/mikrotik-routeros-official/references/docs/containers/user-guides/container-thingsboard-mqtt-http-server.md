# Container - ThingsBoard MQTT/HTTP server

> Run the ThingsBoard IoT platform in a RouterOS container, send data to it from RouterOS with MQTT, and enable HTTPS and MQTT over TLS with a certificate made on the router.

# Container - ThingsBoard MQTT/HTTP server

## Introduction

With containers, RouterOS can run servers that would otherwise need a separate device or machine on your network.

Many users need a server that collects data, stores it and shows it in a way that is easy to understand. [ThingsBoard](https://thingsboard.io/) is such a platform. It is positioned as an IoT platform; see its [use cases](https://thingsboard.io/iot-use-cases/).

For RouterOS, ThingsBoard works as an MQTT broker and as an HTTP server: RouterOS can send data to it with [MQTT publish](../../internet-of-things/mqtt/index.md) or with an [HTTP POST](../../system-information-and-utilities/fetch.md). See the ThingsBoard [MQTT API](https://thingsboard.io/docs/reference/mqtt-api/) and [HTTP API](https://thingsboard.io/docs/reference/http-api/).

With [scripting](../../developer-guides/scripting/index.md), you can collect RouterOS statistics (uptime, GPS coordinates, packet counters and almost anything that you can print in the terminal), build a JSON message from them, and send it to ThingsBoard from the [scheduler](../../system-information-and-utilities/scheduler.md). See [MQTT and ThingsBoard configuration](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md) for an example script. ThingsBoard stores the data and shows it in dashboards with [widgets](https://thingsboard.io/docs/user-guide/ui/widget-library/): graphs, tables, maps and more.

ThingsBoard provides single-instance images with different databases, for example:

- [thingsboard/tb-postgres](https://hub.docker.com/r/thingsboard/tb-postgres/) - With PostgreSQL.
- [thingsboard/tb-cassandra](https://hub.docker.com/r/thingsboard/tb-cassandra/) - With Cassandra.

This guide uses **tb-postgres**, a single instance of ThingsBoard with a PostgreSQL database, with the `in-memory` queue. This is a setup for testing; for production, see the queue options in the [ThingsBoard Docker installation guide](https://thingsboard.io/docs/user-guide/install/docker/).

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode. The MQTT test needs the `iot` package.

The tb-postgres image is available for ARM64 and AMD64 (CHR and x86) only; check its [tags](https://hub.docker.com/r/thingsboard/tb-postgres/tags) for the current list.

ThingsBoard is a server that needs more resources than most containers:

- **Disk** - the image takes about 1 GB to download and about 1.1 GB after extraction, and the database grows with the data that you store. This example uses an external disk, `disk1`; plan a reserve, especially if you run more containers.
- **RAM** - the ThingsBoard documentation recommends at least 1 GB of RAM for a single instance with PostgreSQL and a light load (a few messages per second), and 2-4 GB for more. ThingsBoard alone, without load, uses about 750 MB; on a router with 1 GB of RAM, little memory is left for RouterOS and other services, so use a device with more RAM. See [Memory](../#memory) for how to limit the memory that a container uses.

## Configuration

### Networking

Add a veth interface for the container:

```routeros
/interface/veth/add name=veth5 address=172.22.0.2/24 gateway=172.22.0.1
```

Create a bridge for the container, give it an address, and add the veth interface to it:

```routeros
/interface/bridge/add name=thingsboard
/ip/address/add address=172.22.0.1/24 interface=thingsboard
/interface/bridge/port/add bridge=thingsboard interface=veth5
```

Add NAT for the container's outgoing traffic:

```routeros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.22.0.0/24
```

Devices in the router's LAN can reach the container at `172.22.0.2`. To use the router's LAN address instead (`192.168.88.1` in this example), forward the ThingsBoard ports to the container: TCP 9090 for the web interface and TCP 1883 for MQTT.

```routeros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=9090 \
    protocol=tcp to-addresses=172.22.0.2 to-ports=9090
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 \
    protocol=tcp to-addresses=172.22.0.2 to-ports=1883
```

:::warning

Plain HTTP (port 9090) and MQTT without TLS (port 1883) send passwords, access tokens and data unencrypted: anyone who can capture the traffic can read them. Use them only for testing in a local network or through a VPN.

Set everything up with local addresses first and confirm that it works. Before you allow access from the internet:

- Change the passwords of the default ThingsBoard users, or remove the users (see the ThingsBoard documentation), and remove the demo devices.
- Enable HTTPS and MQTT over TLS (see [HTTPS and MQTT over TLS](#https-and-mqtt-over-tls)).
- In the dst-nat rules, use the public address in `dst-address`, the TLS ports, and `src-address` or `src-address-list` to allow only trusted addresses, for example your branch office.

You are responsible for the security of the server. Opening a port to the internet without these steps lets anyone try to use it.

:::

### Environment variables and mounts

Check the [tb-postgres](https://hub.docker.com/r/thingsboard/tb-postgres) documentation for the mounts and variables that the image uses.

Set the queue type:

```routeros
/container/envs/add list=tb_envs key=TB_QUEUE_TYPE value="in-memory"
```

Mount folders for the data (including the database) and for the logs:

```routeros
/container/mounts/add list=mytb-data src=disk1/tb/mytb-data dst=/data
/container/mounts/add list=mytb-logs src=disk1/tb/mytb-logs dst=/var/log/thingsboard
```

### Image

This example downloads the image from Docker Hub (see [Registry](../#registry)); you can also import it from a [.tar](../#option-b-import-image-from-pc) file. Set the directory where the downloaded image is extracted:

```routeros
/container/config/set tmpdir=disk1/pull
```

Add the container:

```routeros
/container/add remote-image=thingsboard/tb-postgres:latest interface=veth5 \
    root-dir=disk1/thingsboard mountlists=mytb-data,mytb-logs envlists=tb_envs \
    logging=yes name=thingsboard
```

RouterOS downloads and extracts the image. Check the progress with `/container/print`; when the extraction is done, the container status is `stopped`.

### Start the container

```routeros
/container/start [find where name=thingsboard]
```

On the first start, ThingsBoard creates its database and loads the system data, which takes several minutes, longer on slower devices. The following starts are faster. The web interface answers when the log shows that the server has started (`/log/print where topics~"container"`):

```text
2026-11-24 11:37:09 container,info,debug thingsboard: 2026-11-24 11:37:09,177 [main] INFO  o.t.s.ThingsboardServerApplication - Started ThingsboardServerApplication in 38.581 seconds (process running for 40.201)
```

## Verification

### Management access

Open the web interface in a browser: from the LAN at `http://172.22.0.2:9090`, or at `http://192.168.88.1:9090` through the dst-nat rule:

![ThingsBoard login page](./img/container-thingsboard-mqtt-http-server-01.webp)

The default users (user name / password) are:

- **System Administrator**: `sysadmin@thingsboard.org` / `sysadmin`
- **Tenant Administrator**: `tenant@thingsboard.org` / `tenant`

Change their passwords before you use the server for anything other than testing.

### MQTT test

Log in as the tenant administrator and create a device. In the **Devices** menu, select **+** (Add device) and choose **Add new device**:

![ThingsBoard Devices menu](./img/container-thingsboard-mqtt-http-server-02.webp)

Name it and select **Add**:

![ThingsBoard Add device dialog](./img/container-thingsboard-mqtt-http-server-03.webp)

Select the new device and open **Manage credentials**. Copy the access token, or enter your own; this example uses `YOUR_TOKEN`:

![ThingsBoard device credentials](./img/container-thingsboard-mqtt-http-server-04.webp)

On the router, add ThingsBoard as an [MQTT broker](../../internet-of-things/mqtt/index.md), with the access token as the user name:

```routeros
/iot/mqtt/brokers/add name=tb address=172.22.0.2 port=1883 username=YOUR_TOKEN
```

Publish a test message in JSON format:

```routeros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

The device's **Latest telemetry** tab shows the value:

![ThingsBoard Latest telemetry tab](./img/container-thingsboard-mqtt-http-server-05.webp)

## HTTPS and MQTT over TLS

By default, ThingsBoard uses HTTP and MQTT without TLS. As explained in [Networking](#networking), this is safe only in a protected network, so enable HTTPS and MQTT over TLS. See the ThingsBoard guides [HTTP over SSL](https://thingsboard.io/docs/user-guide/ssl/http-over-ssl/) and [MQTT over SSL](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) for all options.

TLS needs a certificate. This example makes a self-signed [certificate](../../authentication-authorization-accounting/certificates.md) on the router; you can also use a certificate from a certificate authority, or one made with OpenSSL or other tools. ThingsBoard reads the certificate and its key from PEM files, which this example passes to the container through a mount and environment variables. The settings are kept in the container configuration, so they stay when you update the image.

### Create the certificate

Create a certificate for the addresses that clients use to connect: the router's LAN address and the container address. One certificate serves both HTTPS and MQTT:

```routeros
/certificate/add name=thingsboard common-name=thingsboard \
    subject-alt-name=IP:192.168.88.1,IP:172.22.0.2 days-valid=3650
/certificate/sign thingsboard
```

Create a folder for the files and export the certificate and its key there. RouterOS exports a private key only with a passphrase:

```routeros
/file/add name=disk1/tb/ssl type=directory
/certificate/export-certificate thingsboard type=pem \
    export-passphrase="Example-key-pass-1" file-name=disk1/tb/ssl/thingsboard
```

This creates `disk1/tb/ssl/thingsboard.crt` and `disk1/tb/ssl/thingsboard.key`. Use your own passphrase.

ThingsBoard cannot read the encrypted key that RouterOS exports, also not with `SSL_PEM_KEY_PASSWORD`, and Java cannot read the RouterOS PKCS#12 export as a keystore. Remove the passphrase on a PC with OpenSSL instead. Download `thingsboard.key` with SFTP (the SSH [service](../../system-information-and-utilities/services.md) must be enabled), then run the following and enter the passphrase:

```shell
openssl pkey -in thingsboard.key -out thingsboard-key.pem
```

Upload `thingsboard-key.pem` to `disk1/tb/ssl`:

```shell
sftp admin@192.168.88.1
sftp> put thingsboard-key.pem disk1/tb/ssl/thingsboard-key.pem
sftp> exit
```

The key in `thingsboard-key.pem` is not encrypted: anyone who can read the router's files can copy it. Keep access to the router's files limited to administrators.

### Configure ThingsBoard

Mount the folder in the container:

```routeros
/container/mounts/add list=mytb-ssl src=disk1/tb/ssl dst=/ssl
```

Add the TLS settings to the container's environment variables:

```routeros
/container/envs/add list=tb_envs key=SSL_ENABLED value="true"
/container/envs/add list=tb_envs key=SSL_PEM_CERT value="/ssl/thingsboard.crt"
/container/envs/add list=tb_envs key=SSL_PEM_KEY value="/ssl/thingsboard-key.pem"
/container/envs/add list=tb_envs key=MQTT_SSL_ENABLED value="true"
/container/envs/add list=tb_envs key=MQTT_SSL_PEM_CERT value="/ssl/thingsboard.crt"
/container/envs/add list=tb_envs key=MQTT_SSL_PEM_KEY value="/ssl/thingsboard-key.pem"
```

- `SSL_*` - HTTPS for the web interface, on the same port, 9090.
- `MQTT_SSL_*` - MQTT over TLS on port 8883. MQTT without TLS on port 1883 stays available; to turn it off, see `MQTT_ENABLED` in the ThingsBoard documentation.

Stop the container, add the mount, and start it again:

```routeros
/container/stop [find where name=thingsboard]
/container/set [find where name=thingsboard] mountlists=mytb-data,mytb-logs,mytb-ssl
/container/start [find where name=thingsboard]
```

If ThingsBoard cannot load the certificate or the key, the container stops, and the log shows the reason, for example `Unable to load private key`.

### Confirm HTTPS access

Open `https://192.168.88.1:9090` (the address from the dst-nat rule) in a browser:

![ThingsBoard login page over HTTPS](./img/container-thingsboard-mqtt-http-server-06.webp)

:::info

The certificate is self-signed and not issued by a trusted authority, so the browser warns that the connection is not secure. View the certificate in the browser, check that it is the one you made, accept the risk and continue.

:::

### Confirm MQTT over TLS

MQTT over TLS uses port 8883. To use it at the router's LAN address, change `dst-port` and `to-ports` of the MQTT forwarding rule from [Networking](#networking) from 1883 to 8883.

This example tests a [one-way SSL communication with an access token](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario).

#### From the router that runs the container

The router that made the certificate already trusts it. Add a broker with TLS:

```routeros
/iot/mqtt/brokers/add name=tbssl address=172.22.0.2 port=8883 username=YOUR_TOKEN ssl=yes
```

Publish a test message:

```routeros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

The device's **Latest telemetry** tab shows the value:

![ThingsBoard Latest telemetry tab after MQTT over TLS](./img/container-thingsboard-mqtt-http-server-07.webp)

#### From another device

Another RouterOS device, for example an [LtAP](https://mikrotik.com/product/ltap) with the `iot` package, must trust the certificate before it connects. Without it, the connection fails, and the log on that device shows `ssl failure [ssl: no trusted CA certificate found]`.

On the router that runs the container, export the certificate without its key (no passphrase):

```routeros
/certificate/export-certificate thingsboard type=pem file-name=thingsboard-cert
```

Copy `thingsboard-cert.crt` to the other device (for example, drag and drop it in WinBox **Files**), and import it there:

```routeros
/certificate/import file-name=thingsboard-cert.crt passphrase=""
```

Do not copy the key to other devices: clients need only the certificate.

Add the broker with the router's address from the 8883 forwarding rule, and publish a test message:

```routeros
/iot/mqtt/brokers/add name=tbssl address=192.168.88.1 port=8883 username=YOUR_TOKEN ssl=yes
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

The value appears in the device's **Latest telemetry** tab in ThingsBoard.

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/config`](../../cli-reference/container/config), [`/container/mounts`](../../cli-reference/container/mounts), [`/container/envs`](../../cli-reference/container/envs), [`/certificate`](../../cli-reference/certificate/certificate.md), [`/iot/mqtt/brokers`](../../cli-reference/iot/mqtt/brokers) and [`/iot/mqtt/publish`](../../cli-reference/iot/mqtt/publish).
