# priority-flow-control

> PFC configuration is organized in profiles. Different switch ports can be assigned to different PFC profiles. The maximum number of hardware Tx managers depends on the switch chip model. The builtin profile named...

-----------

## interface/ethernet/switch/qos/priority-flow-control 
**Syscap:** rbswitch and crs_prestera and !prestera-ac3
**Type:** Directory

[PFC](../../../../../bridging-and-switching/quality-of-service.md#priority-based-flow-control-pfc) configuration is organized in profiles. Different switch ports can be assigned to different PFC profiles. The maximum number of hardware Tx managers depends on the switch chip model. The builtin profile named "**disabled**" cannot be changed.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">The user-defined name of the PFC profile.</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="multi { array-id, tc: num [ .. 7]
 }" mandatory="1">The list of PFC-enabled traffic classes.</ArgTableRow>
<ArgTableRow arg="rx" typ="bool">Enables receiving of PFC frames. The received PFC frame pauses the specific priority queues on the port that received the PFC frame for the duration specified by the PFC frame. Disabling rx disables queue pausing.</ArgTableRow>
<ArgTableRow arg="tx" typ="bool">Enables transmission of PFC frames.</ArgTableRow>
<ArgTableRow arg="pause-threshold" typ="alt { pause-threshold-pct: num [ .. 100]
, pause-threshold-byte: num [1536 .. ]
 }">Transmits a pause frame (XOFF) when the total size of enqueued packets reaches this threshold. Enqueued packets are counted per ingress port. Applies only when **tx=yes**. The value can be given either explicitly in bytes or percent of the respective shared pool size (**shared-poolX-byte-cap**).</ArgTableRow>
<ArgTableRow arg="resume-threshold" typ="alt { resume-threshold-pct: num [ .. 100]
, resume-threshold-byte: num [256 .. ]
 }">Transmits a resume frame (XON) when the total size of enqueued packets drops down to this threshold. Enqueued packets are counted per ingress port. Applies only when **tx=yes**. The value can be given either explicitly in bytes or percent of the respective shared pool size (**shared-poolX-byte-cap**).</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
