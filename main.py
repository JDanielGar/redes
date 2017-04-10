from graficacion import *

a = Neurona('numeros');

b= Neurona('2');
c= Neurona('3');

d= Neurona('pares')
e = Neurona('impares')

a.conectarAxon(b)
a.conectarAxon(c)

b.conectarAxon(d)
c.conectarAxon(e)

b.conectarAxon(d)
b.conectarAxon(d)
b.conectarAxon(d)

interaccionNeuronal(a);

interfaz.activarPantalla()
