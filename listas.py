class ListaContigua:
    def __init__(self):
        self.lista = []
    
    def insertar(self, elemento):
        self.lista.append(elemento)
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
    
    def mostrar(self):
        print("Lista Contigua:", self.lista)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
    
    def mostrar(self):
        actual = self.cabeza
        print("Lista Ligada:", end=" ")
        while actual:
            print(actual.dato, "->", end=" ")
            actual = actual.siguiente
        print("NULL")

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeLigada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, valor):
        nuevo_nodo = NodoDoble(valor)
        nuevo_nodo.siguiente = self.cabeza
        if self.cabeza:
            self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
    
    def eliminar(self, valor):
        actual = self.cabeza
        while actual and actual.dato != valor:
            actual = actual.siguiente
        if actual:
            if actual.anterior:
                actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
            if actual == self.cabeza:
                self.cabeza = actual.siguiente
    
    def mostrar(self):
        actual = self.cabeza
        print("Lista Doblemente Ligada:", end=" ")
        while actual:
            print(actual.dato, "<->", end=" ")
            actual = actual.siguiente
        print("NULL")

class ListaIndexada:
    def __init__(self):
        self.lista = []
        self.indices = []
    
    def insertar(self, elemento):
        self.lista.append(elemento)
        self.indices.append(len(self.lista))
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            idx = self.lista.index(elemento)
            del self.lista[idx]
            del self.indices[idx]
    
    def mostrar(self):
        print("Lista Indexada:")
        for i in range(len(self.lista)):
            print(f"Índice: {self.indices[i]} -> Valor: {self.lista[i]}")