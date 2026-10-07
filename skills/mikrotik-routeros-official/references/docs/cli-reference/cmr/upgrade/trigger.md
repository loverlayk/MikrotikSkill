# trigger

> Starts the job of a chosen rule right away, without waiting for the schedule-time. Only one upgrade job runs at a time; triggering another rule while a job is in progress places the new job in a queued state until...

-----------

## cmr/upgrade/trigger 
**Package:** cmr
**Type:** Command

Starts the job of a chosen rule right away, without waiting for the schedule-time. Only one upgrade job runs at a time; triggering another rule while a job is in progress places the new job in a [queued state](job#cmr-upgrade-job) until the current job finishes.

Triggering forces an early upgrade of the rule's covered devices: the job runs immediately and upgrades each covered device that has a newer version available, without waiting for the schedule-time. Covered devices that are already up to date are skipped, so the run's counter counts only the upgraded ones. To upgrade a single device regardless of its rule, see [`/cmr/device/upgrade`](../device/upgrade).
