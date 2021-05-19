'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''

from testes import a, b, c, d, e, f


def permut(m):
    for i in range(len(m[0])):
        tmp = []
        cnt = 0
        for j in m:
            tmp.append(j[i])
        for i in tmp:
            if i not in [0, 1]:
                return False
            elif i == 1:
                cnt += 1
        if cnt != 1:
            return False
    for i in m:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
        if cnt != 1:
            return False
    return True

def escreve_matriz(m):
    height = len(m)
    width = len(m[0])
    for i in range(height):
        for j in range(width):
            print(m[i][j], end=" ")
        print()

def main():
    testes = [a, b, c, d, e, f]                                                 # Matrizes definidas em 'exemplos.py'
    for matriz in testes:
        print('Matriz: \n')
        escreve_matriz(matriz)
        print('\n', permut(matriz), '\n')

main()
