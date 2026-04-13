from ambiente import ambiente

class AgenteTemperatura:
    ac_ligado = False
    aq_ligado = False
    def __innit__ (self):
        #estado interno (?????????)
        pass
    def perceber(self, ambiente):
        #pega temp do ambiente
        pass
    def decidir(self, percepcao):
        #decide se aq ou ac deve ser ligado 
        pass
    def agir(self,ambiente):
        #liga ou desliga aqui (se ligar um tem que desligar o outro)
        pass