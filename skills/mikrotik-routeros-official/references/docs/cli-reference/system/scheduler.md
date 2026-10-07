# scheduler

> Scheduler entries run RouterOS commands or a /system/script entry at a set date and time, repeatedly at an interval, during startup, or on selected weekdays. See the Scheduler guide for examples and for how the next...

-----------

## system/scheduler 
**Type:** Directory

Scheduler entries run RouterOS commands or a `/system/script` entry at a set date and time, repeatedly at an interval, during startup, or on selected weekdays. See the [Scheduler](../../system-information-and-utilities/scheduler) guide for examples and for how the next run is calculated. The `reset` command clears `on-event` and sets `interval` to `0s`; it does not reset `run-count`.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled entry; it does not run until enabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the entry. Log messages from its runs refer to it as `scheduler:<name>`.</ArgTableRow>
<ArgTableRow arg="start-date" typ="date">Date of the first run, in the format `YYYY-MM-DD` (years 1970..2106). Default: the date when the entry is added.</ArgTableRow>
<ArgTableRow arg="start-time" typ="alt { startup: enum (startup) { startup:0xffffffff }
, time: date
 }">
Time of the first run:

- `HH:MM:SS` - The first run happens at this time on `start-date`.
- `startup` - Run during system startup. With `interval=0s` the entry runs once on each startup. With a non-zero `interval` the first run comes one interval after startup (or one interval after the entry is added while the router runs), not at startup itself.

Startup runs happen before interfaces are up and before the DHCP client has an address. Default: the time when the entry is added.
</ArgTableRow>
<ArgTableRow arg="days" typ="alt { day: enum (never | always) { never:0, always:127 }
, day: ubit (sun, mon, tue, wed, thu, fri, sat)
 }" unset="1">
Weekdays on which the entry runs:

- Unset (default) - The weekday is not considered. Runs follow `start-time` plus `interval` continuously across midnight.
- `always` - Every day, with day scheduling: each day starts again at `start-time`.
- `never` - The entry never runs.
- `sun`, `mon`, `tue`, `wed`, `thu`, `fri`, `sat` - Only on the listed days (comma-separated). Each matching day starts at `start-time` and repeats every `interval` until the end of that day. With `interval=0s` the entry runs once on each matching day.

An `interval` of `1d` or longer is not supported when `days` is set; the entry then shows the note `multi-day intervals are not supported with active day scheduling`.
</ArgTableRow>
<ArgTableRow arg="interval" typ="time">Time between runs. Runs happen at `start-date` and `start-time` plus whole multiples of the interval, so a start in the past aligns the schedule: `start-time=00:00:00 interval=1h` runs on every full hour. `0s` runs the entry once at `start-date` and `start-time` (with `days` set, once on each matching day). Default: 0s.</ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }">RouterOS commands to run, or the name of a `/system/script` entry. A script called by name runs with this entry's `policy`; it is refused with `not enough permissions` when the script's own policy has rights this entry's policy lacks. Default: empty.</ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }">Policies the commands run with. Commands that need a missing policy fail with `not enough permissions (9)` in the log. See [script permissions](../../developer-guides/scripting/#script-permissions). Default: the policies of the user who adds the entry, limited to `ftp`, `reboot`, `read`, `write`, `policy`, `test`, `password`, `sniff`, `sensitive` and `romon`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="owner" typ="string">The user who added the entry.</ArgTableRow>
<ArgTableRow arg="run-count" typ="num">Number of runs since the last startup. A reboot resets it to 0.</ArgTableRow>
<ArgTableRow arg="next-run" typ="date">Date and time of the next run. Empty when no run is pending: an entry with `interval=0s` after its run, a `startup` entry with `interval=0s`, or an entry with `days=never`.</ArgTableRow>
</ArgTable>
