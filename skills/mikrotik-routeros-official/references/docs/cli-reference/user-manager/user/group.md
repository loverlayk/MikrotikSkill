# group

> RouterOS directory reference for /user-manager/user/group.

-----------

## user-manager/user/group 
**Package:** userman-5
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="outer-auths" typ="ubit (pap, chap, mschap1, mschap2, eap-tls, eap-ttls, eap-peap, eap-mschap2)"></ArgTableRow>
<ArgTableRow arg="inner-auths" typ="ubit (ttls-pap, ttls-chap, ttls-mschap1, ttls-mschap2, peap-mschap2)"></ArgTableRow>
<ArgTableRow arg="attributes" typ="object { attribute-value: super { attribute: enum
, [value] :string
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
</ArgTable>
