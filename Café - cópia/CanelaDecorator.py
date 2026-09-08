from DecoratorBase import DecoradorBase


class CanelaDecorator(DecoradorBase):
    def get_descricao(self):
        return super().get_descricao() + " Canela"
    
    def get_preco(self):
        return super().get_preco() + 1.0
    