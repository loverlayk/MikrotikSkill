# run-next

> Runs the next scheduled upgrade job right away. For a job of an upgrade rule, the job starts as a new run, and the originally scheduled job remains scheduled. A job scheduled with /cmr/device/upgrade has no schedule...

-----------

## cmr/upgrade/job/run-next 
**Package:** cmr
**Type:** Command

Runs the next scheduled upgrade job right away. For a job of an upgrade rule, the job starts as a new run, and the originally scheduled job remains scheduled. A job scheduled with `/cmr/device/upgrade` has no schedule to keep, so that job itself starts. Only one upgrade job runs at a time, so a job started while another job is already in progress is queued, not interrupted.
