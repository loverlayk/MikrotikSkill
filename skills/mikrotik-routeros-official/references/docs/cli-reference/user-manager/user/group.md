# group

> Groups of users. A group sets the allowed authentication methods and the attributes of its users.

-----------

## user-manager/user/group 
**Package:** userman-5
**Type:** Directory

Groups of users. A group sets the allowed authentication methods and the attributes of its users.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Built-in group.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the group.</ArgTableRow>
<ArgTableRow arg="allowed-auth-methods" typ="ubit (pap, chap, mschap1, mschap2, eap-tls, eap-mschap2, eap-ttls-pap, eap-ttls-chap, eap-ttls-mschap1, eap-ttls-mschap2, eap-peap-mschap2)"></ArgTableRow>
<ArgTableRow arg="offered-eap-methods" typ="ubit (tls, ttls, peap, mschap2)"></ArgTableRow>
<ArgTableRow arg="outer-auths" typ="ubit (pap, chap, mschap1, mschap2, eap-tls, eap-ttls, eap-peap, eap-mschap2)" deprecated="1">Allowed authentication methods: `pap`, `chap`, `mschap1`, `mschap2`, `eap-tls`, `eap-ttls`, `eap-peap`, `eap-mschap2`. A new group has none, and its users cannot log in until a method is set.</ArgTableRow>
<ArgTableRow arg="inner-auths" typ="ubit (ttls-pap, ttls-chap, ttls-mschap1, ttls-mschap2, peap-mschap2)" deprecated="1">Allowed methods inside an EAP-TTLS or EAP-PEAP tunnel: `ttls-pap`, `ttls-chap`, `ttls-mschap1`, `ttls-mschap2`, `peap-mschap2`.</ArgTableRow>
<ArgTableRow arg="attributes" typ="object { attribute-value: super { attribute: enum
, [value] :string
 }
 }">Attributes that are sent in the Access-Accept for the users of the group, as `Name:value` separated with commas.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string">Original name of a built-in group.</ArgTableRow>
</ArgTable>
