import numpy as np
from datetime import datetime
import time
from IDA import Estado, ida, print_cube
from IDFS import Estado_idfs, idfs
from shuffle import make_shuffle

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


#ida
time.ctime()
fmt = '%H:%M:%S'
inicio = time.strftime(fmt)

print("Usando IDA: ")
actual_shuffled = make_shuffle(actual, 4)
print_cube(actual_shuffled.cubo)
ida(actual_shuffled)

time.ctime()
fin = time.strftime(fmt)
print("Tiempo transcurrido (segundos):", datetime.strptime(fin, fmt) - datetime.strptime(inicio, fmt))



#idfs
actual = Estado_idfs()
actual.cubo = estado_inicial

            
time.ctime()
fmt = '%H:%M:%S'
inicio = time.strftime(fmt)

#print("Usando IDFS: ")
#idfs(actual)

time.ctime()
fin = time.strftime(fmt)
#print("Tiempo transcurrido (segundos):", datetime.strptime(fin, fmt) - datetime.strptime(inicio, fmt))
