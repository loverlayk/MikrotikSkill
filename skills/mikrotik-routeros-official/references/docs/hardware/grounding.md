# Grounding

> Grounding requirements for MikroTik RouterOS devices emphasize proper installation of shielded cables, lightning arresters, and reliable grounding infrastructure using 2.5-4 mm² Cu wire with corrosion-resistant...

# Grounding

## Introduction

Shielded cable installation infrastructure (towers and masts), as well as antennas and the router itself, must be properly grounded. Lightning arresters must be installed on all external antenna cables (near the antennas or on the antennas themselves) to prevent equipment damage and human injury. Note that lightning arresters will not be effective if they are not properly grounded.

Use 2.5-4 mm² Cu (AWG 11–13) wire with corrosion-resistant connectors for grounding. Ensure that the grounding infrastructure you use is fully functional (not merely decorative, as seen in some installations):

1. For shielded connectors, please use shielded cables as they provide better immunity.
2. The grounding wire should be connected to the RouterBOARD grounding wire attachment point if such is provided. This wire should then be connected to the base of the tower, ensuring the connection meets grounding standards. The antenna's grounding wire should be connected near the RouterBOARD outdoor case and can be joined with the same grounding wire used for the RouterBOARD.

## Shielded RJ45 Port vs Unshielded RJ45 Port

### Device with Shielded Ports

![shielded.png](./img/grounding-01.webp)
![](./img/grounding-diagram.png)

### Device with Unshielded Ports

![unshielded.png](./img/grounding-02.webp)

### PoE injector with shielded connectors

![poeinjector.png](./img/grounding-03.webp)

## RouterBOARD grounding wire attachment points

![](./img/grounding-04.webp)

![screw1.png](./img/grounding-05.webp)

![screw2.png](./img/grounding-06.webp)

:::info
You should not use Power Sourcing Equipment (PSE) with the positive terminal connected to Protective Earth (PE) if it power a MikroTik device. It may cause a short circuit, harm you and your device.

:::
