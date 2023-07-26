""" Module for parsing command line argument """
import argparse
from Metrics.metrics import Metric
from Readers.readers import Readers

def args_parser():
    """ Parsing command argumen """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type = str, required = True, help = "Path to input file")
    parser.add_argument("-o", "--output", type = str, required = True, help = "Path to output file")
    parser.add_argument(
        "-m",
        "--metric",
        type = str,
        nargs = "+",
        choices = Metric.get_metrics_list()
    )
    parser.add_argument(
        "-f",
        "--format",
        type = str,
        choices = Readers.get_reader_list(),
        default="json"
    )

    return parser.parse_args()

args = args_parser()
reader = Readers.get_format_reader(args.format)(args.input)
inputData = reader.get_list_data()
allResult = {}

for metric in args.metric:
    evaluator = Metric.get_metric_calculator(metric)()
    result = evaluator.evaluate(inputData)
    allResult[metric] = result

reader.write_data(allResult, args.output)
