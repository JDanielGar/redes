from graficacion import *

cajon = Neurona('cajon');
pantalon = Neurona('pantalon');
chaqueta = Neurona ('chaqueta');
blusa = Neurona('blusa');
gafas = Neurona('gafas');
pantaloneta = Neurona('pantaloneta');
falda = Neurona('falda');
blanca = Neurona('blanca');

cajon.conectarAxon(pantalon);
cajon.conectarAxon(chaqueta);
cajon.conectarAxon(blusa);
cajon.conectarAxon(gafas);
pantalon.conectarAxon(pantaloneta);
pantalon.conectarAxon(falda);

interaccionNeuronal(cajon);

