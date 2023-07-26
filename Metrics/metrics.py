""" Module to log error information """
import logging
from Metrics.rouge import Rouge1, Rouge2, RougeL

class Metric:
    """
        Class to get supported metric calculators information.
        Also provide mapping from metric name to metric calculator 
    """
    _MetricsEvaluators = {
        "rouge1": Rouge1,
        "rouge2": Rouge2,
        "rougeL": RougeL,
    }

    @staticmethod
    def get_metrics_list():
        """
            Get name of all supported metrics 
        """
        return Metric._MetricsEvaluators.keys()

    @staticmethod
    def get_metric_calculator(metric):
        """
            Reutrn metric calculator according to given metri name
        """
        aval_metric = Metric._MetricsEvaluators.keys()
        if metric not in aval_metric:
            logging.error("Asking a unImplemented or not supported metric")
            raise NotImplementedError
        return Metric._MetricsEvaluators[metric]
