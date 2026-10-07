# file

> The /file menu lists user files on the router's storage and manages them: creating, editing, copying and deleting files and directories. For an uploaded RouterOS .npk file, the menu also shows package details, such...

-----------

## file 
**Type:** Directory

The `/file` menu lists user files on the router's storage and manages them: creating, editing, copying and deleting files and directories. For an uploaded RouterOS `.npk` file, the menu also shows package details, such as the architecture and build time. Files and directories shared through [File Share](../../network-management/cloud/file-share) (Back To Home) are marked with the shared flag and have a `url` property with the share link. See the [Files](../../system-information-and-utilities/files) guide.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="shared">The file or directory is shared through [File Share](../../network-management/cloud/file-share) (Back To Home).</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file" mandatory="1">Name of the file or directory, including the path. A leading `/` is optional.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (file | directory)">Type of the entry. Default: file.</ArgTableRow>
<ArgTableRow arg="contents" typ="string">The actual content of the file. Limited to just under 60 KiB (61439 bytes): creating a file with longer contents fails, and files larger than that return nothing here. Use [`/file/read`](./read) to read larger files.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="size" typ="num">File size in bytes.</ArgTableRow>
<ArgTableRow arg="last-modified" typ="date">Time when the file was created or last modified.</ArgTableRow>
<ArgTableRow arg="package-name" typ="string">Name of the installable package. Applies only to RouterOS .npk files.</ArgTableRow>
<ArgTableRow arg="package-version" typ="string">Version of the installable package. Applies only to RouterOS .npk files.</ArgTableRow>
<ArgTableRow arg="package-build-time" typ="date">Time when the package was built. Applies only to RouterOS .npk files.</ArgTableRow>
<ArgTableRow arg="package-architecture" typ="string">Architecture that the package is built for. Applies only to RouterOS .npk files.</ArgTableRow>
<ArgTableRow arg="url" typ="string" syscap="cloud-vpn">URL for cloud VPN file sharing. Shown for files and directories shared through [File Share](../../network-management/cloud/file-share) (Back To Home).</ArgTableRow>
</ArgTable>
