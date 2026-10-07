# run-script

> Runs a script on the selected devices.

-----------

## cmr/device/run-script 
**Package:** cmr
**Type:** Command

Runs a script on the selected devices.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="script" typ="alt { script: string
 }">The script to run on the selected devices.</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">Select the devices to run the script on using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.</ArgTableRow>
<ArgTableRow arg="order" typ="object">Execution order (by labels).</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">How devices are processed: `parallel` or `sequential`.</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">Behaviour if a device fails: `continue`, `stop`, or `continue-order`.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time" unset="1">Script execution timeout.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum">Device the script is running on.</ArgTableRow>
<ArgTableRow arg="status" typ="string">Execution status.</ArgTableRow>
<ArgTableRow arg="output" typ="string">Script output.</ArgTableRow>
</ArgTable>
