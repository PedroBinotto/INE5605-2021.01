'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
    Python Version: 3.7.3
'''

m = [
    [ 0, -1,  0,  0],
    [ 0, -1,  0,  0],
    [ 0,  0,  0,  0],
    [-1,  0,  0,  0],
    [ 0,  0,  0,  0]
]

def marcar(m):
    res = []
    cnt = 0
    height = len(m)
    width = len(m[0])

    for i in range(height):
        tmp = []
        for j in range(width):
            if m[i][j] == 0:                                    # Checa se dígito atual representa bloco preto
                vert = False                                    # FLAG
                if i + 1 < height - 1:                          # Checa se próximo dígito existe na matriz  (verticalmente)
                    if m[i + 1][j] == 0:                        # Checa se próximo dígito é zero            (verticalmente)
                        if i - 1 > -1:                          # Checa se dígito anterior existe na matriz (verticalmente)
                            if m[i - 1][j] != 0:                # Checa se dígito anterior é zero           (verticalmente)
                                cnt += 1
                                tmp.append(cnt)
                                vert = True
                        else:
                            cnt += 1
                            tmp.append(cnt)
                            vert = True
                if not vert:                                    # Executa apenas caso não seja início vertical
                    if j + 1 < width - 1:                       # Checa se próximo dígito existe na matriz  (horizontalmente)
                        if m[i][j + 1] == 0:                    # Checa se próximo dígito é zero            (horizontalmente)
                            if j - 1 > -1:                      # Checa se dígito anterior existe na matriz (horizontalmente)
                                if m[i][j - 1] != 0:            # Checa se dígito anterior é zero           (horizontalmente)
                                    cnt += 1
                                    tmp.append(cnt)
                                else:
                                    tmp.append(m[i][j])
                            else:
                                cnt += 1
                                tmp.append(cnt)
                        else:
                            tmp.append(m[i][j])
                    else:
                        tmp.append(m[i][j])
            else:
                tmp.append(m[i][j])
        res.append(tmp)
    return res


for i in marcar(m):
    print(i)

