# mirror

> You can mirror packages (for all architectures) from your main local package server by using this menu. Downloaded packages are saved into the packs folder in the root directory.

-----------

## system/package/local-update/mirror 
**Type:** Settings Directory

You can mirror packages (for all architectures) from your main local package server by using this menu. Downloaded packages are saved into the `packs` folder in the root directory.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether to enable periodic check and download of packages from the local package server.</ArgTableRow>
<ArgTableRow arg="primary-server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">IP address of the primary local package server.</ArgTableRow>
<ArgTableRow arg="secondary-server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">IP address of the secondary local package server.</ArgTableRow>
<ArgTableRow arg="check-interval" typ="time">Time interval at which the device checks the local package server for new package availability. If a new package is located, the package download begins. Only downloads the packages that are not already present on the device.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username for accessing the local package server.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for accessing the local package server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="software-id" typ="string">Software ID of the device.</ArgTableRow>
</ArgTable>
