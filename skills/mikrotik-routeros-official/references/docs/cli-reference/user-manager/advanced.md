# advanced

> Settings of the web pages and of payments with PayPal.

-----------

## user-manager/advanced 
**Package:** userman-5
**Type:** Settings Directory

Settings of the web pages and of payments with PayPal.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="web-private-username" typ="string">User name for the `/um/PRIVATE/` folder of the web server, which has the generated vouchers and reports. While it is empty, the folder cannot be opened.</ArgTableRow>
<ArgTableRow arg="web-private-password" typ="string">Password for the `/um/PRIVATE/` folder.</ArgTableRow>
<ArgTableRow arg="paypal-allow" typ="bool">Lets users buy profiles with PayPal on the web page. Default: `no`.</ArgTableRow>
<ArgTableRow arg="paypal-use-sandbox" typ="bool">Uses the test environment of PayPal. Default: `no`.</ArgTableRow>
<ArgTableRow arg="paypal-user" typ="string">User name of the PayPal API account.</ArgTableRow>
<ArgTableRow arg="paypal-password" typ="string">Password of the PayPal API account.</ArgTableRow>
<ArgTableRow arg="paypal-signature" typ="string">Signature of the PayPal API account.</ArgTableRow>
<ArgTableRow arg="paypal-currency" typ="string">Currency of the `price` of the profiles. Default: `USD`.</ArgTableRow>
</ArgTable>
