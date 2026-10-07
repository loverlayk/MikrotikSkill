# Branding

> RouterOS Branding package enables customization of system elements including router name, company URLs, ASCII logos, and WebFig interfaces. It supports custom file inclusion for login pages, skins, and hotspot logos...

# Branding

RouterOS allows slight system customization with the help of a branding package (modify default configuration, LCD logo, WebFig homepage, etc.).

This is a special system package, which you can generate from within your [mikrotik.com](https://mikrotik.com) account, in the account section "Branding maker". The resulting file will have a .dpk extension and can be installed by all the same means as an .npk package.

To install the package on a router, the branding package has to be uploaded to it and then the router has to reboot. The Netinstall tool can be used for the same effect.

The generated package can be installed in any RouterOS version.

:::info
Note that specific branding features are available starting from specific RouterOS versions.

:::

## Options

Options that can be configured using a branding package:

- **Router name** - Branding package name, device identity and [platform name](../diagnostics-monitoring-and-troubleshooting/resource.md) in RouterOS, can only be one word, don't use spaces or special characters.
- **Company URL**- Value that appears in the console when you connect to a RouterOS device.
- **Manual URL**- Documentation link, which can be opened in [WebFig](./webfig.md).
- **ASCII Logo** - A text logo that is shown when logging into the command line interface, i.e., Telnet, SSH, WinBox Terminal. A logo can be created in the [branding maker](https://mikrotik.com/client/branding) or copied from any other plaintext editor. A logo height cannot be larger than 8 lines, width is not limited, but note that in a narrow terminal window a logo might be distorted.
- **Hide "Mikrotik" from SNMP information** - The MikroTik name will be hidden in SNMP information.
- **Do not run script on install** - Do not run Default configuration script on branding package install.
- **Hide Default configuration prompt**- Hide the Default configuration prompt after configuration reset *(available starting from RouterOS 7.15)*.
- **Hide default caps-mode-script** - Hide default caps-mode-script *(available starting from RouterOS 7.15)*.

## Custom files

Custom files such as the WebFig login page, WebFig logo, hotspot, skins, Default configuration, LCD logo and CAPs mode script can be included in the branding package.

:::warning
Any reset button mode will restore the default configuration from the branding package.

:::

#### WebFig login page

The WebFig login page is a customized default RouterOS login interface that appears when accessing the router's IP address. This page can be customized to meet branding or functional requirements.

- **Customization Files:**

  - **`/index2.html`**: Main template for the login page.
  - **`/assets/style.css`**:  MikroTik RouterOS stylesheet.
  - **`/assets/script.js`** is responsible for handling the login functionality and contains code that gives the button interactivity.
- **Required Elements for the `script.js`:**

  1. **Form for Login:**  
     `<form id="login">`
  2. **Username Field:**  
     `<input id="name" data-defaultuser="admin">`
     - The `admin` value can be changed to another username or left blank.
  3. **Password Field:**  
     `<input id="password">`
  4. **Error Display Section:**  
      ``
- Here is an example of a user-customized login page with a "Show Password" button, achieved using a modified **`[index2.html](pathname:///assets/295239801_index2.html)`** along with additional [toggle_button.css](pathname:///assets/295239803_toggle_button.css) and [show_password.js](pathname:///assets/295239802_show_password.js) files.  
  The HTML file must be named "index2.html" and should use properly nested HTML to ensure compatibility with all browsers.
- The uploaded images or JavaScript files must reference the same path as the index file. No custom folder names can be used.

---

#### WebFig logo

RouterOS WebFig page (configuration page) logo. To overwrite the MikroTik logo on the WebFig login page, upload your custom logo named "mikrotik\_logo.png".

#### hotspot

Hotspot login page logo. The file must be named "logobottom.png".

#### skins

A skin file with the name "your\_file\_name.json". To apply a particular skin to a specific user group, you don't need to log into the router. You can do it with branding by uploading a Default configuration file.

#### Default configuration

A RouterOS default configuration file that will override the RouterOS default configuration. This configuration will persist even after a RouterOS reset. Factory passwords can be reapplied using the read-only variables *$defconfPassword* and *$defconfWifiPassword* (access to factory passwords is available starting RouterOS 7.10).

:::warning
If a Default configuration or CAPs mode script execution takes more than 2 minutes, the script will fail, and LOG will contain *"runtime limit exceeded"* or in rare cases *"std failure: timeout"* error.

:::

#### LCD logo

The LCD logo will be displayed on devices equipped with an LCD screen. The logo size cannot be larger than 160px width and 72px height. The CCR1xxx series has a white (0xffffff) background, the 2011 series have a black (0x000000) background.

#### Custom files

Custom files will be copied into a folder named "branding" and will be accessible from within RouterOS.

#### CAPs mode script

A RouterOS CAPs mode script that will override the RouterOS default CAPs mode script. It is possible to reapply the factory passwords by utilizing the read-only variables *$defconfPassword* and *$defconfWifiPassword* (available starting from RouterOS 7.15).

:::warning
Any reset button mode will restore the default configuration from the branding package. The CAPs mode script can only be applied via the GUI or CLI by performing a [configuration reset](../getting-started/configuration-management/index.md#configuration-reset) after the device has fully booted.

:::

:::warning
If a Default configuration or CAPs mode script execution takes more than 2 minutes, the script will fail, and the LOG will contain *"runtime limit exceeded"* or in rare cases *"std failure: timeout"* error.

:::
