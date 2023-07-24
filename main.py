import argparse
from Evaluators.Evaluators import Evaluator
from Readers.Readers import Readers

def ArgsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type = str, required = True, help = "Path to input file")
    parser.add_argument("-o", "--output", type = str, required = True, help = "Path to output file")
    parser.add_argument("-m", "--metric", type = str, nargs = "+", choices = Evaluator.GetMetricsList() )
    parser.add_argument("-f", "--format", type = str, choices = Readers.GetReaderList(), default="json")

    return parser.parse_args()

args = ArgsParser()
inputData = Readers.GetFormatReader(args.format)(args.input).GetListData()
allResult = {}

for metric in args.metric:
    evaluator = Evaluator.GetMetricsEvaluator(metric)()
    result = evaluator.evaluate(inputData)
    allResult[metric] = result

print(allResult)



