from queue import Queue
from queue import PriorityQueue
from cube import RubikCube
import copy

class Heuristics:
    @staticmethod
    def heu1(a):
        return a
    
    @staticmethod
    def heu2(a):
        return a*2
    
    @staticmethod
    def heu3(a):
        return a*3

class Nodo:
    def __init__(self, cubo):
        self.cubo = cubo
        self.distancia = 0
        self.movimientos = []
        self.movs_letras = ["R1", "R2", "L1", "L2", "U1", "U2", "D1", "D2", "F1", "F2", "B1", "B2"]
        self.heuristic_val = -1
    
    def calculate_heuristic(self, other, heuristic):
        self.heuristic_value = heuristic(self, other)

    def imp_mov(self):
        for i in self.movimientos:
            print(self.movs_letras[i], end=" ")
        print()

class RubikSolver:
    def __init__(self):
        self.cubo = RubikCube()
        self.solved = (0, 2396745, 4793490, 7190235, 9586980, 11983725)
        self.mov_resuelto = []
        self.iteraciones = 0

    def revolver(self, azar, movs):
        if azar is True:
            self.cubo.shuffle_azar(movs)
        else:
            self.cubo.shuffle(movs)
        self.cubo.print_faces()

    def bfs(self):
        if(tuple(self.cubo.caras) == self.solved):
            print("Already solved.")
            return
        source = Nodo(self.cubo)
        cola = Queue()
        cola.put(source)
        visited = set()
        visited.add(tuple(self.cubo.caras))
        visited.add(self.solved)
        while cola.empty() is not True:
            self.iteraciones += 1
            aux = cola.get()
            for i in range(12):
                aux_c = copy.deepcopy(aux)
                aux_c.cubo.movs(i)
                aux_c.distancia += 1
                aux_c.movimientos.append(i)
                lista = tuple(aux_c.cubo.caras)
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
        pq = PriorityQueue()
        source = Nodo(self.cubo)
        target = Nodo(RubikCube())
        pq.put(source)

        visited = set()
        visited.add(tuple(self.cubo.caras))

        while not pq.empty():
            current = pq.get()
            if current == target:
                print("---SOLVED---")
                print("Movimientos para resolver: ", current.distancia)
                current.imp_mov()
                return
            for i in range(12):
                curr2 = copy.deepcopy(current)
                curr2.cubo.movs(i)
                lista = tuple(curr2.cubo.caras)
                if lista not in visited:
                    curr2.distancia += 1
                    curr2.movimientos.append(i)
                    curr2.calculate_heuristic(target, heuristic)
                    visited.add(lista)
                    pq.put(curr2)

    def a_star(self):
        pass

solucionador = RubikSolver()
solucionador.revolver(True, 4)
solucionador.bfs()

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