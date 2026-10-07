# settings

> RouterOS settings reference for /routing/settings.

-----------

## routing/settings 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="single-process" typ="bool">When enabled, all routing-related processes combine into a single routing process to reduce RAM usage. When disabled, routing-related processes run separately and can improve performance and stability in some setups.  By default, single-process is enabled only for devices with 64 MB of RAM or less.  Reboot is required for this change to take effect.</ArgTableRow>
<ArgTableRow arg="dynamic-in-chain" typ="enum" unset="1">Name of the chain used to process all dynamically added routes.</ArgTableRow>
<ArgTableRow arg="connected-in-chain" typ="enum" unset="1">Name of the chain used to process `connected` routes.</ArgTableRow>
<ArgTableRow arg="check-gateway-ping-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-count" typ="num"></ArgTableRow>
<ArgTableRow arg="policy-rules" typ="object { chain: enum
 }">Defines the order of routing decision rules. By default, `user` is the chain where user-defined `/routing/rule` entries are added. You can add custom chains anywhere in the list.</ArgTableRow>
</ArgTable>
