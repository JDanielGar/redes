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
			ovalos.crearLinea()

interfaz = Interfaz();

class Ovalo:
	def __init__(self, neurona, pos_x=1, pos_y=0):
		self.neurona = neurona
		self.pos_x = pos_x;
		self.pos_y = pos_y;
		self.posicion = calcularPos(self.pos_x, self.pos_y);
	def Mostrar(self):
		print(self.neurona)
		canvas.create_oval(10 + self.posicion[0], 250 + self.posicion[1], 80 + self.posicion[0], 300 + self.posicion[1], fill='white')
		canvas.create_text(45 + self.posicion[0], 275 + self.posicion[1], fill="black", text=self.neurona)

	def crearLinea(self):
		lineaProxima = [];
		for posicion in range(len(interfaz.ovalos)):
			if(interfaz.ovalos[posicion].neurona == self.neurona):
				for ovalo in range(posicion):
					if(self.pos_x-1==interfaz.ovalos[ovalo].pos_x):
						x = interfaz.ovalos[ovalo].posicion[0];
						y = interfaz.ovalos[ovalo].posicion[1];
				break
		if(self.pos_x>1):
			canvas.create_line(80 + x, 275 + y, 10 + self.posicion[0], 275 + self.posicion[1], fill='black')


def calcularPos(pos_x, pos_y):
    if(pos_y>0):
        pos_x = (pos_x-1)*100
        pos_y = (pos_y)*60
    else:
        pos_x = (pos_x-1)*100
        pos_y = -(-pos_y)*60
    return pos_x, pos_y