# alert

> An alert rule defines conditions and runs its actions on the CMR controller. Device rules select devices with labels. State alerts remain active while all configured state conditions match and run actions once when...

-----------

## cmr/alert 
**Package:** cmr
**Type:** Directory

An alert rule defines conditions and runs its actions on the CMR controller. Device rules select devices with `labels`. State alerts remain active while all configured state conditions match and run actions once when they become active. They fire again only after their conditions stop matching and then match again. Event alerts run actions for each matching occurrence and never remain active or contribute to active-alert counters. A rule can contain multiple state conditions but at most one event condition. Most alerts apply per device; `upgrade-job-done` is a system event for a whole upgrade job. See [CMR - Alert rules](../../../management-tools/cmr/#alert-rules) for conditions, actions, and alert scope.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Alert rule is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1">Name of the alert rule.</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">
Select the devices, by labels, that the alert rule applies to. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

When `labels` is not set, the rule applies to all connected devices (`labels=all`).
</ArgTableRow>
<ArgTableRow arg="connected" typ="bool" unset="1">
State condition that matches whether the device is connected (`yes`) or disconnected (`no`).

Default: no.
</ArgTableRow>
<ArgTableRow arg="cpu-above" typ="num" unset="1">
Alert when CPU load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="cpu-below" typ="num" unset="1">
Alert when CPU load is below the given percent value (0..100); it fires only for values strictly below the threshold.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="hdd-above" typ="num" unset="1">
Alert when disk (HDD) load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="hdd-below" typ="num" unset="1">
Alert when disk (HDD) load is below the given percent value (0..100); it fires only for values strictly below the threshold.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="mem-above" typ="num" unset="1">
Alert when RAM load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="mem-below" typ="num" unset="1">
Alert when RAM load is below the given percent value (0..100); it fires only for values strictly below the threshold.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="health-above" typ="num" unset="1">
Alert when the health sensor named by `health-value` goes above the given value; a value equal to the threshold also fires the rule. Devices that do not report the sensor are ignored.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="health-below" typ="num" unset="1">
Alert when the health sensor named by `health-value` goes below the given value; it fires only for values strictly below the threshold. Devices that do not report the sensor are ignored.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="health-value" typ="string" unset="1">Name of the health sensor to compare, matching a name from `/system/health/print`, for example `cpu-temperature`. Uses the `[cpu-temperature]` style placeholder in the action text.</ArgTableRow>
<ArgTableRow arg="interface-change" typ="alt { change: enum (any)
, change: ubit (running, not-running, added, removed)
 }" unset="1">
Alert on an interface state change:

- `any` (default) - Any state change.
- `running` - An interface's link comes up.
- `not-running` - An interface's link goes down.
- `added` - An interface is first seen.
- `removed` - An interface is no longer seen.

`running` and `not-running` follow the link state of the interface, not its admin state: enabling or disabling an interface with no connection does not fire, while an actual link loss or recovery does.
</ArgTableRow>
<ArgTableRow arg="interface-type" typ="alt { type: enum (any)
, type: ubit (ethernet, wifi, bridge)
 }" unset="1">
Restrict `interface-change` alerts to one interface type:

- `any` (default) - Interfaces of any type.
- `ethernet` - Ethernet ports.
- `wifi` - Wireless interfaces.
- `bridge` - Bridge interfaces.
</ArgTableRow>
<ArgTableRow arg="upgrade-available" typ="bool" unset="1">
Alert when a newer RouterOS version is available for the device.

Default: no.
</ArgTableRow>
<ArgTableRow arg="disconnected-more-than" typ="time" unset="1">
Alert when a device has been disconnected for longer than the given time.

Default: unset.
</ArgTableRow>
<ArgTableRow arg="upgrade-job-done" typ="alt { cond: enum (yes)
, cond: ubit (success, fail)
 }" unset="1">
Alert when an upgrade job finishes; the rule fires once for the whole job, when the last device of the job is done:

- `yes` (default) - Any outcome.
- `success` - The job finished successfully.
- `fail` - The job failed.

A job that ends without installing an upgrade is treated as a failed job, so the `yes` and `fail` variants both fire.
</ArgTableRow>
<ArgTableRow arg="upgrade-done" typ="alt { cond: enum (yes)
, cond: ubit (success, fail)
 }" unset="1">
Alert when the upgrade of a device finishes; the rule fires once for every device that finished its upgrade:

- `yes` (default) - Any outcome.
- `success` - The upgrade finished successfully.
- `fail` - The upgrade failed.

When no newer version is available for a device, its upgrade still finishes as a failure (the `[upgrade-error]` is `no upgrade available`), so the `yes` and `fail` variants both fire.
</ArgTableRow>
<ArgTableRow arg="unpaired-device-connected" typ="bool" unset="1">
Alert when a device that is not paired to the controller connects.

Default: no.
</ArgTableRow>
<ArgTableRow arg="rebooted" typ="bool" unset="1">
Event condition that fires when the device unexpectedly reboots.

Default: no.
</ArgTableRow>
<ArgTableRow arg="log-topics" typ="multi { array-id, array-id, topic: super { !
, topic: enum
 }
 }" unset="1">Log topics to follow; prefix a topic with `!` to exclude it. Together with `log-regex`, defines a log-message event condition. CMR automatically instructs the device to forward matching log messages.</ArgTableRow>
<ArgTableRow arg="log-regex" typ="string" unset="1">Match log messages against the given regular expression. Each message matching the configured topics and regular expression fires the actions without creating a persistent active alert.</ArgTableRow>
<ArgTableRow arg="action.log" typ="string" unset="1">Write a message to the log when the alert fires. The message may contain placeholders such as `[device]` or `[cpu-usage]`, replaced with the values of the device that fired; an inapplicable placeholder is rendered as `unknown`.</ArgTableRow>
<ArgTableRow arg="action.log-topics" typ="multi { array-id, topic: enum
 }" unset="1">
Log topics to write the message to.

Default: `cmr,info`.
</ArgTableRow>
<ArgTableRow arg="action.log-prefix" typ="string" unset="1">Prefix for the log message. When set, the prefix is prepended to the message without a separator; when unset the message is written as it is.</ArgTableRow>
<ArgTableRow arg="action.script" typ="enum" unset="1">Run a named system script when the alert fires. The script must allow itself to run with reduced rights; otherwise the action fails with `executing script ... from cmr failed ... (not enough permissions)`. Set the script's `dont-require-permissions` to yes.</ArgTableRow>
<ArgTableRow arg="action.script-vars" typ="multi { array-id, script-var: string
 }" unset="1">List of variable names to make available to the `action.script`: each variable is filled with the value for the device that fired. For example `device`, `identity`, `address`, `board`, `version` become `$device`, `$identity`, and so on in the script. A name with a hyphen (for example `cpu-usage`) cannot be read as an ordinary script variable.</ArgTableRow>
<ArgTableRow arg="action.http-url" typ="string" unset="1">HTTP webhook URL to call when the alert fires. On a failed call the alert writes `alert "<name>" HTTP action failed: <reason>` to the `cmr` topic with `warning` severity and counts the failure in `action-failures`; the other actions still run.</ArgTableRow>
<ArgTableRow arg="action.http-method" typ="enum (get | post | put | delete | head | patch)" unset="1">
HTTP method used for the webhook:

- `get`
- `post`
- `put`
- `delete`
- `head`
- `patch`
</ArgTableRow>
<ArgTableRow arg="action.http-body" typ="string" unset="1">HTTP request body sent to the webhook. Supports the same placeholders as the log message, substituted per device (for example `[device]` and `[version]`). No `Content-Type` header is added automatically; add one with `action.http-headers` when the receiver expects it, for example `Content-Type: application/json` for a JSON body.</ArgTableRow>
<ArgTableRow arg="action.http-headers" typ="multi { header: string
 }" unset="1">Additional HTTP headers sent with the webhook, each as `Header: value`. The request also carries the controller's `RouterOS <version>` user-agent.</ArgTableRow>
<ArgTableRow arg="reset-on-disconnect" typ="enum (yes | no) { yes:0, no:-1 }" unset="1">Clear (reset) a state alert when the device disconnects, so a reconnecting device fires the rule again if it still matches: `yes` or `no`. Default: `no` (the state is kept across a disconnect). Event alerts have no persistent state to reset.</ArgTableRow>
<ArgTableRow arg="severity" typ="enum (critical | high | medium | low)" unset="1">
Severity of the alert:

- `critical`
- `high`
- `medium` (default)
- `low`
</ArgTableRow>
<ArgTableRow arg="category" typ="multi { array-id, category: enum
 }" unset="1">Categories assigned to the alert. The category is a grouping label: the server assigns one according to the rule's conditions (for example `performance`, `availability`, `version`, `network`, or `logging`), and it can be changed to any value.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="devices" typ="num">Number of devices the alert rule matches (the devices selected by `labels`). When the rule covers all devices, this count includes the controller itself.</ArgTableRow>
<ArgTableRow arg="devices-on" typ="num">Number of devices with an active state alert. Event occurrences do not add to this count.</ArgTableRow>
<ArgTableRow arg="fired" typ="num">Total number of times the alert has fired.</ArgTableRow>
<ArgTableRow arg="action-failures" typ="num">Number of times an alert action has failed, for example a webhook that could not be reached.</ArgTableRow>
</ArgTable>
