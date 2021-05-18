'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''

from exemplos import a, b, c, d, e, f


def permut(m):
    for i in range(len(m[0])):
        tmp = []
        for j in m:
            tmp.append(j[i])
        if 1 not in tmp:
            return False
    for i in m:
        if 1 not in i:
            return False
    return True

def main():
    testes = [a, b, c, d, e, f]
    for matriz in testes:
        print(permut(matriz))

main()
