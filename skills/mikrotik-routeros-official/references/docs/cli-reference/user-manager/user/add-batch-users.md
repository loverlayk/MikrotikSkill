# add-batch-users

> Creates users with random names and passwords.

-----------

## user-manager/user/add-batch-users 
**Package:** userman-5
**Type:** Command

Creates users with random names and passwords.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="username-length" typ="num">Number of random characters in a name.</ArgTableRow>
<ArgTableRow arg="number-of-users" typ="num">Number of users to create.</ArgTableRow>
<ArgTableRow arg="username-prefix" typ="string">Text at the start of each name.</ArgTableRow>
<ArgTableRow arg="password-length" typ="enum (empty | same-as-username)">Number of characters in a password.</ArgTableRow>
<ArgTableRow arg="username-characters" typ="ubit (uppercase, lowercase, numbers)">Characters of the names: `lowercase`, `uppercase`, `numbers`.</ArgTableRow>
<ArgTableRow arg="password-characters" typ="ubit (uppercase, lowercase, numbers)">Characters of the passwords: `lowercase`, `uppercase`, `numbers`.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Profile to give to the new users.</ArgTableRow>
<ArgTableRow arg="group" typ="enum">Group of the new users.</ArgTableRow>
<ArgTableRow arg="caller-id" typ="enum (bind)">`caller-id` of the new users.</ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited) { unlimited:0x0 }">`shared-users` of the new users.</ArgTableRow>
<ArgTableRow arg="disabled" typ="bool">Creates the users disabled.</ArgTableRow>
<ArgTableRow arg="comment" typ="string">Comment of the new users.</ArgTableRow>
</ArgTable>
