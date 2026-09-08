from DecoratorBase import DecoradorBase


class ChocolateDecorator(DecoradorBase):
    def get_descricao(self):
        return super().get_descricao() + " Chocolate"
    
    def get_preco(self):
        return super().get_preco() + 3.0
