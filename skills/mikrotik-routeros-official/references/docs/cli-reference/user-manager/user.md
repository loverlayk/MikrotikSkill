# user

> Users of User Manager.

-----------

## user-manager/user 
**Package:** userman-5
**Type:** Directory

Users of User Manager.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled. The user cannot log in.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the user.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password of the user.</ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string">Key for time-based one-time passwords, in Base32 format. When set, the user must add the current six-digit code to the password. A code works for one login.</ArgTableRow>
<ArgTableRow arg="group" typ="enum">Group of the user. Default: `default`.</ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited) { unlimited:0 }">Number of simultaneous sessions, or `unlimited`. At the limit, a new login is refused and the oldest session is disconnected. Default: 1.</ArgTableRow>
<ArgTableRow arg="caller-id" typ="enum (bind)">Allows the login only when the Calling-Station-Id of the request has this value.</ArgTableRow>
<ArgTableRow arg="attributes" typ="object { attribute-value: super { attribute: enum
, [value] :string
 }
 }">Attributes that are sent in the Access-Accept for the user, as `Name:value` separated with commas.</ArgTableRow>
</ArgTable>
