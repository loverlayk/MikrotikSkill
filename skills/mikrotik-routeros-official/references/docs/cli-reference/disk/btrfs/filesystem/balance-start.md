# balance-start

> RouterOS command reference for /disk/btrfs/filesystem/balance-start.

-----------

## disk/btrfs/filesystem/balance-start 
**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="data-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">Profile to convert the `data` chunks to: `single` stores chunks once (only sensible with a single device), `dup` stores them twice on the same device, the `raid*` profiles spread them across multiple devices. Change the profiles after [`add-device`](add-device) to turn a single-disk file system into a Btrfs RAID, for example `data-profile=raid1`.</ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">Profile to convert the `meta` (metadata) chunks to. Metadata is small compared to data, so `dup` (default for a single device) or `raid1` are the common choices.</ArgTableRow>
<ArgTableRow arg="system-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">Profile to convert the `system` chunks to; keep it the same as `metadata-profile`.</ArgTableRow>
<ArgTableRow arg="data-usage" typ="range">Only relocate data chunks that are at most this percentage full, for example `data-usage=50` skips chunks that are more than half full. Balancing is faster but incomplete with a lower value.</ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="range">Only relocate metadata chunks that are at most this percentage full.</ArgTableRow>
<ArgTableRow arg="system-usage" typ="range">Only relocate system chunks that are at most this percentage full.</ArgTableRow>
</ArgTable>
