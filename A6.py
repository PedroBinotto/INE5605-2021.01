'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: TODO 
    Python Version: 3.7.3
'''

from abc import ABC, abstractmethod
from typing import Iterable


class InstrumentoMusical(ABC):
    def __init__(self, fabricante: str, material: str, acorde: bool):
        self.__fabricante = fabricante
        self.__material = material
        self.__acorde = acorde
    
    @property
    def fabricante(self):
        return self.__fabricante

    @property
    def material(self):
        return self.__material

    @property
    def acorde(self):
        return self.__acorde
    
    @fabricante.setter
    def fabricante(self, novo_fabricante: str):
        self.__fabricante = novo_fabricante

    @material.setter
    def material(self, novo_material: str):
        self.__material = novo_material

    @acorde.setter
    def acorde(self, novo_acorde: bool):
        self.__acorde = novo_acorde

    @abstractmethod
    def tocar(self, notas: Iterable[int]):
        pass


class Violao(InstrumentoMusical):
    def __init__(self,
        fabricante: str,
        material: str,
        acorde: bool,
        quantidade_de_cordas: int,
        cordas_de_aço: bool):

        super().__init__(fabricante, material, acorde)
        self.__quantidade_de_cordas = quantidade_de_cordas
        self.__cordas_de_aço = cordas_de_aço
    
    @property
    def quantidade_de_cordas(self):
        return self.__quantidade_de_cordas
    
    @quantidade_de_cordas.setter
    def quantodade_de_cordas(self, nova_quantidade: str):
        self.quantidade_de_cordas = nova_quantidade

    @property
    def cordas_de_aço(self):
        return self.__cordas_de_aço
    
    @cordas_de_aço.setter
    def quantodade_de_cordas(self, novas_cordas: str):
        self.cordas_de_aço = novas_cordas

    def afinar_corda(self, x):
        if not x > self.quantidade_de_cordas:
            print("Afinando corda " + str(x))
        else:
            print("Este instumento só possui {} cordas!"\
                .format(self.quantidade_de_cordas))
     
    def tocar(self, notas: Iterable[int]):
        pass


class Flauta(InstrumentoMusical):
    def __init__(self,
        fabricante: str,
        material: str,
        acorde: bool,
        quantidade_de_notas: int):

        super().__init__(fabricante, material, acorde)
        self.__quantidade_de_notas = quantidade_de_notas

    @property
    def quantidade_de_notas(self):
        return self.__quantidade_de_notas
    
    @quantidade_de_notas.setter
    def quantodade_de_notas(self, nova_quantidade: str):
        self.quantidade_de_notas = nova_quantidade

    def afinar(self, x):
        if not x > self.__quantidade_de_notas:
            print("Afinando nota " + str(x))
        else:
            print("Este instumento só possui {} notas!"\
                .format(self.quantidade_de_notas))
    
    def tocar(self, notas: Iterable[int]):
        pass


def main():
    violao1 = Violao('Martin', 'Mogno', True, 6, True)
    violao2 = Violao('Yamaha', 'Mogno', True, 6, False)
    
    flauta1 = Flauta('Muramatsu', 'Prata', False, 36)
    flauta2 = Flauta('Artley', 'Madeira', False, 36)

    flauta1.tocar([20])
    violao1.tocar([1, 2, 3, 8, 6])

main()

# if len(notas) > 7:
#     print('Não é possível tocar mais de sete notas por vez!')
# else:
# for nota in notas:
#     if not nota in range (1, self.quantidade_de_cordas + 1):
#         print('Não é possível tocar essa nota ({}) neste \
# instrumento!'.format(nota))
#         notas.remove(nota)
# super().tocar(notas)

