# Container - mosquitto MQTT server

> This page introduces using MikroTik RouterOS containers to run an eclipse-mosquitto MQTT server for IoT applications, detailing container setup steps including networking, environment variables, and mounts with SSL...

# Container - mosquitto MQTT server

## Introduction

With containers, RouterOS can run servers that would otherwise need a separate device or machine on your network.

This guide shows how to run the [eclipse-mosquitto](https://mosquitto.org/) MQTT broker in a container. MQTT is a lightweight publish-subscribe protocol, an OASIS and ISO standard, widely used in IoT networks. A typical setup has publishers (devices that send messages), a broker (the server that receives the messages and passes them on), and subscribers (devices that receive the messages for the topics they subscribed to).

RouterOS can [publish and subscribe](../../internet-of-things/mqtt/index.md) over MQTT itself; with a container, the router can also run the broker. The guide uses this to test the broker from the router.

The image is [eclipse-mosquitto on Docker Hub](https://hub.docker.com/_/eclipse-mosquitto). Check its [tags](https://hub.docker.com/_/eclipse-mosquitto/tags) for the architectures it is available for.

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode.

The example uses the router's own storage. The mosquitto image is small, so a device with 128 MB of storage, such as the [RB1100AHx4](https://mikrotik.com/product/rb1100ahx4), has room for it.

:::warning

This guide shows **a very basic** configuration. See the [mosquitto documentation](https://mosquitto.org/documentation/) for other options and settings. Before using the broker in production, **harden its security**:

- Use the [firewall](../../cli-reference/ip/firewall/filter/filter.md) to allow access to the container only from trusted addresses.
- Configure the broker with strong passwords and without anonymous access.
- Use MQTT over TLS, as shown in the SSL MQTT section.

:::

## Container configuration

### Networking

Add a veth interface for the container:

```routeros
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```

Create a bridge for the container and add the veth interface to it:

```routeros
/interface/bridge/add name=msqt
/ip/address/add address=172.19.0.1/24 interface=msqt
/interface/bridge/port/add bridge=msqt interface=veth2
```

Optionally, to reach the broker through the router's LAN address (192.168.88.1 in this example) on the non-TLS port 1883, forward that port to the container:

```routeros
/ip/firewall/nat/add action=dst-nat chain=dstnat \
    dst-address=192.168.88.1 dst-port=1883 protocol=tcp \
    to-addresses=172.19.0.2 to-ports=1883
```

### Mount

The broker reads its configuration from `/mosquitto/config/mosquitto.conf`. Mount the whole folder, not only the file, so that you can also put the TLS certificates there later:

```routeros
/container/mounts/add list=msqt_config src=/mosquitto_mounted \
    dst=/mosquitto/config
```

### Image

This example downloads the image from Docker Hub (see [Registry](../#registry)); you can also import it from a [.tar](../#option-b-import-image-from-pc) file. Set the directory where the downloaded image is extracted:

```routeros
/container/config/set tmpdir=pull
```

Add the container:

```routeros
/container/add remote-image=library/eclipse-mosquitto:latest \
    interface=veth2 root-dir=mosquitto mountlists=msqt_config \
    logging=yes name=mosquitto
```

RouterOS downloads and extracts the image. Check the progress with `/container/print`; when the extraction is done, the container status is `stopped`.

### Start the container

```routeros
/container/start [find where name=mosquitto]
```

On the first start, RouterOS creates the `mosquitto_mounted` folder and copies the image's default `mosquitto.conf` into it. With container logging enabled, the [log](../../diagnostics-monitoring-and-troubleshooting/log/index.md) shows the broker start (`/log/print where topics~"container"`, some lines left out):

```text
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: mosquitto version 2.1.4 starting
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: Config loaded from /mosquitto/config/mosquitto.conf.
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: Opening ipv4 listen socket on port 1883.
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: Opening ipv6 listen socket on port 1883.
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: Opening http api listen socket on port 9883.
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: Using http_dir /usr/share/mosquitto/dashboard/
 2026-11-23 14:49:51 container,info,debug mosquitto: 1795445391: mosquitto version 2.1.4 running
```

This default file comes with the image. To control what the broker listens on, replace it with your own, as shown next.

### Mosquitto configuration file

The configuration file is in the mounted folder, `mosquitto_mounted/mosquitto.conf`. Download it with SFTP or FTP (the SSH or FTP [service](../../system-information-and-utilities/services.md) must be enabled), edit it, and upload it back.

:::warning

This section configures a basic MQTT setup without TLS, for testing. MQTT without TLS is not secure in production unless other restrictions are in place: anyone who can capture the traffic can read the messages and the credentials. Where the MQTT traffic can be captured or is routed over the internet, use TLS as shown in the SSL MQTT section.

:::

For a basic test setup, replace the content of `mosquitto.conf` with these two lines:

```text
listener 1883
allow_anonymous true
```

- `listener 1883` - the broker listens for connections on port 1883.
- `allow_anonymous true` - clients that connect without a user name are allowed.

Upload the file into the mounted folder, for example with SFTP from the folder where you edited it:

```shell
sftp admin@192.168.88.1
sftp> cd mosquitto_mounted
sftp> put mosquitto.conf
sftp> exit
```

Restart the container to load the new configuration:

```routeros
/container/restart [find where name=mosquitto]
```

:::note

Changing any setting of a running container with `/container/set`, even its name or comment, also restarts it.

:::

## MQTT publish and subscribe

To test the broker from the router, use the [MQTT](../../internet-of-things/mqtt/index.md) client of RouterOS. It needs the `iot` package.

Add the broker:

```routeros
/iot/mqtt/brokers/add name=mosquitto username=test address=172.19.0.2
```

Subscribe to a topic:

```routeros
/iot/mqtt/subscribe broker=mosquitto topic=test/topic
```

Publish a message to the topic:

```routeros
/iot/mqtt/publish broker="mosquitto" topic="test/topic" \
    message="{\"test\":\"123\"}"
```

Check the received messages:

```routeros
/iot/mqtt/subscriptions/recv/print
```

```text
0  broker=mosquitto topic="test/topic" data="{"test":"123"}"
   time=2026-11-23 14:54:29
```

The container log shows the router's connection:

```text
 2026-11-23 14:54:26 container,info,debug mosquitto: 1795445666: New connection from 172.19.0.1:50554 on port 1883.
 2026-11-23 14:54:26 container,info,debug mosquitto: 1795445666: New client connected from 172.19.0.1:50554 as MT (p4, c1, k60, u'test').
```

## SSL MQTT

Using MQTT without TLS in production **is not secure**: anyone who can [capture](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) the traffic between the broker and its clients can read the credentials and the messages.

The first step is to create the certificates. This example uses a simple root CA setup, without client certificates. Follow the official [mosquitto-tls guide](https://mosquitto.org/man/mosquitto-tls-7.html) to create:

- `ca.crt` - the certificate of the certificate authority (CA);
- `server.crt` - the broker's certificate, signed by the CA;
- `server.key` - the broker's private key.

### Server configuration

Replace the content of `mosquitto.conf` with these lines:

```text
listener 8883
tls_version tlsv1.2
allow_anonymous true
cafile /mosquitto/config/ca.crt
keyfile /mosquitto/config/server.key
certfile /mosquitto/config/server.crt
```

- `listener 8883` - the broker listens for connections on port 8883. The `listener` line must come before the TLS options, which apply to it; otherwise, the broker does not start and logs `Error: The 'tls_version' option requires a listener to be defined first.`
- `tls_version tlsv1.2` - the minimum TLS version.
- `allow_anonymous true` - clients that connect without a user name are allowed.
- `cafile`, `keyfile`, `certfile` - the paths to the CA certificate, the server key and the server certificate, as the container sees the mounted folder.

:::warning

This is a basic TLS configuration for testing. `allow_anonymous true` is not a secure setting in production.

:::

Upload the certificate files and the new `mosquitto.conf` into the mounted folder:

```shell
sftp admin@192.168.88.1
sftp> cd mosquitto_mounted
sftp> put ca.crt
sftp> put server.crt
sftp> put server.key
sftp> put mosquitto.conf
sftp> exit
```

Restart the container:

```routeros
/container/restart [find where name=mosquitto]
```

The log confirms that the broker listens on port 8883:

```text
 2026-11-23 14:51:58 container,info,debug mosquitto: 1795445518: Config loaded from /mosquitto/config/mosquitto.conf.
 2026-11-23 14:51:58 container,info,debug mosquitto: 1795445518: Opening ipv4 listen socket on port 8883.
 2026-11-23 14:51:58 container,info,debug mosquitto: 1795445518: Opening ipv6 listen socket on port 8883.
 2026-11-23 14:51:59 container,info,debug mosquitto: 1795445518: mosquitto version 2.1.4 running
```

### Test the TLS connection

The router must trust the CA that signed the broker's certificate. Upload `ca.crt` to the router's file list (for example, with `put ca.crt` in the root folder over SFTP), and import it:

```routeros
/certificate/import file-name=ca.crt passphrase=""
```

Add the broker for the TLS connection:

```routeros
/iot/mqtt/brokers/add name=mosquittoSSL username=test \
    address=172.19.0.2 port=8883 ssl=yes
```

Subscribe to the topic:

```routeros
/iot/mqtt/subscribe broker=mosquittoSSL topic=test/topic
```

Publish a message:

```routeros
/iot/mqtt/publish broker="mosquittoSSL" topic="test/topic" \
    message="{\"test\":\"456\"}"
```

Check the received messages:

```routeros
/iot/mqtt/subscriptions/recv/print
```

```text
0  broker=mosquittoSSL topic="test/topic" data="{"test":"456"}"
   time=2026-11-23 14:52:31
```

The container log shows the TLS session:

```text
 2026-11-23 14:52:28 container,info,debug mosquitto: 1795445548: Client MT negotiated TLSv1.2 cipher ECDHE-RSA-AES256-GCM-SHA384
```

If the router does not trust the CA, the connection fails, and the router logs:

```text
 2026-11-23 14:52:20 mqtt,error ssl failure [ssl: no trusted CA certificate found]
```

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/mounts`](../../cli-reference/container/mounts) and [`/container/config`](../../cli-reference/container/config).
