from graficacion import *

a = Neurona('Nathaly');

b = Neurona('Novia');
c = Neurona('Humano');
d = Neurona('Estudiante');
e = Neurona('Joven');

f = Neurona('Daniel');
g = Neurona('Moso');

h = Neurona('Mamifero');

a.conectarAxon(b);
a.conectarAxon(c);

c.conectarAxon(f)
c.conectarAxon(g)
c.conectarAxon(h)

h.conectarAxon(d)
h.conectarAxon(e)

interaccionNeuronal(a);

interfaz.activarPantalla()
