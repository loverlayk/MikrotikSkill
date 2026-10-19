# Python3 Example

> This page provides a Python3 example client for interacting with RouterOS via its API, demonstrating sentence exchange, plain-text and legacy challenge-response login, and socket communication over the API and...

# Python3 Example

A simple Python3 API client.

- usage: `api.py <ip-address> <username> <password> <secure(True|False)>`,
  for example: `api.py 10.0.0.1 admin Badpassword123 False` (an empty password is fine)
- after starting the script, type the words of an API sentence, one word per line; press Enter after each word
- an empty line terminates the sentence and sends it to the router — press Enter **twice** after the last word
- press `Ctrl-D` on an empty line to quit
- in the output, `<<<` marks a word the client sends and `>>>` a word received from the router

The client tries the plain-text login method first. If the router answers the login with a challenge (`=ret=`), the client completes the legacy challenge-response exchange instead. The secure option connects to the API-SSL service (port 8729); the router must have a certificate configured for the api-ssl service, and the client must trust that certificate (see the [API reference](index.md)).

For the legacy exchange, the response for the empty password and the challenge `93b438ec9b80057c06dd9fe67d56aa9a` is `00e134102a9d330dd7b1849fedfea3cb57` — a useful test vector for your own implementation.

Example output:

```bash
$ ./api.py 10.0.0.1 admin '' False
<<< /login
<<< =name=admin
<<< =password=
<<<
>>> !done
>>>
/system/identity/print

<<< /system/identity/print
<<<
>>> !re
>>> =name=MyRouter
>>>
>>> !done
>>>
```

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ApiRos:
    """Client for the RouterOS binary API protocol."""

    def __init__(self, sk):
        self.sk = sk

    def login(self, username, pwd):
        # Plain-text login method first.
        for repl, attrs in self.talk(
            ["/login", "=name=" + username, "=password=" + pwd]
        ):
            if repl == "!trap":
                return False
            if "=ret" in attrs:
                # The router asked for the legacy challenge-response method.
                return self._login_legacy(username, pwd, attrs["=ret"])
        return True

    def _login_legacy(self, username, pwd, challenge):
        # The response is the MD5 digest of 0x00, the password and the
        # received challenge, prefixed with "00".
        chal = binascii.unhexlify(challenge)
        md = hashlib.md5()
        md.update(b"\x00")
        md.update(pwd.encode("utf-8"))
        md.update(chal)
        response = "00" + binascii.hexlify(md.digest()).decode("ascii")
        for repl, _attrs in self.talk(
            ["/login", "=name=" + username, "=response=" + response]
        ):
            if repl == "!trap":
                return False
        return True

    def talk(self, words):
        if self.write_sentence(words) == 0:
            return
        replies = []
        while True:
            i = self.read_sentence()
            if len(i) == 0:
                continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find("=", 1)
                if j == -1:
                    attrs[w] = ""
                else:
                    attrs[w[:j]] = w[j + 1:]
            replies.append((reply, attrs))
            if reply == "!done":
                return replies

    def write_sentence(self, words):
        count = 0
        for w in words:
            self.write_word(w)
            count += 1
        self.write_word("")
        return count

    def read_sentence(self):
        words = []
        while True:
            w = self.read_word()
            if w == "":
                return words
            words.append(w)

    def write_word(self, w):
        print("<<< " + w, flush=True)
        data = w.encode("utf-8")
        self.write_len(len(data))
        self.write_bytes(data)

    def read_word(self):
        w = self.read_bytes(self.read_len()).decode("utf-8", "replace")
        print(">>> " + w, flush=True)
        return w

    def write_len(self, l):
        if l < 0x80:
            self.write_bytes(bytes([l]))
        elif l < 0x4000:
            l |= 0x8000
            self.write_bytes(l.to_bytes(2, "big"))
        elif l < 0x200000:
            l |= 0xC00000
            self.write_bytes(l.to_bytes(3, "big"))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.write_bytes(l.to_bytes(4, "big"))
        else:
            self.write_bytes(bytes([0xF0]) + l.to_bytes(4, "big"))

    def read_len(self):
        c = self.read_bytes(1)[0]
        if (c & 0x80) == 0x00:
            return c
        if (c & 0xC0) == 0x80:
            return ((c & ~0xC0) << 8) + self.read_bytes(1)[0]
        if (c & 0xE0) == 0xC0:
            b = self.read_bytes(2)
            return ((c & ~0xE0) << 16) + (b[0] << 8) + b[1]
        if (c & 0xF0) == 0xE0:
            b = self.read_bytes(3)
            return ((c & ~0xF0) << 24) + (b[0] << 16) + (b[1] << 8) + b[2]
        if (c & 0xF8) == 0xF0:
            return int.from_bytes(self.read_bytes(4), "big")
        # Any other first byte is a reserved control byte; the stream cannot
        # be decoded further.
        raise RuntimeError("received reserved control byte 0x%02x" % c)

    def write_bytes(self, b):
        n = 0
        while n < len(b):
            r = self.sk.send(b[n:])
            if r == 0:
                raise RuntimeError("connection closed by remote end")
            n += r

    def read_bytes(self, length):
        data = b""
        while len(data) < length:
            s = self.sk.recv(length - len(data))
            if s == b"":
                raise RuntimeError("connection closed by remote end")
            data += s
        return data

def open_socket(dst, port, secure=False):
    res = socket.getaddrinfo(dst, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    af, socktype, proto, _canonname, sockaddr = res[0]
    skt = socket.socket(af, socktype, proto)
    if secure:
        # The router's api-ssl service needs a certificate, and the client
        # must trust it. The name used here must match the certificate; to
        # connect by IP address, the certificate needs a matching IP address
        # entry.
        context = ssl.create_default_context()
        s = context.wrap_socket(skt, server_hostname=dst)
    else:
        s = skt
    s.connect(sockaddr)
    return s

def main():
    dst = sys.argv[1]
    user = "admin"
    passw = ""
    secure = False

    if len(sys.argv) > 2:
        user = sys.argv[2]
    if len(sys.argv) > 3:
        passw = sys.argv[3]
    if len(sys.argv) > 4:
        secure = sys.argv[4].lower() == "true"

    port = 8729 if secure else 8728
    s = open_socket(dst, port, secure)
    apiros = ApiRos(s)

    if not apiros.login(user, passw):
        print("login failed")
        s.close()
        return

    inputsentence = []
    while True:
        r = select.select([s, sys.stdin], [], [], None)
        if s in r[0]:
            apiros.read_sentence()
        if sys.stdin in r[0]:
            line = sys.stdin.readline()
            # Ctrl-D (EOF) on an empty line quits the client.
            if line == "":
                if inputsentence:
                    apiros.write_sentence(inputsentence)
                break
            line = line.rstrip("\r\n")
            if line == "":
                apiros.write_sentence(inputsentence)
                inputsentence = []
            else:
                inputsentence.append(line)

    # Best effort: read out replies that are still pending before closing the
    # connection (a listen command may still have updates in flight).
    s.settimeout(0.5)
    try:
        while True:
            apiros.read_sentence()
    except socket.timeout:
        pass
    s.close()

if __name__ == "__main__":
    main()
```

## Use the client from a script

The example above is interactive. To script it, use the client classes directly:

```python

from api import ApiRos, open_socket  # the client above, saved as api.py

s = open_socket("10.0.0.1", 8728)
api = ApiRos(s)
if not api.login("admin", "S3cret"):
    sys.exit("login failed")
for repl, attrs in api.talk(["/system/resource/print", "=.proplist=uptime,cpu-load"]):
    if repl == "!re":
        print(attrs)
s.close()
```

`talk()` returns a list of `(reply, attributes)` pairs up to and including the `!done` reply. Commands that return data (for example `print` and `getall`) produce one `!re` pair per item; a command without data produces only the `!done` pair; a `print` with no matching items produces an `!empty` pair.
