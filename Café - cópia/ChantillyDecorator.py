from DecoratorBase import DecoradorBase


class ChantillyDecorator(DecoradorBase):
    def get_preco(self):
        return super().get_preco() + 2.50
    
    def get_descricao(self):
        return super().get_descricao() + " Chantilly"
