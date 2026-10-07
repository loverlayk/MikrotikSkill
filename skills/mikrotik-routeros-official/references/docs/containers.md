# Container

> This page documents MikroTik RouterOS container support, covering configuration, virtual interfaces, storage, and security considerations. It details properties like restart intervals, DNS settings, CPU allocation,...

# Container

This section covers RouterOS container support, including container configuration, virtual Ethernet interfaces, storage, and application examples. Use it to run supported containerized services on RouterOS devices.

<DocCardList />

**Packages required:** `container`

A container is MikroTik's implementation of Linux containers, allowing users to run containerized environments within RouterOS. The container feature works in the latest MikroTik RouterOS v7.x version. Containers are compatible with images from Docker Hub, GCR, Quay, or other providers, as well as those built on other devices, using the same formats supported by these providers. While RouterOS uses different syntax compared to Docker, it still achieves similar functionality.

## Disclaimer

:::danger
You need physical access to your RouterOS device to enable support for the container feature; it is disabled by default;

- once the container feature is enabled, containers can be added/configured/started/stopped/removed remotely!
- if your RouterOS device is compromised, containers can be used to easily install malicious software in your RouterOS device and over the network;
- your RouterOS device is as secure as anything you run in a container;
- if you run a container, there is no security guarantee of any kind;
- running a 3rd party container image on your RouterOS device could open a security hole/attack vector/attack surface;
- an expert with knowledge of how to build exploits will be able to jailbreak/elevate to root;

:::

### Security risks

- When a security expert publishes his exploit research - anyone can apply such an exploit.
- Someone can build a container image that can use the exploit AND provide a Linux root shell.
- By using a root shell someone may leave a permanent backdoor/vulnerability in your RouterOS system even after the container image is removed and the container feature is disabled.
- If a vulnerability is injected into the primary or secondary RouterBOOT (or vendor pre-loader), then even Netinstall may not be able to fix it.

## Requirements

Container package is compatible with **arm, arm64** and **x86** architectures. Use of remote-image (similar to docker pull) functionality requires a lot of free space in main memory, 16MB SPI flash boards may use pre-built images on USB or other disk media.

:::danger

- An external disk supporting at least 100MB/s sequential read/write speed and 10K random iops is recommended. When using slower disks, container extraction times may become longer.
- The Container package needs to be installed
- For devices with EN7562CT CPU like the hEX Refresh, only [arm32v5](https://hub.docker.com/u/arm32v5) container images are supported, meaning a limited number of containers can be run.

:::

**Sub-menu:** `/container`

## Properties

| Property | Description |
| :-- | :-- |
| **restart-interval** (*string*; Default: ) | Specify an interval at which Container will be restarted on Container failure. Example: 10s |
| **cmd** (*string*; Default: ) | The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well. |
| **comment** (*string*; Default: ) | Short description |
| **dns** (*string*; Default: ) | If the container needs different DNS, it can be configured here |
| **domain-name** (*string*; Default: ) | Sets the container's domain name |
| **entrypoint** (*string*; Default: ) | An ENTRYPOINT allows you to specify an executable to run when starting the container. Example: `/bin/sh` |
| **envlist** (*string*; Default: ) | List of environmental variables (configured under *`/container/envs`* ) to be used with the container |
| **file** (*string*; Default: ) | A container \*tar.gz tarball if the container is imported from a file |
| **hostname** (*string*; Default: ) | Assigning a hostname to a container helps in identifying and managing the container more easily |
| **interface** (*string*; Default: ) | veth interface to be used with the container |
| **logging** (*string*; Default: ) | if set to yes, all container-generated output will be shown in the RouterOS log |
| **start-on-boot** (*string*; Default: ) | if set to yes, the container will be started automatically on device start-up. |
| **mountlists** (*string*; Default: ) | mounts from /container/mounts/ sub-menu to be used with this container |
| **mount** (*string*; Default: ) | specify a directory to be used as a mount |
| **remote-image** (*string*; Default: ) | the container image name to be installed if an external registry is used (configured under `/container/config/set` registry-url=...) |
| **root-dir** (*string*; Default: ) | used to save container store outside main memory |
| **stop-signal** (*string*; Default: 15) | defines which Linux signal is sent to terminate the container if it is still running after 10 seconds. Different signals may allow graceful shutdown, immediate termination, or trigger application-specific actions |
| **workdir** (*string*; Default: ) | the working directory for cmd entrypoint |
| **devices** (*string*; Default: ) | passes through a physical device to the container |
| **cpu-list** (*string*; Default: ) | specifies which CPU cores the container is allowed to run on |
| **user** (*string*; Default: ) | sets the user and group the container process runs as before execution. |
| **memory-high** (*int*; Default: ) | "Soft" RAM usage limit in bytes for a specific container. If  usage goes over the high boundary, the processes are throttled and put under reclaim pressure. |
| **memory-max** (*int*; Default: ) | Max RAM usage limit in bytes per container (The container process will be terminated if the memory-max value is smaller than the container memory-current) starting 7.23, this parameter cannot be set lower than 1MB, to avoid a situation where the container is terminated too early in the startup process |
| **swap-max** (*int*; Default: ) | Maximum amount of swap space (in bytes) that the container may use. Requires swap to be enabled on the device (see [Swap space](../hardware/disks/index.md)). |
| **stop-time** (*string*; Default: ) | Time limit for the container to stop gracefully before the stop-signal is sent. |
| **tmpfs** (*string*; Default: ) | Temporary filesystem mount points for the container. Format: `size@dir`, e.g., `64M@/tmp`. |
| **layer-dir** (*string*; Default: ) | Directory for storing container image layers, used for shared layer storage between containers. |
| **shm-size** (*int*; Default: ) | Size of the `/dev/shm` shared memory filesystem in bytes for the container. |
| **default-dns** (*string*; Default: ) | Default DNS servers inherited from the system `/ip/dns` configuration. |
| **hosts** (*string*; Default: ) | Custom hostname-to-IP address mappings for the container. Format: `host=ip`. |
| **restart-policy** (*string*; Default: ) | Defines the restart policy for the container: `no` (never restart), `on-failure` (restart only on non-zero exit code), or `always` (always restart). |
| **restart-max-count** (*int*; Default: ) | Maximum number of restart attempts allowed within the restart-interval time frame. |
| **stop-on-unhealthy** (*string*; Default: ) | If set to `yes`, the container will be automatically stopped when the healthcheck status becomes unhealthy. |

:::warning
By default the container uses the same DNS as configured in the `/ip/dns` sub-menu. If no DNS is configured here and the container's `dns` parameter is not specified, the container will not start!
:::

### Menu specific commands

| Property | Description |
| :-- | :-- |
| **update** | Updates the container image. Automatically pulls from container repository and extracts it, replacing the original image. |
| **kill** | Kills the specified running container. |
| **restart** | Restarts the specified running container. |
| **repull** | Re-pulls/extracts the container image. |
| **shell** | Enters the container shell of a running container. |
| **run** | Starts the container and enters its shell. Useful if container shuts down after running. |
| **save** | Saves the container image as a tar archive with root-dir content and ROS-specific parameters. See [Saving a container](#saving-a-container). |

## Container configuration

**Sub-menu:** `/container/config`

| Property | Description |
| :-- | :-- |
| **registry-url** | external registry url from where the container will be downloaded (default: `https://lscr.io/`) |
| **tmpdir** | container extraction directory |
| **layer-dir** | directory for storing container image layers, used for shared layer storage between containers |
| **memory-high** | Global "soft" RAM usage limit in bytes for a specific container. If  usage goes over the high boundary, the processes are throttled and put under reclaim pressure. |
| **memory-max** | Global max RAM usage limit in bytes per container (The container process will be terminated if the memory-max value is smaller than the container memory-current) starting 7.23, this parameter cannot be set lower than 1MB, to avoid a situation where the container is terminated too early in the startup process |
| **swap-max** (*int*; Default: ) | Global default for the maximum amount of swap space (in bytes) per container. Individual containers can override this with their own `swap-max` setting. Requires swap to be enabled on the device (see [Swap space](../hardware/disks/index.md)). |
| **username** | Specifies the username for authentication (starting from ROS 7.8) |
| **password** *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Specifies the password for authentication (starting from ROS 7.8) |

### Read-only properties

| Property | Description |
| :-- | :-- |
| **assumed-registry-url** | Automatically detected registry URL. |
| **memory-current** | Current total memory usage of all containers in bytes. |

## Saving a container

The **save** command under the `/container` menu writes the container image as a valid OCI archive which can be imported in podman, docker environments or RouterOS.

Save by default writes all filesystem layers including root-dir, but keeps does not include it in the OCI format. It writes a special ros-container.json within the tarball with additional information specified in RouterOS, including root-dir layer info, envlists etc. ros-container.json will be used when importing into ROS containers - in docker or podman it will be ignored.

Saving with the **commit** parameter will add root-dir layer to OCI archive format or change original image config. Importing image in podman or docker saved without **commit** will not show changes made in ROS container entry like specified environment values, entrypoints, files in root-dir and any other changes.

The root directory layer together with additional parameters specified in ROS container entry can be saved (commited) to OCI image for importing in podman or docker using the **commit** parameter.

### Command syntax

```routeros
/container/save <container> file=<archive> [name=<name>] [commit]
```

### Parameters

| Parameter | Description |
| :-- | :-- |
| **file** | Path to save archive as |
| **name** | Set image name to save as |
| **commit** | Commit changes to OCI archive |

### Save and re-import

This example shows how to save a container with root-dir content, remove it, and re-add it from the saved file.

For the example let's add a simple container:

```routeros
/container/add name=alpine remote-image=alpine interface=veth1 check-certificate=no
```

Modify the container:

```routeros
/container/run alpine
/ # apk add python3
...
/ # cat <<EOF > main.py
> import os
> import sys
> ...
> EOF
/ # exit
```

Set container entrypoint, cmd etc:

```routeros
/container/set alpine entrypoint="python main.py" cmd="foo bar" env=FOO=1,BAR=2 envlists=foo,bar
```

Run the modified container and verify env vars:

```routeros
/container/run 0
>>> os.environ
environ({'BAR': '2', 'BAR2': 'this is bar 2', 'EGGS': 'e33s', 'FOO': '1', 'HOME': '/root', 'HOSTNAME': 'CHR', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'SPAM': 'spam12', 'TERM': 'xterm', 'TZ': 'manual'})
>>> exit()
```

Save the container with root directory content (keep OCI image intact):

```routeros
/container/save 0 file=out.tar
```

This save action adds root-dir content to archive together with some ROS container parameters like env, envlists etc. This does not change original image config parameters.

Remove the container and add it back from the saved file:

```routeros
/container/remove 0
/container/add file=out.tar interface=veth1
```

Run the re-imported container and verify env vars again:

```routeros
/container/run 0
>>> os.environ
environ({'BAR': '2', 'BAR2': 'this is bar 2', 'EGGS': 'e33s', 'FOO': '1', 'HOME': '/root', 'HOSTNAME': 'CHR', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'SPAM': 'spam12', 'TERM': 'xterm', 'TZ': 'manual'})
>>> exit()
```

### Commit changes to OCI

Save the container image and *commit* changes to OCI image:

```routeros
/container/save 0 file=out.tar commit
```

Commited images adds root-dir content as another layer and sets entrypoint, cmd etc. values as standard container image parameters. This changed image can be loaded in podman or docker systems.

Loading the saved container in podman:

```shell
$ podman image load < out.tar
Getting image source signatures
Copying blob 2db82ee6251c done
Copying blob b1928d1de551 done
Copying config 3dc8d32889 done
Writing manifest to image destination
Loaded image: localhost/alpine:latest
```

Running the loaded image:

```shell
$ podman run -it --rm localhost/alpine:latest
>>> os.environ
environ({'BAR': '2', 'BAR2': 'this is bar 2', 'EGGS': 'e33s', 'FOO': '1', 'HOME': '/root', 'HOSTNAME': 'CHR', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'SPAM': 'spam12', 'TERM': 'xterm', 'TZ': 'manual'})
>>> exit()
```

## Examples

### Running Pi-hole

#### Prerequisites

   1. RouterOS device with RouterOS v7.4beta or later and **installed Container package -** [How to install packages](../getting-started/installation-and-upgrade/packages.md)
   2. Physical access to a device to enable container mode - will be explained down below
   3. Attached HDD, SSD or USB drive for storage - formatted with a filesystem supported by RouterOS - [How to format/manage disks](../hardware/disks/index.md)

#### Steps to run Pi-hole

1. Enable Container mode and follow the instructions the command gives you (read more about [Device-mode](../system-information-and-utilities/device-mode.md). You will need to confirm the device-mode with a press of the [reset button](../getting-started/configuration-management/routeros-configuration-reset.md), or a cold reboot (if using Containers on x86):  

   ```routeros
   /system/device-mode/update container=yes 
   ```

   :::danger
   [Device-mode](../system-information-and-utilities/device-mode.md) limits container use by default, before granting container mode access - make sure your device is fully secured.
   :::
2. Create a new veth interface and assign an IP address in a range that is unique in your network:  

   ```routeros
   /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
   ```

   :::info
   The following configuration is equivalent to "bridge" networking mode in other Container engines such as Docker. It is possible to create a "host" equivalent configuration as well.

   **Important:** One veth interface can be used for many Containers. You can create multiple veth interfaces to create [isolated](./index.md#isolated-containers) networks for different Containers.
   :::
3. Create a new [bridge](../bridging-and-switching/index.md) that is going to be used for your Containers and assign the same IP address that was used for the veth interface's gateway:  

   ```routeros
   /interface/bridge/add name=containers
   /ip/address/add address=172.17.0.1/24 interface=containers
   ```

4. Add the veth interface to your newly created bridge:  

   ```routeros
   /interface/bridge/port/add bridge=containers interface=veth1
   ```

5. Create a NAT for outgoing traffic:  

   ```routeros
   /ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
   ```

6. Create environment variables for the Container:  

   ```routeros
   /container/envs/add list=ENV_PIHOLE key=TZ value="Europe/Riga"
   /container/envs/add list=ENV_PIHOLE key=FTLCONF_webserver_api_password value="mysecurepassword"
   /container/envs/add list=ENV_PIHOLE key=DNSMASQ_USER value="root"
   ```

7. Create mounted volumes for the Container:  

   ```routeros
   /container/mounts/add list=MOUNT_PIHOLE_PIHOLE src=disk1/volumes/pihole/pihole dst=/etc/pihole
   /container/mounts/add list=MOUNT_PIHOLE_DNSMASQD src=disk1/volumes/pihole/dnsmasq.d dst=/etc/dnsmasq.d
   ```

   :::warning
   `src=`  points to RouterOS location (could also be `src=disk1/etc_pihole` if, for example, you decide to put configuration files on external USB media), `dst=` points to defined location (consult containers manual/wiki/github for information on where to point). If `src`  directory does not exist on first time use then it will be populated with whatever container has in `dst`  location.
   :::

   :::warning
   It is highly recommended to place any Container volume on an attached disk to your RouterOS device. Avoid placing Container volumes on the built-in storage.
   :::
8. Configure to use a specific Container repository, for example, to use Docker.io:  

   ```routeros
   /container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
   ```

9. Add a Container:  

   ```routeros
   /container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

   :::tip
   If you wish to see container output in `/log/print`  , then add `logging=yes`  when creating a Container, root-dir should point to an external drive. It's not recommended to use internal storage for Containers.

   **Important:** There are multiple ways you can get a Container image, check the [Adding a Container image](./index.md#adding-a-container-image) section if you need an alternative way of adding a Container image.

   **Important:** Adding a Container will start downloading or extracting it, the Container itself will not be started after it has been added, you need to start it manually for the first time after it has been downloaded/extracted.
   :::
10. Check the status of your Container and wait until downloading/extracting has been finished and the `status=stopped` :  

    ```routeros
    /container/print
    ```

11. Start the Container:  

    ```routeros
    /container/start pihole
    ```

12. Create a port forwarding for your Container:  

    ```ros
    /ip/firewall/nat
    add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
    ```

13. You should be able to access the Pi-hole web panel by navigating to `http://192.168.88.1/admin/`  in your web browser.
14. To start using Pi-hole on your devices, change their DNS configuration to use `192.168.88.1` as your DNS server.

### Adding a Container image

There are multiple ways you can get a Container image running on your RouterOS device. Check the examples below.

#### Option A: Get an image from an external library

Set registry-url (for downloading containers from the Docker registry)  and set extract directory (tmpdir) to the attached USB media:

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
```

pull an image:

```ros
/container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

The image will be automatically pulled and extracted to root-dir. Status can be checked by using

```ros
/container/print
```

#### Option B: Import image from PC

You can use your PC running either Docker or Podman to download your required container image and save it to an archive. We recommend using [Podman](https://podman.io/docs/installation) since it is easier to build and download containers for specific architectures using Podman.

1. Download your required image based on the architecture of your RouterOS device.  

   ```routeros
   #For ARM64
   podman pull --arch=arm64 docker.io/pihole/pihole

   #For ARM
   podman pull --arch=arm docker.io/pihole/pihole

   #For AMD64
   podman pull --arch=amd64 docker.io/pihole/pihole
   ```

2. Save the container image to an archive.  

   ```routeros
   podman save pihole > pihole.tar
   ```

3. Upload the archive to your RouterOS device, for example:  

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   You can also use Winbox to upload files!
   :::
4. Create a Container on your RouterOS device using the uploaded container image archive file.  

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

#### Option C: Build an image on PC

You can build your own Containers and use them on your RouterOS device. While you can build Containers using Docker, we recommend using [Podman](https://podman.io/docs/installation) since it is easier to build Containers for a specific architecture using Podman.

1. Get source files for your required Container image, for example by using git.  

   ```routeros
   git clone https://github.com/pi-hole/docker-pi-hole.git
   cd docker-pi-hole
   ```

2. Build the Container image by specifying the Dockerfile or Containerfile and the target architecture.  

   ```routeros
   #For ARM64
   podman build --platform linux/arm64 --tag pihole -f ./src/Dockerfile

   #For ARM
   podman build --platform linux/arm --tag pihole -f ./src/Dockerfile

   #For AMD64
   podman build --platform linux/amd64 --tag pihole -f ./src/Dockerfile
   ```

3. Save the container image to an archive.  

   ```routeros
   podman save pihole > pihole.tar
   ```

4. Upload the archive to your RouterOS device, for example.  

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   You can also use Winbox to upload files!
   :::
5. Create a Container on your RouterOS device using the uploaded container image archive file.  

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

##### Alternative: Using Docker to build Container images

To use Dockerfile and make your own docker package - docker needs to be installed as well as buildx or another builder toolkit.

After installation check if extra architectures are available:

```bash
docker buildx ls
```

should return:

```bash
NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker
  default default         running linux/amd64, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
```

If not - install extra architectures:

```bash
docker run --privileged --rm tonistiigi/binfmt --install all
```

Pull or create your project with Dockerfile included  and build, extract image (adjust --platform if needed):

```bash
git clone https://github.com/pi-hole/docker-pi-hole.git
cd docker-pi-hole
docker buildx build  --no-cache --platform arm64 --output=type=docker -t pihole .
docker save pihole > pihole.tar
```

Upload *pihole.tar* to your RouterOS device.

Images and objects on the Linux system can be `pruned`

Create a container from the tar image

```ros
/container/add file=pihole.tar interface=veth1 mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

### Networking examples

#### Bridge with NAT

In this networking setup, all Containers use the same veth interface and communicate with each other without any Firewall restrictions, but you need to forward ports in order to allow access to a Container's port.

For example, a database Container needs to communicate with a web application Container; the web application needs the port `80` to be exposed to the world, but the database Container does not need any ports to be exposed to the world.

- The network configuration:  

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/bridge/add name=containers
  /ip/address/add address=172.17.0.1/24 interface=containers
  /interface/bridge/port/add bridge=containers interface=veth1
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  ```

- The database Container configuration:  

  ```routeros
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_DB value="webapp"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_USER value="webapp"
  /container/envs/add list=ENV_POSTGRES key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES src=disk1/volumes/postgres/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres mountlists=MOUNT_POSTGRES envlist=ENV_POSTGRES name=postgres start-on-boot=yes logging=yes
  ```

- The webapp Container configuration:  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

In this example, the `pgadmin` port 80 is accessible to everyone, but the `postgres` port 5432 is not accessible to everyone; it can only be accessed through either `pgadmin` as `127.0.0.1` or through the RouterOS device running the Container as `172.17.0.2`.

#### Isolated Containers

In this networking setup, you have multiple Containers and you want to make sure that some of them can communicate without Firewall restrictions, but some need to be isolated from other Containers. For example, you might want to create two database Containers and isolate them.

- The network configuration.  

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/veth/add name=veth2 address=172.18.0.2/24 gateway=172.18.0.1
  /interface/bridge/add name=containers1
  /interface/bridge/add name=containers2
  /ip/address/add address=172.17.0.1/24 interface=containers1
  /ip/address/add address=172.18.0.1/24 interface=containers2
  /interface/bridge/port/add bridge=containers1 interface=veth1
  /interface/bridge/port/add bridge=containers2 interface=veth2
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add chain=srcnat action=masquerade src-address=172.18.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=81 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=82 protocol=tcp to-addresses=172.18.0.2 to-ports=80
  ```

- The first and second database container configurations.  

  ```routeros
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_DB value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_USER value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES1 src=disk1/volumes/postgres1/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres1 mountlists=MOUNT_POSTGRES1 envlist=ENV_POSTGRES1 name=postgres1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_DB value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_USER value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES2 src=disk1/volumes/postgres2/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth2 root-dir=disk1/images/postgres2 mountlists=MOUNT_POSTGRES2 envlist=ENV_POSTGRES2 name=postgres2 start-on-boot=yes logging=yes
  ```

- The first and second webapp container configurations.  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin1 name=pgadmin1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth2 root-dir=disk1/images/pgadmin2 name=pgadmin2 start-on-boot=yes logging=yes
  ```

In this example, `pgadmin1` is able to reach `postgres1`, but is not able to reach `postgres2`. Similarly, `pgadmin2` is able to reach `postgres2`, but is not able to reach `postgres1`.

#### Container in Layer2 network

In this networking setup, your Container is directly attached to a Layer2 network with other physical network devices. This networking setup is equivalent to "host" networking mode on other Container engines such as Docker.

:::danger
In this networking setup, all the ports on your Container are exposed. This is considered insecure, but does slightly improve the Container's networking performance.
:::

- The networking configuration.  

  ```routeros
  /interface/veth/add name=veth1 address=192.168.88.2/24 gateway=192.168.88.1
  /interface/bridge/port/add bridge=bridge interface=veth1
  ```

- In case your RouterOS device has services running on the same port, you need to disable them.  

  ```routeros
  /ip/service/disable [find where name=www]
  ```

- The webapp configuration.  

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

In this example, `pgadmin` Container does not need port forwarding, but all other ports that the Container is using are now accessible to others on the same Layer2 network. This type of setup should only be used when your application requires that the Container has an IP address in the same Layer2 network such as applications that use broadcast traffic for service discovery (in most cases such requirements can still be bypassed by using NAT).

### IPv4 and IPv6 for Container

In this networking setup your Container will be able to communicate over IPv4 and IPv6. The solution is based on the [Bridge with NAT](./index.md#bridge-with-nat) networking setup.

- The network configuration.  

  ```routeros
  /ip/address
  add address=172.17.0.1/24 interface=containers
  /ip/firewall/nat
  add action=masquerade chain=srcnat src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  /ipv6/address
  add address=fd8d:5ad2:24:2::1 interface=containers
  /ipv6/firewall/nat
  add action=masquerade chain=srcnat src-address=fd8d:5ad2:24:2::/64
  add action=dst-nat chain=dstnat dst-address=fd8d:5ad2:24:2::1 dst-port=80 protocol=tcp to-addresses=fd8d:5ad2:24:2::2 to-ports=80
  /interface/veth
  add address=172.17.0.2/24,fd8d:5ad2:24:2::2/64 gateway=172.17.0.1 gateway6=fd8d:5ad2:24:2::1 name=veth1
  /interface/bridge/port/add bridge=containers interface=veth1
  ```

- The webapp container configuration.

  ```routeros
  /container/add remote-image=nginx interface=veth1 root-dir=disk1/images/nginx name=nginx start-on-boot=yes logging=yes
  ```

## Healthcheck

Starting RouterOS 7.23 healthcheck support has been implemented in RouterOS.
Healthcheck is a mechanism that helps verify that the application within the container is running correctly.

Healthchecks rely on standard exit codes. The command used for the healthcheck should return 0 when the application is healthy and a non-zero exit code when it is unhealthy.

In most cases, on containers running a web interface, a simple HTTP GET request to localhost is enough to verify if the application is responding properly.

| Property | Description |
| :-- | :-- |
| **healthcheck-cmd** (*string*; *Default*:)| command used for healthcheck |
| **healthcheck-interval** (*time*; *Default*: 00:00:30)| time interval in format HH:MM:SS |
| **healthcheck-retries** (*int*; *Default*: 3)| in the case of a failed check - number of retries before container application is considered unhealthy|
| **healthcheck-start-interval** (*time*; *Default*: 00:00:05)| time between healthchecks in the start period |
| **healthcheck-start-period** (*time*; *Default*: 00:00:00) | provides time for the container to start. any failures within the start period will not be added to the retries counter|
| **healthcheck-status** (*string*)| current health status of container. displays the current status of the application within the container as well as the output from the probe|
| **healthcheck-timeout** (*time*; *Default*: 00:00:30)| if healthcheck probing takes longer than the specified period, the check will count as a fail |

### Healthcheck example

For this example we will be setting up a HomeAssistant container and set up a simple healthcheck on it.

For a guide on setting up a HomeAssistant container, please refer to our [HomeAssistant setup guide](./user-guides/container-homeassistant.md)

To set up the E-mail tool. Please refer to our [E-mail documentation page](../system-information-and-utilities/e-mail.md)

1. Check your container name

    ```ros
    [admin@ROSE] > container print 
    Flags: S - STOPPED, R - RUNNING
    Columns: NAME, ROOT-DIR, INTERFACE, MEMORY-CURRENT, CPU-USAGE, CONTAINER-SIZE, DATA-SIZE, TAG
    #   NAME                ROOT-DIR                                        INTERFACE                MEMORY-CURRENT  CPU-USAGE  CONTAINER-SIZE  DATA-SIZE  TAG                                                                   
    1 S home-assistant  /nvme1/apps/home-assistant/home-assistant_root  veth-home-assistant                          0  2201.9MiB       471.9KiB   docker.io/homeassistant/home-assistant:latest
    ```

2. After a container has been created, we can enable healthcheck on it by setting the healthcheck command. For this specific container. We can increase the healthcheck-interval as well as specify a start-period as HomeAssistant is a heavy container and may start slower on some devices.

    ```ros
    /container/set home-assistant healthcheck-cmd="curl -f http://localhost:8123" healthcheck-interval="00:01:00" healthcheck-start-period="00:02:00"
    ```

    If successful and the container starts - you should see the container running with the "Healthy" status.
    Additionally, the healthcheck-status field is populated with the current status of the container as well as the output from the curl command.

    ```ros
    [admin@ROSE] > container print proplist=name,healthcheck-status
    Flags: S - STOPPED, R - RUNNING, H - HEALTHY
    Columns: NAME, HEALTHCHECK-STATUS
    #   NAME                HEALTHCHECK-STATUS                                                                           
    
     H home-assistant  good, output:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                                              Dload  Upload   Total   Spent    Left  Speed     
    ```

As an extra step, you can create a script that polls the container status and sends a notification to your e-mail if healthcheck fails and add a scheduler to run the script regularly.

1. Create the script:

    ```ros
    /system script
    add name=unhealthy-container-alert source="
    :global lastState\
        \n:local currentState \"\"\
        \n:local msg \"\"\
        \n:foreach i in=[/container find where unhealthy] do={\
        \n:local name [/container get \$i name]\
        \n:set currentState (\$currentState . \$name . \";\")\
        \n}\
        \n:if ([:len \$currentState] = 0) do={\
        \n:set lastState \"\"\
        \n} else={\
        \n:if (\$currentState != \$lastState) do={\
        \n:set lastState \$currentState\
        \n:foreach i in=[/container find where unhealthy] do={\
        \n:local name [/container get \$i name]\
        \n:set msg (\$msg . \$name . \" is UNHEALTHY\\n\")\
        \n}\
        \n/tool e-mail send to=\"admin@example.com\" subject=\"Unhealthy container(s)\" body=\$msg\
        \n}\
        \n}"
    ```

    :::warning
    Make sure to replace admin@example.com with your email.
    :::

2. Create the scheduler:

    ```ros
    /system scheduler
    add interval=2m name=container-healthcheck-alert on-event="/system/script/run unhealthy-container-alert"
    ```

## Memory

There are three parameters that control container memory behavior: `memory-max`, `memory-high`, and `swap-max`. Each can be configured per-container or globally in `/container/config`. The global values act as defaults — if both a per-container and a global limit are set, the **lower** value applies (this works both ways).

### memory-max

Sets the hard upper limit for container RAM usage (in bytes). If a container exceeds this limit, it will be killed. When set on both levels, e.g. the per-container limit is 500MB and the global limit is 300MB, the 300MB limit takes effect. If swap is enabled, the container may attempt to swap out the excess memory instead of being killed.

### memory-high

Sets a soft upper limit for container RAM usage (in bytes). When the limit is reached, the container processes are throttled and put under heavy memory reclaim pressure — the system will try to free memory (including swapping). Unlike `memory-max`, the container is **never** killed for exceeding this limit.

### swap-max

Defines the maximum amount of swap space (in bytes) that a container may use. Works together with `memory-max` — once a container hits its `memory-max` limit, the excess memory will be swapped out up to the `swap-max` limit. For example, if a container has a `memory-max` of 600MB and a process is trying to use 800MB, the remaining 200MB will be pushed into swap. Swap must be enabled on the device (see [Swap space](../hardware/disks/index.md)).

## Tips and tricks

- Containers use up a lot of disk space. USB/SATA, NVMe attached media is highly recommended. For devices with USB ports - USB to SATA adapters can be used with 2.5" drives - for extra storage and faster file operations.
- For starting containers after a router reboot use the start-on-boot option (starting from 7.6beta6):

  ```ros
  /container/print
    0 name="2e679415-2edd-4300-8fab-a779ec267058" tag="test_arm64:latest" os="linux" arch="arm" interface=veth2 
      root-dir=disk1/alpine mountlists="" dns="" logging=yes start-on-boot=yes status=running 

  /container/set 0 start-on-boot=yes
  ```

- It is possible to get to a **running** container shell:

  ```ros
  /container/shell 0
  ```

- It's possible to set the container timeout in seconds, otherwise it will stay open indefinitely:

  ```ros
  /container/shell 0 timeout=120
  ```

- Enable logging to get output from the container:

  ```ros
  /container/set 0 logging=yes
  ```

- Some containers will require additional privileges in order to be able to run properly:  

  ```routeros
  /container/set 0 user=0:0
  ```

- You can execute commands inside a Container with a specific user and without invoking `/bin/sh`:  

  ```routeros
  /container/shell nextcloud user=www-data cmd="php /var/www/html/cron.php" no-sh
  ```

- Starting from version 7.11beta5 multiple addresses and ipv6 addresses can be added:

  ```ros
  /interface/veth/add address=172.17.0.3/16,fd8d:5ad2:24:2::2/64 gateway=172.17.0.1 gateway6=fd8d:5ad2:24:2::1
  ```

- Active running /dev/ nodes to container:

  ```shell
  /dev/full	/dev/null	/dev/random		/dev/tty	/dev/urandom	/dev/zero	/dev/console	/dev/net/tun	/dev/kvm	/dev/fuse
  ```

- Using the `Devices` parameter, it is possible to allow the serial terminal to be exposed to the container.

```ros
/container/set your-container devices=serial0:""
```

:::info
To allow the container to use the serial console port, you must first free the serial console used by RouterOS under `/system/console`
:::
