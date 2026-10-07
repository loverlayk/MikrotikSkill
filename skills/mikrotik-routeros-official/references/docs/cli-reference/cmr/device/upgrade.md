# upgrade

> Starts an upgrade (job) for the selected devices. The upgrade runs as a job in /cmr/upgrade/job, with the same job states and result counters.

-----------

## cmr/device/upgrade 
**Package:** cmr
**Type:** Command

Starts an upgrade (job) for the selected devices. The upgrade runs as a job in [`/cmr/upgrade/job`](../upgrade/job), with the same job states and result counters.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="L" typ="controller">Include the CMR server itself (self-client).</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices to upgrade using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="order" typ="object" unset="1">Execution order (by labels).</ArgTableRow>
<ArgTableRow arg="channel" typ="alt" unset="1">Upgrade channel (`long-term`, `stable`, `testing`, or `development`) or a pinned version, for example `channel=7.24.4`.</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="super { time: date
, [day] [ @enum (sun | mon | tue | wed | thu | fri | sat) { sun:1, mon:2, tue:3, wed:4, thu:5, fri:6, sat:7 }]
 }" unset="1">When the upgrade starts: a time with an optional weekday given after `@`, for example `14:00:00` or `00:00:00@sat`.</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum (parallel | sequential)" unset="1">How devices are upgraded: `parallel` upgrades all covered devices at the same time; `sequential` upgrades them one after another and waits for each to finish. With `continue-order` the devices are processed per label group in the order given by `order`: in `parallel` the devices of each group are upgraded together, in `sequential` one at a time. Default: `parallel`.</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum (continue | stop | continue-order)" unset="1">Behaviour if a device fails: `continue` skips the failed device and continues with the rest; `stop` stops the whole upgrade on the first failure and does not continue with the remaining devices or with the next label group (with `strategy=parallel` it requires `order`, and `parallel` combined with `stop` without `order` is rejected); `continue-order` skips the failed device and continues with the next label group, processing the labels one group after another in the order given by `order`. With `sequential` the rest of the failed device's group is skipped; with `parallel` only the failed device is abandoned and devices already in progress in the group finish. Default: `continue`.</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { package: string
 }" unset="1">Packages to upgrade.</ArgTableRow>
</ArgTable>
