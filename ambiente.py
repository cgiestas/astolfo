import random
import time

class ambiente:
    def __innit__(self):
        self.temp = 24.0

    def oscilacao (self, temp):
        aleatorio = round(random.uniform(1,0, -1.0), 1)
        osc = 0
        while osc < 5:
            temp = temp + aleatorio
            osc+=1
    
    def calorExtremo (self, temp):
        count = 0
        while count < 5:
            count+=1
            temp = temp + 0.5
            time.sleep(5)

    def resfriamentoGradual (self, temp):
        count = 0
        while count < 5:
            count+=1
            temp = temp - 0.1
            time.sleep(2)
    
#provavelmente essa ideia de incrementar com o tempo não vai funcionar, pq vai incrementar tudo de uma vez só
#melhorar
#mas a de oscilação acho que tá ok