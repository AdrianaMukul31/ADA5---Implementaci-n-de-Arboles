class Arbol:
    def __init__(self):
        self.raiz = None
    def esVacio(self):
        return self.raiz is None
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)
    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(valor, nodo.izquierda)
        else:
            return self._buscar(valor, nodo.derecha)

    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo.derecha)
    def recorrido_inorden(self):
        self._recorrido_inorden(self.raiz)
        print()

    def _recorrido_inorden(self, nodo):
        if nodo:
            self._recorrido_inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._recorrido_inorden(nodo.derecha)

    def __del__(self):
        self._eliminar_nodos(self.raiz)
        print("Árbol destruido")

    def _eliminar_nodos(self, nodo):
        if nodo:
            self._eliminar_nodos(nodo.izquierda)
            self._eliminar_nodos(nodo.derecha)
            del nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
arbol = Arbol()
print("¿Árbol vacío?", arbol.esVacio())  
arbol.insertar(20)
arbol.insertar(7)
arbol.insertar(67)
print("¿Árbol vacío?", arbol.esVacio())  
print("Buscar 7:", arbol.buscar(7))
print("Buscar 10:", arbol.buscar(10))

print("Recorrido Inorden:")
arbol.recorrido_inorden()
