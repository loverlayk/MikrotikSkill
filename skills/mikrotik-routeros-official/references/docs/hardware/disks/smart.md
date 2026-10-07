# S.M.A.R.T. info

> S.M.A.R.T. drive health monitoring in RouterOS: read drive health, temperature, use and error counters with the /disk smart-info command, and what the reported attributes mean.

# S.M.A.R.T. info

[*S.M.A.R.T. info CLI Reference*](../../cli-reference/disk/smart-info)

S.M.A.R.T. (Self-Monitoring, Analysis and Reporting Technology) is a monitoring system built into modern storage drives. It lets you read diagnostics of the drive: overall health, temperature, use, error counters and, for NVMe drives, the SMART/Health attributes.

:::info
S.M.A.R.T. information requires the [Storage](../../storage/) package.
:::

For any attached storage device that supports S.M.A.R.T., read the diagnostics with the `/disk/smart-info` command:

```ros
[admin@MikroTik] > /disk/smart-info nvme1
```

```ros
[admin@R2DUTRDS22162XG4S4XS2XQ20DISKS] > disk/smart-info nvme1
Columns: OUTPUT
OUTPUT                                                                     
smartctl 7.1 2019-12-30 r5022 [aarch64-linux-5.6.3] (local build)          
Copyright (C) 2002-19, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===                                       
Model Number:                       U.2 SSD 4TG2-P                         
Serial Number:                      <S/N>                      
Firmware Version:                   E21T4C                                 
PCI Vendor/Subsystem ID:            0x1bc0                                 
IEEE OUI Identifier:                0x24693e                               
Controller ID:                      0                                      
Number of Namespaces:               1                                      
Namespace 1 Size/Capacity:          960,197,124,096 [960 GB]               
Namespace 1 Formatted LBA Size:     512                                    
Namespace 1 IEEE EUI-64:            <EUI-64>                  
Firmware Updates (0x02):            1 Slot                                 
Optional Admin Commands (0x0017):   Security Format Frmw_DL Self_Test      
Optional NVM Commands (0x0054):     DS_Mngmt Sav/Sel_Feat Timestmp         
Maximum Data Transfer Size:         512 Pages                              
Warning  Comp. Temp. Threshold:     100 Celsius                            
Critical Comp. Temp. Threshold:     110 Celsius                            
Supported Power States                                                     
St Op     Max   Active     Idle   RL RT WL WT  Ent_Lat  Ex_Lat             
 0 +    20.00W       -        -    0  0  0  0        5       5             
Supported LBA Sizes (NSID 0x1)                                             
Id Fmt  Data  Metadt  Rel_Perf                                             
 0 +     512       0         0                                             
=== START OF SMART DATA SECTION ===                                        
SMART overall-health self-assessment test result: PASSED                   
SMART/Health Information (NVMe Log 0x02)                                   
Critical Warning:                   0x00                                   
Temperature:                        33 Celsius                             
Available Spare:                    100%                                   
Available Spare Threshold:          10%                                    
Percentage Used:                    0%                                     
Data Units Read:                    5,774,165 [2.95 TB]                    
Data Units Written:                 10,770,860 [5.51 TB]                   
Host Read Commands:                 75,868,764                             
Host Write Commands:                61,379,337                             
Controller Busy Time:               22                                     
Power Cycles:                       579                                    
Power On Hours:                     4,203                                  
Unsafe Shutdowns:                   105                                    
Media and Data Integrity Errors:    0                                      
Error Information Log Entries:      0                                      
Warning  Comp. Temperature Time:    0                                      
Critical Comp. Temperature Time:    0                                      
Temperature Sensor 1:               45 Celsius                             
Temperature Sensor 2:               33 Celsius                             
Temperature Sensor 3:               33 Celsius                             
Temperature Sensor 4:               34 Celsius                             
Temperature Sensor 5:               34 Celsius                             
Temperature Sensor 6:               35 Celsius                             
Temperature Sensor 7:               32 Celsius                             
Temperature Sensor 8:               31 Celsius                             
Error Information (NVMe Log 0x01, max 64 entries)                          
No Errors Logged      
```

## Reading the output

The important values for drive health:

- `SMART overall-health self-assessment test result`  -  the drive reports whether it considers itself healthy. A drive that reports `FAILED` should be replaced.
- `Temperature`  -  the current temperature of the drive. The warning and critical thresholds are listed in the information section.
- `Available Spare`  -  how much spare capacity the drive still has before it cannot remap bad blocks. When it drops to the `Available Spare Threshold`, the drive is close to the end of its life.
- `Percentage Used`  -  the estimated lifetime use of the drive, based on the manufacturer's rated endurance. At 100% the drive has reached its rated lifespan.
- `Unsafe Shutdowns` and `Media and Data Integrity Errors`  -  how often the drive lost power unexpectedly and how many data errors it detected. Repeated unsafe shutdowns increase the risk of corruption.

The output is the same as `smartctl` reports on Linux, so the S.M.A.R.T. documentation of the drive vendor applies.

:::note
Some USB enclosures cannot pass S.M.A.R.T. information through. If the drive is behind such an enclosure, `/disk/smart-info` reports an error even though the drive itself supports S.M.A.R.T.
:::

## Related

- [Disks](./)  -  formatting, mounting and managing drives.
