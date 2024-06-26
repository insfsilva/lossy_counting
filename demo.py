from lossy_counting import LossyCounting
from exact_counter import ExactCounter

import re
import string
import numpy as np


class Demo:
    def __init__(self, minSupport, error):
        self.lossyCounter = LossyCounting(minSupport=minSupport, error=error)
        self.exactCounter = ExactCounter(minSupport=minSupport)

    def printOutput(self):
        sortedLossyCounter = {k: v for k, v in
                              sorted(self.lossyCounter.getFrequentItems().items(), key=lambda item: item[1],
                                     reverse=True)}
        sortedExactCounter = {k: v for k, v in
                              sorted(self.exactCounter.getFrequentItems().items(), key=lambda item: item[1],
                                     reverse=True)}

        print("Lossy count frequencies: " + str(sortedLossyCounter))
        print("Exact frequencies: " + str(sortedExactCounter))


class ParetoDistributionDemo(Demo):
    def start(self):
        numberOfElements = 1000000
        shape = 2.0  # Forma da distribuição de Pareto
        scale = 1.0  # Escala da distribuição de Pareto
        for i in range(numberOfElements):
            randomElement = round(np.random.pareto(shape) * scale)
            self.lossyCounter.processNextElement(randomElement)
            self.exactCounter.processNextElement(randomElement)


class WebDataDemo(Demo):
    def start(self):
        with open("anonymous-msweb.data") as file:
            line = file.readline()
            while line:
                line = line.strip(' \n')
                data = line.split(" ")
                for item in data:
                    self.lossyCounter.processNextElement(item)
                    self.exactCounter.processNextElement(item)
                line = file.readline()


class ParadiseDemo(Demo):
    def start(self):
        with open("paradise.txt") as file:
            line = file.readline()
            while line:
                line = line.lower()
                line = re.sub(r'\d+', '', line)  # remove numbers
                line = line.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
                line = line.strip(' \n')
                if line == '':  # skip empty line
                    line = file.readline()
                    continue

                data = line.split(" ")
                for item in data:
                    self.lossyCounter.processNextElement(item)
                    self.exactCounter.processNextElement(item)
                line = file.readline()
