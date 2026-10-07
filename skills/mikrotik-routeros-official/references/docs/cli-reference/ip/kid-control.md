# kid-control

> RouterOS directory reference for /ip/kid-control.

-----------

## ip/kid-control 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="P" typ="paused">paused</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
<ArgTableRow arg="L" typ="rate-limited">rate-limited</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="tur-sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">time with unlimited rate on Sunday</ArgTableRow>
<ArgTableRow arg="tur-mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pause-left" typ="time"></ArgTableRow>
<ArgTableRow arg="pause-till" typ="date"></ArgTableRow>
</ArgTable>
