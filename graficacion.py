from interfaz_objetos import *
from neurona import *
from pulsador import *


def interaccionNeuronal(neurona):
    direccion = int(input("Seleccione la direccion: \n1.Axonal. \n2.Dendrital."));
    neuronaMadre(neurona, direccion);

def neuronaMadre(neurona, direccion):
    if(direccion==1):
        Axonal(neurona);
    else:
        Dendrital(neurona);
        
def Axonal(neurona, pos_x = 1, pos_y = 0):
    interfaz.crearOvalo(neurona.dato, pos_x, pos_y)
    pos_x+=1;
    print("Aqui esta la pos_y", pos_y)
    if(len(neurona.axon)>0):
        posicionesY = determinarPosicion(len(neurona.axon), pos_y)
        for pos_abs in range(len(posicionesY)):
            for neurona_hija in neurona.axon:
                Axonal(neurona_hija, pos_x, posicionesY[pos_abs]);
                pos_abs+=1
            break;
    else:
        print("La neurona:", neurona.dato,"no tiene mas conexiones");

def Dendrital(neurona, pos_x = 1, pos_y = 0):
    interfaz.crearOvalo(neurona.dato, pos_x, pos_y)
    pos_x+=1;
    print("Aqui esta la pos_y", pos_y)
    if(len(neurona.dendrita)>0):
        posicionesY = determinarPosicion(len(neurona.dendrita), pos_y)
        for pos_abs in range(len(posicionesY)):
            for neurona_hija in neurona.dendrita:
                Dendrital(neurona_hija, pos_x, posicionesY[pos_abs]);
                pos_abs+=1
            break;
    else:
        print("La neurona:", neurona.dato,"no tiene mas conexiones");