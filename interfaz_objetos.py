import tkinter as tk
from tkinter import *

programa = Tk()

canvas = Canvas(programa, width=800, height = 600);
canvas.pack()

class Interfaz:
	def __init__(self):
		self.ovalos = [];
	def crearOvalo(self, neurona, pos_x=1, pos_y=0):
		self.ovalos.append(Ovalo(neurona, pos_x, pos_y))
	def activarPantalla(self):
		for ovalos in self.ovalos:
			ovalos.Mostrar();

interfaz = Interfaz();

class Ovalo:
	def __init__(self, neurona, pos_x=1, pos_y=0):
		self.neurona = neurona
		self.pos_x = pos_x;
		self.pos_y = pos_y;
	def Mostrar(self):
		self.posicion = calcularPos(self.pos_x, self.pos_y);
		canvas.create_oval(10 + self.posicion[0], 250 + self.posicion[1], 80 + self.posicion[0], 300 + self.posicion[1], fill='white')
		canvas.create_text(45 + self.posicion[0], 275 + self.posicion[1], fill="black", text=self.neurona)
		pos_abs = calcularLinea(self.pos_x, self.pos_y);
		canvas.create_line(10 + self.posicion[0], 275 + self.posicion[1], -20 + self.posicion[0], 275 + pos_abs, fill='red')


def calcularPos(pos_x, pos_y):
    if(pos_y>0):
        pos_x = (pos_x-1)*100
        pos_y = (pos_y)*60
    else:
        pos_x = (pos_x-1)*100
        pos_y = -(-pos_y)*60
    return pos_x, pos_y

def calcularLinea(pos_x, pos_y):
	objeto = interfaz.ovalos
	objeto.reverse
	for ovalo in objeto:
		if(ovalo.pos_x == pos_x-1):
			pos_x = ovalo.posicion[1]
			break;
	return pos_x
