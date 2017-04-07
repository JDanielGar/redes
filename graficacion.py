from interfaz import *
from neurona import *
from pulsador import *
def interaccionNeuronal(neurona):
    direccion = int(input("Seleccione la direccion: \n1.Axonal. \2.Dendrital."));
    neuronaMadre(neurona, direccion);

def neuronaMadre(neurona, direccion):
    if(direccion==1):
        Axonal(neurona);
    else:
        Dendrital(neurona);
        
def Axonal(neurona, pos_x = 1, pos_y = 0):
    dibujarEstado(neurona.dato, pos_x, pos_y)
    pos_x += 1;
    if(len(neurona.axon)>0):
        pos_y = pulsadorY(len(neurona.axon), pos_y);
        for numero in range(len(pos_y)):
            for neurona_hija in neurona.axon:
                Axonal(neurona_hija, pos_x, pos_y[numero])
                numero+=1;
            break
    else:
        print("Neurona sin hijos")
        
def Dendrital(neurona, pos_x = 1):
    pos_x += 1;
    pos_y = len(neurona.dendrita);
    for neurona_hija in neurona.dendrita:
        print("Hola2")


        
