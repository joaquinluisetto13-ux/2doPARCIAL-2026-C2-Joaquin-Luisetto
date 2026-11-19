from ejercicio_01 import Cancion


class CancionNoEncontradaError(Exception):
    """Excepción lanzada cuando no se encuentra una canción por su id en la biblioteca."""
    pass


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion: Cancion) -> None:
        self._canciones.append(cancion)

    def cantidad(self) -> int:
        return len(self._canciones)

    def obtener(self, id: int) -> Cancion:
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No se encontró ninguna canción con el id {id}.")

    def listar(self) -> list[str]:
        return [str(cancion) for cancion in self._canciones]

    def __iter__(self):
        return iter(self._canciones)


if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    bib.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316))

    print("Cantidad:", bib.cantidad())        # 2
    print("Obtener 12:", bib.obtener(12))     # #12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16
    print("Listar:", bib.listar())

    for c in bib:
        print("Iterando:", c.titulo)

    try:
        bib.obtener(999)
    except CancionNoEncontradaError as e:
        print("Error capturado correctamente:", e)

# Teoría:
# La biblioteca almacena el catálogo maestro y único con todas las canciones disponibles en el sistema, actuando como fuente de datos principal.
# En cambio, una playlist guarda una secuencia ordenada (o cola de reproducción) de referencias a un subconjunto de esas canciones, permitiendo incluso repetirlas o reordenarlas sin alterar el catálogo original.