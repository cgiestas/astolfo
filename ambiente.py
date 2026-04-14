import random

class Ambiente:
    def __init__(self):
        self.temp = 24.0

    def oscilacao(self):
        self.temp += round(random.uniform(-0.3, 0.3), 1)

    def calorExtremo(self):
        self.temp += 0.8 

    def resfriamentoGradual(self):
        self.temp -= 0.2