# settings

> Settings shared by all DLNA media servers in /ip/media. See DLNA Media Server.

-----------

## ip/media/settings 
**Conditions:** !smips
**Type:** Settings Directory

Settings shared by all DLNA media servers in [`/ip/media`](.). See [DLNA Media Server](../../../storage/dlna).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="thumbnails" typ="string">Comma separated list of filenames (should end with .jpg). If name of a file in a directory matches any filename in the list, that file is treated as a thumbnail to any media file in that directory: it is no longer listed as a picture, and players show it as the cover picture of the other files. See [DLNA Media Server](../../../storage/dlna). Default: empty.</ArgTableRow>
</ArgTable>
