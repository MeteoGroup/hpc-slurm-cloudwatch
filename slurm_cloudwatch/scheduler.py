from common import get_cmd_output

def parse_scheduler_data():
    """Get output of sinfo and create metrics"""

    cmd = "/usr/bin/sdiag"
    data = get_cmd_output(cmd)

    scheduler_metrics = {
            "slurm_scheduler_threads": [0, "Count"],
            "slurm_scheduler_queue_size": [ 0, "Count"],
            "slurm_scheduler_last_cycle": [0, "Microseconds"],
            "slurm_scheduler_mean_cycle": [0, "Microseconds"],
            "slurm_scheduler_cycle_per_minute": [0*60, "Seconds"],
            "slurm_scheduler_backfill_last_cycle": [0, "Microseconds"],
            "slurm_scheduler_backfill_mean_cycle": [0, "Microseconds"],
            "slurm_scheduler_backfill_depth_mean": [0,"Count"]
            }

    backfill = False
    for line in data.split("\n"):
        if "Backfilling" in line:
            backfill = True
        if ":" in line:
            config, value = map(lambda s: s.strip(), line.split(":")[:2])
            try:
               value = int(value) 
            except:
               continue
            if "Server thread count" == config:
                scheduler_metrics["slurm_scheduler_threads"][0] = value
            elif "Agent queue size" == config:
                scheduler_metrics["slurm_scheduler_queue_size"][0] = value
            if not backfill:
               if "Last cycle" == config:
                   scheduler_metrics["slurm_scheduler_last_cycle"][0] = value
               elif "Mean cycle" == config:
                   scheduler_metrics["slurm_scheduler_mean_cycle"][0] = value
               elif "Cycles per minute" == config:
                   scheduler_metrics["slurm_scheduler_cycle_per_minute"][0] = value
            if backfill:
                if "Last cycle" == config:
                    scheduler_metrics["slurm_scheduler_backfill_last_cycle"][0] = value
                elif "Mean cycle" == config:
                    scheduler_metrics["slurm_scheduler_backfill_mean_cycle"][0] = value
                elif "Depth Mean" == config:
                    scheduler_metrics["slurm_scheduler_backfill_depth_mean"][0] = value
    return scheduler_metrics
