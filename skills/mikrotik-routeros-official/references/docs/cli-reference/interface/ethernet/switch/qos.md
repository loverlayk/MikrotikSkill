# qos

> The entire QoS hardware configuration is located under /in/eth/sw/qos. This centralized approach allows you to store all QoS-related configuration items in one place, making it easy to monitor and export settings...

-----------

## interface/ethernet/switch/qos 
**Syscap:** rbswitch and crs_prestera
**Type:** Directory

The entire QoS hardware configuration is located under `/in/eth/sw/qos`. This centralized approach allows you to store all QoS-related configuration items in one place, making it easy to monitor and export settings using `/in/eth/sw/qos/export`.

QoS entries have two major flag indicators:

- **H** - Hardware-offloaded entry.
- **I** - Inactive entry.
