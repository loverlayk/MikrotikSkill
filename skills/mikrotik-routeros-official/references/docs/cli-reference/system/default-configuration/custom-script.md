# custom-script

> Shows the custom default configuration script, if one is installed. A custom script replaces MikroTik's default configuration: it runs when the configuration is reset (/system/reset-configuration, the TR-069...

-----------

## system/default-configuration/custom-script 
**Type:** Settings Directory

Shows the custom default configuration script, if one is installed. A custom script replaces MikroTik's default configuration: it runs when the configuration is reset (`/system/reset-configuration`, the TR-069 FactoryReset RPC). It is installed with Netinstall or with the TR-069 Download RPC (`X MIKROTIK Factory Configuration File`). After a Download of the script, `/system/default-configuration/print` keeps showing MikroTik's script, and `/export` starts with a comment that a custom script is installed.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="custom-script" typ="string">Text of the custom default configuration script. Empty when none is installed.</ArgTableRow>
</ArgTable>
