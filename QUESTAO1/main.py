'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''
from time import sleep

from classes import Flauta, Violao


def main():
    print('Instanciando violões...\n')

    violao1 = Violao('Martin', 'Mogno', True, 6, True)
    violao2 = Violao('Yamaha', 'Mogno', True, 7, False)

    sleep(1)

    print('Violão 1:\n')
    print("Fabricante: {}".format(violao1.fabricante))
    print("Material: {}".format(violao1.material))
    print("Acorde: {}".format(violao1.acorde))
    print("Quantidade de Cordas: {}".format(violao1.quantidade_de_cordas))
    print("Cordas de Aço: {}\n".format(violao1.cordas_de_aço))

    violao1.afinar_corda(1)
    violao1.tocar([1, 3, 5, 8])

    print('\nViolão 2:\n')
    print("Fabricante: {}".format(violao2.fabricante))
    print("Material: {}".format(violao2.material))
    print("Acorde: {}".format(violao1.acorde))
    print("Quantidade de Cordas: {}".format(violao2.quantidade_de_cordas))
    print("Cordas de Aço: {}\n".format(violao2.cordas_de_aço))
 
    violao2.afinar_corda(2)
    violao2.tocar([5, 3, 5, 1])
    
    print('\nInstanciando flautas...\n')

    sleep(1)

    flauta1 = Flauta('Muramatsu', 'Prata', False, 24)
    flauta2 = Flauta('Artley', 'Madeira', False, 36)

    print('Flauta 1:\n')
    print("Fabricante: {}".format(flauta1.fabricante))
    print("Material: {}".format(flauta1.material))
    print("Acorde: {}".format(flauta1.acorde))
    print("Quantidade de Notas: {}\n".format(flauta1.quantidade_de_notas))

    flauta1.afinar(1)
    flauta1.tocar([1])

    print('\nFlauta 2:\n')
    print("Fabricante: {}".format(flauta2.fabricante))
    print("Material: {}".format(flauta2.material))
    print("Acorde: {}".format(flauta2.acorde))
    print("Quantidade de Notas: {}\n".format(flauta2.quantidade_de_notas))

    flauta2.afinar(2)
    flauta2.tocar([2])

main()
