# user-profile

> Profiles of users. A user can have several profiles and uses one at a time.

-----------

## user-manager/user-profile 
**Package:** userman-5
**Type:** Directory

Profiles of users. A user can have several profiles and uses one at a time.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum" mandatory="1">Name of the user.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1">Name of the profile.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (waiting | running | running-active | used)">
- `waiting` - the profile has `starts-when=first-auth` and the user has not logged in yet.
- `running-active` - the profile that the user has now.
- `running` - a valid profile that is not in use.
- `used` - the validity time is over.
</ArgTableRow>
<ArgTableRow arg="end-time" typ="alt { constant: enum (not-yet-running | unlimited)
, date: date
 }">Date and time when the validity of the profile ends, `unlimited`, or `not-yet-running`.</ArgTableRow>
</ArgTable>
