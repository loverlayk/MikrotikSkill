# Apps

> Install, manage, and create container applications with the RouterOS Apps menu, including the setup wizard and custom compose YAML files.

# Apps

The Apps menu provides a catalog of applications you can run on RouterOS. An app can contain one or more containers, and RouterOS creates the required container configuration, VETH interface, bridge port, firewall rules, and reverse proxy entry. The catalog is maintained by MikroTik and sources images from Docker Hub, GCR, Quay, and other registries. You can edit an app's configuration before you enable it and view its YAML at any time.

The [list of available Apps](available-apps) shows the catalog. The same YAML format is used by catalog apps and custom apps.

## Prerequisites

- Install the `container` package.
- Use an arm64, arm32 or x86 device. Devices with an EN7562CT CPU such as hEX Refresh run only arm32v5 images, so only apps that list `arm_v5` in `supported-archs` are available.
- Enable container mode with `/system/device-mode/update container=yes`. This requires physical access and a reset-button confirmation or a cold reboot on x86. See [Device mode](../../system-information-and-utilities/device-mode/).
- Format a storage disk with ext4, btrfs, or xfs and mount it in `/disk`. External storage is recommended. Devices with 16 MB SPI flash need external storage for container images.
- Provide enough RAM for the containers. The app's current memory use is shown as `memory-current` in `/app/print detail`.
- Configure the app disk, router IP address, and LAN bridge in `/app/settings` or with the [setup wizard](#setup-wizard).
- For HTTPS app URLs, the router needs a working app certificate from the cloud service.

:::warning
Running third-party container images can expose the device to the same security risks as the images themselves. A compromised router can also use containers to install malicious software. Review [Container](../) before you enable container mode.
:::

## Setup wizard

Run `/app/setup` in the terminal or select Setup in WebFig. The wizard writes the values to `/app/settings`, where you can change them later.

### Select the app disk

The wizard lists disks that are formatted and mounted. Format a disk in `/disk` with ext4, btrfs, or xfs before you run the wizard.

Use a disk with at least 100 MB/s sequential read/write speed and 10,000 random IOPS. Verify the disk with `/disk/test`.

The wizard sets the media path to `<disk>/media` and the download path to `<disk>/media/downloads`. App images and data are stored under `<disk>/apps`.

### Select the LAN bridge

Select the bridge that represents your LAN. Apps with `network=lan` attach their VETH interface to this bridge. Some apps use the LAN for autodiscovery.

### Set the router IP

Select the IP address at which clients reach the router. Apps use this address in generated URLs and port-forwarding rules, so set it before you enable apps. An app enabled without it stays in `status=waiting for router ip to be configured`.

### Review the settings

The wizard stores the selected values in `/app/settings`. Check them with:

```routeros
/app/settings/print
```

## Install and run an app

Catalog apps are present but disabled. Enable an app in WebFig or in the terminal:

```routeros
/app/print
/app/enable <app>
```

The first enable pulls and extracts the images, creates the network, and starts the containers. Check the progress with:

```routeros
/app/print detail where name="<app>"
```

While the app starts, `status` shows `downloading/extracting` or `starting`. When the app runs, `status` is empty, flag `R` appears, and `ui-url` contains the access URL.

With `use-https=yes`, RouterOS creates a reverse proxy rule and uses the app certificate from `/app/settings`. The URL uses the cloud hostname. With `use-https=no`, the URL is `http://<router-ip>:<port>`. An app with a port named `web` gets a UI URL. See [Container apps](../../network-management/proxy/reverse-proxy#container-apps) for the reverse proxy details.

## Manage apps

### Flags and status

| Flag | Meaning |
| :-- | :-- |
| `X` | The app is disabled. |
| `R` | The app is running. |
| `c` | The app is a custom app. |
| `s` | The app comes from a custom app store. |

`app print` can show different columns depending on the terminal width. Use `print detail` or `proplist` to read a specific field.

`status` is empty while the app is running. During startup or after a failure it can show values such as `waiting for router ip to be configured`, `downloading/extracting`, or `starting`.

### Update, restart, and stop apps

```routeros
/app/update <app>
/app/restart <app>
/app/disable <app>
/app/enable <app>
```

`/app/update` pulls the app images again, extracts them, and restarts the app. `/app/restart` stops and starts the containers without pulling images.

Set `auto-update=yes` on an app to check for a new image when the app starts after a reboot. The global `auto-update` setting in `/app/settings` provides the default for installed apps. When the image has not changed, RouterOS skips the import and starts the existing image.

### Remove apps

`/app/cleanup` stops the app and removes its containers, data, and network configuration. The app entry remains, disabled. This operation cannot be undone:

```text
/app/cleanup <app>
App data will be lost, continue? [y/N]:
```

Use `/app/remove` to delete the app entry itself. Run cleanup first to remove the app data.

:::warning
Cleanup permanently deletes application data, configuration, and state. Back up any data you need before you continue.
:::

### Network settings

- `network` selects the app network. `internal` places the app behind NAT, `lan` attaches the VETH interface to the LAN bridge, and `default` uses the app's default network.
- `network-pvid` sets the PVID of the app's bridge port. The default is `1`.
- `network-outgoing-access=no` blocks outgoing connections from the app with a mangle drop rule. Please keep in mind this may interfere with your existing firewall.
- `use-https` controls whether the app uses the HTTPS reverse proxy and cloud URL or plain HTTP with a port forwarded to the router IP.

## Custom apps

Create a custom app when the catalog does not contain the service you need or when you need a different container configuration. Custom apps use the same compose YAML format as catalog apps and are marked with flag `c`. You can also publish custom apps in a custom app store.

### Create a blank app

Create an app and assign it to the LAN network:

```routeros
/app/add network=lan
```

The app is created disabled with the name `app` and no service containers. Add the YAML configuration in the terminal:

```routeros
/app/edit app yaml
```

Paste the YAML, press <kbd>Control</kbd>+<kbd>O</kbd> to save, and enable the app.

### Import a YAML file

Save the compose file, upload it to the device, and use its contents as the app YAML:

```routeros
/app/add yaml=[/file/get <filename> contents]
```

The app is created disabled. Enable it after you check the imported configuration.

### Add a custom app store

Set one or more app store URLs in `/app/settings`:

```routeros
/app/settings/set app-store-urls="<url>"
```

Each URL must return a YAML array in which every element is an app definition. Apps loaded from a custom store appear with flag `s`.

### Write YAML for a custom app

This example creates an iperf3 server from an openEuler image that already contains iperf3:

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

The image already contains `iperf3`, the ports are forwarded to the router IP, and `command` starts the server when the container starts.

To install iperf3 at container startup, use a plain base image:

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

This example installs iperf3 and starts it at every container start. The container needs internet access to download the package. The `networks` section places the app directly on the LAN instead of forwarding ports.

To install a package only when it is missing, use a conditional command:

```yaml
command: /bin/sh -c "if ! command -v iperf3 >/dev/null 2>&1; then apk add --no-cache iperf3; fi; exec iperf3 -s"
```

### Map ports

Use `<router-port>:<container-port>` or `<router-port>:<container-port>:<name>`:

```yaml
ports:
  - 8080:80:web
  - 9000:9000:api
  - 6000:6000/udp:dns
```

Ports are TCP unless you add `/udp`. The first TCP port becomes the web port if no port is named `web`. A port named `web` gets a reverse proxy entry and a UI URL. A `web` port with no listener inside the container keeps the app in `starting`, so name the ports explicitly.

### Set a URL path

Use `url-path` to append a path to the generated app URL:

```yaml
url-path: /admin
```

The UI URL then ends with `/admin`.

## YAML reference

A YAML document defines one app. The app-level section contains metadata, and the `services` section contains one or more container definitions.

### App-level fields

| Field | Type | Description |
| :-- | :-- | :-- |
| `name` | *string* | Unique name of the app. |
| `descr` | *string* | Description of the app. |
| `page` | *string* | URL of the project page, shown as the `project-page` property. |
| `category` | *string* | Classification group shown in the app list. |
| `default-credentials` | *string* | Login credentials in `username:password` format. Informative only. |
| `icon` | *string* | URL of an icon shown in WebFig. |
| `url-path` | *string* | Path appended to the app URL, for example `/login` or `/web`. |
| `auto-update` | *boolean* | Update the app when a new image is available. |
| `supported-archs` | *list of strings* | Supported architectures: `arm`, `arm64`, `arm_v5`, and `x86`. The catalog uses this list to select apps for the device. |
| `compatible-boards` | *list of strings* | Supported board names, for example `RDS2216`. The `*` wildcard is accepted. The catalog uses this list to select apps for the device. |
| `services` | *map* | Container service definitions. At least one service is required. |
| `volumes` | *map* | Named volume declarations used by the services. |
| `secrets` | *map* | Secret names referenced with `[secret:name]` in `environment`. |
| `configs` | *map* | Configuration file declarations mounted into the services. |
| `networks` | *map* | Network declarations used by the services. |

Custom apps remain visible even when their `supported-archs` value does not match the device.

### Service fields

| Field | Type | Description |
| :-- | :-- | :-- |
| `image` | *string* | App image to use for the container. Required. |
| `container_name` | *string* | Name used for the container in `/container`. |
| `command` | *string* | Startup command executed inside the container. |
| `entrypoint` | *string* | Executable used as the container entry point. |
| `environment` | *list or map* | Environment variables passed to the container. |
| `volumes` | *list* | Mount points attached to the container. |
| `ports` | *list* | Port mappings from the router to the container. |
| `expose` | *list* | Ports exposed to other containers without publishing them on the router. |
| `restart` | *string* | Restart policy: `unless-stopped`, `always`, or `on-failure`. |
| `depends_on` | *list* | Service names that must start before this service. |
| `healthcheck` | *map* | Probe that checks whether the service is running. |
| `shm_size` | *string* | Shared memory size, for example `512mb` or `1gb`. |
| `stop_grace_period` | *string* or *int* | Timeout for graceful shutdown, for example `30s` or `0`. |
| `devices` | *list* | Hardware devices passed through to the container. |
| `user` | *string* | Linux user or UID the container runs as. |
| `hostname` | *string* | Hostname set in the container. |
| `security_opt` | *list* | Container security options. |
| `build` | *map* | Build configuration for a locally built image. |
| `secrets` | *list* | Secret names available to this service as files at `/run/secrets/<name>`. |
| `configs` | *list* | Configuration files mounted into this service. |

### Healthcheck

A health check probes the service and considers it healthy when the command exits with code 0. Use `CMD` with separate arguments for an executable:

```yaml
healthcheck:
  test: ["CMD", "wget", "-qO-", "http://localhost/"]
  interval: 30s
  retries: 3
  start_period: 30s
  timeout: 10s
```

Use `CMD-SHELL` when the command contains shell syntax such as `||` or a pipeline:

```yaml
healthcheck:
  test: ["CMD-SHELL", "wget -qO- http://localhost/ || exit 1"]
  interval: 30s
  retries: 3
  start_period: 30s
  timeout: 10s
```

With `CMD`, each list element becomes one argument. A shell expression placed in a single `CMD` argument is passed as text and fails.

### Runtime placeholders

Environment values and `default-credentials` can contain placeholders that RouterOS replaces when the app runs.

| Placeholder | Description |
| :-- | :-- |
| `[accessIP]` | IP address or hostname used to access the app from outside. |
| `[accessPort]` | Router port mapped to the app web interface. |
| `[accessProto]` | Protocol used to access the app: `http` or `https`. |
| `[containerIP]` | IP address assigned to the container. |
| `[containerInterface]` | Name of the VETH interface inside the container. The name is limited to 15 characters. |
| `[routerIP]` | IP address of the router from `/app/settings router-ip`. |
| `[networkRouterIP]` | Router IP address on the app network. |
| `[env:variable]` | Value of an environment variable of the app. |
| `[env:service:variable]` | Value of an environment variable of the named service. |
| `[secret:name]` | Value of the secret declared in the app-level `secrets` section. |

Example environment values:

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
      - data:/data
      - appdata/conf:/etc/app
```

`data` is a named volume in the app storage. A path such as `appdata/conf` is a subdirectory of the app storage and is mounted at `/etc/app`.

### Secrets

Declare secrets in the app-level `secrets` section and reference them with `[secret:name]`. RouterOS generates the value when the app runs:

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

To mount a secret as a file, list it under the service. The file is available at `/run/secrets/<name>`:

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

Configs provide configuration files to containers as text. Declare the content in the app-level `configs` section and mount it into a service with `source`, `target`, and optional `mode`:

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

`source` is the name of the app-level config declaration, `target` is the path inside the container, and `mode` is the file permission.

### Networks

By default, an app runs on an internal network behind NAT and services are reached through mapped ports. To place the app directly on a network, define the default network with an external network:

```yaml
networks:
  default:
    name: lan
    external: true
```

The app then attaches its VETH interface to the LAN bridge from `/app/settings`.

### Custom app store

A custom app store is a YAML array in which every element is an app definition. The file must be reachable by the router:

```yaml
- name: code-server
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

Add more list items to publish more apps.

## App properties

The app menu has the following properties. `/app/add` creates new apps disabled.

| Property | Type | Default | Description |
| :-- | :-- | :-- | :-- |
| **auto-update** | *yes* &#124; *no* | *no* | Checks for a new image when the app starts after a reboot. |
| **check-certificate** | *yes* &#124; *no* | *yes* | Verifies the registry certificate against the router certificate store. |
| **container-command-lines** | *string* | *(empty)* | Container commands generated from the YAML. |
| **devices** | *string* | *(empty)* | Additional hardware devices passed to the container. |
| **disabled** | *yes* &#124; *no* | *yes* | Whether the app is disabled. New apps are created disabled. |
| **environment** | *string* | *(empty)* | Environment variables in `service:key=value` form. |
| **extra-mounts** | *string* | *(empty)* | Additional mount points attached to the container. |
| **firewall-redirects** | *string* | *(empty)* | Port redirects in `router-port:container-port:protocol:name` form. |
| **network** | *default* &#124; *lan* &#124; *internal* | *default* | Network used by the app. `default` uses the app's default network. |
| **network-outgoing-access** | *yes* &#124; *no* | *yes* | Allows outgoing connections from the app. When set to `no`, RouterOS adds a mangle drop rule. |
| **network-pvid** | *integer* | *1* | PVID of the app's bridge port. |
| **required-hw-devices** | *string* | *(empty)* | Hardware devices that must be present for the app to start. |
| **required-mounts** | *string* | *(empty)* | Mount directories required by the app. |
| **use-https** | *yes* &#124; *no* | *yes* | Uses HTTPS and the reverse proxy for the app URL. |
| **yaml** | *string* | *(empty)* | Compose YAML that defines the app. |

Read-only values:

| Property | Description |
| :-- | :-- |
| **app-size** | Size of the app image in MiB. |
| **app-store-url** | URL of the custom app store the app came from. |
| **data-size** | Size of the app data. |
| **default-credentials** | Default login credentials from the YAML. |
| **default-network** | Default network from the YAML. |
| **description** | App description from the YAML. |
| **interface** | VETH interface used by the app. |
| **ip-address** | IP address assigned to the VETH interface. |
| **memory-current** | Current memory use of the app. |
| **name** | App name. |
| **project-page** | Project page URL from the YAML. |
| **status** | Current startup or error state. Empty while the app is running. |
| **ui-url** | Generated URL for the app web interface. |
| **variables-to-use-in-environment** | Placeholders and their current values. |

The `/app/settings` parameters are documented in the CLI reference.

## Technical details

An enabled app creates the following objects:

- A VETH interface named `veth-app-<app>`.
- A bridge port on the internal bridge or the LAN bridge.
- For an internal network, the `internal` bridge, the `172.18.0.1/24` address, and a source NAT masquerade rule.
- One destination NAT rule for each mapped port.
- A reverse proxy rule for the `web` port when `use-https=yes`.
- One container per service, named `app-<app>-<service>`.

Storage paths on the selected disk:

- `<disk>/apps/layers` holds shared image layers.
- `<disk>/apps/<app>/<service>_root` holds the container root directory.
- `<disk>/apps/<app>/<volume>` holds named volumes.
- `<disk>/apps/<app>/secret-<name>` holds secret files.
- `<disk>/apps/<app>/config-<name>` holds configuration files.

Set `router-ip` before enabling an app so that its generated URLs and environment values use the final address.

## Related topics

- [Container](../) for manual container configuration.
- [VETH](../veth) for virtual Ethernet interfaces.
- [Reverse proxy](../../network-management/proxy/reverse-proxy#container-apps) for HTTPS app URLs.
- [Certificates](../../authentication-authorization-accounting/certificates) for certificate management.
- [List of available Apps](available-apps).
