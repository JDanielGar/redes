def determinarPosicion(nivel_y, pos_y):
    posicionesY = []
    if(nivel_y%2==0):
        for nueva_pos in range(nivel_y):
            posicionesY.append(pos_y+nueva_pos-nivel_y/2+0.5)
    else:
        for nueva_pos in range(nivel_y):
            posicionesY.append(pos_y+nueva_pos-(nivel_y-1)/2)
    print('Aca estan las posiciones', posicionesY)
    return posicionesY
