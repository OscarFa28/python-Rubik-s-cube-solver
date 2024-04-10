from queue import Queue
from queue import PriorityQueue
from cube import RubikCube
import copy

class Heuristics:
    @staticmethod
    #Manhattan distance between edges and their right place
    def heuristic_1(node):
        val = 0
        for i in range(6):
            for j in [1, 3, 4, 6]:
                if (node.Rubik.cubo[i][j] == i+3) or (node.Rubik.cubo[i][j] == i-3):
                    val += 2
                elif node.Rubik.cubo[i][j] != i:
                    val += 1
        return val
    
    @staticmethod
    def heu2(a):
        return a*2
    
    @staticmethod
    def heu3(a):
        return a*3

class Nodo:
    def __init__(self, Rubik):
        self.Rubik = Rubik
        self.distancia = 0
        self.movimientos = []
        self.movs_letras = ["R1", "R2", "L1", "L2", "U1", "U2", "D1", "D2", "F1", "F2", "B1", "B2"]
        self.heuristic_val = -1
    
    def calculate_heuristic(self, heuristic):
        self.heuristic_value = heuristic(self)

    def __eq__(self, other):
        if not isinstance(other, Nodo):
            return False
        return self.Rubik.caras == other.Rubik.caras
    
    def __lt__(self, other):
        if not isinstance(other, Nodo):
            return False
        return self.heuristic_value < other.heuristic_value

    def imp_mov(self):
        for i in self.movimientos:
            print(self.movs_letras[i], end=" ")
        print()

class RubikSolver:
    def __init__(self):
        self.Rubik = RubikCube()
        self.solved = (0, 2396745, 4793490, 7190235, 9586980, 11983725)
        self.mov_resuelto = []
        self.iteraciones = 0

    def revolver(self, azar, movs):
        if azar is True:
            self.Rubik.shuffle_azar(movs)
        else:
            self.Rubik.shuffle(movs)
        self.Rubik.print_faces()

    def bfs(self):
        if(tuple(self.Rubik.caras) == self.solved):
            print("Already solved.")
            return
        source = Nodo(self.Rubik)
        cola = Queue()
        cola.put(source)
        visited = set()
        visited.add(tuple(self.Rubik.caras))
        visited.add(self.solved)
        while cola.empty() is not True:
            self.iteraciones += 1
            aux = cola.get()
            for i in range(12):
                aux_c = copy.deepcopy(aux)
                aux_c.Rubik.movs(i)
                aux_c.distancia += 1
                aux_c.movimientos.append(i)
                lista = tuple(aux_c.Rubik.caras)
                if lista not in visited:
                    cola.put(aux_c)
                    visited.add(lista)
                elif lista == self.solved:
                    print("---SOLVED---")
                    print("Movimientos para resolver: ", aux_c.distancia)
                    aux_c.imp_mov()
                    return
        print("Not possible")

    def best_first_search(self, heuristic):
        if(tuple(self.Rubik.caras) == self.solved):
            print("Already solved.")
            return
        
        pq = PriorityQueue()
        source = Nodo(self.Rubik)
        target = Nodo(RubikCube())
        pq.put(source)

        visited = set()
        visited.add(tuple(self.Rubik.caras))

        while not pq.empty():
            current = pq.get()
            if current == target:
                print("---SOLVED---")
                print("Movimientos para resolver: ", current.distancia)
                current.imp_mov()
                return
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

    def a_star(self):
        pass

solucionador = RubikSolver()
solucionador.revolver(True, 4)
#solucionador.bfs()
solucionador.best_first_search(Heuristics.heuristic_1)

"""
PRUEBA CORTA DE HEURISTICA 1
NOTA: LA HEURISTICA 1 DE ARISTAS A SU LUGAR CORRESPONDIENTE NO FUNCIONA OPTIMAMENTE
a = RubikCube()
a.movs(0)
a.movs(0)
a.movs(0)
prueba = Nodo(a)
prueba.calculate_heuristic(Heuristics.heuristic_1)
print(prueba.heuristic_value)
"""

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