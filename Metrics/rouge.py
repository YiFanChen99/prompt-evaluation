""" Package supporting calculate rouge score in Chinese/English"""
from sumeval.metrics.rouge import RougeCalculator

class Rouge:
    """
        Base class for classes calculating rouge score
    """
    def __init__(self):
        self.evaluator = RougeCalculator(stopwords=True, lang="zh")

class Rouge1(Rouge):
    """
        Class calculate rouge1 score
    """
    def evaluate(self, input_data):
        """
            Calculate rouge1 score on $input_data
        """
        return [
            self.evaluator.rouge_1(
                        references = data[0],
                        summary = data[1],
                    )
            for data in input_data
        ]

class Rouge2(Rouge):
    """
        Class calculate rouge2 score
    """
    def evaluate(self, input_data):
        """
            Calculate rouge2 score on $input_data
        """
        return [
            self.evaluator.rouge_2(
                        references = data[0],
                        summary = data[1],
                    )
            for data in input_data
        ]

class RougeL(Rouge):
    """
        Class calculate rougeL score
    """
    def evaluate(self, input_data):
        """
            Calculate rougeL score on $input_data
        """
        return [
            self.evaluator.rouge_l(
                        references = data[0],
                        summary = data[1],
                    )
            for data in input_data
        ]
    