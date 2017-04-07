from graficacion import *

a = Neurona('Nathaly');

b = Neurona('Novia');
c = Neurona('Humano');
d = Neurona('Estudiante');
e = Neurona('Joven');

f = Neurona('Daniel');
g = Neurona('Moso');

a.conectarAxon(b);
a.conectarAxon(c);
a.conectarAxon(d);
a.conectarAxon(e);

b.conectarAxon(f);
b.conectarAxon(g);

interaccionNeuronal(a);


for objetos in interfaz.ovalos:
    print('Nombre:', objetos.neurona)
    print('Pos_X:', objetos.pos_x)
    print('Pos_Y:', objetos.pos_y)
    print('#################################')
