""" This module is used for calculating bleu score of input data """
from sumeval.metrics.bleu import BLEUCalculator

class Bleu:
    """
        Class calculate bleu score
    """
    def __init__(self):
        self.calculator = BLEUCalculator(lang="zh")

    def evaluate(self, input_data):
        """
            Calculate bleu score on $input_data
        """
        return [
            self.calculator.bleu(
                        references = data[0],
                        summary = data[1],
                    )
            for data in input_data
        ]
