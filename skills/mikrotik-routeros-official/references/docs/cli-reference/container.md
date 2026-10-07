# container

> RouterOS directory reference for /container.

-----------

## container 
**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="stopped"></ArgTableRow>
<ArgTableRow arg="N" typ="starting"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="T" typ="stopping"></ArgTableRow>
<ArgTableRow arg="E" typ="downloading/extracting"></ArgTableRow>
<ArgTableRow arg="D" typ="deleting"></ArgTableRow>
<ArgTableRow arg="F" typ="download/extract failed"></ArgTableRow>
<ArgTableRow arg="C" typ="starting-with-healthcheck"></ArgTableRow>
<ArgTableRow arg="H" typ="healthy"></ArgTableRow>
<ArgTableRow arg="U" typ="unhealthy"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file"></ArgTableRow>
<ArgTableRow arg="remote-image" typ="string"></ArgTableRow>
<ArgTableRow arg="ignore-remote-image-change" typ="bool"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="privileged" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="env" typ="object { key-and-value-element: super { !
, key-and-value: composite { key: string
, value: string
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="envlists" typ="multi { envlist: enum
 }"></ArgTableRow>
<ArgTableRow arg="entrypoint" typ="multi { cmd: string
 }"></ArgTableRow>
<ArgTableRow arg="cmd" typ="multi { cmd: string
 }"></ArgTableRow>
<ArgTableRow arg="shell" typ="multi { cmd: string
 }"></ArgTableRow>
<ArgTableRow arg="stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS) { 1-SIGHUP:1, 2-SIGINT:2, 3-SIGQUIT:3, 4-SIGILL:4, 5-SIGTRAP:5, 6-SIGABTR:6, 7-SIGBUS:7, 8-SIGFPE:8, 9-SIGKILL:9, 10-SIGUSR1:10, 11-SIGSEGV:11, 12-SIGUSR2:12, 13-SIGPIPE:13, 14-SIGALRM:14, 15-SIGTERM:15, 16-SIGSTKFLT:16, 17-SIGCHLD:17, 18-SIGCONT:18, 19-SIGSTOP:19, 20-SIGTSTP:20, 21-SIGTTIN:21, 22-SIGTTOU:22, 23-SIGURG:23, 24-SIGXCPU:24, 25-SIGXFSZ:25, 26-SIGVTALRM:26, 27-SIGPROF:27, 28-SIGWINCH:28, 29-SIGIO:29, 30-SIGPWR:30, 31-SIGSYS:31 }"></ArgTableRow>
<ArgTableRow arg="stop-time" typ="time"></ArgTableRow>
<ArgTableRow arg="root-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="mount" typ="object { src-dst-mode: composite { src: file
, dst-mode: composite { dst: string
, mode: enum (rw | ro | rw,noexec | ro,noexec)
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="tmpfs" typ="object { dst-size-mode: composite { dst: string
, size-mode: composite { size: num
, mode: string
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="mountlists" typ="multi { mountlist: enum
 }"></ArgTableRow>
<ArgTableRow arg="shm-size" typ="num"></ArgTableRow>
<ArgTableRow arg="dns" typ="multi { dns-server-ip: address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="default-dns" typ="multi { dns-server-ip: address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="hostname" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-name" typ="string"></ArgTableRow>
<ArgTableRow arg="workdir" typ="string"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="start-on-boot" typ="bool"></ArgTableRow>
<ArgTableRow arg="stop-on-unhealthy" typ="bool"></ArgTableRow>
<ArgTableRow arg="restart-policy" typ="enum (no | on-failure | always)"></ArgTableRow>
<ArgTableRow arg="restart-max-count" typ="num"></ArgTableRow>
<ArgTableRow arg="restart-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu-list" typ="multi { cpu: enum
 }"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="num"></ArgTableRow>
<ArgTableRow arg="swap-max" typ="num"></ArgTableRow>
<ArgTableRow arg="devices" typ="object { dst-size-mode: composite { device: enum
, container-dev-name: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="hosts" typ="object { host-entry: composite { host-name: string
, host-addr: address (flags=46)
 }
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-cmd" typ="multi { healthcheck-cmd: string
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-period" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="healthcheck-status" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tag" typ="string"></ArgTableRow>
<ArgTableRow arg="os" typ="string"></ArgTableRow>
<ArgTableRow arg="arch" typ="string"></ArgTableRow>
<ArgTableRow arg="env-current" typ="object { key-and-value: composite { key: string
, value: string
 }
 }"></ArgTableRow>
<ArgTableRow arg="default-entrypoint" typ="string"></ArgTableRow>
<ArgTableRow arg="default-cmd" typ="string"></ArgTableRow>
<ArgTableRow arg="default-shell" typ="string"></ArgTableRow>
<ArgTableRow arg="default-stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS) { 1-SIGHUP:1, 2-SIGINT:2, 3-SIGQUIT:3, 4-SIGILL:4, 5-SIGTRAP:5, 6-SIGABTR:6, 7-SIGBUS:7, 8-SIGFPE:8, 9-SIGKILL:9, 10-SIGUSR1:10, 11-SIGSEGV:11, 12-SIGUSR2:12, 13-SIGPIPE:13, 14-SIGALRM:14, 15-SIGTERM:15, 16-SIGSTKFLT:16, 17-SIGCHLD:17, 18-SIGCONT:18, 19-SIGSTOP:19, 20-SIGTSTP:20, 21-SIGTTIN:21, 22-SIGTTOU:22, 23-SIGURG:23, 24-SIGXCPU:24, 25-SIGXFSZ:25, 26-SIGVTALRM:26, 27-SIGPROF:27, 28-SIGWINCH:28, 29-SIGIO:29, 30-SIGPWR:30, 31-SIGSYS:31 }"></ArgTableRow>
<ArgTableRow arg="default-workdir" typ="string"></ArgTableRow>
<ArgTableRow arg="restart-count" typ="num"></ArgTableRow>
<ArgTableRow arg="default-user" typ="string"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="num"></ArgTableRow>
<ArgTableRow arg="swap-current" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="container-size" typ="num"></ArgTableRow>
<ArgTableRow arg="data-size" typ="num"></ArgTableRow>
<ArgTableRow arg="image-id" typ="string"></ArgTableRow>
<ArgTableRow arg="config-json" typ="string"></ArgTableRow>
<ArgTableRow arg="layers" typ="multi { layer: enum
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-cmd" typ="multi { default-healthcheck-cmd: string
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-period" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-retries" typ="num"></ArgTableRow>
</ArgTable>
