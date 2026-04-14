from ambiente import Ambiente

ambiente_obj = Ambiente()

class AgenteTemperatura:
    def __init__(self):
        self.percepcao_atual = 24.0

    def perceber(self, leitura):
        self.percepcao_atual = float(leitura) 

    def decidir(self):
        if self.percepcao_atual > 24.5:
            return "LIGAR_AC"
        elif self.percepcao_atual < 23.5:
            return "LIGAR_AQUECEDOR"
        else:
            return "MANTER"

    def agir(self, acao, ambiente_obj):
        if acao == "LIGAR_AC":
            ambiente_obj.temp -= 1.0
        elif acao == "LIGAR_AQUECEDOR":
            ambiente_obj.temp += 1.0