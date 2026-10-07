# update

> Manage the check-for-updates channel and perform RouterOS upgrades.

-----------

## system/package/update 
**Type:** Settings Directory

Manage the `check-for-updates` channel and perform RouterOS upgrades.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="channel" typ="enum (long-term | stable | testing | development)">Upgrade [channel](#channel) to use when checking for new versions.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (https | http)">Protocol for connecting to the MikroTik download server. Use `http` only if your network blocks HTTPS. HTTPS is recommended.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">Whether and how to validate the server SSL certificate. Always use `yes` to ensure a secure connection. `yes-without-crl` can be used to skip CRL validation.</ArgTableRow>
<ArgTableRow arg="ip-version" typ="enum (auto | ipv4 | ipv6)">IP version preference for connecting to the MikroTik download server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="installed-version" typ="string">Currently installed RouterOS version.</ArgTableRow>
<ArgTableRow arg="latest-version" typ="string">Latest available RouterOS version in the selected [channel](#channel).</ArgTableRow>
<ArgTableRow arg="status" typ="string">Current status of the update process (for example, `New version is available`).</ArgTableRow>
</ArgTable>
