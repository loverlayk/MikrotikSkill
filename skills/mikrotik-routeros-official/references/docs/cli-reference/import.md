# import

> Runs a script file (.rsc) line by line, for example a configuration made with export. The import adds to the existing configuration and stops at the first line that fails; the lines before it stay applied. See...

-----------

## import 
**Type:** Command

Runs a script file (`.rsc`) line by line, for example a configuration made with `export`. The import adds to the existing configuration and stops at the first line that fails; the lines before it stay applied. See [Configuration Management](../getting-started/configuration-management/#import-a-configuration).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="file">Script file to run.</ArgTableRow>
<ArgTableRow arg="from-line" typ="num">Starts the import at this line of the file. Works only with `verbose=yes`; without it, the router warns `from-line parameter does not work for non-verbose import` and runs the whole file.</ArgTableRow>
<ArgTableRow arg="verbose" typ="enum (no | yes | progress)">With `yes`, prints each line with its number (`#line N`) before it runs, so the output shows where the import stops. With `no`, runs the file without printing the lines.</ArgTableRow>
<ArgTableRow arg="dry-run" typ="switch">Checks the file without changing the configuration and reports `No syntax errors found in the import file` when it finds none. Works only with `verbose=yes`; without it, the import fails with `dry-run parameter cannot be used in non-verbose mode`.</ArgTableRow>
</ArgTable>
