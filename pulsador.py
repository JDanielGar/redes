def pulsadorY(pos_y, pos_ini=0):
    if(pos_y%2==0):
        pos_y = conversorPar(pos_y, pos_ini);
    else:
        pos_y = conversorImpar(pos_y, pos_ini);
    return pos_y

def conversorPar(pos_y, pos_ini=0):
    if(pos_ini!=0):

        pos_y = (list(range(int(pos_ini-pos_y/2), int(pos_ini+pos_y/2))));
    else:
        pos_y = (list(range(int(pos_ini-pos_y/2), int(pos_ini+pos_y/2))));
        for number in range(len(pos_y)):
            pos_y[number]+=0.5
    return pos_y
