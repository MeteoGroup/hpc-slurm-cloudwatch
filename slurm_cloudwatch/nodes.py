from common import get_cmd_output

def parse_node_data():
    """Get output of sinfo and create metrics"""
    # Execute the squeue command and return its output
    cmd = "sinfo -h  -o %n,%T"
    data = get_cmd_output(cmd)
    node_metrics_prefix = "slurm_node_"
    node_metrics = {
       "slurm_node_fail": [0, "Count"],
       "slurm_node_drain": [0, "Count"],
       "slurm_node_down": [0, "Count"],
       "slurm_node_err": [0, "Count"],
       "slurm_node_alloc": [0, "Count"],
       "slurm_node_comp": [0, "Count"],
       "slurm_node_idle": [0, "Count"],
       "slurm_node_maint": [0, "Count"],
       "slurm_node_mix": [0, "Count"],
       "slurm_node_resv": [0, "Count"]
    }
    for line in data.split("\n"):
        node_status = ''.join(s for s in line.split(",")[-1] if s.isalnum() or s == "_")
        if len(node_status) > 0:
          slurm_node_state  = node_metrics_prefix + node_status
          if slurm_node_state in node_metrics:
              node_metrics[slurm_node_state][0] += 1
          else:
              node_metrics[slurm_node_state] = [1, "Count"]
    return node_metrics
