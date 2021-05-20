'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''

from testes import a, b, c


def vertical(m, i, j, height):
    if i + 1 <= height - 1:                                                     # Checa se próximo dígito existe na matriz  (verticalmente)
        if m[i + 1][j] == 0:                                                    # Checa se próximo dígito é zero            (verticalmente)
            if i - 1 > -1:                                                      # Checa se dígito anterior existe na matriz (verticalmente)
                if m[i - 1][j] != 0:                                            # Checa se dígito anterior é zero           (verticalmente)
                    return True
                return False
            return True
        return False
    return False


def horizontal(m, i, j, width):
    if j + 1 <= width - 1:                                                      # Checa se próximo dígito existe na matriz  (horizontalmente)
        if m[i][j + 1] == 0:                                                    # Checa se próximo dígito é zero            (horizontalmente)
            if j - 1 > -1:                                                      # Checa se dígito anterior existe na matriz (horizontalmente)
                if m[i][j - 1] != 0:                                            # Checa se dígito anterior é zero           (horizontalmente)
                    return True
                return False
            return True
        return False
    return False


def marcar(m):
    res = []
    cnt = 0
    height = len(m)
    width = len(m[0])

    for i in range(height):
        tmp = []
        for j in range(width):
            if m[i][j] == 0:                                                    # Checa se dígito atual representa bloco preto
                if vertical(m, i, j, height):                                   # Executa apenas caso não seja início vertical
                    cnt += 1
                    tmp.append(cnt)
                elif horizontal(m, i, j, width):
                    cnt += 1
                    tmp.append(cnt)
                else:
                    tmp.append(m[i][j])
            else:
                tmp.append(m[i][j])
        res.append(tmp)
    return res


def escreve_matriz(m):
    col = 4
    height = len(m)
    for i in range(height):
        print("".join(str(j).rjust(col) for j in m[i]), end=' ')                # Tratar cada elemento como str para justificar com 'rjust';
        print()                                                                 # dessa forma, a matriz exibida continua alinhada,
                                                                                # mesmo com elementos de comprimentos diferentes.


def main():
    matrizes = [a, b, c]
    for i in range(len(matrizes)):
        print('Matriz {}:\n'.format(i))
        escreve_matriz(matrizes[i])

        print('\nResultado após marcação: \n')
        escreve_matriz(marcar(matrizes[i]))
        print('\n')

main()
