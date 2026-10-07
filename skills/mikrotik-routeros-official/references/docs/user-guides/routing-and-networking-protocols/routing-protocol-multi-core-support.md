# Routing Protocol Multi-core Support

> RouterOS v7 enables multi-core routing by distributing tasks like FIB updates, BGP processing, and protocol handling across separate processes. Each sub-task uses private or shared memory, with BGP input/output...

# Routing Protocol Multi-core Support

RouterOS v7 can split tasks between multiple processes.

One "**main**" task starts and stops sub‑tasks and processes data between them. Each sub‑task can allocate "private" memory (accessible only to that task) and "shared" memory (accessible by all route tasks).

The following tasks run in separate processes when multiprocess routing is enabled:

- FIB update.
- Routing Policy configuration.
- Configuration and reporting - handling of the static route configuration, "route print" command, SNMP monitoring, etc.
- BFD protocol handling
- OSPF protocol handling.
- RIP protocol handling.
- ISIS protocol handling.
- EVPN handling.
- PIM-SM.
- LDP protocol handling.
- Fantasy - handles generation of dummy routing entries for testing purposes.
- BGP connection and configuration handling.
- BGP receive (one task per peer or grouped by specific parameters).
- BGP send (one task per peer or grouped by specific parameters).

## BGP Sub-Tasks

BGP receive and send can be split into sub‑tasks by specific parameters. For example, you can run input per peer or group all peer inputs and run them in the main process. You control this split with the [`input.affinity`](../../cli-reference/routing/bgp/connection.md#input.affinity) and [`output.affinity`](../../cli-reference/routing/bgp/connection.md#output.affinity) parameters in [`/routing/bgp/template`](../../cli-reference/routing/bgp/template.md). On devices with few cores, adjusting affinity values can boost performance because sharing data between tasks is slightly slower than processing the same data within a single task. For example, on single-core or dual-core devices, running input and output in the main or instance process improves performance.

:::warning
BGP can spawn up to 100 unique processes.
:::

You can monitor all currently used tasks and their allocated private/shared memory with the [`/routing/stats/process/print`](../../cli-reference/routing/stats/process/process.md) command.

Sample Output:

```text
[admin@BGP_MUM] /routing/stats/process> print interval=1
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-BUSY, MAX-BUSY, CUR-CALC, MAX-CALC
   #  TASKS                         PRIVATE-M  SHARED-M  PSS        RSS      VMS      R  ID       PID  R  PROCESS-  KERNEL-TI  CUR-  MAX-BUSY  CUR-  MAX-CALC
   0  routing tables                11.8MiB    20.0MiB   19.8MiB    42.2MiB  51.4MiB  7  main     195  0  15s470ms  2s50ms     20ms  1s460ms   20ms  35s120ms
      rib                                                                                                                                                    
      connected networks                                                                                                                                     
   1  fib                           2816.0KiB  0         8.1MiB     27.4MiB  51.4MiB     fib      255  1  5s730ms   7m4s790ms        23s350ms        23s350ms
   2  ospf                          512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     ospf     260  1  20ms      100ms            20ms            20ms    
      connected networks                                                                                                                                     
   3  fantasy                       256.0KiB   0         1898.0KiB  5.8MiB   51.4MiB     fantasy  261  1  40ms      60ms             20ms            20ms    
   4  configuration and reporting   4096.0KiB  512.0KiB  9.2MiB     28.4MiB  51.4MiB     static   262  1  3s210ms   40ms             220ms           220ms   
   5  rip                           512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     rip      259  1  50ms      90ms             20ms            20ms    
      connected networks                                                                                                                                     
   6  routing policy configuration  768.0KiB   768.0KiB  2250.0KiB  6.2MiB   51.4MiB     policy   256  1  70ms      50ms             20ms            20ms    
   7  BGP service                   768.0KiB   0         3359.0KiB  14.9MiB  51.4MiB     bgp      257  1  4s260ms   8s50ms           30ms            30ms    
      connected networks                                                                                                                                     
   8  BFD service                   512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     12       258  1  80ms      40ms             20ms            20ms    
      connected networks                                                                                                                                     
   9  BGP Input 10.155.101.232      8.2MiB     6.8MiB    17.0MiB    39.1MiB  51.4MiB     20       270  1  24s880ms  3s60ms           18s550ms        18s550ms
      BGP Output 10.155.101.232                                                                                                                              
  10  Global memory                            256.0KiB                                  global     0  0    
```

## Routing Table Update Mechanism

The following illustration explains, in a more user‑friendly way, how the routing table update mechanism works.

![](img/37224450.png)

Routing protocols continuously loop through the following procedures:

- The "**main**" process waits for updates from other sub‑tasks (1).
- "**main**" starts calculating new routes (2–4) if:
  - an update from a sub‑task is received;
  - the protocol has not published all routes;
  - the configuration or link state has changed.
- During new route calculation (5), the following events occur:
  - all received updates are applied to the route;
  - gateway reachability is determined;
  - recursive routes are resolved;
- The "**publish**" event runs, publishing "**current**" routes. During this phase, "**current**" routes do not change, but protocols can still receive and send updates (6).
- Perform cleanup and free unused memory (7). At this step, anything no longer used in the new "**current**" table is removed (routes, attributes, etc.).

Consider "**updated**" and "**current**" as two copies of the routing table. The "**current**" table (2) is used at the moment, while "**updated**" (1) is the table of candidate routes to be published in the next publish event (3 and 4). This method prevents protocols from filling memory with buffered updates while the "**main**" process performs "**publish**". Instead, protocols send the newest updates directly to the main process, which then copies the new updates into the "**updated**" table. OSPF is slightly more complicated: it internally has a similar process to select current OSPF routes, which are then sent to the "**main**" for further processing.
