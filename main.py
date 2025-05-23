'''
from model.ficha import Ficha
from model.classe import Classe
from model.subclasse import Subclasse
from model.habilidade import Habilidade
from model.magia import Magia
from model.item import Item
from model.subespecie import Subespecie
from model.jogador import Jogador

if __name__ == '__main__':
    lista_todas_habilidades = []
    lista_todos_itens = []
    lista_todas_magias = []

    # Habilidades de teste
    habilidade_teste_especie = Habilidade('Correr', 1, 78, 'especie')
    habilidade_teste_subespecie = Habilidade('visão noturna', 1, 145, 'subespecie')
    habilidade_teste_classe = Habilidade('passos furtivos', 1, 176, 'classe')
    habilidade_teste_subclasse = Habilidade('camuflagem', 1, 201, 'subclasse')

    habilidade_teste_classe_nivel_2 = Habilidade('Ação ardilosa', 2, 177, 'classe')

    lista_todas_habilidades.append(habilidade_teste_especie)
    lista_todas_habilidades.append(habilidade_teste_subespecie)
    lista_todas_habilidades.append(habilidade_teste_classe)
    lista_todas_habilidades.append(habilidade_teste_subclasse)

    # Itens de teste

    item_teste = Item('Espada', 10, 'COMUM', 345)
    lista_todos_itens.append(item_teste)

    # Magias de teste

    magia_teste = Magia('Bola de fogo', 1, 91)
    lista_todas_magias.append(magia_teste)

    # classes teste

    classe_teste = Classe('Ranger', 6)
    tiro_preciso = Habilidade('Tiro preciso', 1, 56, 'classe')
    classe_teste.add_hab(tiro_preciso)
    classe_teste.add_hab(habilidade_teste_classe_nivel_2)

    # subclasse teste

    subclasse_teste = Subclasse('Guerreiro', 'Mestre de batalha', 8)
    # teste especie

    sub_especie_teste = Subespecie('Elfo', 'das montanhas', 10, 133)

    ficha_teste = Ficha('Roger', 'Comum', 'Caça e tem um passarinho chamado Xavier', classe_teste, sub_especie_teste, ['furtividade'])
    ficha_teste2 = Ficha('Jurandir', 'Robusto', 'pinga!', subclasse_teste, sub_especie_teste, ['intimidacao'])

    # teste pessoa
    eu = Jogador('Victor', 923450145, 'Rua Cristóvão Colombo', ['Terça'])
    eu.add_ficha(ficha_teste)
    print(eu)

    #### Playground ####

    ficha_teste.add_magia(magia_teste)
    ficha_teste.add_item_inventario(item_teste)
    print(ficha_teste)
    classe_teste.rm_hab(tiro_preciso)
    ficha_teste.rm_magia(magia_teste)
    ficha_teste.rm_item_inventario(item_teste)
    print(ficha_teste)
    ficha_teste.subir_nivel()
    '''
from controller.controlador_sistema import ControladorSistema

if __name__ == '__main__':
    ControladorSistema().abre_tela()
