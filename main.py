from solver import RubikSolver, Heuristics
from text import Texts
import time

'''
Rubik's cube python proyect
Oscar Fabrizio de Alba
Jose Arturo Reza Quezada
'''
class Main:
    def __init__(self):
        self.solver = RubikSolver()
    
    def print_movements(self):
        pass
    
    def menu(self):
        Texts.i()
        while True:
            action = input()
            if action == '1' or action == '2':
                self.action(action)
                break
            Texts.w()
        
    def action(self, action):
        if action == '1':
            Texts.i1()
            n = int(input())
            self.solver.revolver(True, n)
            self.solve()
        else:
            Texts.movs()
            
            while True:
                Texts.i2()
                m = int(input())
                if m == -1:
                    self.solve()
                    break
                elif m >= 1 and m <= 12:
                    self.solver.make_move(m)
                else:
                    Texts.w()
    
    def solve(self):
        Texts.s()
        while True:
            metodo = int(input())
            if metodo > 0 and metodo <= 4:
                break
            
        Texts.h()

        # Si el método no requiere heurística
        if metodo == 1:
            inicio = time.time()
            self.solver.bfs()
            fin = time.time()
            Texts.t(fin - inicio)

        # Si el método requiere heurística
        elif metodo in [2, 3, 4]:
            while True:
                heuristica = int(input())
                if heuristica > 0 and heuristica <= 4:
                    break
                Texts.w()
                
            heuristic_functions = {
                1: Heuristics.heu_1,
                2: Heuristics.heu_2,
                3: Heuristics.heu_3,
                4: Heuristics.heu_4
            }

            # Verificar si la heurística seleccionada es válida
            if heuristica in heuristic_functions:
                heuristic_function = heuristic_functions[heuristica]
                if metodo == 2:
                    inicio = time.time()
                    self.solver.best_first_search(heuristic_function)
                    fin = time.time()
                    Texts.t(fin - inicio)
                elif metodo == 3:
                    inicio = time.time()
                    self.solver.a_star(heuristic_function)
                    fin = time.time()
                    Texts.t(fin - inicio)
                elif metodo == 4:
                    inicio = time.time()
                    self.solver.ida_star(heuristic_function)
                    fin = time.time()
                    Texts.t(fin - inicio)
    
main = Main()

main.menu()
