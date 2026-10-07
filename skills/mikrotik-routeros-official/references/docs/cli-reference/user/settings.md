# settings

> Password complexity policy enforced when adding a user in /user or changing a password with /password. See User for the full guide.

-----------

## user/settings 
**Type:** Settings Directory

Password complexity policy enforced when adding a user in [`/user`](.) or changing a password with `/password`. See [User](../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="minimum-password-length" typ="num">Shortest accepted password length, in characters. A shorter password is rejected with "password is too short - must be at least N characters". Range 0 to 4294967295. Default: 0.</ArgTableRow>
<ArgTableRow arg="minimum-categories" typ="num">Number of character categories a password must use, out of four: digits, lowercase letters, uppercase letters and symbols. A weaker password is rejected with "password is too weak - it must contain characters from at least N categories (digits, lower and upper case letters, symbols)". Range 0 to 4. Default: 0.</ArgTableRow>
</ArgTable>
