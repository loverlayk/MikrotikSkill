# Apps

> The Apps menu provides a catalog of pre-configured applications deployable via containers, with automatic RouterOS configuration and support for multiple container registries. It requires Container package...

# Apps

#### Summary

**Sub-menu:** `/app`  
**Packages required:** `container`

The App menu provides a catalog of applications that can be deployed in a couple of clicks. Each app can consist of one or multiple pre-configured containers and the necessary RouterOS configuration such as firewall rules and address translation will be applied automatically. This catalog is prepared and maintained by MikroTik, but the container images get sourced from multiple registries such as Docker Hub, GCR and Quay.

The configuration parameters, however, can be edited before enabling an app, and the applied yaml file can always be viewed.

#### Requirements

The App system inherits the same requirements as the Container package:

- **Architecture Support:** arm64 and x86 architectures.
- **Container Package:** Must be installed.
- **Device Mode:** Container mode must be enabled (requires physical access and device reset).
- **External Storage:** Highly recommended for optimal performance.
- **Memory Requirements:** Adequate RAM for container operations (16MB SPI flash devices may require external storage for images).
- **Architecture Limitations:** Devices with EN7562CT CPU (like hEX Refresh) are not supported.

#### Security Considerations

As with the underlying Container system, the App menu inherits security implications:

- Physical access is required to initially enable container support.
- Once enabled, containers can be managed remotely.
- Compromised devices can use containers to install malicious software.
- Device security is equivalent to the security of running containers.
- Third-party container images may introduce security vulnerabilities.

## Properties

| Property | Type | Default | Description |
| :-- | :-- | :-- | :-- |
| **auto-update** | *yes* &#124; *no* | *no* | Enables or disables automatic updating when a new container image version is available. |
| **check-certificate** | *yes* &#124; *no* | *yes* | Verifies the registry certificate against the router’s [certificate store](../../authentication-authorization-accounting/certificates.md) before pulling the container image. |
| **container-command-lines** | *string* | *(empty)* | Specifies the command-line argument(s) to pass to the application when starting the container. |
| **devices** | *string* | *(empty)* | Specifies additional hardware devices to pass through to the container application. |
| **environment** | *string* | *(empty)* | Defines environment variables to be available to the running application. Specify as a list of key-value pair(s). |
| **extra-mounts** | *string* | *(empty)* | Specifies additional mount points to attach to the container. |
| **firewall-redirects** | *string* | *(empty)* | Configures port redirection from the host device to the container. |
| **network** | *default* &#124; *lan* &#124; *internal* | *default* | Specifies which network the container will use: **internal** (behind NAT), **lan** (on the LAN network), or **default** (varies per application; can be internal or lan). |
| **network-outgoing-access** | *yes* &#124; *no* | *yes* | Allows network outgoing access for the specific container app, when set to `no`, a mangle drop rule is created. |
| **pvid** | *integer* | *1* | Sets the Port VLAN ID (PVID) for the container's virtual Ethernet interface in the bridge. |
| **required-hw-devices** | *string* | *(empty)* | Hardware devices that must be present on the host for the container to start. This property is configurable only after adding the YAML configuration. **Compose format:**`[host-hw-device]:[device-in-app]` |
| **required-mounts** | *string* | *(empty)* | Mount directories required for the container to start. This property is configurable only after adding the YAML configuration. **Compose format:**`[dir-on-host]:[dir-in-app]` |
| **use-https** | *yes* &#124; *no* | *yes* | Uses HTTPS for the application URL. This option will not work on devices that do not support cloud services. |
| **yaml** | *string* | *(empty)* | Provides the YAML composition for the application. See the documentation for configuration examples. |

## Read-only Properties

| Property | Type | Default | Description |
| :-- | :-- | :-- | :-- |
| **app-size** | | | The total size of the application. |
| **app-store-url** | *string* | | The URL of the app store from which the application was installed. |
| **cpu-usage** | | | The current CPU usage percentage by the application. |
| **custom** | *yes* &#124; *no* | | Indicates whether the application is a custom application created by the user. |
| **data-size** | | | The size of the data stored by the application. |
| **default-credential** | *string* | | The default credentials required for the application. |
| **default-network** | *lan* &#124; *internal* | | The default network used by the application. Valid values are `lan` or `internal`. |
| **description** | *string* | | The application description as defined in the `descr` parameter of the YAML configuration. |
| **from-app-store** | *yes* &#124; *no* | | Indicates whether the application was installed from a custom app store. |
| **interface** | *string* | | The VETH interface used by the application. |
| **ip-address** | *IP* | | The IP address assigned to the VETH interface. |
| **memory-current** | | | The amount of memory currently used by the application. |
| **name** | *string* | | The application name as defined in the `name` parameter of the YAML configuration. |
| **project-page** | *string* | | The application project page URL as defined in the `page` parameter of the YAML configuration. |
| **running** | | | Indicates whether the application is currently running. |
| **status** | *acquire veth* &#124; *configuring container(s)* &#124; *downloading/extracting* &#124; *starting* | | The current status of the application. Possible values indicate the application is acquiring a VETH interface, configuring containers, downloading/extracting, or starting. |
| **ui-url** | *string* | | The generated URL for the application's web interface, if available. |
| **variables-to-be-used-in-environment** | | | A list of all variables present in the application environment. |

#### Setup Wizard

The App menu includes a setup wizard (button "Setup" in the GUI, or command `/app/setup`). This wizard automates all the networking, storage, and registry setup that would otherwise require multiple manual steps.

##### Step 1: Storage Selection

Select a storage disk for application installation. The system automatically detects available formatted disks drives (such as nvme1, usb1, disk1, and similar devices). If no suitable disk appears in the list, you must first format the disk using either the ext4 or btrfs file system, then mount it through the `/disk` menu.

**Requirements:**

- A minimum of 100 MB/s sequential read/write speed is recommended.
- A minimum of 10,000 random IOPS (Input/Output Operations Per Second) is recommended.
- Use the `/disk/test` command to verify storage performance before proceeding.
- External storage devices are highly recommended for optimal performance.

##### Step 2: Bridge Configuration

Select the LAN bridge interface for container networking. This configuration enables automatic port forwarding and application autodiscovery on the local network. The setup wizard automatically configures the following:

- Virtual ethernet (veth) interface creation
- Addition of the veth interface to the configured bridge
- NAT rules for outbound connectivity

##### Step 3: IP Configuration

Define the router's IP address to enable application access. The system automatically detects the primary IP address; however, manual configuration is supported for complex network setups. The specified IP address serves the following purposes:

- Generating application UI URLs.
- Creating automatic port forwarding rules.
- Providing WebFig integration links.

##### Completion

Once you complete the setup wizard, the App system is ready for immediate use. You can enable applications directly through the interface. The system automatically handles all underlying container configuration.

#### Configuration

App configuration is accessible through `/app/settings` and provides a simplified setup compared to manual Container configuration

## Properties

| Property | Type | Default | Description |
| :-- | :-- | :-- | :-- |
| **app-store-urls** | *string* | *(empty)* | URL to a custom app store. The URL must point to a YAML array where each application is an element within the array. |
| **auto-update** | *yes* &#124; *no* | *no* | Global setting that enables automatic updates for all installed applications packages. |
| **disk** | *string* | *(empty)* | Global setting that specifies which disk will be used for storage operations. |
| **download-path** | *string* | *(empty)* | Manually specifies the directory path where all downloaded content will be stored. |
| **lan-bridge** | *string* | *(empty)* | Manually specifies the bridge interface that represents the local area network. |
| **media-path** | *string* | *(empty)* | Manually specifies the directory path where all media files will be stored. |
| **registry-mirrors** | *string* | *(empty)* | Specifies one or more registry mirror URLs addresses for container image retrieval. |
| **router-ip** | *IP* | *(empty)* | Manually specifies the IP address at which the current RouterOS device can be reached. |
| **show-in-webfig** | *yes* &#124; *no* | *yes* | Controls whether links to enabled applications are displayed on the WebFig login page. |

### Auto-Configured Settings

Certain parameters are initially configured automatically based on network detection. These values can always be manually overridden if required.

| Property | Type | Default | Description |
| :-- | :-- | :-- | :-- |
| **assumed-router-ip** | *IP* | *(detected)* | Automatically detected network IP address of the RouterOS device. |
| **assumed-lan-bridge** | *string* | *(detected)* | Automatically detected bridge interface used for LAN connectivity. |
| **assumed-media-path** | *string* | *disk/media* | Default media storage path, typically located on the system disk. |
| **assumed-download-path** | *string* | *disk/media/downloads* | Default download directory path, typically located within the media storage area. |

#### Application Management

Applications are managed through the `/app` interface, providing status monitoring and lifecycle control similar to the underlying `/container` system:

```
/app> print 
Flags: X - DISABLED, R - RUNNING
Columns: NAME, UI-URL, MEMORY-CURRENT, APP-SIZE, DATA-SIZE, CATEGORY, DESCRIPTION
```

##### Status Indicators and Metadata

- **Flags:**
  - X (DISABLED) - Can indicate two states: not downloaded/installed (APP-SIZE and DATA-SIZE will be empty), or downloaded but disabled (APP-SIZE and DATA-SIZE show storage usage).
  - R (RUNNING) - Application actively running and accessible.
- **UI-URL:** Direct web interface access URL when application is running.
- **MEMORY-CURRENT:** Real-time memory consumption in MiB (only when running).
- **APP-SIZE:** Container image storage consumption in MiB (shows space used when downloaded).
- **DATA-SIZE:** Application persistent data size in KiB/MiB (shows configuration and user data).
- **CATEGORY:** Application functional classification.
- **DESCRIPTION:** Application functionality description.

##### Application Lifecycle Management

### Deployment Process

Unlike manual Container deployment which requires multiple configuration steps (veth interface, bridge setup, environment variable, mount, and firewall rules), App deployment automates the entire process:

1. **Selection:** Choose an application from the catalog via CLI or WebFig.
2. **Download:** Automatic container image download and extraction.
3. **Network Setup:** Automatic veth interface and bridge configuration.
4. **Port Forwarding:** Automatic firewall rule creation for web access.
5. **Startup:** Container initialization with pre-configured settings.
6. **Access:** UI-URL becomes available for immediate web interface access.

#### Cleanup Command

The cleanup command provides complete application removal, including all associated data. This operation is destructive and irreversible:

```
/app> cleanup pihole 
App data will be lost, continue? [y/N]:
```

**Cleanup Process:**

1. Stops the running container.
2. Removes all application data and configuration files.
3. Deletes the container image from storage.
4. Resets the application to an uninstalled state (empty APP-SIZE and DATA-SIZE).
5. Removes network configuration specific to the application.

:::warning

All user data, configuration settings, and application state will be permanently lost. The application will return to its original catalog state and require complete reconfiguration if cleaned-up.

:::

## Custom Apps

Starting with RouterOS v7.22, you can create your own custom apps using a 'compose' YAML file. This lets experienced users build solutions that fit their specific network needs.

How it works:

- You define the app internals and limited RouterOS configuration in YAML format
- RouterOS pulls the specified image/s and creates your app
- The app runs on RouterOS hardware and delivers new features at no cost
- Optionally, have it interact with our API

Why use it:

- Build exactly what you need for your network
- No need to wait for official app releases
- Great for automation, custom routing, or specialized services
- Declarative setup makes management easier

### How to add apps

There are three options, but they all rely on YAML.

#### Method 1: Create a Blank App and Edit YAML

First, create the app and assign it to the LAN network:

```routeros
/app/add network=lan
```

By default, the app will be named "app".

Next, add the YAML configuration. In the Terminal, run:

```routeros
/app/edit app yaml
```

This opens a text editor where you can paste your YAML. After pasting, press <kbd>Control</kbd>+<kbd>O</kbd> to save your changes. Finally, enable the app to start it running.

#### Method 2: Import from a File

Alternatively, save your compose text to a file and upload it to the device. Then, set the file as the app's YAML using the following command:

```routeros
/app/add yaml=[/file/get alpine-iperf.yml contents]
```

This method is useful when you have a pre-configured YAML file ready to import.

#### Method 3: Add custom app-store URL

If you or someone you know has hosted their own app or a list of apps on a webserver, you can simply add the URL in your APP settings. This way it is possible to have a dynamically updated catalog of custom apps.

```routeros
/app/settings set app-store-urls="<custom_url>"
```

For this to work correctly, the URL should simply return the text contents of a YAML file, where multiple apps are listed in a simple list according to standard YAML syntax.

### Writing YAML for a Custom App

This example creates an iperf3 app using an existing openEuler base image.

```yaml
name: openeuler-iperf
descr: openEuler container running iperf3 server
page: https://iperf.fr/
category: networking
default-credentials: none
services:
  iperf:
    image: docker.io/openeuler/iperf:latest
    ports:
      - 5201:5201:tcp
      - 5201:5201/udp:udp
    command: /bin/sh -c "iperf3 -s"

```

Key distinctions:
- base image already has iperf installed
- necessary ports are forwarded/mapped to routers IP
- the 'command' executes at containers startup and runs iperf3

Alternatively, you could use a plain base image like Alpine Linux and install iperf3 using 'command'.

```yaml
name: alpine-iperf
descr: Alpine Linux container running iperf3 server
page: https://iperf.fr/
category: networking
default-credentials: none
services:
  iperf:
    image: docker.io/alpine:latest
    command: /bin/sh -c "apk add --no-cache iperf3 && iperf3 -s"
networks:
  default:
    name: lan
    external: true

```

Key distinctions:
- clean base image
- iperf3 is installed and ran at each startup
- the app's network is set to your LAN (alternative to forwarding ports)

Optionally, if you want to ensure that 'command' executes something only once, consider using conditional one-liners such as this:

```yaml
command: /bin/sh -c "if ! command -v iperf3 >/dev/null 2>&1; then apk add --no-cache iperf3; fi; exec iperf3 -s"
```

### Port Mapping

When mapping ports use the X:Y or X:Y:Z syntax where X is the port on your router, Y is a port on the container and Z gives the port a name, however some names can have special functionality, for example, 'web' will cause RouterOS to set up reverse proxy with an auto-generated URL.
Some valid examples:

```yaml
2211:21
888:80:web
9000:9000:api
9001:9001:api-secure

```

All ports are set up as TCP by default, unless you define them as UDP, like so:

```yaml
6000:6000/udp:udp
8000:8000/udp:custom_name

```

:::warning
By default, port `80` is assumed to be a web port, unless you explicitly set it to a different type. There is a healthcheck that probes this port — if nothing is listening, the app will appear stuck in a `starting` state. When port `80` is not mapped, the first defined port is used instead. To avoid ambiguity, name your used ports explicitly.
:::

## YAML Field Reference

A YAML document defines one App: an app-level section with the App's metadata, and a `services` section with one or more container definitions.

### App-level Fields

| Field | Type | Description |
|---|---|---|
| `name` | *string* | Unique name of the App. |
| `descr` | *string* | Description of the app. |
| `page` | *string* | URL of the project page, shown as the `project-page` property of the App. |
| `category` | *string* | Classification group shown in the App list (e.g., network, system, utilities). |
| `default-credentials` | *string* | Login credentials in the `username:password` format. Informative only; can be left blank.|
| `icon` | *string* | URL of an icon image displayed in the WebFig landing page. |
| `url-path` | *string* | Path appended to the App URL, for example `/login` or `/web`. |
| `auto-update` | *boolean* | When `true`, the App is updated automatically when a new container image is available. |
| `supported-archs` | *list of strings* | CPU architectures supported by the App: `arm`, `arm64`, `arm_v5`, and `x86`. Devices not matching the specified architecture will not display the app. |
| `compatible-boards` | *list of strings* | Board names supported by the App, for example `RDS2216`. The `*` wildcard is accepted. Devices not matching the specified board name will not display the app. |
| `services` | *map* | Container service definitions. At least one service is required. |
| `volumes` | *map* | Named volume declarations used by the services. |
| `secrets` | *map* | Secret names for the App, referenced with `[secret:name]` in `environment`. |
| `configs` | *map* | Configuration file declarations mounted into the services. |
| `networks` | *map* | Network declarations used by the services. |

### Service Fields

| Field | Type | Description |
|---|---|---|
| `image` | *string* | App image to use for the container. Required. |
| `container_name` | *string* | Name to use with the specific image, as shown in the `/container` menu. |
| `command` | *string* | Startup command executed inside the container. |
| `entrypoint` | *string* | Executable used as the container entry point. |
| `environment` | *list or map* | Environment variables passed to the container.|
| `volumes` | *list* | Mount points attached to the container. |
| `ports` | *list* | Port mappings from the router to the container. |
| `expose` | *list* | Ports exposed to other containers without publishing them on the router. |
| `restart` | *string* | Restart policy of the container. `unless-stopped`, `always`, and `on-failure`. |
| `depends_on` | *list* | Service names that must start before this service. |
| `healthcheck` | *map* | Run a healthcheck when container starts. See example below. |
| `shm_size` | *string* | Shared memory size, for example `512mb` or `1gb`. |
| `stop_grace_period` | *string* or *int* | Timeout for graceful shutdown, for example `30s` or `0`. 30 seconds by default. |
| `devices` | *list* | Hardware devices passed through to the container, for example `- /dev/ttyACM0:/dev/ttyACM0`. |
| `user` | *string* | Linux user or UID the container runs as. |
| `hostname` | *string* | Hostname set in the container. |
| `security_opt` | *list* | Container security options. |
| `build` | *map* | Build configuration for a locally built image. |
| `secrets` | *list* | Secret names available to this service, mounted as files at `/run/secrets/<name>`. |
| `configs` | *list* | Configuration files mounted into this service. |

### Healthcheck

A health check probes the service to verify that the application is running correctly. The 'test' parameter runs inside the container, and the service is considered healthy when the command returns exit code 0:

```yaml
healthcheck:
  test: ["CMD", "curl -f http://localhost:8080/ || exit 1"]
  interval: 30s
  retries: 3
  start_period: 30s
  timeout: 10s
```

### Runtime Placeholders

Environment variable values and the default-credentials field can contain placeholders that RouterOS replaces when the App runs.

| Placeholder | Description |
|---|---|
| `[accessIP]` | IP address or hostname used to access the App from outside. |
| `[accessPort]` | Router port mapped to the App web interface. |
| `[accessProto]` | Protocol used to access the App, `http` or `https`. |
| `[containerIP]` | IP address assigned to the container. |
| `[containerInterface]` | Name of the VETH interface created for the App. |
| `[routerIP]` | IP address of the router on the App network. |
| `[env:variable]` | Value of an environment variable of the App. |
| `[env:service:variable]` | Value of an environment variable of the specifiec service. |
| `[secret:name]` | Value of the secret declared in the app-level `secrets` section. |

Use placeholders in environment values to configure services automatically:

```yaml
environment:
  - NEXTCLOUD_TRUSTED_DOMAINS=[accessIP]
  - APP_URL=[accessProto]://[accessIP]:[accessPort]
```

### Volumes

Add persistent data to a service:

```yaml
services:
  app:
    image: docker.io/example/app:latest
    volumes:
      - data:/data              # persistent directory in the App storage
      - appdata/conf:/etc/app   # sub-directory, mounted at /etc/app
      - ./custom:/custom        # relative to the storage path
```

### Secrets

Secrets store passwords and keys separately from the environment. Declare secrets in the app-level `secrets` section and reference them with `[secret:name]` in environment values and default-credentials. RouterOS generates the secret value when the App runs:

```yaml
secrets:
  db_password:
  admin_password:
services:
  db:
    image: docker.io/postgres:17
    environment:
      POSTGRES_PASSWORD: "[secret:db_password]"
  server:
    image: docker.io/example/server:latest
    environment:
      ADMIN_PASSWORD: "[secret:admin_password]"
```

Alternatively, list a secret under a service to mount it as a file at `/run/secrets/<name>`:

```yaml
services:
  server:
    image: docker.io/example/server:latest
    environment:
      DB_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
```

### Configs

Configs provide configuration files to containers as text. Declare content in the app-level `configs` section and mount it into a service with `source`, `target`, and optional `mode`.

```yaml
configs:
  mosquitto_conf:
    content: |
      listener 1883
      allow_anonymous true
services:
  mosquitto:
    image: docker.io/eclipse-mosquitto:latest
    configs:
      - source: mosquitto_conf
        target: /mosquitto/config/mosquitto.conf
        mode: 0644
```

The `source` is the name of the app-level config declaration, `target` is the path inside the container, and `mode` is the file permission.

### Networks

By default, an App runs on an internal network behind NAT and services are reached through mapped ports. To place the App directly on a network, define the default network in the app-level `networks` section with an external network.

```yaml
networks:
  default:
    name: lan
    external: true
```

## Custom app store

The App system supports custom app stores served as a YAML array, where each element of the array is an app definition. The file must be hosted on a server the device can reach over the network.

Example of a YAML array consisting of two apps:

```yaml
- name: code-server-xxx
  descr: Code-server is VS Code running on a remote server, accessible through the browser.
  page: https://coder.com
  category: development
  icon: https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/code-server-logo.png
  default-credentials: <no_username>:password
  services:
    code-server:
      image: lscr.io/linuxserver/code-server:latest
      container_name: code-server
      user: "0:0"
      environment:
        PUID: 0
        PGID: 0
        PASSWORD: password
        PWA_APPNAME: code-server
      volumes:
        - config:/config
        - media:/data/media
      ports:
        - 8443:8443:web
- name: code-server-yyy
  descr: Code-server is VS Code running on a remote server, accessible through the browser.
  page: https://coder.com
  category: development
  icon: https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/code-server-logo.png
  default-credentials: <no_username>:password
  services:
    code-server:
      image: lscr.io/linuxserver/code-server:latest
      container_name: code-server
      user: "0:0"
      environment:
        PUID: 0
        PGID: 0
        PASSWORD: password
        PWA_APPNAME: code-server
      volumes:
        - config:/config
        - media:/data/media
      ports:
        - 8443:8443:web
```

## Tips and Best Practices

- **Storage:** For optimal performance and greater capacity, consider using external storage devices such as USB drive, SATA drive, or NVMe SSD.

- **Memory:** Keep track of your application's memory consumption by running the `/app/print` command in the terminal.

- **Updates:** Only update your system when required and deemed necessary. While automatic updates can provide security patches and new features, it's important to assess whether an update is needed for your specific use case before enabling or applying it.

- **Networking:** The application automatically manages port forwarding and generates the necessary URL for external access.

- **Data Persistence:** Your application data is stored in the designated storage path and will remain intact even after the application restarts or the system reboots.
