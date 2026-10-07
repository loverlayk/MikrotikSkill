# scan

> RouterOS command reference for /interface/wireless/scan.

-----------

## interface/wireless/scan 
**Package:** wireless-rep
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active"></ArgTableRow>
<ArgTableRow arg="P" typ="privacy"></ArgTableRow>
<ArgTableRow arg="R" typ="routeros-network"></ArgTableRow>
<ArgTableRow arg="N" typ="nstreme"></ArgTableRow>
<ArgTableRow arg="T" typ="tdma"></ArgTableRow>
<ArgTableRow arg="W" typ="wds"></ArgTableRow>
<ArgTableRow arg="B" typ="bridge"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="background" typ="bool"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="sig" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="snr" typ="num"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
</ArgTable>
