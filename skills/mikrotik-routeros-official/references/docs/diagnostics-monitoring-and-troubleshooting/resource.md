# Resource

> The /system/resource menu shows the router's identity and usage: uptime, RouterOS version, memory, disk/NAND, CPU model and load; submenus break load down per core (cpu), per interrupt (irq), steer packet handling...

# Resource

The [`/system/resource`](../cli-reference/system/resource) menu shows the overall resource usage and identity of the router: uptime, version, memory, disk, CPU model, architecture and the bad-block percentage of the NAND. All values are read-only.

```ros
[admin@MikroTik] > /system/resource/print
                   uptime: 2h31m3s
                  version: 7.26beta1
               build-time: 2026-10-01 13:29:47
          minimum-version: 7.0.9
              free-memory: 678.7MiB
             total-memory: 1024.0MiB
                      cpu: ARM64
                cpu-count: 4
            cpu-frequency: 864MHz
                 cpu-load: 0%
           free-hdd-space: 91.9MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 437
         write-sect-total: 263060
               bad-blocks: 0%
        architecture-name: arm64
               board-name: hAP ax^2
                 platform: MikroTik
```

The properties (uptime, version, build-time, memory, hdd space, write-sector and bad-block counters, board and platform names) are described in the [`/system/resource`](../cli-reference/system/resource) CLI reference page.

## Watch usage live

`/system/resource/monitor` prints a live-updating view of CPU usage per core and the free memory (the table refreshes continuously; bound it with `duration`):

```ros
[admin@MikroTik] > /system/resource/monitor duration=2
           cpu-used: 0%
  cpu-used-per-core: 1%
                     0%
                     0%
                     0%
        free-memory: 694948KiB
```

`free-memory` here is in KiB (694948 KiB ≈ 678.7 MiB shown by `print`).

## Read per-core breakdown

`/system/resource/cpu` shows usage per core, split into user load (`load`), interrupt handling (`irq`) and disk I/O (`disk`):

```ros
[admin@MikroTik] > /system/resource/cpu/print
Columns: CPU, LOAD, IRQ, DISK
#  CPU   LOAD  IRQ  DISK
0  cpu0  0%    0%   0%
1  cpu1  0%    0%   0%
2  cpu2  1%    0%   0%
3  cpu3  0%    0%   0%
```

## Interrupts (IRQ)

The [`/system/resource/irq`](../cli-reference/system/resource/irq) menu shows all used IRQs on the router, including the CPU the IRQ is assigned to and the interrupt counter rows for each device:

```ros
[admin@MikroTik] > /system/resource/irq/print where count>0
Flags: o - READ-ONLY
Columns: IRQ, USERS, CPU, ACTIVE-CPU, COUNT
 #   IRQ  USERS                                CPU   ACTIVE-CPU   COUNT
 0     6  bam_dma                              auto           0      68
 1     8  78b5000.spi                          auto           2     157
 2     9  glink-native                         auto           3     116
```

IRQ assignment with `cpu=auto` is done by the interrupt routing (which uses [NAPI](https://docs.kernel.org/networking/napi.html) interrupt consolidation). The `o` flag marks hardware-fixed IRQs, whose CPU assignment cannot be changed.

To pin an IRQ to a specific core:

```ros
/system/resource/irq/set [find irq=6] cpu=2
```

### Receive packet steering

[`/system/resource/irq/rps`](../cli-reference/system/resource/irq/rps) is Receive Packet Steering (RPS), similar to Receive Side Scaling (RSS), but implemented in software: it directs packet processing work of an interface to a chosen CPU. RPS is useful when packets require additional processing that uses a relatively large amount of CPU time, such as PPP tunnel termination, VPLS, or firewall processing: the cost of RPS steering is outweighed by spreading the heavy work over the cores.

RPS does not always pay off. If a network device has multiple hardware queues, its receive side scaling (RSS) already maps queues to CPUs, and RPS steering costs more than it saves. Configure RPS when the hardware has fewer queues than CPUs, or when RSS does not cover the path (for example packets decapsulated off a tunnel interface).

## Hardware map

`/system/resource/hardware` lists devices attached over the PCI, USB and SCSI buses with their bus location, vendor/device identifiers, firmware-reported name, driver owner, negotiated speed, USB version and so on. A board with no enumeration-capable bus (for example the hAP ax²) prints an empty list.

### USB device authorization

When USB device authorization is turned on globally (`authorization=yes` in [`/system/resource/hardware/usb-settings`](../cli-reference/system/resource/hardware/usb-settings)), newly attached USB devices stay disabled until the administrator allows them in [`/system/resource/hardware/authorize`](../cli-reference/system/resource/hardware/authorize).

### Reset USB devices

To reset a misbehaving USB modem or drive without rebooting the router, power-cycle its USB port with [`/system/resource/hardware/usb-power-reset`](../cli-reference/system/resource/hardware/usb-power-reset) (the `bus` and `slot` come from the device's `/system/resource/hardware` row):

```ros
/system/resource/hardware/usb-power-reset bus=1 slot=2 duration=5s
```

## Technical details

- `cpu-load` sums the usage of all cores of the CPU; use `/system/resource/cpu` or `monitor` for the per-core breakdown.
- `write-sect-since-reboot`/`write-sect-total` and `bad-blocks` help spot flash wear on NAND devices (together with the [Health](health) readings and `.65`-style early warnings).

For all parameters and their defaults, see the [`/system/resource`](../cli-reference/system/resource), [`cpu`](../cli-reference/system/resource/cpu), [`irq`](../cli-reference/system/resource/irq), [`irq/rps`](../cli-reference/system/resource/irq/rps), [`hardware`](../cli-reference/system/resource/hardware), [`usb-settings`](../cli-reference/system/resource/hardware/usb-settings), [`authorize`](../cli-reference/system/resource/hardware/authorize) and [`usb-power-reset`](../cli-reference/system/resource/hardware/usb-power-reset) CLI reference pages.
