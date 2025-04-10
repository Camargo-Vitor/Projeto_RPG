from ficha import Ficha
from classe import Classe
from especie import Especie

Mago = Classe('Mago', 6)
x = Especie('humano', 5, 180, ['furtividade'])
p1 = Ficha('Vi', 'Normal', 'Nasceu  e ta vivendo', Mago, x, ['acrobacia'])
Mago.add_hab('Bola de fogo', 1)
print(p1._Ficha__atributos)
print(p1._Ficha__vida)
print(p1._Ficha__vida)
print(p1._Ficha__atributos)
print(p1._Ficha__classe._Classe__habilidades)
print(p1._Ficha__dic_pericias)
print(p1)