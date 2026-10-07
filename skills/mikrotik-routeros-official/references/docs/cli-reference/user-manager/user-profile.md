# user-profile

> RouterOS directory reference for /user-manager/user-profile.

-----------

## user-manager/user-profile 
**Package:** userman-5
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (waiting | running | running-active | used)"></ArgTableRow>
<ArgTableRow arg="end-time" typ="alt { constant: enum (not-yet-running | unlimited)
, date: date
 }"></ArgTableRow>
</ArgTable>
