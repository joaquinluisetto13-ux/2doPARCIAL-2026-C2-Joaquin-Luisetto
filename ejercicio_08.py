from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones: list[Cancion]) -> list[Cancion]:
    """Ordenamiento por selección in-place. Ordena por `anio` de mayor a menor y devuelve la misma lista."""
    n = len(canciones)
    for i in range(n - 1):
        ind_mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[ind_mayor].anio:
                ind_mayor = j
        if ind_mayor != i:
            canciones[i], canciones[ind_mayor] = canciones[ind_mayor], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones: list[Cancion]) -> list[Cancion]:
    """Ordenamiento por inserción in-place. Ordena por `duracion_seg` de menor a mayor y devuelve la misma lista."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        # Comparación estricta (>): si tienen la misma duración, no se desplaza (conserva orden relativo)
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


if __name__ == "__main__":
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c62 = Cancion(62, "De Musica Ligera (Unplugged)", "Soda Stereo", "Comfort y Musica Para Volar", "Rock", 1996, 221)
    c70 = Cancion(70, "Ji Ji Ji (Remix)", "Patricio Rey y sus Redonditos de Ricota", "Remixes", "Rock", 2020, 300)

    lista = [c1, c12, c62, c70]

    print("Por año (mayor a menor):")
    for c in ordenar_por_anio_seleccion(lista):
        print(" ", c)

    print("\nPor duración (menor a mayor):")
    for c in ordenar_por_duracion_insercion(lista):
        print(" ", c)

# Teoría:
# - Complejidad de peor caso: ambos algoritmos tienen una complejidad temporal cuadrática de O(n²) en el peor caso (tanto selección como inserción realizan aproximadamente n*(n-1)/2 comparaciones).
# - Estabilidad (orden relativo): el ordenamiento por inserción es el que conserva el orden relativo de dos canciones con la misma clave, porque solo desplaza un elemento hacia la derecha cuando el anterior es estrictamente mayor (`canciones[j].duracion_seg > actual.duracion_seg`), sin saltar elementos iguales. En cambio, selección realiza intercambios a distancia que pueden alterar el orden original de elementos con clave empatada.