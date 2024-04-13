import numpy as np
from Movements import make_movement
movimientos = []
array = np.array([
    [[0, 0, 2], [1, 0, 2], [2, 0, 2]],
    [[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 0, 2], [0, 1, 2], [0, 2, 2]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 1]],
    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 1, 0], [2, 1, 0]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[2, 0, 0], [2, 0, 1], [2, 0, 2]],
    [[2, 1, 0], [2, 1, 1], [2, 1, 2]],
    [[2, 2, 0], [2, 2, 1], [2, 2, 2]],
    [[2, 0, 2], [1, 0, 2], [0, 0, 2]],
    [[2, 1, 2], [1, 1, 2], [0, 1, 2]],
    [[2, 2, 2], [1, 2, 2], [0, 2, 2]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[0, 2, 1], [1, 2, 1], [2, 2, 1]],
    [[0, 2, 2], [1, 2, 2], [2, 2, 2]],
])

class Estado:
    cubo = None
    g = 0 #Costo acumulado del camino desde el estado inicial hasta el estado actual
    h = 0 #Heurística que estima el costo restante desde el estado actual hasta el estado objetivo
    padre = None
    movimiento = None

def print_all_movements(actual):
    for mov in movimientos:
        print(mov)
    
# Función que verifica si se ha alcanzado el objetivo y escribe el estado final en output.txt
def objetivo_alcanzado(actual):
    if actual.h != 0:
        return False

    cubo = actual.cubo
    print_all_movements(actual)
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

# Algoritmo IDA*
def ida(start):
    start.h = suma_max_esquinas_borde(start.cubo)
    limite_costo = start.h
    nodos = 0
    frontera = list()
    factores_de_rama = list()
    ar=1
    while True:
        print("arbol: "+str(ar))
        minimo = None
        frontera.append(start)
        f = 1
        while len(frontera) != 0:
            
            print("frontera: "+str(f))
            actual = frontera.pop()

            if objetivo_alcanzado(actual):
                print('Altura de la meta:', actual.g)
                print('Factor de ramificación:', sum(factores_de_rama)/len(factores_de_rama))
                print("Nodos generados:", nodos)
                return

            b = 0
            nodos += 12
            for i in range(12):
                nuevo = Estado()
                nuevo.cubo = np.array(actual.cubo)
                nuevo.g = actual.g + 1
                nuevo.padre = actual
                nuevo.movimiento = make_movement(nuevo.cubo, i + 1, 0)
                #movimientos.append(make_movement(nuevo.cubo, i + 1, 0))
                
                nuevo.h = suma_max_esquinas_borde(nuevo.cubo)
                print("heu: "+str(i)+"="+str(nuevo.h))

                if nuevo.g + nuevo.h > limite_costo:
                    if minimo is None or nuevo.g + nuevo.h < minimo:
                        minimo = nuevo.g + nuevo.h
                    continue
                if actual.padre is not None and (contiene_ancestro(nuevo.cubo, actual) or contiene_frontera(nuevo.cubo, frontera)):
                    continue
                frontera.append(nuevo)
                b += 1
            if b != 0:
                factores_de_rama.append(b)
            f +=1

        limite_costo = minimo
        ar += 1
        
# Función para calcular la distancia de Manhattan
def distancia_manhattan(cubo, i, z, esquina):
    c1 = array[i, z]
    centro = None
    for c in [1, 4, 7, 10, 13, 16]:
        if cubo[i, z] == cubo[c, 1]:
            centro = c
            break

    if esquina:
        c2 = array[centro - 1, 0]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro - 1, 2]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro + 1, 0]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro + 1, 2]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)
    else:
        c2 = array[centro - 1, 1]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro, 0]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro, 2]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = array[centro + 1, 1]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)

# Función para calcular la suma máxima de esquinas y bordes
def suma_max_esquinas_borde(cubo):
    esquinas = 0
    bordes = 0
    for i in range(18):
        if i % 3 == 0 or i % 3 == 2:
            esquinas = esquinas + distancia_manhattan(cubo, i, 0, True) + distancia_manhattan(cubo, i, 2, True)
            bordes = bordes + distancia_manhattan(cubo, i, 1, False)
        else:
            bordes = bordes + distancia_manhattan(cubo, i, 0, False) + distancia_manhattan(cubo, i, 2, False)
    return max(esquinas / 12, bordes / 8)

