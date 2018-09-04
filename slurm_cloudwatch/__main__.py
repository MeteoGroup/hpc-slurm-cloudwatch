from .common import parse_args
from .common import prepare_cloudwatch_metrics
from .common import put_metric_data
from .nodes import parse_node_data
from .queue import parse_queue_data
from .scheduler import parse_scheduler_data


def main():
    args = parse_args()
    dimensions = args.dimensions
    namespace = args.namespace

    # Node data
    node_data = prepare_cloudwatch_metrics(parse_node_data(), dimensions)
    put_metric_data(node_data, namespace)

    # Queue data
    queue_data = prepare_cloudwatch_metrics(parse_queue_data(), dimensions)
    put_metric_data(queue_data ,namespace)

    # Scheduler data
    scheduler_data = prepare_cloudwatch_metrics(parse_scheduler_data(), dimensions)
    put_metric_data(scheduler_data, namespace)


if __name__ == '__main__':
    main()
