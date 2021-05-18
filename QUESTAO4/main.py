'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''

from utils import concat


def main():
    n1 = int(input('Defina o comprimento da lista L1: '))
    l1 = []
    for i in range(0, n1):
        elem = input('Elemento {}: '.format(i))
        l1.append(elem)

    n2 = int(input('Defina o comprimento da lista L2: '))
    l2 = []
    for i in range(0, n2):
        elem = input('Elemento {}: '.format(i))
        l2.append(elem)

    l3 = concat(l1, l2)
    print('Lista concatenada: ', l3)

main()
