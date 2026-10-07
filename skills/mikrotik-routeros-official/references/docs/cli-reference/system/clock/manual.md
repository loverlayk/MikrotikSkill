# manual

> Manual GMT offset and daylight saving settings, applied while time-zone-name in /system/clock is manual. See the Clock guide.

-----------

## system/clock/manual 
**Type:** Settings Directory

Manual GMT offset and daylight saving settings, applied while `time-zone-name` in [`/system/clock`](.) is `manual`. See the [Clock](../../../system-information-and-utilities/clock) guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="time-zone" typ="timezone">GMT offset while daylight saving time is not active. Has an effect only when `time-zone-name` is `manual`. Default: +00:00.</ArgTableRow>
<ArgTableRow arg="dst-delta" typ="timezone">Offset added to `time-zone` while daylight saving time is active. Negative values are accepted, for time zones where the winter time is the daylight saving period. Default: +00:00.</ArgTableRow>
<ArgTableRow arg="dst-start" typ="date">Local date and time when the daylight saving period starts. Daylight saving time is active from `dst-start` until `dst-end` exactly as configured: the period is a single date range and does not repeat in the following years. If `dst-start` is later than `dst-end`, daylight saving time is never active. Format: YYYY-MM-DD HH:MM:SS. An omitted date or time part is reset, the date to 1970-01-01 or the time to 00:00:00 (for example `dst-start=05:00:00` gives `1970-01-01 05:00:00`), so always give both parts. Default: 1970-01-01 00:00:00.</ArgTableRow>
<ArgTableRow arg="dst-end" typ="date">Local date and time when the daylight saving period ends. See `dst-start` for how the period is applied. Format: YYYY-MM-DD HH:MM:SS. An omitted date or time part is reset, the date to 1970-01-01 or the time to 00:00:00, so always give both parts. Default: 1970-01-01 00:00:00.</ArgTableRow>
</ArgTable>
