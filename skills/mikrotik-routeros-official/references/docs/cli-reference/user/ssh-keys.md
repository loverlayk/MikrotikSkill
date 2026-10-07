# ssh-keys

> Public SSH keys assigned to users; the keys authenticate those users' incoming SSH logins. When a user has at least one key assigned, the SSH server refuses password authentication for that user and offers only...

-----------

## user/ssh-keys 
**Type:** Directory

Public SSH keys assigned to users; the keys authenticate those users' incoming SSH logins. When a user has at least one key assigned, the SSH server refuses password authentication for that user and offers only public-key authentication. See [User](../../../authentication-authorization-accounting/user) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum">System user the key is assigned to.</ArgTableRow>
<ArgTableRow arg="info" typ="string">Free-text label for the key. When adding a key with `key`, a trailing comment in the pasted OpenSSH key string becomes the key's `info` and overrides this parameter.</ArgTableRow>
<ArgTableRow arg="key" typ="string">Public key string, set only when adding a new key. Only the OpenSSH single-line format is accepted; PEM blocks are rejected.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519 | ed25519-sk)">Type of the key: `rsa`, `ed25519` or `ed25519-sk`.</ArgTableRow>
<ArgTableRow arg="bits" typ="num">Key length in bits.</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string">SHA256 fingerprint of the key in base64 (for example `SHA256:...`).</ArgTableRow>
</ArgTable>
