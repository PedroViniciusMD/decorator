from Componente import Componente


class DecoradorBase(Componente):
    def __init__(self, componente: Componente):
        self.componente = componente
        
    def get_preco(self):
        return self.componente.get_preco() 
    
    def get_descricao(self):
        return self.componente.get_descricao()
    