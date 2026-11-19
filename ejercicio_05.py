from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    """Excepción lanzada cuando se intenta desapilar o consultar el tope de una pila vacía."""
    pass


class Pila:
    def __init__(self):
        self._datos = ListaEnlazada()

    def esta_vacia(self) -> bool:
        return self._datos.esta_vacia()

    def apilar(self, dato) -> None:
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía, no se puede desapilar.")
        return self._datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía, no hay tope para ver.")
        return self._datos.primero.dato


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion: Cancion) -> None:
        self._pila.apilar(cancion)

    def anterior(self) -> Cancion:
        return self._pila.desapilar()

    def ultima(self) -> Cancion:
        return self._pila.ver_tope()


if __name__ == "__main__":
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c15 = Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", "Folk", 1969, 298)
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)

    historial = HistorialReproduccion()
    historial.registrar(c12)
    historial.registrar(c15)
    historial.registrar(c1)

    print("Última reproducida (sin sacar):", historial.ultima())  # De Musica Ligera
    print("Primer anterior():", historial.anterior())              # De Musica Ligera
    print("Segundo anterior():", historial.anterior())             # Alfonsina y el mar

    historial.anterior()  # Saca Jijiji
    try:
        historial.anterior()
    except PilaVaciaError as e:
        print("Error capturado correctamente:", e)

# Teoría:
# El primer `anterior()` devuelve "De Música Ligera".
# Esto ocurre porque la pila sigue una política LIFO (Last In, First Out — el último en entrar es el primero en salir): al ser "De Música Ligera" la última canción registrada, quedó en el tope de la pila (el primer nodo de la lista enlazada) y es la primera que se desapila.