from common import get_cmd_output

def parse_queue_data():
    """Get output of squeue and create metrics"""
    # Execute the squeue command and return its output
    cmd = "squeue -h -o %A,%T"
    data = get_cmd_output(cmd)
    queue_metrics_prefix = "slurm_queue_"
    queue_metrics = {
      "slurm_queue_cancelled": [0, "Count"],
      "slurm_queue_completed": [0, "Count"],
      "slurm_queue_completing": [0, "Count"],
      "slurm_queue_failed": [0, "Count"],
      "slurm_queue_pending": [0, "Count"],
      "slurm_queue_preempted": [0, "Count"],
      "slurm_queue_running": [0, "Count"],
      "slurm_queue_suspended": [0, "Count"],
      "slurm_queue_submitted": [0, "Count"],
      "slurm_queue_timeout": [0, "Count"],
      "slurm_queue_started": [0, "Count"]
    }
    for line in data.split("\n"):
        queue = line.split(",")[-1].lower()
        if len(queue) > 0:
            slurm_queue_state = queue_metrics_prefix + queue
            if slurm_queue_state in queue_metrics:
                queue_metrics[slurm_queue_state][0] += 1
            else:
                queue_metrics[slurm_queue_state] = [1, "Count"]
    cmd = "/usr/bin/sdiag"
    data = get_cmd_output(cmd)
    for line in data.split("\n"):
        if line.count(":") == 1:
          config, value = map(lambda s: s.strip(), line.split(":")[:2])
          try: 
            value = int(value)
          except:
            continue
          if config == "Jobs completed":
            queue_metrics["slurm_queue_completed"][0] = value
          elif config == "Jobs canceled":
            queue_metrics["slurm_queue_cancelled"][0] = value
          elif config == "Jobs submitted":
            queue_metrics["slurm_queue_submitted"][0] = value
          elif config == "Jobs failed":
            queue_metrics["slurm_queue_failed"][0] = value
          elif config == "Jobs running":
            queue_metrics["slurm_queue_running"][0] = value
          elif config == "Jobs started":
            queue_metrics["slurm_queue_started"][0] = value
          else:
            continue
    return queue_metrics
