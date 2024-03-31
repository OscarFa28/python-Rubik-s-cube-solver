from Movements import make_movement
import numpy as np


class Estado_idfs:
    cubo = None
    costo = 0
    padre = None
    movimiento = None
    
def objetivo_alcanzado_idfs(cubo):
    for ref in [0, 3, 6, 9, 12, 15]:
        first = cubo[ref, 0]
        for i in range(3):
            for j in range(3):
                if first != cubo[ref + i, j]:
                    return False
    #print_cube(cubo)
    return True

def print_cube(cubo):
    print("              ", cubo[0, 0:3])
    print("              ", cubo[1, 0:3])
    print("              ", cubo[2, 0:3])
    print(cubo[3, 0:3], cubo[6, 0:3], cubo[9, 0:3], cubo[12, 0:3])
    print(cubo[4, 0:3], cubo[7, 0:3], cubo[10, 0:3], cubo[13, 0:3])
    print(cubo[5, 0:3], cubo[8, 0:3], cubo[11, 0:3], cubo[14, 0:3])
    print("              ", cubo[15, 0:3])
    print("              ", cubo[16, 0:3])
    print("              ", cubo[17, 0:3])

# Función que verifica si un estado es ancestro de otro estado
def contiene_ancestro(hijo, padre):
    actual = padre.padre
    while actual is not None:
        if np.array_equal(actual.cubo, hijo):
            return True
        actual = actual.padre

    return False

# Función que verifica si un estado está en la frontera
def contiene_frontera(hijo, frontera):
    for actual in frontera:
        if np.array_equal(actual.cubo, hijo):
            return True

    return False





def idfs(inicio):
    limite_costo = 1
    nodos = 0
    frontera = list()
    factores_de_rama = list()

    while True:
        frontera.append(inicio)

        while len(frontera) != 0:
            actual = frontera.pop()

            if objetivo_alcanzado_idfs(actual.cubo):
                print('Altura de la meta:', actual.costo)
                print('Factor de ramificación:', sum(factores_de_rama)/len(factores_de_rama))
                # while actual is not None:
                #    if actual.move is not None:
                #        print(actual.move)
                #    actual = actual.parent
                print("Nodos generados:", nodos)
                return

            if actual.costo + 1 <= limite_costo:
                costo_hijo = actual.costo + 1
                b = 0
                for i in range(12):
                    nodos = nodos + 1
                    nuevo = Estado_idfs()
                    nuevo.cubo = np.array(actual.cubo)
                    nuevo.costo = costo_hijo
                    nuevo.padre = actual
                    nuevo.movimiento = make_movement(nuevo.cubo, i + 1, 0)
                    # if actual.parent is not None and np.array_equal(actual.parent.cubo, nuevo.cubo):
                    if actual.padre is not None and (contiene_ancestro(nuevo.cubo, actual) or contiene_frontera(nuevo.cubo, frontera)):
                        continue
                    frontera.append(nuevo)
                    b = b + 1
                factores_de_rama.append(b)

        factores_de_rama.clear()
        limite_costo = limite_costo + 1