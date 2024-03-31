import numpy as np
from datetime import datetime
import time
from IDA import Estado, ida
from IDFS import Estado_idfs, idfs

# Estado inicial del cubo
estado_inicial = np.array([
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
])

actual = Estado()
actual.cubo = estado_inicial
manejar = open('C:\\Users\\of_de\\OneDrive\\Documentos\\UP\\Estructura_de_d_y_a_III\\Proyecto_intermedio\\prueba\\input.txt')

indices = [0, 1, 2, 3, 6, 9, 12, 4, 7, 10, 13, 5, 8, 11, 14, 15, 16, 17]
indice = 0
for linea in manejar:
    linea = linea.replace(' ', '')
    for fila in linea.split('['):
        if len(fila) != 0:
            i = indices[indice]
            actual.cubo[i, 0] = fila[1]
            actual.cubo[i, 1] = fila[4]
            actual.cubo[i, 2] = fila[7]
            indice += 1 

time.ctime()
fmt = '%H:%M:%S'
inicio = time.strftime(fmt)

print("Usando IDA: ")
ida(actual)

time.ctime()
fin = time.strftime(fmt)
print("Tiempo transcurrido (segundos):", datetime.strptime(fin, fmt) - datetime.strptime(inicio, fmt))




actual = Estado_idfs()
actual.cubo = estado_inicial

indices = [0, 1, 2, 3, 6, 9, 12, 4, 7, 10, 13, 5, 8, 11, 14, 15, 16, 17]
indice = 0
for linea in manejar:
    linea = linea.replace(' ', '')
    for fila in linea.split('['):
        if len(fila) != 0:
            i = indices[indice]
            actual.cubo[i, 0] = fila[1]
            actual.cubo[i, 1] = fila[4]
            actual.cubo[i, 2] = fila[7]
            indice += 1 
            
time.ctime()
fmt = '%H:%M:%S'
inicio = time.strftime(fmt)

#print("Usando IDFS: ")
#idfs(actual)

time.ctime()
fin = time.strftime(fmt)
print("Tiempo transcurrido (segundos):", datetime.strptime(fin, fmt) - datetime.strptime(inicio, fmt))
