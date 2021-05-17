'''
    Solução para a avaliação A6 da disciplina INE5603 do semestre 2020.2.

    Author: Pedro Santi Binotto (20200634)
    Date created: 17/05/2021
    Date last modified: TODO 
    Python Version: 3.7.3
'''

class InstrumentoMusical:
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

    def tocar(self, notas):
        for nota in notas:
            print(nota)


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
    
    def afinar_corda(self, x):
        if not x > self.__quantidade_de_cordas:
            print("Afinando corda " + str(x))
        else:
            print("Este instumento só possui {} cordas!"\
                .format(self.__quantidade_de_cordas))
     
    def tocar(self):
        notas = list(range(1, self.__quantidade_de_cordas + 1))
        super().tocar(notas)


class Flauta(InstrumentoMusical):
    def __init__(self,
        fabricante: str,
        material: str,
        acorde: bool,
        quantidade_de_notas: int):

        super().__init__(fabricante, material, acorde)
        self.__quantidade_de_notas = quantidade_de_notas
    
    def afinar(self, x):
        if not x > self.__quantidade_de_notas:
            print("Afinando nota " + str(x))
        else:
            print("Este instumento só possui {} notas!"\
                .format(self.__quantidade_de_notas))
    
    def tocar(self):
        notas = list(range(1, self.__quantidade_de_notas + 1))
        super().tocar(notas)
