import logging
from Evaluators.Rouge import *

class Evaluator:
    _MetricsEvaluators = {
        "rouge1": Rouge1,
        "rouge2": Rouge2,
        "rougeL": RougeL,
    }

    @staticmethod
    def GetMetricsList():
        return Evaluator._MetricsEvaluators.keys()
    
    @staticmethod
    def GetMetricsEvaluator(metric):
        if metric not in Evaluator._MetricsEvaluators.keys():
            logging.error("Asking a unImplemented or not supported metric")
            raise NotImplementedError
        return Evaluator._MetricsEvaluators[metric]
