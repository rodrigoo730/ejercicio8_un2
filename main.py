from claseConjunto import Conjunto
from claseMenu import Menu

def test():
    print('test')
    lista1 = [3, 5, 6]
    conj1 = Conjunto()
    conj1.cargarConjunto(lista1)
    conj1.mostrar()
    lista2 = [6, 3, 5]
    conj2 = Conjunto()
    conj2.cargarConjunto(lista2)
    conj2.mostrar()
    input()
if __name__ == '__main__':
    p = input('Desea ejecutar test:  1:si  2:no  :')
    if p == '1':
        test()

    lista1 = [3,5,6,1]
    conj1 = Conjunto()
    conj1.cargarConjunto(lista1)
    lista2 = [6,3,5,9]
    conj2 = Conjunto()
    conj2.cargarConjunto(lista2)
    menu = Menu()
    bandera = False
    while not bandera:
        print(
            "\n------------Menu------------\n1. Union de conjuntos \n2. Diferencia de conjuntos \n3. Igualdad de conjuntos \n4. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, conj1, conj2)
        if op == 4:
            bandera = True
# See

