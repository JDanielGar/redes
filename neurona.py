class Neurona:
    def __init__(self, dato):
        self.dato = dato;
        self.dendrita = [];
        self.axon = [];
    def conectarAxon(self, neurona):
        # Creacion Axon neurona actual #
        self.axon.append(neurona);
        # Creacion Dendrita neurona adyacente #
        neurona.dendrita.append(self);
    def conectarDendrita(self, neurona):
        # Creacion Dendrita neuron actual #
        self.dendrita.append(neurona);
        # Creacion Axon neurona adyacente #
        neurona.axon.append(self);
