# fantasy

> Fantasy menu is a fancy way to generate large amount of routes for testing purposes. Main benefits of this approach compared to a script are the generation speed and simplicity. It is easy to remove all fantasy...

-----------

## routing/fantasy 
**Type:** Directory

Fantasy menu is a fancy way to generate large amount of routes for testing purposes. Main benefits of this approach compared to a script are the generation speed and simplicity. It is easy to remove all fantasy generated routes just by disabling the fantasy rule.

Fantasy uses a random generator from hashed route sequence number, seed and other parameters.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46it/)">Prefix from which route will be generated.</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="range">Prefix length for generated route (can be specified as integer range). For example `dst-address=192.168.0.0/16` and `prefix-length=24` will generate /24 routes from `192.168.0.0/16` subnet.</ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46iv/)"></ArgTableRow>
<ArgTableRow arg="scope" typ="range">Scope to be set; can be set as range.</ArgTableRow>
<ArgTableRow arg="target-scope" typ="range">Target scope to be set; can be set as range.</ArgTableRow>
<ArgTableRow arg="instance-id" typ="range"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="range"></ArgTableRow>
<ArgTableRow arg="seed" typ="string">Random generator seed.</ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num">Route sequence number offset.</ArgTableRow>
<ArgTableRow arg="priv-offs" typ="range"></ArgTableRow>
<ArgTableRow arg="priv-size" typ="range"></ArgTableRow>
<ArgTableRow arg="use-hold" typ="bool"></ArgTableRow>
</ArgTable>
