# Slurm Performance Metrics in CloudWatch

Get slurm performance metrics and put into cloudwatch

## Exported Metrics

### State of the Nodes

* **Allocated**: nodes which has been allocated to one or more jobs.
* **Completing**: all jobs associated with these nodes are in the process of being completed.
* **Down**: nodes which are unavailable for use.
* **Drain**: with this metric two different states are accounted for:
  - nodes in ``drained`` state (marked unavailable for use per system administrator request)
  - nodes in ``draining`` state (currently executing jobs but which will not be allocated for new ones).
* **Fail**: these nodes are expected to fail soon and are unavailable for use per system administrator request.
* **Error**: nodes which are currently in an error state and not capable of running any jobs.
* **Idle**: nodes not allocated to any jobs and thus available for use.
* **Maint**: nodes which are currently marked with the __maintenance__ flag.
* **Mixed**: nodes which have some of their CPUs ALLOCATED while others are IDLE.
* **Resv**: these nodes are in an advanced reservation and not generally available.

[Information extracted from the SLURM **sinfo** command](https://slurm.schedmd.com/sinfo.html)

### Status of the Jobs

* **PENDING**: Jobs awaiting for resource allocation.
* **RUNNING**: Jobs currently allocated.
* **SUSPENDED**: Job has an allocation but execution has been suspended and CPUs have been released for other jobs.
* **CANCELLED**: Jobs which were explicitly cancelled by the user or system administrator.
* **COMPLETING**: Jobs which are in the process of being completed.
* **COMPLETED**: Jobs have terminated all processes on all nodes with an exit code of zero.
* **CONFIGURING**: Jobs have been allocated resources, but are waiting for them to become ready for use.
* **FAILED**: Jobs terminated with a non-zero exit code or other failure condition.
* **TIMEOUT**: Jobs terminated upon reaching their time limit.
* **PREEMPTED**: Jobs terminated due to preemption.
* **NODE_FAIL**: Jobs terminated due to failure of one or more allocated nodes.

[Information extracted from the SLURM **squeue** command](https://slurm.schedmd.com/squeue.html)

### Scheduler Information

* **Server Thread count**: The number of current active ``slurmctld`` threads. 
* **Queue size**: The length of the scheduler queue.
* **Last cycle**: Time in microseconds for last scheduling cycle.
* **Mean cycle**: Mean of scheduling cycles since last reset.
* **Cycles per minute**: Counter of scheduling executions per minute.
* **(Backfill) Last cycle**: Time in microseconds of last backfilling cycle.
* **(Backfill) Mean cycle**: Mean of backfilling scheduling cycles in microseconds since last reset.
* **(Backfill) Depth mean**: Mean of processed jobs during backfilling scheduling cycles since last reset.

[Information extracted from the SLURM **sdiag** command](https://slurm.schedmd.com/sdiag.html)

### TODO

 - Add testcase 
 - try using pyslurm module instead of slurm commands
