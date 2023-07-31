""" This module helps user loading metric calculator they want """
import logging
from Metrics.rouge import Rouge1, Rouge2, RougeL
from Metrics.bleu import Bleu
from Metrics.llm import OpenAILLM

class Metric:
    """
        Class to get supported metric calculators information.
        Also provide mapping from metric name to metric calculator
    """
    _MetricsEvaluators = {
        "rouge1": Rouge1(),
        "rouge2": Rouge2(),
        "rougeL": RougeL(),
        "bleu": Bleu(),
    }

    _LLMEvaluators = {
        "gpt-3.5-turbo": OpenAILLM("gpt-3.5-turbo"),
        "gpt-4": OpenAILLM("gpt-4"),
    }

    @staticmethod
    def get_metrics_list():
        """
            Get name of all supported metrics
        """
        return Metric._MetricsEvaluators.keys()

    @staticmethod
    def get_llm_list():
        """
            Get name of all supported LLM
        """
        return Metric._LLMEvaluators.keys()

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

    @staticmethod
    def get_llm_evaluator(llm):
        """
            Reutrn metric calculator according to given metri name
        """
        aval_llm = Metric._LLMEvaluators.keys()
        if llm not in aval_llm:
            logging.error("Asking a unImplemented or not supported metric")
            raise NotImplementedError
        return Metric._LLMEvaluators[llm]
