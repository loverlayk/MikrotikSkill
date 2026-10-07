# local-update

> Instead of connecting directly to MikroTik servers, you can upload package files to one of your local RouterOS devices and use it as a local package server.

-----------

## system/package/local-update 
**Type:** Directory

Instead of connecting directly to MikroTik servers, you can upload package files to one of your local RouterOS devices and use it as a local package server.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="download" typ="bool">Whether to download available packages from the local package server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="source" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">IP address of the local package server.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the package.</ArgTableRow>
<ArgTableRow arg="version" typ="string">Version of the package.</ArgTableRow>
<ArgTableRow arg="status" typ="enum (installed | downloaded | downloading | scheduled | available) { installed:0, downloaded:1, downloading:2, scheduled:3, available:4 }">Current status of the package.</ArgTableRow>
<ArgTableRow arg="completed" typ="num">Download completion percentage.</ArgTableRow>
</ArgTable>
