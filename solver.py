from queue import Queue
from cube import RubikCube
import copy

class RubikSolver:
    def __init__(self, cubo):
        self.cubo = cubo
        self.solved = [7190235, 40210718148900, 80421429107565]
        self.distancia = 0
        self.mov_resuelto = []

    def bfs(self):
        cola = Queue()
        cola.put(self.cubo)
        self.cubo.calcular_caras()
        visited = set()
        visited.add(tuple(self.cubo.caras))
        while cola.empty() is not True:
            self.distancia += 1
            aux = cola.get()
            if aux.caras == self.solved:
                print("SOLVED")
                break
            for i in range(12):
                aux.movs(i)
                if tuple(aux.caras) not in visited:
                    cola.put(copy.deepcopy(aux))
                    visited.add(tuple(aux.caras))

a = RubikCube()
a.shuffle_azar(2)
a.print_faces()
b = RubikSolver(a)
b.bfs()
print(b.distancia)

#23375 movs, 7.886s
#799 movs, 0.383s
#13 movs, 0.175s
#1 movs, 0.127s
#18233 movs, 6.031s
#NEW IS WAY TOO SLOW, TAKES ALMOST TWICE THE TIME