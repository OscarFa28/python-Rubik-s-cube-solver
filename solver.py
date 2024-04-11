#Jose Arturo Reza Quezada
#Oscar Fabrizio de Alba 

#Librerias, usamos el queue, priority queue, el copy para usar el deepcopy después, e importamos el RubikCube
from queue import Queue
from queue import PriorityQueue
from cube import RubikCube
import copy

#Una clase para usar y definir las heuristicas usadas
class Heuristics:
    @staticmethod
    #Distancia manhattan desde las aristas del cubo, a su lugar correspondiente
    def heu_1(node):
        val = 0
        for i in range(6):
            for j in [1, 3, 4, 6]:
                if (node.Rubik.cubo[i][j] == i+3) or (node.Rubik.cubo[i][j] == i-3):
                    val += 2
                elif node.Rubik.cubo[i][j] != i:
                    val += 1
        return val
    
    @staticmethod
    #Cuenta cuántas líneas de 3 bloques seguidos no tienen el mismo color. En el caso de las cruces de cada cara, la penalización vale por dos
    def heu_2(node):
        val = 0
        for i in range(6):
            if not(node.Rubik.cubo[i][0] == node.Rubik.cubo[i][1] and node.Rubik.cubo[i][1] == node.Rubik.cubo[i][2]):
                val += 1
            if not(node.Rubik.cubo[i][0] == node.Rubik.cubo[i][3] and node.Rubik.cubo[i][3] == node.Rubik.cubo[i][5]):
                val += 1
            if not(node.Rubik.cubo[i][2] == node.Rubik.cubo[i][4] and node.Rubik.cubo[i][4] == node.Rubik.cubo[i][7]):
                val += 1
            if not(node.Rubik.cubo[i][5] == node.Rubik.cubo[i][6] and node.Rubik.cubo[i][6] == node.Rubik.cubo[i][7]):
                val += 1
            if not(node.Rubik.cubo[i][1] == node.Rubik.cubo[i][6] and node.Rubik.cubo[i][1] == i):
                val += 2
            if not(node.Rubik.cubo[i][3] == node.Rubik.cubo[i][4] and node.Rubik.cubo[i][3] == i):
                val += 2
        return val
    
    @staticmethod
    #Cuenta cuántos bloques estan en la misma cara, son adjuntos y no tienen el mismo color, sin contar el centro
    def heu_3(node):
        val = 0
        l = [0, 1, 2, 4, 7, 6, 5, 3]
        for i in range(6):
            for j in range(7):
                if node.Rubik.cubo[i][l[j]] != node.Rubik.cubo[i][l[j+1]]:
                    val += 1
            if node.Rubik.cubo[i][l[7]] != node.Rubik.cubo[i][l[0]]:
                val += 1
        return val
    
    @staticmethod
    #heuristica creativa, puede que poco efectiva, que solo saca el promedio de las 3 heuristicas pasadas
    def heu_4(node):
        val1 = Heuristics.heu_1(node)
        val2 = Heuristics.heu_2(node)
        val3 = Heuristics.heu_3(node)
        return (val1 + val2 + val3) / 3
    
#Clase de nodo para ir guardando estados del cubo, asi como todo lo relacionado a la heuristica de ese cubo
class Nodo:
    #En el inicializador, le pasamos un elemento de la clase RubikCube
    def __init__(self, Rubik):
        self.Rubik = Rubik
        #Distancia para saber a cuantos movimientos esta la solucion, y self.movimientos para irlos guardando
        self.distancia = 0
        self.movimientos = []
        #Esto nada más es para traducir los movimientos del cubo, por las letras a las que le corresponde el movimiento
        self.movs_letras = ["R1", "R2", "L1", "L2", "U1", "U2", "D1", "D2", "F1", "F2", "B1", "B2"]
        #Valor heuristico que se calcula a cada paso, y el total para usarlo en A*
        self.heuristic_value = 0
        self.total_heuristic = 0
    
    #Funcion para calcular la heuristica del nodo en cada paso, con una heuristica pasada como parametro
    def calculate_heuristic(self, heuristic):
        self.heuristic_value = heuristic(self)
    
    #Funcion para devolver el valor heuristico, usado en IDA
    def return_heuristic_value(self, heuristic):
        return heuristic(self)

    #Definimos el operador == para comparar dos nodos y saber si son iguales
    def __eq__(self, other):
        #Primero preguntamos si es que ambos elementos son de tipo Nodo
        if not isinstance(other, Nodo):
            return False
        #Y si el valor binario de las caras del cubo son iguales, entonces también lo es el cubo
        return self.Rubik.caras == other.Rubik.caras
    
    #Aqui definimos el operador < para que la priority queue sepa cómo funcionar y guardar Nodos
    def __lt__(self, other):
        if not isinstance(other, Nodo):
            return False
        #Si el valor heuristico total del primer nodo es menor que el total del segundo, el primero es menor
        return self.heuristic_value+self.total_heuristic < other.heuristic_value+other.total_heuristic

    #Con esta funcion imprimimos los movimientos guardados en cada nodo, pero con la traduccion a letras que guardamos arriba
    def imp_mov(self):
        for i in self.movimientos:
            print(self.movs_letras[i], end=" ")
        print()


#Clase para solucionar el cubo Rubik
class RubikSolver:
    #Inicializamos guardando en Rubik un elemento de la clase RubikCube, y guardamos cómo se vería el estado resuelto por caras del cubo
    def __init__(self):
        self.Rubik = RubikCube()
        self.solved = (0, 2396745, 4793490, 7190235, 9586980, 11983725)

    #Función para revolver el cubo, azar es un booleano que nos dice si es al azar o no, y movs es la cantidad de movs al azar, o bien la lista de movimientos a hacer
    def revolver(self, azar, movs):
        #Si se hace al azar, llamamos shuffle_azar, que aplica la cantidad llamada de movimientos aleatorios
        if azar is True:
            self.Rubik.shuffle_azar(movs)
        #Si no se hace al azar, se manda a llamar shuffle del cubo, con la lista a movimientos que tiene que hacer
        else:
            self.Rubik.shuffle(movs)
        #Aqui nada más imprimimos cómo se ve el cubo revuelto para darnos una idea qué tan difícil está
        self.Rubik.print_faces()
    
    #Función externa, no se usa en sí pero es para testear el hacer un sólo movimiento sobre el cubo y ver cómo resulta
    def make_move(self, move):
        self.Rubik.movs(move)
        self.Rubik.print_faces()

    #Función para resolver el cubo mediante Breath-First-Search
    def bfs(self):
        #Si inicialmente la cara del cubo es igual a la resuelta, el cubo está resuelto y no hace falta buscar nada
        if(tuple(self.Rubik.caras) == self.solved):
            print("Already solved.")
            return
        #Creamos el nodo inicial, llamando a Nodo con parámetro el cubo revuelto que queremos que resuelva
        source = Nodo(self.Rubik)
        #Creamos una cola con la librería Queue()
        cola = Queue()
        #Metemos el nodo inicial a la cola
        cola.put(source)
        #Creamos un set para visitados, a los que meteremos tuplas de 6 enteros para comparar más rápidamente
        visited = set()
        #Inicialmente añadimos las caras ya calculadas del cubo revuelto
        visited.add(tuple(self.Rubik.caras))
        #Pero también metemos como visitado la forma resuelta de las caras, como si ya lo hubieramos resuelto
        visited.add(self.solved)
        #Mientras la cola tenga elementos, va a iterar en cada Nodo
        while cola.empty() is not True:
            aux = cola.get()
            #Con un rango de 12 movimientos como los definimos, aplicamos cada uno y vamos expandiendo la búsqueda
            for i in range(12):
                #Aquí usamos copy.deepcopy porque como python funciona con punteros, el cambio nunca se aplicaba realmente
                aux_c = copy.deepcopy(aux)
                #Luego aplicamos uno de los 12 movimientos
                aux_c.Rubik.movs(i)
                #Sumamos la distancia del nodo, para figurar que se hizo un movimiento más
                aux_c.distancia += 1
                #Y también añadimos qué movimiento fue el que se hizo para resolverlo
                aux_c.movimientos.append(i)
                #Guardamos en una variable nueva, el cálculo de caras del cubo
                lista = tuple(aux_c.Rubik.caras)
                #Si no está visitado ese estado del cubo, lo metemos
                if lista not in visited:
                    #Metemos el nuevo estado a la cola
                    cola.put(aux_c)
                    #Y marcamos como visitado ese estado
                    visited.add(lista)
                #Pero si el elemento que buscamos ya está visitado, solamente preguntamos si es el caso resuelto del cubo
                elif lista == self.solved:
                    #Si ya es el caso resuelto, imprimimos que se encontró, imprimimos cuántos y cuáles movimientos le tomó y lo imprimimos
                    print("---SOLVED---")
                    print("Movimientos para resolver: ", aux_c.distancia)
                    aux_c.imp_mov()
                    return

    def best_first_search(self, heuristic):
        if(tuple(self.Rubik.caras) == self.solved):
            print("Already solved.")
            return
        
        pq = PriorityQueue()
        source = Nodo(self.Rubik)
        pq.put(source)

        visited = set()
        visited.add(tuple(self.Rubik.caras))
        visited.add(self.solved)

        while not pq.empty():
            current = pq.get()
            for i in range(12):
                curr2 = copy.deepcopy(current)
                curr2.Rubik.movs(i)
                lista = tuple(curr2.Rubik.caras)
                if lista not in visited:
                    curr2.distancia += 1
                    curr2.movimientos.append(i)
                    curr2.calculate_heuristic(heuristic)
                    visited.add(lista)
                    pq.put(curr2)
                elif lista == self.solved:
                    curr2.distancia += 1
                    curr2.movimientos.append(i)
                    print("---SOLVED---")
                    print("Movimientos para resolver: ", curr2.distancia)
                    curr2.imp_mov()
                    return

    def a_star(self, heuristic):
        if(tuple(self.Rubik.caras) == self.solved):
            print("Already solved.")
            return
        
        pq = PriorityQueue()
        source = Nodo(self.Rubik)
        pq.put(source)

        visited = set()
        visited.add(tuple(self.Rubik.caras))
        visited.add(self.solved)

        while not pq.empty():
            current = pq.get()
            for i in range(12):
                curr2 = copy.deepcopy(current)
                curr2.Rubik.movs(i)
                lista = tuple(curr2.Rubik.caras)
                if lista not in visited:
                    curr2.distancia += 1
                    curr2.movimientos.append(i)
                    curr2.calculate_heuristic(heuristic)
                    curr2.total_heuristic += curr2.heuristic_value
                    visited.add(lista)
                    pq.put(curr2)
                elif lista == self.solved:
                    curr2.distancia += 1
                    curr2.movimientos.append(i)
                    print("---SOLVED---")
                    print("Movimientos para resolver: ", curr2.distancia)
                    curr2.imp_mov()
                    return
    
    def ida_star(self, heuristic):
        # Método IDA* para resolver el cubo de Rubik
        # Comprueba si el cubo ya está resuelto
        if tuple(self.Rubik.caras) == self.solved:
            print("Already solved.")
            return
        
        source = Nodo(self.Rubik)  # Nodo de origen con el estado actual del cubo
        threshold = source.return_heuristic_value(heuristic)  # Umbral inicial
        while True:
            print(threshold)  # Imprime el umbral actual (para propósitos de depuración)
            # Realiza una búsqueda con IDA* hasta que encuentre una solución o alcance un umbral máximo
            temp = self.__search(source, 0, threshold, heuristic)
            if temp == "FOUND":  # Si se encuentra una solución, termina el algoritmo
                return
            if temp == float('inf'):  # Si no es posible resolver el cubo, devuelve un mensaje de error
                return "Not possible"
            threshold = temp  # Actualiza el umbral para la siguiente iteración

    def __search(self, node, g, threshold, heuristic):
        # Método privado para realizar la búsqueda recursiva con IDA*
        f = g + node.return_heuristic_value(heuristic)  # Costo total actual (g + heurística)
        if f > threshold:  # Si el costo total supera el umbral, termina la búsqueda en este nodo
            return f
        if node == self.solved:  # Si se alcanza el estado objetivo, se encontró una solución
            return "FOUND"
        min = float('inf')  # Inicializa el mínimo con infinito
        for i in range(12):  # Itera sobre los posibles movimientos del cubo (12 en total)
            node2 = copy.deepcopy(node)  # Crea una copia del nodo actual para simular el movimiento
            node2.Rubik.movs(i)  # Aplica el movimiento al cubo
            # Realiza una búsqueda recursiva con IDA* desde el nuevo nodo generado
            temp = self.__search(node2, g + 1, threshold, heuristic)
            if temp == "FOUND":  # Si se encuentra una solución, termina la búsqueda
                return "FOUND"
            if temp < min:  # Actualiza el mínimo si se encuentra un nuevo valor menor
                min = temp
        return min  # Retorna el mínimo encontrado después de explorar todos los movimientos


solucionador = RubikSolver()
solucionador.revolver(True, 2)
#solucionador.bfs()
#solucionador.best_first_search(Heuristics.heu_2)
#solucionador.a_star(Heuristics.heu_3)
#solucionador.ida_star(Heuristics.heu_1)

"""
LIST OF MOVES:
0 = R1
1 = R2
2 = L1
3 = L2
4 = U1
5 = U2
6 = D1
7 = D2
8 = F1
9 = F2
10 = B1
11 = B2
"""