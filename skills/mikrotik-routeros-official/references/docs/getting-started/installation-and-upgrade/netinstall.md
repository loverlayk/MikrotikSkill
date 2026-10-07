# Netinstall

> This page introduces Netinstall, the MikroTik utility for installing and reinstalling RouterOS, helps choose between the Windows, Linux, and Netinstall package methods, and describes the common device installation...

# Netinstall

Netinstall is a utility for installing and reinstalling RouterOS on MikroTik devices. It can be used to recover inaccessible devices, perform clean installations, or reinstall RouterOS when the system is corrupted or misconfigured.

The tool is available for Windows (graphical interface) and Linux (command-line). Starting with RouterOS 7.24beta1, the **Netinstall package** is available for all MikroTik architectures except SMIPS devices.

## Choose a Netinstall Method

Select the installation method that matches your environment:

- [**Windows Netinstall**](./netinstall-windows.md) - Graphical interface for Windows systems.
- [**Linux Netinstall**](./netinstall-linux.md) - Command-line utility for Linux systems.
- [**Netinstall Package**](./netinstall-package.md) - RouterOS package that enables Netinstall functionality directly on supported MikroTik devices.

You can download Netinstall tools and RouterOS packages from the [MikroTik Downloads](https://mikrotik.com/download) page.

:::danger
Netinstall reformats the system drive, which erases all configuration data and user files.

Netinstall does not remove the RouterOS license key, nor does it reset RouterBOOT settings. For example, the CPU frequency remains unchanged during reinstallation.
:::

## Device Installation Workflow Using Netinstall

The workflow below applies to all Netinstall methods.

### Prepare the Netinstall host

Start Netinstall on a computer or MikroTik router connected to the same Layer 2 (L2) network segment as the device being reinstalled. For best results, use a dedicated network interface and a simple switch or hub to avoid IP, DHCP, or BOOTP conflicts.

### Boot the device into Etherboot mode

Etherboot mode is a special boot state on MikroTik devices that allows you to reinstall RouterOS using Netinstall.

Two booter options are available: the **Regular Booter** and the **Backup Booter**. It is recommended to verify both options in case one does not work.

- **Regular Booter:** To enter etherboot mode using the serial console, press and hold <kbd>Control</kbd>+<kbd>E</kbd>. Alternatively, press the **Reset** button after powering on the device and waiting 1–2 seconds.

- **Backup Booter:** Power off the device. Press and hold the **Reset** button, then power on the device. Wait for the **LED** sequence (blinking → steady → off), then release the button. The device will boot into **BOOTP** mode, ready for RouterOS reinstallation via Netinstall. Depending on the model, this may be indicated by the **USR, USER, System**, or **ACT** LED, or by the SFP port LED.

### Install the device

Use Netinstall to install RouterOS with the desired packages, parameters, and configuration scripts.

## Additional References

- [RouterOS configuration management](../../configuration-management/index.md)
- [RouterOS packages](../packages.md)
- [RouterBOOT configuration](../routerboot.md)
- [MikroTik downloads](https://mikrotik.com/download)
