# users

> Users for SOCKS5 username/password authentication, used when /ip/socks has auth-method=password. New users are created enabled. For more information, see SOCKS.

-----------

## ip/socks/users 
**Type:** Directory

Users for SOCKS5 username/password authentication, used when [`/ip/socks`](.) has `auth-method=password`. New users are created enabled. For more information, see [SOCKS](../../../network-management/socks).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled. The user cannot authenticate. New users are created enabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Username for SOCKS5 authentication.</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">Password for SOCKS5 authentication. Not shown in `print` output.</ArgTableRow>
<ArgTableRow arg="only-one" typ="bool"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Rate limit applied to the user's proxied connections, in bits per second, for example `64000`.</ArgTableRow>
</ArgTable>
