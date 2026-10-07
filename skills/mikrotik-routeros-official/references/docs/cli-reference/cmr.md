# cmr

> Settings of the CMR server, the router that controls a fleet of CMR clients. Enable the server with enabled=yes; it then distributes software packages, discovers and tracks the devices, and evaluates the alert rules...

-----------

## cmr 
**Package:** cmr
**Type:** Settings Directory

Settings of the CMR server, the router that controls a fleet of CMR clients. Enable the server with `enabled=yes`; it then distributes software packages, discovers and tracks the devices, and evaluates the alert rules that monitor them. See [CMR](../../management-tools/cmr) for an overview of the package.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (yes | no)">Whether CMR server is enabled or not. Default: no.</ArgTableRow>
<ArgTableRow arg="local-id" typ="string" unset="1">Unique CMR specific device identifier.</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password | confirm)" unset="1">
Defines what the remote device must do before this device accepts the pairing:
- **none** - this device accepts pairing automatically, without additional checks
- **password** - the remote device may approve pairing by giving the username and password of a RouterOS user on this device; CMR has no separate pairing password
- **confirm** - pairing must be approved locally by running the `pair` command on this device; approval from the remote side is not possible
</ArgTableRow>
<ArgTableRow arg="packages-directory" typ="file" unset="1">Directory on the server's file system containing RouterOS packages that the server distributes to the managed devices and serves from when it matches the version an upgrade needs. The value is picked from the router's file list: directory entries are entered with a trailing slash (for example `cmrpkgs/`), plain files without one. Packages are resolved individually: a package already present here for the required version is sent directly without downloading it again, and only the missing packages are downloaded and cached. A value that does not point to an existing directory is kept but cannot be used; the `/cmr` menu then shows `directory does not exist, using memory` and packages are served from memory instead.</ArgTableRow>
<ArgTableRow arg="packages-cache-type" typ="enum (directory | memory)" unset="1">Where the server stores the package files it downloads: `directory` keeps them on the server's storage, `memory` keeps them in RAM. With `directory`, the server stores them in a `cmrcache` subdirectory of `packages-directory`, which it creates in the router's file list; packages that are already present in `packages-directory` are served from there without being downloaded. When the directory is missing or unusable the server reports `directory does not exist, using memory` in the `/cmr` menu, stores the packages in RAM instead, and switches back to the directory when it becomes available again.</ArgTableRow>
<ArgTableRow arg="packages-cache-limit" typ="num" unset="1">Maximum amount of package data held in the cache, in megabytes. A value larger than the available RAM or storage is accepted and the server shows an informational note; the cache then uses all the space that is available and evicts older entries when a file larger than the remaining space must be stored.</ArgTableRow>
<ArgTableRow arg="upgrade-check-interval" typ="time" unset="1">How often the CMR server checks the MikroTik update servers for available versions. The minimum value is 1 minute. Default: `10h`.</ArgTableRow>
<ArgTableRow arg="track-topology" typ="bool" unset="1">Enables network topology discovery. Fetches the following information from CMR clients: routes, WiFi registration table, ARP table, neighbors, DHCP state, and interface states. This information is required for full CMR functionality, for example, automatic link discovery in the `/cmr/layout` menu. Default: yes.</ArgTableRow>
<ArgTableRow arg="fetch-comments" typ="bool" unset="1">Enables fetching of comments for interfaces/ports and the WiFi registration table. Default: yes.</ArgTableRow>
<ArgTableRow arg="controller-addresses" typ="multi { array-id, address: address (flags=46D)
 }" unset="1">CMR server IP addresses that are sent to the devices when the controller address cannot be discovered automatically (MNDP, or DNS: the client resolves `_cmr._tcp.lan` and `_cmr._tcp.` followed by the domain name from DHCP).</ArgTableRow>
<ArgTableRow arg="apptraffic-devices" typ="object" unset="1">Select devices using labels for which to collect app traffic data. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. Default: `gateway`; `all` selects every device.</ArgTableRow>
<ArgTableRow arg="auto-labels" typ="alt { auto-labels: enum (none | all) { none:0, all:0xffff }
, auto-labels: ubit (version, architecture, model, board-name, identity, address)
 }" unset="1">Whether to fetch labels information from the connected cmr-client devices. Can be configured to fetch only specific labels. Default: all.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="self-client-id" typ="string" unset="1">ID that is used by CMR server to connect to itself, for it to be displayed in a device list.</ArgTableRow>
</ArgTable>
