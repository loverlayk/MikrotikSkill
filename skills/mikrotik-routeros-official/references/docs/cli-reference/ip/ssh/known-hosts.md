# known-hosts

> Host public keys of remote SSH servers that the router's SSH client trusts. A key is stored when you answer y to the interactive client's trust prompt, or pinned manually with add. Each address holds one key; entries...

-----------

## ip/ssh/known-hosts 
**Type:** Directory

Host public keys of remote SSH servers that the router's SSH client trusts. A key is stored when you answer `y` to the interactive client's trust prompt, or pinned manually with `add`. Each address holds one key; entries have no `set` command, so replace a key by removing the entry and adding it again. Used when `known-hosts-validation` is enabled in [`/ip/ssh`](.). See [SSH](../../../management-tools/ssh) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="host" typ="ip6Addr">IP address of the SSH server the key belongs to. The entry applies to every port of that address. A second `add` for the same address fails with `host already exists`.</ArgTableRow>
<ArgTableRow arg="key" typ="string">Public host key of the server as one OpenSSH-style entry: `<type> <base64>`, for example `ssh-ed25519 AAAAC3...`, as in the server's `.pub` host key file; a trailing comment is allowed. Ed25519 and RSA keys are accepted; ECDSA keys and a line that starts with the host address fail with `key import failed!`. Pasting the key of a different server stores it as-is; a mismatched key causes later connections to fail with `host key not trusted`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)">Key type of the pinned host key: `rsa` or `ed25519`.</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string">SHA256 fingerprint of the pinned key. Compare it with the server's `host-key-fingerprint` shown by `/ip/ssh/print` on that server.</ArgTableRow>
</ArgTable>
