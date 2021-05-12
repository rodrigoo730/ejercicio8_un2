
'''La union de dos conjuntos, es un nuevo conjunto con los elementos de ambos conjuntos, si un
elemento está repetido, va una sola vez en el resultado: Ejemplo: Si A=[1,2,3], B=[2,4,6,8] entonces
A+B será [1,2,4,6,8]. La resta de dos conjuntos, es un nuevo conjunto con los elementos del primer
conjunto que no esté en el segundo conjunto. Ejemplo: Si A=[1,2,3], B=[2,4,6,8] entonces A-B será [1,3]
'''

class Conjunto:
    __lista = []

    def __init__(self):
        self.__lista = []

    def mostrar(self):
        print('lista {}'.format(self.__lista))


    def cargarConjunto(self,cadena):
        for i in range(len(cadena)):
            self.__lista.append(int(cadena[i]))

    def getElem(self):
        cadena =[]
        for i in range(len(self.__lista)):
            cadena.append(self.__lista[i])
        return cadena

    @classmethod
    def buscarElem(cls,lista,ele):
        bandero = False
        for i in range(len(lista)):
            if ele == lista[i]:
                bandero = True
        return bandero

    def __add__(self, other):
        if type(other) == Conjunto:
            lista1 = self.getElem()
            j = 0
            p = len(lista1)
            for i in range(p):
                bandera = Conjunto.buscarElem(other.__lista,lista1[j])
                if bandera:
                    lista1.pop(j)
                    j -= 1
                bandera = False
                j += 1
            lista_n = lista1 + other.__lista
            conjunto = Conjunto()
            conjunto.cargarConjunto(lista_n)
            return conjunto

    def __sub__(self, other):
        if type(other) == Conjunto:
            lista1 = self.getElem()
            j = 0
            p = len(lista1)
            for i in range(p):
                bandera = Conjunto.buscarElem(other.__lista,lista1[j])
                if bandera:
                    lista1.pop(j)
                    j -= 1
                bandera = False
                j += 1
            lista_n = lista1
            conjunto = Conjunto()
            conjunto.cargarConjunto(lista_n)
            return conjunto

    def __eq__(self, other):
        if type(other) == Conjunto:
            i= 0
            bandera = False
            if len(self.__lista) == len(other.__lista):
                bandera = True
                while bandera and i < len(self.__lista):
                    bandera = Conjunto.buscarElem(other.__lista, self.__lista[i])
                    i += 1
            return bandera



