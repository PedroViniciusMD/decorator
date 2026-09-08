from ChocolateDecorator import ChocolateDecorator
from ComponenteConcreto import ComponenteConcreto
from LeiteDecorator import LeiteDecorator

cafe = ComponenteConcreto()
cafe_leite = LeiteDecorator(cafe)
cafe_leite_chocolate = ChocolateDecorator(cafe_leite)

print(cafe_leite_chocolate.get_preco())
print(cafe_leite_chocolate.get_descricao())
