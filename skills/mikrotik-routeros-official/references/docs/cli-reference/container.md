# container

> Containers run Linux container images (OCI) on the router. The container package must be installed and the container feature enabled in device-mode. See Container.

-----------

## container 
**Package:** container
**Type:** Directory

Containers run Linux container images (OCI) on the router. The `container` package must be installed and the container feature enabled in device-mode. See [Container](../../containers/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="stopped">The container is stopped.</ArgTableRow>
<ArgTableRow arg="N" typ="starting">The container is starting.</ArgTableRow>
<ArgTableRow arg="R" typ="running">The container is running.</ArgTableRow>
<ArgTableRow arg="T" typ="stopping">The container is stopping.</ArgTableRow>
<ArgTableRow arg="E" typ="downloading/extracting">The image is being downloaded and extracted.</ArgTableRow>
<ArgTableRow arg="D" typ="deleting">The container is being deleted.</ArgTableRow>
<ArgTableRow arg="F" typ="download/extract failed">Downloading or extracting the image failed.</ArgTableRow>
<ArgTableRow arg="C" typ="starting-with-healthcheck">The container is starting and its healthcheck has not passed yet.</ArgTableRow>
<ArgTableRow arg="H" typ="healthy">The healthcheck passes.</ArgTableRow>
<ArgTableRow arg="U" typ="unhealthy">The healthcheck fails.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file">Image archive to create the container from, for example from `podman save` or `/container/save`.</ArgTableRow>
<ArgTableRow arg="remote-image" typ="string">Image to download from the registry, for example `pihole/pihole` or `nginx:alpine`. The registry is set in `/container/config`.</ArgTableRow>
<ArgTableRow arg="ignore-remote-image-change" typ="bool"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool">Verifies the registry's HTTPS certificate when the image is downloaded. Default: `yes`.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the container.</ArgTableRow>
<ArgTableRow arg="privileged" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }" mandatory="1">veth interface of the container (see [veth](../interface/veth)).</ArgTableRow>
<ArgTableRow arg="env" typ="object { key-and-value-element: super { !
, key-and-value: composite { key: string
, value: string
 }
 }
 }">Environment variables set directly on the container, for example `env=FOO=1,BAR=2`.</ArgTableRow>
<ArgTableRow arg="envlists" typ="multi { envlist: enum
 }">Lists of environment variables from `/container/envs` to use in the container.</ArgTableRow>
<ArgTableRow arg="labels" typ="object { key-and-value: composite { key: string
, value: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="entrypoint" typ="multi { cmd: string
 }">Executable that runs when the container starts, replacing the image's entrypoint. Example: `/bin/sh`.</ArgTableRow>
<ArgTableRow arg="cmd" typ="multi { cmd: string
 }">Arguments for the entrypoint, or the command to run, replacing the image's default command. A list: when it has several items, separated by commas, each item is passed as one argument, spaces included (`cmd="-c,print('hello world')"` passes two arguments). A single item is split into arguments at spaces, and single quotes keep words together (`cmd="-c 'b c'"` passes `-c` and `b c`). Double quotes inside the value also separate items, so the text between them stays one argument, spaces included; to pass arguments with spaces, use commas.</ArgTableRow>
<ArgTableRow arg="shell" typ="multi { cmd: string
 }">Shell used to run commands in the container, replacing the image's default shell.</ArgTableRow>
<ArgTableRow arg="stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS) { 1-SIGHUP:1, 2-SIGINT:2, 3-SIGQUIT:3, 4-SIGILL:4, 5-SIGTRAP:5, 6-SIGABTR:6, 7-SIGBUS:7, 8-SIGFPE:8, 9-SIGKILL:9, 10-SIGUSR1:10, 11-SIGSEGV:11, 12-SIGUSR2:12, 13-SIGPIPE:13, 14-SIGALRM:14, 15-SIGTERM:15, 16-SIGSTKFLT:16, 17-SIGCHLD:17, 18-SIGCONT:18, 19-SIGSTOP:19, 20-SIGTSTP:20, 21-SIGTTIN:21, 22-SIGTTOU:22, 23-SIGURG:23, 24-SIGXCPU:24, 25-SIGXFSZ:25, 26-SIGVTALRM:26, 27-SIGPROF:27, 28-SIGWINCH:28, 29-SIGIO:29, 30-SIGPWR:30, 31-SIGSYS:31 }">Linux signal sent to stop the container. Without it, the image's default stop signal is used (`default-stop-signal`).</ArgTableRow>
<ArgTableRow arg="stop-time" typ="time">Time limit for the container to stop gracefully before the stop signal is sent. Default: `10s`.</ArgTableRow>
<ArgTableRow arg="root-dir" typ="file">Directory where the container's files are stored. Use an attached disk rather than the built-in storage.</ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file">Directory for image layers that can be shared between containers.</ArgTableRow>
<ArgTableRow arg="mount" typ="object { src-dst-mode: composite { src: file
, dst-mode: composite { dst: string
, mode: enum (rw | ro | rw,noexec | ro,noexec)
 }
 }
 }">Mount defined directly on the container, as source on the router and destination in the container.</ArgTableRow>
<ArgTableRow arg="tmpfs" typ="object { dst-size-mode: composite { dst: string
, size-mode: composite { size: num
, mode: string
 }
 }
 }">Temporary file system mount points in the container. Format: `size@dir`, for example `64M@/tmp`.</ArgTableRow>
<ArgTableRow arg="mountlists" typ="multi { mountlist: enum
 }">Lists of mounts from `/container/mounts` to use in the container.</ArgTableRow>
<ArgTableRow arg="shm-size" typ="num">Size of the `/dev/shm` shared memory file system in the container. Default: `64MiB`.</ArgTableRow>
<ArgTableRow arg="dns" typ="multi { dns-server-ip: address (flags=46)
 }">DNS servers for the container. Without it, the container uses the router's DNS servers (`default-dns`).</ArgTableRow>
<ArgTableRow arg="default-dns" typ="multi { dns-server-ip: address (flags=46)
 }">DNS servers taken from the router's `/ip/dns` configuration.</ArgTableRow>
<ArgTableRow arg="hostname" typ="string">Host name of the container.</ArgTableRow>
<ArgTableRow arg="domain-name" typ="string">Domain name of the container.</ArgTableRow>
<ArgTableRow arg="workdir" typ="string">Working directory for the entrypoint and command.</ArgTableRow>
<ArgTableRow arg="logging" typ="bool">Writes the container's output to the RouterOS log (topic `container`). Default: `no`.</ArgTableRow>
<ArgTableRow arg="start-on-boot" typ="bool">Starts the container when the router starts. Default: `no`.</ArgTableRow>
<ArgTableRow arg="stop-on-unhealthy" typ="bool">If set to `yes`, the container is stopped when the healthcheck status becomes unhealthy. Default: `no`.</ArgTableRow>
<ArgTableRow arg="restart-policy" typ="enum (no | on-failure | always)">
When the router restarts the container:
- `no` (default) - never.
- `on-failure` - when it exits with a non-zero code.
- `always` - always restart.
</ArgTableRow>
<ArgTableRow arg="restart-max-count" typ="num">Maximum number of restart attempts within `restart-interval`. Default: `0`.</ArgTableRow>
<ArgTableRow arg="restart-interval" typ="time">Time frame for `restart-max-count`. Default: `0s`.</ArgTableRow>
<ArgTableRow arg="user" typ="string">User and group the container process runs as, for example `0:0`.</ArgTableRow>
<ArgTableRow arg="cpu-list" typ="multi { cpu: enum
 }">CPU cores the container may run on.</ArgTableRow>
<ArgTableRow arg="memory-high" typ="num">Soft memory limit in bytes: above it, the container's processes are throttled and put under memory reclaim pressure. If both this and the global value are set, the lower one applies. Default: `unlimited`.</ArgTableRow>
<ArgTableRow arg="memory-max" typ="num">Hard memory limit in bytes. A container that exceeds it is killed; `/container/print` then shows the comment `killed due to out of memory`. Values below 1 MB are refused. If both this and the global value in `/container/config` are set, the lower one applies. Default: `unlimited`.</ArgTableRow>
<ArgTableRow arg="swap-max" typ="num">Maximum swap space in bytes for the container. Requires swap on the router (see [Swap space](../../hardware/disks/)). Default: `unlimited`.</ArgTableRow>
<ArgTableRow arg="devices" typ="object { dst-size-mode: composite { device: enum
, container-dev-name: string
 }
 }">Router devices passed through to the container, for example `devices=serial0:""`.</ArgTableRow>
<ArgTableRow arg="hosts" typ="object { host-entry: composite { host-name: string
, host-addr: address (flags=46)
 }
 }">Host name to address entries for the container. Format: `host=ip`.</ArgTableRow>
<ArgTableRow arg="healthcheck-cmd" typ="multi { healthcheck-cmd: string
 }">Command that checks the container's application; exit code 0 means healthy. Without it, the image's healthcheck is used (`default-healthcheck-cmd`).</ArgTableRow>
<ArgTableRow arg="healthcheck-interval" typ="time">Time between healthchecks. Image default or `30s`.</ArgTableRow>
<ArgTableRow arg="healthcheck-timeout" typ="time">A check that takes longer counts as failed. Image default or `30s`.</ArgTableRow>
<ArgTableRow arg="healthcheck-start-period" typ="time">Time after the start during which failed checks are not counted. Image default or `0s`.</ArgTableRow>
<ArgTableRow arg="healthcheck-start-interval" typ="time">Time between checks during the start period. Image default or `5s`.</ArgTableRow>
<ArgTableRow arg="healthcheck-retries" typ="num">Failed checks in a row before the container is unhealthy. Image default or `3`.</ArgTableRow>
<ArgTableRow arg="healthcheck-status" typ="string">Result of the last healthcheck and the command's output, for example `good, output:`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tag" typ="string">Full image reference, for example `registry-1.docker.io/library/nginx:alpine`.</ArgTableRow>
<ArgTableRow arg="os" typ="string">Operating system of the image.</ArgTableRow>
<ArgTableRow arg="arch" typ="string">Architecture of the image, for example `amd64`.</ArgTableRow>
<ArgTableRow arg="env-current" typ="object { key-and-value: composite { key: string
, value: string
 }
 }">Environment variables of the running container: from the image, `env` and `envlists`.</ArgTableRow>
<ArgTableRow arg="image-labels" typ="object { key-and-value: composite { key: string
, value: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="default-entrypoint" typ="string">Entrypoint defined in the image.</ArgTableRow>
<ArgTableRow arg="default-cmd" typ="string">Command defined in the image.</ArgTableRow>
<ArgTableRow arg="default-shell" typ="string">Shell defined in the image, for example `/bin/sh -c`.</ArgTableRow>
<ArgTableRow arg="default-stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS) { 1-SIGHUP:1, 2-SIGINT:2, 3-SIGQUIT:3, 4-SIGILL:4, 5-SIGTRAP:5, 6-SIGABTR:6, 7-SIGBUS:7, 8-SIGFPE:8, 9-SIGKILL:9, 10-SIGUSR1:10, 11-SIGSEGV:11, 12-SIGUSR2:12, 13-SIGPIPE:13, 14-SIGALRM:14, 15-SIGTERM:15, 16-SIGSTKFLT:16, 17-SIGCHLD:17, 18-SIGCONT:18, 19-SIGSTOP:19, 20-SIGTSTP:20, 21-SIGTTIN:21, 22-SIGTTOU:22, 23-SIGURG:23, 24-SIGXCPU:24, 25-SIGXFSZ:25, 26-SIGVTALRM:26, 27-SIGPROF:27, 28-SIGWINCH:28, 29-SIGIO:29, 30-SIGPWR:30, 31-SIGSYS:31 }">Stop signal defined in the image.</ArgTableRow>
<ArgTableRow arg="default-workdir" typ="string">Working directory defined in the image.</ArgTableRow>
<ArgTableRow arg="restart-count" typ="num">Number of restarts done by `restart-policy`.</ArgTableRow>
<ArgTableRow arg="default-user" typ="string">User defined in the image.</ArgTableRow>
<ArgTableRow arg="memory-current" typ="num">Memory the container uses now.</ArgTableRow>
<ArgTableRow arg="swap-current" typ="num">Swap the container uses now.</ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num">CPU usage of the container.</ArgTableRow>
<ArgTableRow arg="container-size" typ="num">Size of the container's files.</ArgTableRow>
<ArgTableRow arg="data-size" typ="num">Size of the container's data.</ArgTableRow>
<ArgTableRow arg="image-id" typ="string">Identifier of the image.</ArgTableRow>
<ArgTableRow arg="config-json" typ="string"></ArgTableRow>
<ArgTableRow arg="layers" typ="multi { layer: enum
 }">Image layers used by the container (see `/container/layers`).</ArgTableRow>
<ArgTableRow arg="default-healthcheck-cmd" typ="multi { default-healthcheck-cmd: string
 }">Healthcheck command defined in the image.</ArgTableRow>
<ArgTableRow arg="default-healthcheck-interval" typ="time">Healthcheck interval defined in the image, or `30s`.</ArgTableRow>
<ArgTableRow arg="default-healthcheck-timeout" typ="time">Healthcheck timeout defined in the image, or `30s`.</ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-period" typ="time">Healthcheck start period defined in the image, or `0s`.</ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-interval" typ="time">Healthcheck start interval defined in the image, or `5s`.</ArgTableRow>
<ArgTableRow arg="default-healthcheck-retries" typ="num">Healthcheck retries defined in the image, or `3`.</ArgTableRow>
<ArgTableRow arg="check-update-result" typ="enum (none | checking | up-to-date | update-available)"></ArgTableRow>
</ArgTable>
