""" Module for parsing command line argument """
import argparse
from Metrics.load_metrics import Metric
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
        nargs = "*",
        choices = Metric.get_metrics_list()
    )
    parser.add_argument(
        "-f",
        "--format",
        type = str,
        choices = Readers.get_reader_list(),
        default="json"
    )
    parser.add_argument(
        "-llm",
        "--LargeLanguageModel",
        type = str,
        nargs = 2,
        metavar = Metric.get_llm_list(),
    )

    return parser.parse_args()

args = args_parser()
reader = Readers.get_format_reader(args.format)(args.input)
input_data = reader.get_list_data()
allResult = {}

if args.metric:
    for metric in args.metric:
        evaluator = Metric.get_metric_calculator(metric)
        result = evaluator.evaluate(input_data)
        allResult[metric] = result


if args.LargeLanguageModel:
    model_name = args.LargeLanguageModel[0]
    path_to_prompt = args.LargeLanguageModel[1]
    prompt_data = Readers.get_format_reader(args.format)(path_to_prompt).get_list_data()
    model = Metric.get_llm_evaluator(model_name)
    allResult[model_name] = model.evaluate(input_data, prompt_data)

reader.write_data(allResult, args.output)
