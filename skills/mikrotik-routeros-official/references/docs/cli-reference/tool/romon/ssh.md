# ssh

> Open an SSH session to a router over the RoMON overlay, without any IP connectivity.

-----------

## tool/romon/ssh 
**Syscap:** security
**Type:** Command

Open an SSH session to a router over the [RoMON](../../../management-tools/romon) overlay, without any IP connectivity.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr">RoMON ID (MAC address) of the router to connect to</ArgTableRow>
<ArgTableRow arg="command" typ="string">A command to run on the remote router instead of an interactive session</ArgTableRow>
<ArgTableRow arg="user" typ="string">The user account on the remote router to log in with</ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">Save the output of `command` to a file on the local router</ArgTableRow>
</ArgTable>
