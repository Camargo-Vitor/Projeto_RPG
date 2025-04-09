from ficha import Ficha
from classe import Classe
from especie import Especie

Mago = Classe('Mago', 6)
x = Especie()
p1 = Ficha('Vi', 'Normal', 'Nasceu e ta vivendo', Mago, x)
Mago.add_hab('Bola de fogo', 1)
print(p1._Ficha__atributos)
print(p1._Ficha__vida)
print(p1._Ficha__vida)
print(p1._Ficha__atributos)
print(p1._Ficha__classe._Classe__habilidades)

di = {'a': 1, 'b': 2, 'c': 3}
for hab, niv in enumerate(di.items()):
