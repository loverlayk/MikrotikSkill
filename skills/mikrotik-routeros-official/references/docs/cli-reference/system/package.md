# package

> Commands executed in this menu will take place only on the restart of the router. Until then, you can freely schedule or revert the set actions.

-----------

## system/package 
**Type:** Directory

Commands executed in this menu will take place only on the restart of the router. Until then, you can freely schedule or revert the set actions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The package is disabled, or it is not installed yet (with `A`).</ArgTableRow>
<ArgTableRow arg="A" typ="available">The package is available on the download server but not installed. It is listed after `/system/package/update/check-for-updates`; `enable` and `apply-changes` download and install it.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the package.</ArgTableRow>
<ArgTableRow arg="version" typ="string">Version of the package.</ArgTableRow>
<ArgTableRow arg="build-time" typ="date">Date and time the package was built.</ArgTableRow>
<ArgTableRow arg="scheduled" typ="enum ( | scheduled for uninstall | scheduled for disable | scheduled for enable | Use `apply-changes` to proceed with install) { :0, scheduled for uninstall:1, scheduled for disable:2, scheduled for enable:3, Use `apply-changes` to proceed with install:4 }">Scheduled action for the package after the next reboot.</ArgTableRow>
<ArgTableRow arg="bundle" typ="enum">The bundle package this package belongs to.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of the package in bytes.</ArgTableRow>
</ArgTable>
