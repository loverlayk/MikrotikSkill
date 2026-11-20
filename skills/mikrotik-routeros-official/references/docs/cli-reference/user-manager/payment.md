# payment

> Payments of users for profiles.

-----------

## user-manager/payment 
**Package:** userman-5
**Type:** Directory

Payments of users for profiles.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum">User who paid.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">Profile that the user bought.</ArgTableRow>
<ArgTableRow arg="price" typ="num">Amount of the payment.</ArgTableRow>
<ArgTableRow arg="currency" typ="string">Currency of the payment.</ArgTableRow>
<ArgTableRow arg="trans-start" typ="date">Date and time when the transaction started.</ArgTableRow>
<ArgTableRow arg="trans-end" typ="alt { constant: enum (not-finished) { not-finished:0 }
, date: date
 }">Date and time when the transaction ended.</ArgTableRow>
<ArgTableRow arg="trans-status" typ="enum (started | pending | approved | declined | error | timeout | aborted | user-approved)">Status of the transaction: `started`, `pending`, `approved`, `declined`, `error`, `timeout`, `aborted`, `user-approved`. Only `approved` is a complete payment.</ArgTableRow>
<ArgTableRow arg="method" typ="enum (paypal | authorize-net)">Payment service of the transaction (PayPal).</ArgTableRow>
<ArgTableRow arg="user-message" typ="string"></ArgTableRow>
</ArgTable>
