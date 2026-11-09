# settings

> RouterOS settings reference for /app/settings.

-----------

## app/settings 
**Syscap:** app
**Package:** container
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Disk used for app images, data, and downloads. The setup wizard sets it. Default: none.</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">IP address at which clients reach the router. Apps use it in generated URLs and port-forwarding rules. Default: none. An app enabled without it waits with `status=waiting for router ip to be configured`.</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">Bridge used as the LAN. Apps whose default network is `lan` attach their VETH interface to it. Default: none.</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">Directory for app media files. Default: none; RouterOS uses `assumed-media-path`.</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">Directory for downloaded app content. Default: none; RouterOS uses `assumed-download-path`.</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">Whether WebFig shows links to enabled apps on the login page. Default: yes.</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">Default automatic update setting for installed apps. Each app can override it with its own `auto-update` property. Default: no.</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, src-and-dst: composite { src: string
, dst: string
 }
 }">Registry mirror mappings in `source:destination` form, for example `*:mirror.example.com` to use one mirror for every registry. Default: none.</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, app-store-url: string
 }">URLs of custom app stores. Each URL must return a YAML array of app definitions. Default: none.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">Automatically detected router IP address, when available.</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none }">Automatically detected LAN bridge, when available.</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">Default media directory on the selected app disk.</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">Default download directory inside the media directory.</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string">Status of the certificate used for app HTTPS URLs. `ok` means the certificate is usable.</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">Name of the certificate used for app HTTPS URLs.</ArgTableRow>
</ArgTable>
