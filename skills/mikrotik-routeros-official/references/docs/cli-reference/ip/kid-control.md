# kid-control

> Profiles of Kid Control: the allowed time of each day and the rate limit for the devices of a child. See Kid Control.

-----------

## ip/kid-control 
**Type:** Directory

Profiles of Kid Control: the allowed time of each day and the rate limit for the devices of a child. See [Kid Control](../../../firewall-and-quality-of-service/kid-control).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The profile is disabled and does not restrict its devices.</ArgTableRow>
<ArgTableRow arg="P" typ="paused">The profile is paused: its devices are blocked.</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">The devices of the profile are blocked now.</ArgTableRow>
<ArgTableRow arg="L" typ="rate-limited">The devices of the profile are rate-limited now.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the profile, usually the name of the child.</ArgTableRow>
<ArgTableRow arg="sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Sunday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 6h-21h.</ArgTableRow>
<ArgTableRow arg="mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Monday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 7h-21h.</ArgTableRow>
<ArgTableRow arg="tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Tuesday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 7h-21h.</ArgTableRow>
<ArgTableRow arg="wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Wednesday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 7h-21h.</ArgTableRow>
<ArgTableRow arg="thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Thursday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 7h-21h.</ArgTableRow>
<ArgTableRow arg="fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Friday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 7h-22h.</ArgTableRow>
<ArgTableRow arg="sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Saturday in which internet access is allowed, for example `8h-20h`. An empty value (`""`) allows no access on that day. Default: 6h-22h.</ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Data rate limit of each device of the profile during the allowed time, for example `3M`, or `2M/1M` for separate values. The router applies it with a dynamic simple queue. Default: empty (no limit).</ArgTableRow>
<ArgTableRow arg="tur-sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Sunday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Monday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Tuesday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Wednesday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Thursday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Friday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
<ArgTableRow arg="tur-sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">Time of day on Saturday in which `rate-limit` does not apply (time unlimited rate). It does not allow access by itself: outside the allowed time of the day the devices stay blocked. Default: empty.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pause-left" typ="time"></ArgTableRow>
<ArgTableRow arg="pause-till" typ="date"></ArgTableRow>
</ArgTable>
