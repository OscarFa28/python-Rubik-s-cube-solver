class Texts:
    def w():
        print('Incorrecto, reintentar')
    def i():
        print('Seleccione acción: ')
        print('------------------')
        print('1. ---|---- N movimientos aleatorios')
        print('2. ---|---- Movimientos específicos')
        print('------------------')
    def i1():
        print('Digite la cantidad de movimientos: ')
    def i2():
        print('Digite el movimiento ó -1 para continuar con ese cubo: ')
    def movs():
        movimientos = [
            "1.  ------Derecha (1)----",
            "2.  ------Derecha (2)----",
            "3.  ------Izquierda (1)--",
            "4.  ------Izquierda (2)--",
            "5.  ------Arriba (1)-----",
            "6.  ------Arriba (2)-----",
            "7.  ------Abajo (1)------",
            "8.  ------Abajo (2)------",
            "9.  ------Frente (1)-----",
            "10. ------Frente (2)-----",
            "11. ------Atrás (1)------",
            "12. ------Atrás (2)------"
        ]
        for movimiento in movimientos:
            print('Movimientos disponibles: ')
            print(movimiento)
    def s():
        print('Elige el metodo a usar: ')
        metodos = [
            "1.  ------BFS------------------",
            "2.  ------Best First Search----",
            "3.  ------A Star---------------",
            "4.  ------IDA Star-------------",
        ]
        for metodo in metodos:
            print (metodo)
    def h():
        print('Elige Heuristica a usar: ')
        heuristicas = [
            "1.  ------Manhattan-----------------------------------",
            "2.  ------Caras correctas-----------------------------",
            "3.  ------Bloques misma cara y adjuntos---------------",
            "4.  ------Promedio de Heuristicas---------------------",
        ]
        for heuristica in heuristicas:
            print (heuristica)