from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


def busqueda_lineal(canciones: list[Cancion], campo: str, valor: str) -> list[Cancion]:
    """Devuelve todas las canciones cuyo `campo` ('titulo', 'artista' o 'genero') es igual a `valor`."""
    if campo not in ("titulo", "artista", "genero"):
        raise ValueError(f"Campo de búsqueda no válido: {campo}. Debe ser 'titulo', 'artista' o 'genero'.")

    encontradas = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            encontradas.append(cancion)
    return encontradas


def busqueda_binaria_por_titulo(canciones_ordenadas: list[Cancion], titulo: str) -> Cancion:
    """Búsqueda binaria iterativa sobre una lista ordenada alfabéticamente por `titulo`.
       Devuelve la primera Cancion encontrada con ese título o lanza CancionNoEncontradaError."""
    izq = 0
    der = len(canciones_ordenadas) - 1

    while izq <= der:
        medio = (izq + der) // 2
        titulo_medio = canciones_ordenadas[medio].titulo

        if titulo_medio == titulo:
            return canciones_ordenadas[medio]
        elif titulo_medio > titulo:
            der = medio - 1
        else:
            izq = medio + 1

    raise CancionNoEncontradaError(f"No se encontró ninguna canción con el título '{titulo}'.")


if __name__ == "__main__":
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c15 = Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "Mujeres Argentinas", "Folklore", 1969, 298)
    c16 = Cancion(16, "Gracias a la Vida", "Mercedes Sosa", "Hasta la Victoria", "Folklore", 1971, 271)
    c61 = Cancion(61, "Gracias a la Vida", "Violeta Parra", "Las Ultimas Composiciones", "Folklore", 1966, 258)

    catalogo = [c1, c12, c15, c16, c61]

    print("Búsqueda lineal Rock:", [c.titulo for c in busqueda_lineal(catalogo, "genero", "Rock")])
    print("Búsqueda lineal Mercedes Sosa:", [c.titulo for c in busqueda_lineal(catalogo, "artista", "Mercedes Sosa")])

    # Lista ordenada alfabéticamente por título
    ordenadas_titulo = [c15, c1, c16, c61, c12]
    print("Binaria 'Jijiji':", busqueda_binaria_por_titulo(ordenadas_titulo, "Jijiji"))
    print("Binaria duplicado 'Gracias a la Vida':", busqueda_binaria_por_titulo(ordenadas_titulo, "Gracias a la Vida"))

    try:
        busqueda_binaria_por_titulo(ordenadas_titulo, "Cancion Inexistente")
    except CancionNoEncontradaError as e:
        print("Error capturado correctamente:", e)

# Teoría:
# `busqueda_binaria_por_titulo` requiere que la lista esté ordenada por título porque en cada paso compara el título buscado con el elemento central para descartar de inmediato la mitad izquierda o derecha donde sabe con certeza que el valor no puede estar.
# Sobre `n` canciones, la búsqueda binaria tiene una complejidad temporal de O(log n) en el peor caso (ya que divide el espacio de búsqueda a la mitad en cada iteración), mientras que la búsqueda lineal por artista tiene una complejidad de O(n) porque debe recorrer y revisar todos los elementos de la lista uno por uno.