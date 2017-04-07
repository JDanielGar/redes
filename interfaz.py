import tkinter as tk
from tkinter import *

programa = Tk()

canvas = Canvas(programa, width=800, height = 600);
canvas.pack()


def dibujarEstado(neurona, pos_x=1, pos_y=0):
    color='white'
    posicion = calcularPos(pos_x, pos_y);
    if(pos_x==1):
        color='red'
    canvas.create_oval(10 + posicion[0], 250 + posicion[1], 80 + posicion[0], 300 + posicion[1], fill=color)
    canvas.create_text(45 + posicion[0], 275 + posicion[1], fill="black", text=neurona)
    

def calcularPos(pos_x, pos_y):
    if(pos_y>0):
        pos_x = (pos_x-1)*100
        pos_y = (pos_y)*60
    else:
        pos_x = (pos_x-1)*100
        pos_y = -(-pos_y)*60
    return pos_x, pos_y