from astolfo import AgenteTemperatura
from ambiente import ambiente
import random

astolfo = AgenteTemperatura()
escritorio = ambiente()
def estado(self):
    opcao = random.randint(1,3)
    match opcao:
        case 1:
            self.escritorio.oscilacao
        case 2:
            #escolhe calor extremo
            pass
        case 3:
            #escolhe resfriamento gradual
            pass