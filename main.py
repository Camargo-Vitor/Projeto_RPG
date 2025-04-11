from ficha import Ficha
from classe import Classe
from especie import Especie
from habilidade import Habilidade
from magia import Magia
from item import Item

lista_todas_habilidades = []
lista_todos_itens = []
lista_todas_magias =[]
Mago = Classe('Mago', 6)
x = Especie('humano',9.0, 180, ['visão no escuro'])
p1 = Ficha('Vi', 'Normal', 'Nasceu  e ta vivendo', Mago, x, ['acrobacia'])
Mago.add_hab('Conjurar Magia', 1)
nova_habilidade = Habilidade('Pacto', 5, 'Bruxo')
novo_item = Item('Espada, g.p.c', 1300, 'épico', 157)
nova_magia = Magia('Bola de fogo', 3, 231)
p1.add_magia(nova_magia)
p1.add_hab(nova_habilidade)
p1.add_item_inventario(novo_item)
print(p1._Ficha__atributos)
print(p1._Ficha__vida)
print(p1._Ficha__classe._Classe__habilidades)
print(p1._Ficha__dic_pericias)
print(p1)
print(nova_habilidade)