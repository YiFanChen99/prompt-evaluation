from sumeval.metrics.rouge import RougeCalculator

class Rouge:
    def __init__(self):
        self.evaluator = RougeCalculator(stopwords=True, lang="zh")

class Rouge1(Rouge):
    def evaluate(self, inputData):
        return [ 
            self.evaluator.rouge_1(
                        references = data[0],
                        summary = data[1],
                    )
            for data in inputData
        ]
        
        
    
class Rouge2(Rouge):
    def evaluate(self, inputData):
        return [ 
            self.evaluator.rouge_2(
                        references = data[0],
                        summary = data[1],
                    )
            for data in inputData
        ]
    
class RougeL(Rouge):
    def evaluate(self, inputData):
        return [ 
            self.evaluator.rouge_l(
                        references = data[0],
                        summary = data[1],
                    )
            for data in inputData
        ]
    