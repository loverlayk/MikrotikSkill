# known-hosts

> Host public keys of remote SSH servers that the router's SSH client trusts. A key is stored when you answer y to the interactive client's trust prompt, or pinned manually with add. Used when known-hosts-validation is...

-----------

## ip/ssh/known-hosts 
**Type:** Directory

Host public keys of remote SSH servers that the router's SSH client trusts. A key is stored when you answer `y` to the interactive client's trust prompt, or pinned manually with `add`. Used when `known-hosts-validation` is enabled in [`/ip/ssh`](.). See [SSH](../../../management-tools/ssh) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="host" typ="ip6Addr">IP address of the SSH server the key belongs to.</ArgTableRow>
<ArgTableRow arg="key" typ="string">Public host key of the server as one OpenSSH-style entry: `<type> <base64>`, for example `ssh-rsa AAAAB3...`. Pasting the key of a different server stores it as-is; a mismatched key causes later connections to fail with `host key not trusted`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)">Key type of the pinned host key: `rsa` or `ed25519`.</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string">SHA256 fingerprint of the pinned key. Compare it with the server's `host-key-fingerprint` shown by `/ip/ssh/print` on that server.</ArgTableRow>
</ArgTable>
