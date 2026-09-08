from DecoratorBase import DecoradorBase


class LeiteDecorator(DecoradorBase):
    def get_preco(self) -> float:
        return super().get_preco() + 2.0
    
    def get_descricao(self) -> str:
        return super().get_descricao() + " leite"
