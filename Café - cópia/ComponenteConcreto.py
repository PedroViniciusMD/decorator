from Componente import Componente


class ComponenteConcreto(Componente):
    
    def get_descricao(self):
        return "Café"
    
    def get_preco(self):
        return 5.0