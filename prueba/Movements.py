import numpy as np

def RotarFrontalHorario(x):  # acción 1
    x[6:9, 0:3] = np.fliplr(x[6:9, 0:3].transpose())
    temp1 = np.array(x[2, 0:3])
    temp2 = np.array(x[9:12, 0])
    temp3 = np.array(x[15, 0:3])
    temp4 = np.array(x[3:6, 2])
    x[2, 0:3] = np.fliplr([temp4])[0]
    x[9:12, 0] = temp1
    x[15, 0:3] = np.fliplr([temp2])[0]
    x[3:6, 2] = temp3

def RotarFrontalAntihorario(x):  # acción 2
    RotarFrontalHorario(x)
    RotarFrontalHorario(x)
    RotarFrontalHorario(x)

def RotarSuperiorHorario(x):  # acción 3
    x[0:3, 0:3] = np.fliplr(x[0:3, 0:3].transpose())
    temp1 = np.array(x[12, 0:3])
    temp2 = np.array(x[9, 0:3])
    temp3 = np.array(x[6, 0:3])
    temp4 = np.array(x[3, 0:3])
    x[12, 0:3] = temp4
    x[9, 0:3] = temp1
    x[6, 0:3] = temp2
    x[3, 0:3] = temp3

def RotarSuperiorAntihorario(x):  # acción 4
    RotarSuperiorHorario(x)
    RotarSuperiorHorario(x)
    RotarSuperiorHorario(x)

def RotarInferiorHorario(x):  # acción 5
    x[15:18, 0:3] = np.fliplr(x[15:18, 0:3].transpose())
    temp1 = np.array(x[8, 0:3])
    temp2 = np.array(x[11, 0:3])
    temp3 = np.array(x[14, 0:3])
    temp4 = np.array(x[5, 0:3])
    x[8, 0:3] = temp4
    x[11, 0:3] = temp1
    x[14, 0:3] = temp2
    x[5, 0:3] = temp3

def RotarInferiorAntihorario(x):  # acción 6
    RotarInferiorHorario(x)
    RotarInferiorHorario(x)
    RotarInferiorHorario(x)

def RotarIzquierdaHorario(x):  # acción 7
    x[3:6, 0:3] = np.fliplr(x[3:6, 0:3].transpose())
    temp1 = np.array(x[0:3, 0])
    temp2 = np.array(x[6:9, 0])
    temp3 = np.array(x[15:18, 0])
    temp4 = np.array(x[12:15, 2])
    x[0:3, 0] = np.fliplr([temp4])[0]
    x[6:9, 0] = temp1
    x[15:18, 0] = temp2
    x[12:15, 2] = np.fliplr([temp3])[0]

def RotarIzquierdaAntihorario(x):  # acción 8
    RotarIzquierdaHorario(x)
    RotarIzquierdaHorario(x)
    RotarIzquierdaHorario(x)

def RotarDerechaHorario(x):  # acción 9
    x[9:12, 0:3] = np.fliplr(x[9:12, 0:3].transpose())
    temp1 = np.array(x[0:3, 2])
    temp2 = np.array(x[12:15, 0])
    temp3 = np.array(x[15:18, 2])
    temp4 = np.array(x[6:9, 2])
    x[0:3, 2] = temp4
    x[12:15, 0] = np.fliplr([temp1])[0]
    x[15:18, 2] = np.fliplr([temp2])[0]
    x[6:9, 2] = temp3

def RotarDerechaAntihorario(x):  # acción 10
    RotarDerechaHorario(x)
    RotarDerechaHorario(x)
    RotarDerechaHorario(x)

def RotarTraseraHorario(x):  # acción 11
    x[12:15, :] = np.fliplr(x[12:15, :].transpose())
    temp1 = np.array(x[0, 0:3])
    temp2 = np.array(x[3:6, 0])
    temp3 = np.array(x[17, 0:3])
    temp4 = np.array(x[9:12, 2])
    x[0, 0:3] = temp4
    x[3:6, 0] = np.fliplr([temp1])[0]
    x[17, 0:3] = temp2
    x[9:12, 2] = np.fliplr([temp3])[0]

def RotarTraseraAntihorario(x):  # acción 12
    RotarTraseraHorario(x)
    RotarTraseraHorario(x)
    RotarTraseraHorario(x)

def ImprimirCubo(x):
    print("             ", x[0, 0:3])
    print("             ", x[1, 0:3])
    print("             ", x[2, 0:3])
    print(x[3, 0:3], x[6, 0:3], x[9, 0:3], x[12, 0:3])
    print(x[4, 0:3], x[7, 0:3], x[10, 0:3], x[13, 0:3])
    print(x[5, 0:3], x[8, 0:3], x[11, 0:3], x[14, 0:3])
    print("             ", x[15, 0:3])
    print("             ", x[16, 0:3])
    print("             ", x[17, 0:3])

def make_movement(x, movimiento, invertir):
    # movimiento número
    # invertir si es 0 movimiento original si es 1 movimiento inverso del movimiento de entrada

    if invertir == 1:
        if movimiento % 2 == 0:
            movimiento = movimiento - 1
        else:
            movimiento = movimiento + 1
    if movimiento == 1:
        RotarFrontalHorario(x)
        return "RotarFrontalHorario"

    if movimiento == 2:
        RotarFrontalAntihorario(x)
        return "RotarFrontalAntihorario"

    if movimiento == 3:
        RotarSuperiorHorario(x)
        return "RotarSuperiorHorario"

    if movimiento == 4:
        RotarSuperiorAntihorario(x)
        return "RotarSuperiorAntihorario"

    if movimiento == 5:
        RotarInferiorHorario(x)
        return "RotarInferiorHorario"

    if movimiento == 6:
        RotarInferiorAntihorario(x)
        return "RotarInferiorAntihorario"

    if movimiento == 7:
        RotarIzquierdaHorario(x)
        return "RotarIzquierdaHorario"

    if movimiento == 8:
        RotarIzquierdaAntihorario(x)
        return "RotarIzquierdaAntihorario"

    if movimiento == 9:
        RotarDerechaHorario(x)
        return "RotarDerechaHorario"

    if movimiento == 10:
        RotarDerechaAntihorario(x)
        return "RotarDerechaAntihorario"

    if movimiento == 11:
        RotarTraseraHorario(x)
        return "RotarTraseraHorario"

    if movimiento == 12:
        RotarTraseraAntihorario(x)
        return "RotarTraseraAntihorario"
