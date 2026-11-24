# reset-configuration

> Removes the configuration, reboots the router and applies the default configuration (or the custom default configuration script, if one is installed). In an interactive session the command asks Dangerous! Reset...

-----------

## system/reset-configuration 
**Type:** Command

Removes the configuration, reboots the router and applies the default configuration (or the custom default configuration script, if one is installed). In an interactive session the command asks `Dangerous! Reset anyway? [y/N]:` first. Users are removed and `admin` gets its default password back; files are kept. See [Configuration Management](../../getting-started/configuration-management/#reset-the-configuration).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="keep-users" typ="bool">Keeps the users and their passwords.</ArgTableRow>
<ArgTableRow arg="keep-apps" typ="bool"></ArgTableRow>
<ArgTableRow arg="no-defaults" typ="bool">Does not apply the default configuration after the reset.</ArgTableRow>
<ArgTableRow arg="caps-mode" typ="bool">Runs the CAPs mode script (`/system/default-configuration/caps-mode-script`) after the reset.</ArgTableRow>
<ArgTableRow arg="wps-sync-mode" typ="bool" syscap="wpssync"></ArgTableRow>
<ArgTableRow arg="skip-backup" typ="bool">Saves no backup before the reset. Without it, the router saves the configuration to `auto-before-reset.backup`.</ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool"></ArgTableRow>
<ArgTableRow arg="shutdown" typ="bool">Powers the router off after the reset instead of rebooting. The router starts with the reset configuration when it is powered on.</ArgTableRow>
<ArgTableRow arg="run-after-reset" typ="file">Script file (`.rsc`) that runs after the reset instead of the default configuration. A script that runs longer than two minutes is stopped. Errors are logged as `error while running run-after-reset script:` followed by the error, for example `runtime limit exceeded`.</ArgTableRow>
</ArgTable>
