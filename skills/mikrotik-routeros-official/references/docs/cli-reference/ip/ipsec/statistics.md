# statistics

> This menu shows various IPsec statistics and errors.

-----------

## ip/ipsec/statistics 
**Type:** Settings Directory

This menu shows various IPsec statistics and errors.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="in-errors" typ="num">Number of input error events.</ArgTableRow>
<ArgTableRow arg="in-buffer-errors" typ="num">Number of input buffer errors.</ArgTableRow>
<ArgTableRow arg="in-header-errors" typ="num">Number of input header errors.</ArgTableRow>
<ArgTableRow arg="in-no-states" typ="num">Number of packets dropped due to no matching state.</ArgTableRow>
<ArgTableRow arg="in-state-protocol-errors" typ="num">Number of input state protocol errors.</ArgTableRow>
<ArgTableRow arg="in-state-mode-errors" typ="num">Number of input state mode errors.</ArgTableRow>
<ArgTableRow arg="in-state-sequence-errors" typ="num">Number of input state sequence errors.</ArgTableRow>
<ArgTableRow arg="in-state-expired" typ="num">Number of input packets with expired state.</ArgTableRow>
<ArgTableRow arg="in-state-mismatches" typ="num">Number of input state mismatches.</ArgTableRow>
<ArgTableRow arg="in-state-invalid" typ="num">Number of input packets with invalid state.</ArgTableRow>
<ArgTableRow arg="in-template-mismatches" typ="num">Number of input template mismatches.</ArgTableRow>
<ArgTableRow arg="in-no-policies" typ="num">Number of input packets with no matching policy.</ArgTableRow>
<ArgTableRow arg="in-policy-blocked" typ="num">Number of input packets blocked by policy.</ArgTableRow>
<ArgTableRow arg="in-policy-errors" typ="num">Number of input policy errors.</ArgTableRow>
<ArgTableRow arg="out-errors" typ="num">Number of output error events.</ArgTableRow>
<ArgTableRow arg="out-bundle-errors" typ="num">Number of output bundle errors.</ArgTableRow>
<ArgTableRow arg="out-bundle-check-errors" typ="num">Number of output bundle check errors.</ArgTableRow>
<ArgTableRow arg="out-no-states" typ="num">Number of output packets dropped due to no matching state.</ArgTableRow>
<ArgTableRow arg="out-state-protocol-errors" typ="num">Number of output state protocol errors.</ArgTableRow>
<ArgTableRow arg="out-state-mode-errors" typ="num">Number of output state mode errors.</ArgTableRow>
<ArgTableRow arg="out-state-sequence-errors" typ="num">Number of output state sequence errors.</ArgTableRow>
<ArgTableRow arg="out-state-expired" typ="num">Number of output packets with expired state.</ArgTableRow>
<ArgTableRow arg="out-policy-blocked" typ="num">Number of output packets blocked by policy.</ArgTableRow>
<ArgTableRow arg="out-policy-dead" typ="num">Number of output packets with dead policy.</ArgTableRow>
<ArgTableRow arg="out-policy-errors" typ="num">Number of output policy errors.</ArgTableRow>
</ArgTable>
