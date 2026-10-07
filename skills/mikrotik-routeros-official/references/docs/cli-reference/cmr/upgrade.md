# upgrade

> An upgrade rule describes when and to which channel to upgrade selected devices (by labels).

-----------

## cmr/upgrade 
**Package:** cmr
**Type:** Directory

An upgrade rule describes when and to which channel to upgrade selected devices (by labels).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Rule is disabled.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Rule is dynamic.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1">Name of the upgrade rule.</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices the rule covers using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. If omitted, the rule covers all connected devices. Default: `all`.</ArgTableRow>
<ArgTableRow arg="order" typ="object">Execution order (by labels). Required when `fail-policy=continue-order`, and required when `fail-policy=stop` is combined with `strategy=parallel`.</ArgTableRow>
<ArgTableRow arg="channel" typ="alt" mandatory="1">Upgrade channel: `long-term`, `stable`, `testing`, or `development`. Alternatively, pin a specific version by giving the version directly as the value, for example `channel=7.24.4`.</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="multi { array-id, array-id, time: super { time: date
, [day] [ @enum (sun | mon | tue | wed | thu | fri | sat) { sun:1, mon:2, tue:3, wed:4, thu:5, fri:6, sat:7 }]
 }
 }" unset="1">When upgrades start: a time with an optional weekday given after `@`. For example `14:00:00` starts every day at 14:00 and `00:00:00@sat` starts every Saturday at midnight. Multiple entries are comma-separated, for example `00:00:00@sat,00:00:00@sun`.</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">How devices are upgraded: `parallel` upgrades all covered devices at the same time; `sequential` upgrades them one after another and waits for each to finish. With `continue-order` the devices are processed per label group in the order given by `order`: in `parallel` the devices of each group are upgraded together, in `sequential` one at a time. Default: `parallel`.</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">Behaviour if a device fails: `continue` skips the failed device and continues with the rest; `stop` stops the whole upgrade on the first failure and does not continue with the remaining devices or with the next label group (with `strategy=parallel` it requires `order`, and `parallel` combined with `stop` without `order` is rejected); `continue-order` skips the failed device and continues with the next label group, processing the labels one group after another in the order given by `order`. With `sequential` the rest of the failed device's group is skipped; with `parallel` only the failed device is abandoned and devices already in progress in the group finish. Default: `continue`.</ArgTableRow>
</ArgTable>
