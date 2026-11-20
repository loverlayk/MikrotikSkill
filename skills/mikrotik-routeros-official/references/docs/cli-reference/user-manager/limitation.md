# limitation

> Sets of limits for profiles: speed, traffic and time. A limitation is connected to a profile in /user-manager/profile-limitation. The traffic and time limits count all sessions of a user together and are checked when...

-----------

## user-manager/limitation 
**Package:** userman-5
**Type:** Directory

Sets of limits for profiles: speed, traffic and time. A limitation is connected to a profile in `/user-manager/profile-limitation`. The traffic and time limits count all sessions of a user together and are checked when the router sends accounting updates.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the limitation.</ArgTableRow>
<ArgTableRow arg="download-limit" typ="num">Bytes that a user can download. Default: 0 (no limit).</ArgTableRow>
<ArgTableRow arg="upload-limit" typ="num">Bytes that a user can upload. Default: 0 (no limit).</ArgTableRow>
<ArgTableRow arg="transfer-limit" typ="num">Bytes that a user can download and upload together. Default: 0 (no limit).</ArgTableRow>
<ArgTableRow arg="uptime-limit" typ="time">Time that a user can be connected. Default: `0s` (no limit).</ArgTableRow>
<ArgTableRow arg="reset-counters-start-time" typ="date">Date and time from which `reset-counters-interval` is counted.</ArgTableRow>
<ArgTableRow arg="reset-counters-interval" typ="alt { constant: enum (disabled | hourly | daily | weekly | monthly)
, reset-counters-interval: time
 }">How often the counters of the users are cleared: `hourly`, `daily`, `weekly`, `monthly` or `disabled`. Default: `disabled`.</ArgTableRow>
<ArgTableRow arg="rate-limit-rx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: the speed that the router receives from the user (upload), in bits per second.</ArgTableRow>
<ArgTableRow arg="rate-limit-tx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: the speed that the router sends to the user (download), in bits per second.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-rx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst rate for upload.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-tx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst rate for download.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-rx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst threshold for upload.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-tx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst threshold for download.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-rx" typ="time">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst time for upload.</ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-tx" typ="time">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: burst time for download.</ArgTableRow>
<ArgTableRow arg="rate-limit-min-rx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: guaranteed rate (`limit-at`) for upload.</ArgTableRow>
<ArgTableRow arg="rate-limit-min-tx" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: guaranteed rate (`limit-at`) for download.</ArgTableRow>
<ArgTableRow arg="rate-limit-priority" typ="num">Part of the rate limit that is sent in the Mikrotik-Rate-Limit attribute: priority of the queue.</ArgTableRow>
</ArgTable>
