from astolfo import AgenteTemperatura
from ambiente import Ambiente
import time

astolfo = AgenteTemperatura()
escritorio = Ambiente()

print("Iniciando Astolfo - Controlador de Temperatura")

for i in range(20): 
    #testes
    escritorio.oscilacao()
    #escritorio.calorExtremo()
    #escritorio.resfriamentoGradual()

    astolfo.perceber(escritorio.temp)
    
    decisao = astolfo.decidir()

    print(f"Ciclo {i+1} | Temp antes da ação: {escritorio.temp:.1f}°C | Decisão: {decisao}")
    
    astolfo.agir(decisao, escritorio)

    time.sleep(1)