class RubikCube:
    def __init__(self):
        self.colors_l = ["W", "R", "G", "Y", "O", "B"]
        self.colors = ["000", "001", "010", "011", "100", "101"]
        self.cubo = [[self.colors[i]]*8 for i in range(6)]
        self.caras = [0, 0, 0, 0, 0, 0]
    
    def calcular_caras(self):
        for i in range(0, 6):
            cadena = ""
            for j in self.cubo[i]:
                cadena += j
            self.caras[i] = int(cadena, 2)
    
    def cambio(self, cara1, cara2, cara3, cara4, a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4):
        aux = self.cubo[cara1][a1]
        self.cubo[cara1][a1] = self.cubo[cara2][a2]
        self.cubo[cara2][a2] = self.cubo[cara3][a3]
        self.cubo[cara3][a3] = self.cubo[cara4][a4]
        self.cubo[cara4][a4] = aux
        aux = self.cubo[cara1][b1]
        self.cubo[cara1][b1] = self.cubo[cara2][b2]
        self.cubo[cara2][b2] = self.cubo[cara3][b3]
        self.cubo[cara3][b3] = self.cubo[cara4][b4]
        self.cubo[cara4][b4] = aux
        aux = self.cubo[cara1][c1]
        self.cubo[cara1][c1] = self.cubo[cara2][c2]
        self.cubo[cara2][c2] = self.cubo[cara3][c3]
        self.cubo[cara3][c3] = self.cubo[cara4][c4]
        self.cubo[cara4][c4] = aux
    
    def cambio_cara(self, cara, horario):
        if(horario):
            aux = self.cubo[cara][1]
            self.cubo[cara][1] = self.cubo[cara][3]
            self.cubo[cara][3] = self.cubo[cara][6]
            self.cubo[cara][6] = self.cubo[cara][4]
            self.cubo[cara][4] = aux
            aux = self.cubo[cara][0]
            self.cubo[cara][0] = self.cubo[cara][5]
            self.cubo[cara][5] = self.cubo[cara][7]
            self.cubo[cara][7] = self.cubo[cara][2]
            self.cubo[cara][2] = aux
        else:
            aux = self.cubo[cara][1]
            self.cubo[cara][1] = self.cubo[cara][4]
            self.cubo[cara][4] = self.cubo[cara][6]
            self.cubo[cara][6] = self.cubo[cara][3]
            self.cubo[cara][3] = aux
            aux = self.cubo[cara][0]
            self.cubo[cara][0] = self.cubo[cara][2]
            self.cubo[cara][2] = self.cubo[cara][7]
            self.cubo[cara][7] = self.cubo[cara][5]
            self.cubo[cara][5] = aux

    def R1(self):
        self.cambio(0, 4, 3, 1, 4, 4, 3, 4, 2, 2, 5, 2, 7, 7, 0, 7)
        self.cambio_cara(2, True)
    def R2(self):
        self.cambio(0, 1, 3, 4, 4, 4, 3, 4, 2, 2, 5, 2, 7, 7, 0, 7)
        self.cambio_cara(2, False)

    def L1(self):
        self.cambio(0, 1, 3, 4, 3, 3, 4, 3, 0, 0, 7, 0, 5, 5, 2, 5)
        self.cambio_cara(5, True)
    def L2(self):
        self.cambio(0, 4, 3, 1, 3, 3, 4, 3, 0, 0, 7, 0, 5, 5, 2, 5)
        self.cambio_cara(5, False)

    def U1(self):
        self.cambio(0, 2, 3, 5, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2)
        self.cambio_cara(1, True)
    def U2(self):
        self.cambio(0, 5, 3, 2, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2)
        self.cambio_cara(1, False)

    def D1(self):
        self.cambio(0, 5, 3, 2, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7)
        self.cambio_cara(4, True)
    def D2(self):
        self.cambio(0, 2, 3, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7)
        self.cambio_cara(4, False)

    def F1(self):
        self.cambio(1, 5, 4, 2, 5, 7, 2, 0, 6, 4, 1, 3, 7, 2, 0, 5)
        self.cambio_cara(0, True)
    def F2(self):
        self.cambio(1, 2, 4, 5, 5, 0, 2, 7, 6, 3, 1, 4, 7, 5, 0, 2)
        self.cambio_cara(0, False)

    def B1(self):
        self.cambio(1, 2, 4, 5, 0, 2, 7, 5, 1, 4, 6, 3, 2, 7, 5, 0)
        self.cambio_cara(3, True)
    def B2(self):
        self.cambio(1, 5, 4, 2, 0, 5, 7, 2, 1, 3, 6, 4, 2, 0, 5, 7)
        self.cambio_cara(3, False)

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
a.calcular_caras()
a.R1()
a.U1()
a.L1()
a.B2()
a.D1()
a.print_faces()