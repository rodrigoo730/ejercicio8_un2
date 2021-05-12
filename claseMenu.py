
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.salir}

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,r1,r2):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        bandera = False
        while not bandera:
            if op == 1 or op == 2 or op == 3 or op == 4:
                bandera = True
            else:
                print('Opción no válida')
                op = int(input('Ingrese una opcion: '))

        func(r1,r2)

    def salir(self,r1,r2):
        print('Salir')

    def opcion1(self,r1,r2):
        suma = r1 + r2
        print('r1 + r2 :')
        print(''.format(suma.mostrar()))
        return

    def opcion2(self,r1,r2):
        resta = r1 - r2
        print('r1 - r2:')
        print(''.format(resta.mostrar()))
        return

    def opcion3(self,r1,r2):
        igualdad = r1 == r2
        print('r1 == r2 :{} '.format(igualdad))

        return