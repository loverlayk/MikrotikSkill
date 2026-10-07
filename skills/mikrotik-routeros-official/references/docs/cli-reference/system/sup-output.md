# sup-output

> Creates a support output file (supout.rif), a diagnostic snapshot of the router for MikroTik support, and shows its progress in created. The file is encoded and is opened with the Supout.rif viewer in your MikroTik...

-----------

## system/sup-output 
**Type:** Command

Creates a support output file (`supout.rif`), a diagnostic snapshot of the router for MikroTik support, and shows its progress in `created`. The file is encoded and is opened with the Supout.rif viewer in your MikroTik account. See [Supout.rif](../../getting-started/supout-rif).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the file, or a path such as `usb1/supout` to write it into a folder. RouterOS adds the `.rif` extension when the name has none, so `supout.rif` also writes `supout.rif`. Default: supout.</ArgTableRow>
<ArgTableRow arg="output-width" typ="num" unset="1">Width of the command outputs in the file. Use a larger value, for example `300`, when the viewer shows the outputs cut or wrapped.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="created" typ="num">Progress of the file in percent, from the start up to `100%`.</ArgTableRow>
</ArgTable>
