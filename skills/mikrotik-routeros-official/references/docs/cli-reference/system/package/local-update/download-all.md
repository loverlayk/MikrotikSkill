# download-all

> Download the packages from the local package server that are installed on the router and match its architecture. Downloaded packages are saved in the root directory and installed at the next reboot.

-----------

## system/package/local-update/download-all 
**Type:** Command

Download the packages from the local package server that are installed on the router and match its architecture. Downloaded packages are saved in the root directory and installed at the next reboot.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="download-beta" typ="bool">Whether to include beta versions. Without it, a beta version on the server is not downloaded.</ArgTableRow>
<ArgTableRow arg="reboot-after-download" typ="bool">Whether to automatically reboot the device after all packages finish downloading.</ArgTableRow>
</ArgTable>
