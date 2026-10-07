# key

> Symmetric keys for NTP authentication, selected by their key ID in /system/ntp/client/servers and /system/ntp/server. The key value is sensitive: it is not shown in print or saved in export output. See the NTP guide.

-----------

## system/ntp/key 
**Type:** Directory

Symmetric keys for NTP authentication, selected by their key ID in [`/system/ntp/client/servers`](./client/servers) and [`/system/ntp/server`](./server). The key value is sensitive: it is not shown in `print` or saved in `export` output. See the [NTP](../../../system-information-and-utilities/ntp) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-id" typ="num" mandatory="1">Key identifier, referenced by `auth-key` in the client and server configuration.</ArgTableRow>
<ArgTableRow arg="key-val" typ="string" mandatory="1">The shared secret. Not included in `export` output.</ArgTableRow>
</ArgTable>
