# easymesh

> RouterOS settings reference for /interface/wifi/easymesh.

-----------

## interface/wifi/easymesh 
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (yes | no)"></ArgTableRow>
<ArgTableRow arg="role" typ="enum (agent | controller | controller-and-agent)" unset="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bhaul-configuration" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="fhaul-configurations" typ="multi { array-id, fhaul-configuration: enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="dpp-onboarding" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bhaul-ssid" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="bhaul-passphrase" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="bhaul-authentication-types" typ="ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap, wpa3-psk, wpa3-eap)" unset="1"></ArgTableRow>
<ArgTableRow arg="bhaul-encryption" typ="ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256)" unset="1"></ArgTableRow>
<ArgTableRow arg="agent-state" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="network" typ="string"></ArgTableRow>
</ArgTable>
