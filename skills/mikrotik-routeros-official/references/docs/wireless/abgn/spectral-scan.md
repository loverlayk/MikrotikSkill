# Spectral scan

> The Spectral Scan feature in MikroTik RouterOS allows continuous monitoring and visualization of wireless spectrum activity, including interference detection across 2.4GHz and 5GHz bands using spectral snapshots with...

# Spectral scan

The spectral scan can scan all frequencies supported by your wireless card, and plot them directly in the console. The exact frequency span depends on the card. Allowed ranges on r52n: [4790; 6085], [2182; 2549].

A wireless card can generate 4us long spectral snapshots for any 20mhz wide channel. This is considered a single spectral sample.

To improve data quality, the spectrum is scanned with 10mhz frequency increments, which means doubled sample coverage at each specific frequency (considering 20mhz wide samples).

:::warning
Currently, is NOT supported for Atheros 802.11ac chips (e.g. QCA98xx, IPQ-4018). See [https://mikrotik.com/products](https://mikrotik.com/products) to determine the wireless chip on your device.
:::

## Console

### Spectral History

![](./img/spectral-scan-01.webp)

```ros
/interface/wireless/spectral-history <wireless interface name> 
```

Plots a spectrogram. Legend and frequency ruler are printed every 24 lines. Numbers in the ruler correspond to the value at their leftmost character position. Power values that fall in different ranges are printed as different colored characters with the same foreground and background color, so it is possible to copy and paste the terminal output of this command.

- *value* -- Select the value that is plotted on the output. 'interference' is special as it shows detected interference sources (affected by the 'classify-samples' parameter) instead of power readings, and cannot be made audible.
- *interval* -- Interval at which spectrogram lines are printed.
- *duration* -- Terminate command after a specified time. The default is indefinite.
- *buckets* -- How many values to show in each line of a spectrogram. This value is limited by the number of columns in the terminal. It is useful to reduce this value if using 'audible'.
- *average-samples* -- Number of 4us spectral snapshots to take at each frequency, and calculate average and maximum energy over them. (default 10).
- *classify-samples* -- Number of spectral snapshots taken at each frequency and processed by the interference classification algorithm. Generally, more samples give more chance to spot certain types of interference (default 50).
- *range* --
  - 2.4ghz - scan the whole 2.4ghz band;
  - 5ghz - scan the whole 5ghz band;
  - current-channel - scan the current channel only (20 or 40 MHz wide);
  - range - scan a specific range.

- *audible=yes* -- Play each line as it is printed. There is a short silence between the lines. Each line is played from left to right, with higher frequencies corresponding to higher values in the spectrogram.

### Spectral Scan

![](./img/spectral-scan-02.webp)

```ros
 /interface/wireless/spectral-scan <wireless interface name> 
```

Continuously monitors spectral data. This command uses the same data source as 'spectral-history', and thus shares many parameters.

Each line displays one spectrogram bucket -- frequency, the numeric value of average power, and a character graphic bar. A bar shows average power value with ':' characters and average peak hold with '.' characters. Maximum is displayed as a lone floating ':' character.

- *show-interference* -- adds a column that shows detected interference sources;

Types of possibly classified interference:

- Bluetooth-headset
- Bluetooth-stereo
- cordless-phone
- microwave-oven
- CWA
- video-bridge
- wifi

## The Dude

The Dude is a free network monitoring and management program by MikroTik. You [can download it here](http://www.mikrotik.com/thedude.php).

The Dude has a built-in capability to run graphical Spectral Scan from any of your RouterOS devices with a supported wireless card. Simply select this device in your Dude map, right click and choose Tools -> Spectral Scan.

![](./img/spectral-scan-03.webp)

This will bring up the Spectral Scan GUI with various options and different view modes:

![](./img/spectral-scan-04.webp)
