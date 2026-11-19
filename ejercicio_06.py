from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desencolar o consultar el frente de una cola vacía."""
    pass


class Cola:
    def __init__(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._datos.esta_vacia()

    def encolar(self, dato) -> None:
        self._datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía, no se puede desencolar.")
        return self._datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía, no hay frente para ver.")
        return self._datos.primero.dato


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion: Cancion) -> None:
        self._cola.encolar(cancion)

    def siguiente(self) -> Cancion:
        return self._cola.desencolar()

    def que_sigue(self) -> Cancion:
        return self._cola.ver_frente()


if __name__ == "__main__":
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c15 = Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", "Folk", 1969, 298)
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)

    cola_rep = ColaReproduccion()
    cola_rep.encolar_cancion(c12)
    cola_rep.encolar_cancion(c15)
    cola_rep.encolar_cancion(c1)

    print("Qué sigue (sin sacar):", cola_rep.que_sigue())  # Jijiji
    print("Primer siguiente():", cola_rep.siguiente())      # Jijiji
    print("Segundo siguiente():", cola_rep.siguiente())     # Alfonsina y el mar

    cola_rep.siguiente()  # Saca De Musica Ligera
    try:
        cola_rep.siguiente()
    except ColaVaciaError as e:
        print("Error capturado correctamente:", e)

# Teoría:
# El primer `siguiente()` devuelve "Jijiji".
# A diferencia de la pila del ejercicio 5 (que usa política LIFO: último en entrar, primero en salir, invirtiendo el orden de ingreso), la cola sigue una política FIFO (First In, First Out — primero en entrar, primero en salir), por lo que respeta exactamente el mismo orden en que se agregaron las canciones.