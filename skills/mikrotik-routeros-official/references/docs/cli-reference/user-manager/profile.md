# profile

> Plans for users. Used with use-profiles=yes in /user-manager. A profile is given to a user in /user-manager/user-profile.

-----------

## user-manager/profile 
**Package:** userman-5
**Type:** Directory

Plans for users. Used with `use-profiles=yes` in `/user-manager`. A profile is given to a user in `/user-manager/user-profile`.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the profile.</ArgTableRow>
<ArgTableRow arg="validity" typ="alt { validity: enum (unlimited) { unlimited:0 }
, validity: time
 }" mandatory="1">How long a user can use the profile, or `unlimited`.</ArgTableRow>
<ArgTableRow arg="name-for-users" typ="string">Name of the profile that users see on the web page.</ArgTableRow>
<ArgTableRow arg="starts-when" typ="enum (first-auth | assigned)">
When the validity time starts. Default: `assigned`.
- `assigned` - when the profile is given to the user.
- `first-auth` - at the first login of the user.
</ArgTableRow>
<ArgTableRow arg="price" typ="num">Price of the profile on the web page. Default: 0.</ArgTableRow>
<ArgTableRow arg="override-shared-users" typ="enum (off | unlimited) { off:-1, unlimited:0 }">Number of simultaneous sessions for users with this profile, or `unlimited`. It replaces `shared-users` of the user. Default: `off` (the value of the user applies).</ArgTableRow>
</ArgTable>
