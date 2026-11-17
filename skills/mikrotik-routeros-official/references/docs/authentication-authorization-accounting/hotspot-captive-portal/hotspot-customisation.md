# Hotspot customisation

> Customise the HotSpot login, status, and logout pages: where the page files are, how to use your own directory, the variables and conditions that the pages can use, error messages, translations, and examples such as...

# Hotspot customisation

The pages that the [HotSpot](./) shows to its users are HTML files on the router. You can edit them, or give each HotSpot server profile its own set of pages. The pages contain variables, for example `$(username)`, which the router replaces with their values when it serves a page.

## Where the pages are

A router with a HotSpot server has the `hotspot` directory in its files, with the default pages. On a router that has a `flash` folder in its file list, the directory is `flash/hotspot`. The `html-directory` setting of the server profile in `/ip/hotspot/profile` points to this directory.

To make your own pages:

1. Download the `hotspot` directory from the files of the router to your computer, for example with WinBox, SFTP or FTP.
2. Edit the pages. Use a text editor: an HTML editor can remove the variables and the other parts that the HotSpot needs.
3. Upload the directory to the router under another name, for example `hs-custom`. If the file list of the router has a `flash` folder, upload the directory into `flash`: files outside it are lost on reboot. See [Files](../../system-information-and-utilities/files).
4. Set the directory in the server profile:

   ```ros
   /ip/hotspot/profile/set hsprof1 html-directory-override=hs-custom
   ```

   For a directory in the `flash` folder, set the path with the folder, `html-directory-override=flash/hs-custom`.

Open the login page, `http://hotspot.lan/login`, to check the result. If the directory in `html-directory-override` does not exist, the HotSpot uses the pages from `html-directory`.

To get the default pages back in the `html-directory` of a server, for example after an edit that broke the login page, run:

```ros
/ip/hotspot/reset-html hotspot1
```

## Pages

The pages that the user sees:

- **redirect.html** - redirects the user to another URL, for example to the login page.
- **login.html** - the login page, which asks for a user name and password. The page accepts these parameters:
  - **username** - the user name.
  - **password** - the plain-text password (`http-pap` and `https` login), or the MD5 hash of the chap-id variable, the password, and the CHAP challenge (`http-chap` login). For trial users this value is used as an e-mail address.
  - **dst** - the URL that the user requested before the redirect. It is opened after a successful login.
  - **popup** - whether to open the status page in a pop-up window after a successful login.
  - **radius\<id>** - send the attribute with this ID to the RADIUS server as a text string. Only with RADIUS authentication.
  - **radius\<id>u** - the same, as an unsigned integer.
  - **radius\<id>-\<vnd-id>** - send the attribute with this ID and vendor ID to the RADIUS server as a text string.
  - **radius\<id>-\<vnd-id>u** - the same, as an unsigned integer.
- **md5.js** - JavaScript for the MD5 hash of the password, used by the `http-chap` login method.
- **alogin.html** - shown after a successful login. It opens the status page in a pop-up window and redirects the browser to the page that the user requested.
- **status.html** - the status page with the statistics of the session and the logout button. It also opens advertisements.
- **logout.html** - shown after logout, with the statistics of the finished session. The page accepts this parameter:
  - **erase-cookie** - `on` or `true` removes the cookie of the user on logout, so the browser is not logged in automatically the next time.
- **error.html** - shown on fatal errors.
- **errors.txt** - the texts of the error messages.

Pages for more control. If such a page does not exist, the HotSpot uses the page named in its description:

- **rlogin.html** - redirects a user who is not logged in from the requested URL to the login page. The default page answers with the HTTP status 302.
- **rstatus.html** - redirects a logged-in user who requests the HotSpot address to the status page. Not in the default set; `redirect.html` is used.
- **radvert.html** - redirects the user to the advertisement that is due.
- **flogin.html** - shown instead of `login.html` after a failed login. Not in the default set; `login.html` is used.
- **fstatus.html** - shown when the status page is requested by a user who is not logged in. Not in the default set; `redirect.html` is used.
- **flogout.html** - shown when the logout page is requested by a user who is not logged in. Not in the default set; `redirect.html` is used.

The `xml` sub-directory holds the pages for WISPr clients, which log in without a browser.

### Which page is shown

The HotSpot handles five kinds of requests:

1. **A request for a remote host**
   - The user is logged in and an advertisement is due: `radvert.html`, which redirects to the advertisement.
   - The user is logged in and no advertisement is due: the requested page.
   - The user is not logged in and the host is allowed by the walled garden: the requested page.
   - The user is not logged in and the host is not allowed: `rlogin.html`, or `redirect.html` to the login page.
2. **A request for `/` on the HotSpot address**
   - The user is logged in: `rstatus.html`, or `redirect.html` to the status page.
   - The user is not logged in: `rlogin.html`, or `redirect.html` to the login page.
3. **A request for `/login`**
   - The login succeeded, or the user is already logged in: `alogin.html`, or `redirect.html` to the requested page or the status page.
   - No user name was sent: `login.html`.
   - The login failed: `flogin.html`, or `login.html`, with the error message.
   - Fatal error: `error.html`.
4. **A request for `/status`**
   - The user is logged in: `status.html`.
   - The user is not logged in: `fstatus.html`, or `redirect.html` to the login page.
5. **A request for `/logout`**
   - The user is logged in: `logout.html`.
   - The user is not logged in: `flogout.html`, or `redirect.html` to the login page.

## Variables

To insert a value into a page, write `$(name)`, where `name` is the name of a variable. The router replaces the variables in the pages requested as `/`, `/login`, `/status`, and `/logout`, and in the other text and HTML files (`.txt`, `.htm`, `.html`) of the directory. For example, a link to the login page:

```html
login
```

For a client with the address 192.168.88.254 that requested `http://example.com/`, on a HotSpot with the DNS name `hotspot.lan`, this line of a page:

```text
ip=$(ip) mac=$(mac) link-login=$(link-login)
```

is served as:

```text
ip=192.168.88.254 mac=52:54:09:80:02:01 link-login=http://hotspot.lan/login?dst=http%3A%2F%2Fexample.com%2F
```

Every variable also exists with the `-esc` suffix, for example `$(mac-esc)`. This form is escaped for use inside a URL: `52:54:09:80:02:01` becomes `52%3A54%3A09%3A80%3A02%3A01`. Use it when you put a variable into a link. For example, `` breaks when the user name is `123&456=1 2`; with `$(mac-esc)` and `$(username-esc)` the user name is sent as `123%26456%3D1+2`.

Some links use `http://` URLs. If you use HTTPS, build the link yourself, for example `https://$(hostname)/$(target-dir)status` instead of `$(link-status)`.

### Server

- **hostname** - the DNS name of the HotSpot, or its IP address if no DNS name is set (`hotspot.lan`).
- **identity** - the identity of the router (`MikroTik`).
- **login-by** - the login method that the user used.
- **plain-passwd** - `yes` if the `http-pap` login method is enabled, otherwise `no`.
- **server-address** - the address and port of the HotSpot server (`192.168.88.1:80`).
- **ssl-login** - `yes` if the page was requested over HTTPS, otherwise `no`.
- **server-name** - the name of the HotSpot server in `/ip/hotspot` (`hotspot1`).

### Links

- **link-login** - the login page, with the requested URL (`http://hotspot.lan/login?dst=http%3A%2F%2Fexample.com%2F`).
- **link-login-only** - the login page, without the requested URL (`http://hotspot.lan/login`).
- **link-logout** - the logout page (`http://hotspot.lan/logout`).
- **link-status** - the status page (`http://hotspot.lan/status`).
- **link-orig** - the URL that the user requested (`http://example.com/`).
- **link-redirect** - the URL to which the page redirects the user.
- **link-advert** - the advertisement that is due.

### Client

- **domain** - the domain name of the user (`example.com`).
- **interface-name** - the name of the HotSpot interface (`bridge`).
- **ip** - the IP address of the client (`192.168.88.254`).
- **logged-in** - `yes` if the user is logged in, otherwise `no`.
- **mac** - the MAC address of the client (`52:54:09:80:02:01`).
- **trial** - `yes` if the user can use trial access, otherwise `no`.
- **username** - the name of the user (`anna`).
- **host-ip** - the IP address of the client in `/ip/hotspot/host`.
- **vlan-id** - the ID of the VLAN interface through which the client is connected.

### Session

- **idle-timeout** - the idle timeout (`20m`, or empty if none).
- **idle-timeout-secs** - the idle timeout in seconds (`88`, or `0` if none).
- **limit-bytes-in** - the limit of bytes that the user can send (`1000000`, or `---` if none).
- **limit-bytes-out** - the limit of bytes that the user can receive (`1000000`, or `---` if none).
- **refresh-timeout** - the refresh interval of the status page (`1m30s`, or empty if none).
- **refresh-timeout-secs** - the refresh interval of the status page in seconds (`90`, or `0` if none).
- **session-timeout**, **session-time-left** - the session time that is left (`5h`, or empty if none).
- **session-timeout-secs**, **session-time-left-secs** - the session time that is left, in seconds (`3475`, or `0` if none).
- **uptime** - the time since login (`10h2m33s`).
- **uptime-secs** - the time since login in seconds (`125`).

### Traffic counters

These variables have values only on the status and logout pages:

- **bytes-in** - the number of bytes received from the user (`15423`).
- **bytes-in-nice** - the same in a readable form.
- **bytes-out** - the number of bytes sent to the user (`11352`).
- **bytes-out-nice** - the same in a readable form.
- **packets-in** - the number of packets received from the user (`251`).
- **packets-out** - the number of packets sent to the user (`211`).
- **remain-bytes-in** - the bytes left until `limit-bytes-in` is reached (`337465`, or `---` if no limit).
- **remain-bytes-out** - the bytes left until `limit-bytes-out` is reached (`124455`, or `---` if no limit).
- **remain-bytes-total** - the bytes left until `limit-bytes-total` is reached.

### Other

- **session-id** - the value of the `session-id` parameter of the last request.
- **var** - the value of the `var` parameter of the last request.
- **error** - the error message, if something failed (`invalid username or password`). Only on the login page.
- **error-orig** - the original error message, before it is replaced by the text from `errors.txt`. Only on the login page.
- **chap-id** - the CHAP ID (`\371`). Only on the login page.
- **chap-challenge** - the CHAP challenge (`\357\015\330\013\021\234\145\245\303\253\142\246\133\175\375\316`). Only on the login page.
- **popup** - `true` or `false`: whether to open the status pop-up window. Only on the login page.
- **advert-pending** - `yes` if an advertisement is due, otherwise `no`.
- **http-status** - sets the HTTP status code and message, as described in the HTTP status and headers section.
- **http-header** - sets an HTTP header.

### RADIUS

- **radius\<id>** - the attribute with this ID as a text string. Empty if RADIUS authentication was not used.
- **radius\<id>u** - the attribute with this ID as an unsigned integer. `0` if RADIUS authentication was not used.
- **radius\<id>-\<vnd-id>** - the attribute with this ID and vendor ID as a text string.
- **radius\<id>-\<vnd-id>u** - the attribute with this ID and vendor ID as an unsigned integer.

### Request headers

The pages can read the HTTP headers of the request with `$(header-name)`. For example, `$(user-agent)` is the browser of the user. The last example on this page uses it.

## Conditions

A page can show a part of its content only when a condition is true:

- `$(if name)` - true if the variable is not empty.
- `$(if name == value)` and `$(if name != value)` - compare the variable with a value.
- `$(elif name == value)`, `$(else)`, and `$(endif)` continue and end the condition.

```html
some content, which is always displayed
$(if username == john)
Hey, your username is john
$(elif username == dizzy)
Hello, Dizzy! How are you? Your administrator.
$(elif ip == 10.1.2.3)
You are sitting at that old computer, which is so slow...
$(elif mac == 00:01:02:03:04:05)
This is an ethernet card, which was stolen few months ago...
$(else)
I don't know who you are, so let's live in peace.
$(endif)
other content, which is always displayed
```

Only one of the parts is shown: the first one whose condition is true.

## HTTP status and headers

Two variables are set, not tested, although they are written as conditions. `http-status` sets the status line of the HTTP response, and `http-header` adds a header. The default `rlogin.html` starts with these lines:

```html
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
```

If `$(link-redirect)` is `http://192.168.88.1/login`, the response to the client starts with:

```text
HTTP/1.0 302 Hotspot login required
<regular HTTP headers>
Location: http://192.168.88.1/login
```

The syntax:

```html
$(if http-status == XYZ)HTTP_STATUS_MESSAGE$(endif)
$(if http-header == HTTP_HEADER_NAME)HTTP_HEADER_VALUE$(endif)
```

- `XYZ` - the status code: three digits, the first one not 0.
- `HTTP_STATUS_MESSAGE` - the text after the status code.
- `HTTP_HEADER_NAME` and `HTTP_HEADER_VALUE` - the name and the value of the header.

Variables and conditions inside the message and the header value are processed as usual. If the same header is added several times, the last one is used. This way a page can replace a regular header, for example `Content-Type` or `Cache-Control`.

## Error messages

The texts of the error messages are in the `errors.txt` file of the directory. Edit the file to change or translate them. The file explains each message, and the messages can use variables. For example, this line:

```text
invalid-username = wrong name or password for $(username) from $(ip)
```

shows "wrong name or password for anna from 192.168.88.253" on the login page after a failed login.

## Several versions of the pages

One HotSpot server can have several sets of pages, for example one for each language. Create a sub-directory in the HTML directory and put the pages that differ into it. For a Latvian version, create the `lv` sub-directory with the translated `login.html`, `logout.html`, `status.html`, `alogin.html`, `radvert.html`, and `errors.txt`. A page that is not in the sub-directory is taken from the main directory.

The user selects the version with a link. In the main `login.html`:

```html
Latviski
```

and in the Latvian `login.html`:

```html
English
```

The `target` parameter selects the sub-directory as well:

```html
Latviski
English
```

After the user selects a version, the link variables contain its path, for example `$(link-status)` is `http://hotspot.lan/lv/status`. If the pages use the `$(link-...)` variables for all links, the user stays in the selected version.

## Examples

The examples change the default pages. The lines that they refer to are from the default `login.html`:

```html
<form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()" $(endif)>
    <input type="hidden" name="dst" value="$(link-orig)" />
    <input type="hidden" name="popup" value="true" />
    ...
    <input name="username" type="text" value="$(username)" placeholder="Username" />
    ...
    <input name="password" type="password" placeholder="Password" />
    ...
    <input type="submit" value="Connect" />
</form>
```

With the `http-chap` login method, the form calls the `doLogin()` function, which uses `md5.js` to hash the password together with `$(chap-id)` and `$(chap-challenge)`. Keep this function and the `onSubmit` attribute in your own login page, or the CHAP login fails.

### Change the colours

The default pages have three colour sets. To select another one, change the `<body>` tag of the page to one of these:

```html
<body class="lite">
<body class="dark">
```

### Use a fixed user name or password

To log every user in with the same user name, replace the user name field with a hidden field:

```html
<input name="username" type="hidden" value="hsuser" />
```

To use a fixed password, do the same with the password field:

```html
<input name="password" type="hidden" value="hspass" />
```

### One-click login

With a fixed user name and a fixed password, the login page needs only a button:

1. Create a user for this purpose, and a user profile with `shared-users` set to the number of devices that can be logged in at the same time:

   ```ros
   /ip/hotspot/user/profile/add name=open shared-users=unlimited
   /ip/hotspot/user/add name=guest password=guest profile=open
   ```

2. In your copy of `login.html`, replace the user name and password fields, with their `<label>` elements, by hidden fields, and change the text of the button:

   ```html
   <input name="username" type="hidden" value="guest" />
   <input name="password" type="hidden" value="guest" />
   <input type="submit" value="Proceed to Internet!" />
   ```

3. Set the directory with the changed page as `html-directory-override` of the server profile.

### Show a different text on each HotSpot server

One set of pages can serve several HotSpot servers. Use the server name in a condition:

```html
$(if server-name == hotspot1)
Welcome to the lobby network
$(else)
Welcome to the conference network
$(endif)
```

### Show the session values to the user

The status page can show any of the session variables. This table row from the default `status.html` shows the remaining time only for users who have a time limit:

```html
$(if session-time-left)
    Connected / left$(uptime) / $(session-time-left)
$(else)
    Connected$(uptime)
$(endif)
```

### Open another page after login

After login the browser opens the URL in the `dst` field, which is the page that the user requested. To open your own page instead, change this line of `login.html`:

```html
<input type="hidden" name="dst" value="$(link-orig)" />
```

to:

```html
<input type="hidden" name="dst" value="http://www.example.com" />
```

### Show a banner after login

In `alogin.html`, after the line `$(if popup == 'true')`, add:

```html
open('http://www.example.com/your-banner-page.html', 'my-banner-name','');
```

### Send the MAC address to a registration server

To send users to a registration page together with the MAC address of their device, add a link to `login.html`:

```html
Register
```

Allow the registration server in the walled garden, so that users can open it before login.

### Remove the cookie on logout

The status page opens the logout page with this line:

```html
open('$(link-logout)', 'hotspot_logout', ...
```

To remove the cookie of the user on logout, change it to:

```html
open('$(link-logout)?erase-cookie=on', 'hotspot_logout', ...
```

or add this field to the logout form of the page:

```html
<input type="hidden" name="erase-cookie" value="on">
```

### External authentication

The login page can be on another server, for example on a server that takes a payment before it gives access:

1. Allow access to the external server in the walled garden.
2. Change the login page of the HotSpot so that it redirects to the external server. The external server changes the RADIUS database as needed.
3. The external server logs the user in by sending the browser back to the login page of the HotSpot with the user name and password.

This login page on the HotSpot router redirects to `https://auth.example.com/login.php`. Replace it with the address of your server:

```html
<html>
<title>...</title>
<body>
<form name="redirect" action="https://auth.example.com/login.php" method="post">
<input type="hidden" name="mac" value="$(mac)">
<input type="hidden" name="ip" value="$(ip)">
<input type="hidden" name="username" value="$(username)">
<input type="hidden" name="link-login" value="$(link-login)">
<input type="hidden" name="link-orig" value="$(link-orig)">
<input type="hidden" name="error" value="$(error)">
</form>
<script language="JavaScript">
<!--
   document.redirect.submit();
//-->
</script>
</body>
</html>
```

This page on the external server sends the user back to the HotSpot. Replace `https://hotspot.example.com/login` with the address of your HotSpot router, and `http://www.mikrotik.com/` with the page to open after login:

```html
<html>
<title>Hotspot login page</title>
<body>
<form name="login" action="https://hotspot.example.com/login" method="post">
<input type="text" name="username" value="demo">
<input type="password" name="password" value="none">
<input type="hidden" name="domain" value="">
<input type="hidden" name="dst" value="http://www.mikrotik.com/">
<input type="submit" name="login" value="log in">
</form>
</body>
</html>
```

The HotSpot asks the RADIUS server whether to allow the login. If the login is allowed, `alogin.html` is shown. If not, `flogin.html` or `login.html` is shown, which sends the user back to the external server.

The external page sends the password as it is, so the server profile needs the `https` or `http-pap` login method. Without it, the login fails with the message "web browser did not send challenge response". As in these examples, use HTTPS and the POST method to protect the password.

### Answer differently to one browser

A page can test a request header and return other content instead of the regular page. For example, these lines at the top of `rlogin.html` answer "Success" to one browser instead of redirecting it to the login page:

```html
$(if user-agent == "Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0" )
<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>
$(else)
---- regular content of rlogin.html page  ----
$(endif)
```

This browser no longer opens the login page by itself.
