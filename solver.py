from queue import Queue
from cube import RubikCube
import copy

class Nodo:
    def __init__(self, cubo):
        self.cubo = cubo
        self.distancia = 0
        self.movimientos = []
        self.movs_letras = ["R1", "R2", "L1", "L2", "U1", "U2", "D1", "D2", "F1", "F2", "B1", "B2"]
    
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
        nodo_inicial = Nodo(self.cubo)
        cola = Queue()
        cola.put(nodo_inicial)
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

    def a_star():
        pass

solucionador = RubikSolver()
solucionador.revolver(True, 6)
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