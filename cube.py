class RubikCube:
    def __init__(self):
        self.colors_l = ["W", "R", "G", "Y", "O", "B"]
        self.colors = ["000", "001", "010", "011", "100", "101"]
        self.cubo = [[self.colors[i]]*8 for i in range(6)]
        self.caras = [0, 0, 0, 0, 0, 0]
    
    def calc_caras(self):
        for i in range(0, 6):
            cadena = ""
            for j in self.cubo[i]:
                cadena += j
            self.caras[i] = int(cadena, 2)
    
    def cambio(self, a1, a2, b1, b2, c1, c2, d1, d2):
        aux = self.cubo[a1][a2]
        self.cubo[a1][a2] = self.cubo[b1][b2]
        self.cubo[b1][b2] = self.cubo[c1][c2]
        self.cubo[c1][c2] = self.cubo[d1][d2]
        self.cubo[d1][d2] = aux

    def R1(self):
        self.cambio(0, 4, 4, 4, 3, 3, 1, 4)
        self.cambio(0, 2, 4, 2, 3, 5, 1, 2)
        self.cambio(0, 7, 4, 7, 3, 0, 1, 7)
        self.cambio(2, 1, 2, 3, 2, 6, 2, 4)
        self.cambio(2, 0, 2, 5, 2, 7, 2, 2)
    def R2(self):
        self.cambio(0, 4, 1, 4, 3, 3, 4, 4)
        self.cambio(0, 2, 1, 2, 3, 5, 4, 2)
        self.cambio(0, 7, 1, 7, 3, 0, 4, 7)
        self.cambio(2, 1, 2, 4, 2, 6, 2, 3)
        self.cambio(2, 0, 2, 2, 2, 7, 2, 5)

    def L1(self):
        pass
    def L2(self):
        pass

    def U1(self):
        pass
    def U2(self):
        pass

    def D1(self):
        pass
    def D2(self):
        pass

    def F1(self):
        pass
    def F2(self):
        pass

    def B1(self):
        pass
    def B2(self):
        pass

    def print_faces(self):
        j=0
        for i in self.cubo:
            print("-CARA", j, end="")
            print("-")
            print(self.colors_l[int(i[0], 2)], self.colors_l[int(i[1], 2)], self.colors_l[int(i[2], 2)])
            print(self.colors_l[int(i[3], 2)], self.colors_l[j], self.colors_l[int(i[4], 2)])
            print(self.colors_l[int(i[5], 2)], self.colors_l[int(i[6], 2)], self.colors_l[int(i[7], 2)])
            j += 1

a = RubikCube()
a.calc_caras()
a.R1()
a.print_faces()