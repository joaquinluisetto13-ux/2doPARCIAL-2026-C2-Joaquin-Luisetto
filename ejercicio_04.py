from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


class ListaVaciaError(Exception):
    """Excepción lanzada al intentar quitar un elemento de una lista enlazada vacía."""
    pass


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        contador = 0
        actual = self.primero
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def insertar_al_inicio(self, dato) -> None:
        nuevo = Nodo(dato, self.primero)
        self.primero = nuevo

    def insertar_al_final(self, dato) -> None:
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
            return
        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def quitar_primero(self):
        if self.esta_vacia():
            raise ListaVaciaError("No se puede quitar de una lista vacía.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        return dato

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self, nombre: str = "Mi Playlist"):
        self.nombre = nombre
        self._canciones = ListaEnlazada()

    def agregar(self, cancion: Cancion) -> None:
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id: int) -> None:
        actual = self._canciones.primero
        anterior = None

        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    # El elemento a quitar es el primero
                    self._canciones.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

        raise CancionNoEncontradaError(f"La canción con id {id} no está en la playlist.")

    def listar(self) -> list[str]:
        return [str(cancion) for cancion in self._canciones]

    def duracion_total(self) -> int:
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total


if __name__ == "__main__":
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c15 = Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", "Folk", 1969, 298)

    pl = Playlist("Rock Nacional")
    print("Duración vacía:", pl.duracion_total())  # 0

    pl.agregar(c1)
    pl.agregar(c12)
    pl.agregar(c15)
    print("Listar:", pl.listar())
    print("Duración total:", pl.duracion_total())  # 827

    pl.quitar(12)
    print("Después de quitar #12:", pl.listar())

    try:
        pl.quitar(999)
    except CancionNoEncontradaError as e:
        print("Error esperado:", e)

# Teoría:
# Cuando ya hay `n` elementos y la lista solo guarda una referencia al primer nodo, para insertar al final se recorren los `n` nodos existentes (avanzando `n - 1` enlaces `siguiente` desde el primero hasta alcanzar el último nodo donde `actual.siguiente is None`).
# Por lo tanto, la operación tiene una complejidad temporal lineal de O(n).