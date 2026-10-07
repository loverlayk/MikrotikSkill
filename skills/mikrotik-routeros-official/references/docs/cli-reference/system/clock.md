# clock

> System clock settings: local date and time, time zone selection and automatic time zone detection. See the Clock guide for time sources, daylight saving configuration and troubleshooting.

-----------

## system/clock 
**Type:** Settings Directory

System clock settings: local date and time, time zone selection and automatic time zone detection. See the [Clock](../../../system-information-and-utilities/clock) guide for time sources, daylight saving configuration and troubleshooting.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date">HH:MM:SS, where HH - hour 00..23, MM - minutes 00..59, SS - seconds 00..59. Sets or shows the current local time on the router. When `date` and `time` are set in one command, the time is interpreted with the GMT offset that was in effect before the change.</ArgTableRow>
<ArgTableRow arg="date" typ="date">YYYY-MM-DD, where YYYY - year, MM - month 01..12, DD - date 01..31. Sets or shows the current local date on the router. The date cannot be set before the build date of the installed RouterOS version, and a date after 2038-01-19 03:14:07 UTC is ignored without an error. Local time cannot be exported and is not stored with the rest of the configuration.</ArgTableRow>
<ArgTableRow arg="time-zone-autodetect" typ="bool">If enabled, the MikroTik cloud service looks up the time zone for the location of the router's public IP address at startup and applies it to `time-zone-name`, including daylight saving time. Detection also runs when the setting is enabled again, and the detected zone then replaces a manually set one within seconds. A `time-zone-name` set by hand while detection is on is kept until the next detection. Default: yes.</ArgTableRow>
<ArgTableRow arg="time-zone-name" typ="enum">Name of the time zone from the IANA time zone database, for example `Europe/Riga`. Case sensitive. Daylight saving rules of the zone are applied automatically. The special value `manual` applies the GMT offset and daylight saving period configured in [`/system/clock/manual`](manual). Default: manual.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="gmt-offset" typ="timezone">Current value of GMT offset used by the system, after applying base time zone offset and active daylight saving time offset. `print` shows it as `+03:00`; in scripts, `get gmt-offset` returns the offset in seconds, for example `10800`.</ArgTableRow>
<ArgTableRow arg="dst-active" typ="bool">`yes` while the daylight saving period of the current time zone is in effect.</ArgTableRow>
</ArgTable>
