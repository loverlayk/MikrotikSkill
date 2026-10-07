# settings

> RouterOS settings reference for /app/settings.

-----------

## app/settings 
**Syscap:** app
**Package:** container
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Global setting that specifies which disk will be used for storage operations</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">Manually specifies the IP address at which the current RouterOS device can be reached</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">Manually specifies the bridge interface that represents the local area network</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">Manually specifies the directory path where all media files will be stored</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">Manually specifies the directory path where all downloaded content will be stored</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">Controls whether links to enabled applications are displayed on the WebFig login page</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">Global setting that enables automatic updates for all installed applications packages</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, src-and-dst: composite { src: string
, dst: string
 }
 }">Specifies one or more registry mirror URLs for container image retrieval</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, app-store-url: string
 }">URL to a custom app store. Must point to a YAML array where each application is an element</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">Automatically detected network IP address of the RouterOS device</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none }">Automatically detected bridge interface used for LAN connectivity</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">Default media storage path, typically located on the system disk</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">Default download directory path, typically located within the media storage area</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>
