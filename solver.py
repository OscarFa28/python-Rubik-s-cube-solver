from queue import Queue
from cube import RubikCube
import copy

class RubikSolver:
    def __init__(self, cubo):
        self.cubo = cubo
        self.solved = (7190235, 40210718148900, 80421429107565)
        self.distancia = 0
        self.mov_resuelto = []

    def bfs(self):
        cola = Queue()
        cola.put(self.cubo)
        self.cubo.calcular_caras()
        visited = set()
        visited.add(tuple(self.cubo.caras))
        visited.add(self.solved)
        if(tuple(self.cubo.caras) == self.solved):
            print("Already solved.")
            cola.queue.clear()
        while cola.empty() is not True:
            self.distancia += 1
            aux = cola.get()
            for i in range(12):
                aux_c = copy.deepcopy(aux)
                aux_c.movs(i)
                if tuple(aux_c.caras) not in visited:
                    cola.put(aux_c)
                    visited.add(tuple(aux_c.caras))
                elif tuple(aux_c.caras) == self.solved:
                    print("----SOLVEDDD----")
                    aux_c.print_faces()
                    print(cola.qsize())
                    cola.queue.clear()
                    break

a = RubikCube()
a.shuffle_azar(0)
a.print_faces()
b = RubikSolver(a)
b.bfs()
print(b.distancia)

"""
TESTS ON THE USE OF LISTS AND OLD METHOD:
23375m, 7.886s
799m, 0.383s
13m, 0.175s
1m, 0.127s
18233m, 6.031s

NEW IS WAY (NUMPY) TOO SLOW, TAKES ALMOST TWICE THE TIME
6014m, 4.646s
2020m, 1.73s
5686m, 4.413s
81630m, 52.751s
Why are they 220 movs if the range was one? Time: 0.548s

With the correction on bfs:
A 5 move cube with 35372 movs runs on 18.774 seconds
A 4 move cube with 5130 movs runs on 3.09 seconds
A 3 move cube with 962 movs runs on 0.751 seconds

With a correction in the queue:
A 6 moves, 27724 distance, 15.381s
"""