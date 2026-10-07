# back-to-home-file

> Directories and files shared with File Share. Each share gets a secret link under .routingthecloud.net, and the service runs while at least one share exists. For examples, see File Share. The service state is in...

-----------

## ip/cloud/back-to-home-file 
**Syscap:** cloud-vpn
**Type:** Directory

Directories and files shared with File Share. Each share gets a secret link under `<serial>.routingthecloud.net`, and the service runs while at least one share exists. For examples, see [File Share](../../../../network-management/cloud/file-share). The service state is in [`settings`](settings/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The share is disabled, and its link returns HTTP 404.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The share cannot be served yet, for example while the router requests the certificate. A comment line shows the reason, such as `getting cert status: requesting SSL certificate`.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="path" typ="file">Directory or file to share, as `/file/print` shows it, for example `usb1/photos`. The router shows it with a leading `/`.</ArgTableRow>
<ArgTableRow arg="allow-uploads" typ="bool">Whether visitors of a directory share can upload files and create folders in it. Without it, the router refuses uploads with HTTP 403. Default: no.</ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }">When the share stops working: `never`, a date and time such as `"2026-10-01 00:00:00"`, or a time interval such as `1h`. The router converts an interval to a date. `never` keeps the share until you remove it.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key" typ="string">Random key of the share, the last part of `url`.</ArgTableRow>
<ArgTableRow arg="url" typ="string">Link to the share page, `https://<serial>.routingthecloud.net/s/<key>`. A directory share lists its files; anyone who has the link can open it.</ArgTableRow>
<ArgTableRow arg="direct-url" typ="string">`url` with `?dl`. It downloads the shared file, or the whole directory as `download.zip`.</ArgTableRow>
<ArgTableRow arg="downloads" typ="num">Number of direct downloads of the share. Opening the share page does not count.</ArgTableRow>
</ArgTable>
