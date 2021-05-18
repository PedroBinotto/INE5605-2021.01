'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: 18/05/2021
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
    
    @property
    def cordas_de_aço(self):
        return self.__cordas_de_aço

    def afinar_corda(self, x):
        if not x > self.quantidade_de_cordas:           # Checa se a corda especificada excede a quantidade de cordas.
            print("Afinando corda " + str(x))
        else: 
            print("Este instumento só possui {} cordas!"\
                .format(self.quantidade_de_cordas))
     
    def tocar(self, notas: Iterable[int]):
        if not len(notas) > 7:                          # Comprimento máximo de sete elementos
            print(notas)
        else:
            print('Esse instrumento só pode tocar sete notas de uma vez!')


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

    def afinar(self, x):
        if not x > self.__quantidade_de_notas:          # Checa se a nota especificada excede a quantidade de notas.
            print("Afinando nota " + str(x))
        else:
            print("Este instumento só possui {} notas!"\
                .format(self.quantidade_de_notas))
    
    def tocar(self, notas: Iterable[int]):
        if not len(notas) > 1:                          # Comprimento máximo de um elemento
            print(notas)
        else:
            print('Este instrumento só pode tocar uma nota por vez!')

