# ssh

> SSH server settings (ciphers, forwarding, authentication) and the settings controlling how the router verifies remote servers when it connects as an SSH client. See SSH for the full guide.

-----------

## ip/ssh 
**Type:** Settings Directory

SSH server settings (ciphers, forwarding, authentication) and the settings controlling how the router verifies remote servers when it connects as an SSH client. See [SSH](../../../management-tools/ssh) for the full guide.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ciphers" typ="multi { array-id, cipher: enum (aes-gcm | aes-ctr | aes-cbc | 3des-cbc | null | auto)
 }">Allowed cipher list.</ArgTableRow>
<ArgTableRow arg="forwarding-enabled" typ="enum (no | local | remote | both)">Control which SSH forwarding method to allow: `no` - SSH forwarding is disabled, `local` - allow SSH clients to originate connections from the server (router), this also controls dynamic forwarding, `remote` - allow SSH clients to listen on the server (router) and forward incoming connections, `both` - allow both local and remote forwarding methods.</ArgTableRow>
<ArgTableRow arg="password-authentication" typ="enum (yes | no | yes-if-no-key)">Whether to allow password login when public key authorization is configured for a user.</ArgTableRow>
<ArgTableRow arg="publickey-authentication-options" typ="enum (none | touch-required | verify-required)">Public key authentication options. The `touch-required` option causes public key authentication by using a FIDO authenticator algorithm to always require the signature to attest that a physically present user explicitly confirmed the authentication (usually by touching the authenticator). The `verify-required` option requires a FIDO key signature to attest that the user was verified, for example, by using a PIN.</ArgTableRow>
<ArgTableRow arg="strong-crypto" typ="bool">Use stronger encryption, HMAC algorithms, use bigger DH primes and disallow weaker ones: use 256 and 192 bit encryption instead of 128 bits, disable null encryption, use sha256 for hashing instead of sha1, disable md5, use 2048bit prime for Diffie-Hellman exchange instead of 1024bit.</ArgTableRow>
<ArgTableRow arg="known-hosts-validation" typ="bool">Verify the server's host key against the keys stored in [`known-hosts`](known-hosts) whenever the router connects as an SSH client (fetch SFTP, [`/system/ssh`](../../system/ssh), [`/system/ssh-exec`](../../system/ssh-exec)). With validation enabled and no matching key stored, the interactive client shows the server's fingerprint and asks `do you want to trust this host key?`, while non-interactive commands fail with `host key not trusted`. On new installations validation is enabled; upgraded routers keep the previous value. Default: yes.</ArgTableRow>
<ArgTableRow arg="known-hosts-trusted-subnets" typ="object { subnets: ip6Prefix
 }">Skip host key validation for servers whose address belongs to these subnets, even when `known-hosts-validation` is enabled. Hosts outside the listed subnets are still validated.</ArgTableRow>
<ArgTableRow arg="host-key-size" typ="enum (1024 | 1536 | 2048 | 4096 | 8192) { 1024:1024, 1536:1536, 2048:2048, 4096:4096, 8192:8192 }">RSA key size when host key is regenerated.</ArgTableRow>
<ArgTableRow arg="host-key-type" typ="enum (rsa | ed25519) { rsa:0, ed25519:3 }">Host key type.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="host-key-fingerprint" typ="string">Fingerprint of the current host key. Can be used to verify that you are connecting to the correct router.</ArgTableRow>
</ArgTable>
