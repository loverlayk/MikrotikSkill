# job

> One upgrade job is one upgrade run. Jobs are created from upgrade rules, and their parameters are copied from the rule at creation and are read-only. A scheduled job resolves its device list only when it starts, so...

-----------

## cmr/upgrade/job 
**Package:** cmr
**Type:** Directory

One upgrade job is one upgrade run. Jobs are created from upgrade rules, and their parameters are copied from the rule at creation and are read-only. A scheduled job resolves its device list only when it starts, so `show-devices` for a scheduled job can be empty. Remove a queued or processing job to cancel it. The job state becomes `cancelled`.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Job is disabled.</ArgTableRow>
<ArgTableRow arg="R" typ="rule">Job created from an upgrade rule.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Devices the job covers, selected by labels.</ArgTableRow>
<ArgTableRow arg="order" typ="object">Execution order of the label groups, used with `continue-order`.</ArgTableRow>
<ArgTableRow arg="channel" typ="alt">Upgrade channel or the pinned version the job installs.</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">How the job upgrades devices: `parallel` all at the same time, `sequential` one after another. With `continue-order` the devices are processed per label group in the order given by `order`.</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">Behaviour of the job if a device fails: `continue`, `stop`, or `continue-order`. `stop` halts the whole job on the first failure; `continue-order` continues with the next label group in `order`.</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="date" unset="1">When the job is scheduled to run, in the same format as the rule's `schedule-time`.</ArgTableRow>
<ArgTableRow arg="starts-in" typ="time" unset="1">Time remaining until the job starts. Shown for scheduled jobs.</ArgTableRow>
<ArgTableRow arg="start-time" typ="date" unset="1">When the job started running.</ArgTableRow>
<ArgTableRow arg="end-time" typ="date" unset="1">When the job finished.</ArgTableRow>
<ArgTableRow arg="state" typ="enum (scheduled | queued | waiting devices | queued (busy) | version check | processing | done | cancelled)">Current job state: `scheduled` (waiting to run), `queued` (created while another job runs, starts when it finishes), `waiting devices`, `version check` (looking up the available version), `processing` (upgrading), `done` (finished), or `cancelled` (removed).</ArgTableRow>
<ArgTableRow arg="success" typ="composite { success: num
, total: num
 }" unset="1">Upgraded/total, for example `3/10`. A `0/total` occurs when the devices are already on the target version or a covered device is unreachable when the job starts.</ArgTableRow>
<ArgTableRow arg="run-time" typ="time" unset="1">How long the job took to run.</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { package: string
 }" unset="1">Packages the job upgrades.</ArgTableRow>
</ArgTable>
