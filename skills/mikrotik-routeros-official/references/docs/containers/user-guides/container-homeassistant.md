# Container - HomeAssistant

> Run Home Assistant in a RouterOS container: network, configuration mount, time zone, image download, first start and resource use.

# Container - HomeAssistant

## Introduction

With containers, RouterOS can run servers that would otherwise need a separate device or machine on your network.

[Home Assistant](https://www.home-assistant.io/) is a home automation platform: it collects data from sensors and controls devices through a large number of integrations. This guide runs Home Assistant in a container on the router and opens its web interface.

The image is [homeassistant/home-assistant on Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant). Check its [tags](https://hub.docker.com/r/homeassistant/home-assistant/tags) for the architectures it is available for; at the time of writing, these are ARM64 and AMD64 (CHR and x86).

## Summary

Read the [container](../) guide first, especially the [disclaimer](../#disclaimer) and the [requirements](../#requirements): the `container` package must be installed and containers enabled in device-mode.

Home Assistant needs more resources than most containers. The image takes about 650 MiB to download and about 2.3 GiB after extraction; keep about 3 GB free on the disk for the installation. This example extracts it to an external disk, `disk1`. When it runs without integrations, it uses about 500 MB of RAM (see [Resources](#resources)).

## Container configuration

### Networking

Add a veth interface for the container:

```routeros
/interface/veth/add name=veth4 address=172.21.0.2/24 gateway=172.21.0.1
```

Create a bridge for the container, give it an address, and add the veth interface to it:

```routeros
/interface/bridge/add name=ha
/ip/address/add address=172.21.0.1/24 interface=ha
/interface/bridge/port/add bridge=ha interface=veth4
```

Home Assistant uses internet services, for example to check for alerts. Add NAT for its outgoing traffic:

```routeros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.21.0.0/24
```

Without this rule, Home Assistant still starts and serves its web interface, but the log shows errors such as `Cannot connect to host alerts.home-assistant.io:443`.

### Configuration mount and time zone

Home Assistant keeps its configuration in the `/config` folder. Mount a folder on the disk there, so that the configuration is kept when the container is removed or updated:

```routeros
/container/mounts/add list=ha_config src=disk1/ha_config dst=/config
```

Set the time zone with the `TZ` environment variable; use your own [time zone name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones):

```routeros
/container/envs/add list=ha_env key=TZ value=America/Los_Angeles
```

### Image

This example downloads the image from Docker Hub (see [Registry](../#registry)); you can also import it from a [.tar](../#option-b-import-image-from-pc) file. Set the directory where the downloaded image is extracted:

```routeros
/container/config/set tmpdir=disk1/pull
```

Add the container:

```routeros
/container/add remote-image=homeassistant/home-assistant:latest \
    interface=veth4 root-dir=disk1/ha mountlists=ha_config \
    envlists=ha_env logging=yes name=homeassistant
```

RouterOS downloads and extracts the image, which takes several minutes. Check the progress with `/container/print`; when the extraction is done, the container status is `stopped`.

### Start the container

```routeros
/container/start [find where name=homeassistant]
```

On the first start, Home Assistant creates its configuration files in `disk1/ha_config`. It takes a few minutes before the web interface answers.

## Home Assistant setup

Open the web interface in a browser at `http://172.21.0.2:8123`. Devices in the router's LAN reach the container network through the router.

To open it at the router's LAN address instead, forward TCP port 8123 to the container (`192.168.88.1` is the router's LAN address):

```routeros
/ip/firewall/nat/add chain=dstnat action=dst-nat dst-address=192.168.88.1 \
    dst-port=8123 protocol=tcp to-addresses=172.21.0.2 to-ports=8123
```

Then open `http://192.168.88.1:8123`.

The first page starts the onboarding:

![Home Assistant onboarding page](./img/container-homeassistant-01.webp)

Create the owner account and continue as described in the [Home Assistant onboarding guide](https://www.home-assistant.io/getting-started/onboarding/).

## Resources

The [Home Assistant website](https://www.home-assistant.io/installation/linux/) lists 2 GB of RAM and two CPU cores as the minimum for running Home Assistant in a virtual machine. In a container, Home Assistant without integrations uses about 500 MB of RAM. Check the container's memory use with `/container/print`:

```routeros
/container/print proplist=name,memory-current,container-size where name=homeassistant
```

```text
Flags: R - RUNNING
Columns: NAME, MEMORY-CURRENT, CONTAINER-SIZE
#   NAME           MEMORY-CURRENT  CONTAINER-SIZE
0 R homeassistant  478.2MiB        2318.3MiB     
```

To limit the container's memory, set `memory-high` or `memory-max` (see [Memory](../#memory)).

For the commands used in this guide, see [`/container`](../../cli-reference/container/container.md), [`/container/config`](../../cli-reference/container/config), [`/container/mounts`](../../cli-reference/container/mounts) and [`/container/envs`](../../cli-reference/container/envs).
