from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca, CancionNoEncontradaError


def versiones_de(biblioteca: Biblioteca, versiones: list[tuple[int, int, str]], cancion_id: int) -> list[tuple[str, str]]:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    # Verifica que la canción exista en la biblioteca; si no está, lanza CancionNoEncontradaError
    biblioteca.obtener(cancion_id)

    # 1. Buscar todas las versiones directas donde version_de_id == cancion_id
    directas = []
    for vid, padre_id, tipo in versiones:
        if padre_id == cancion_id:
            directas.append((vid, tipo))

    # 2. Ordenar de menor a mayor cancion_id (inserción manual, respetando restricción del examen)
    for i in range(1, len(directas)):
        actual = directas[i]
        j = i - 1
        while j >= 0 and directas[j][0] > actual[0]:
            directas[j + 1] = directas[j]
            j -= 1
        directas[j + 1] = actual

    # 3. Caso base implícito: si directas está vacía, el bucle no ejecuta y devuelve []
    resultado = []
    for vid, tipo in directas:
        cancion_version = biblioteca.obtener(vid)
        # Preorden: primero la versión directa
        resultado.append((cancion_version.titulo, tipo))
        # Luego todo lo que cuelga recursivamente de esa versión
        resultado.extend(versiones_de(biblioteca, versiones, vid))

    return resultado


if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316))
    bib.agregar(Cancion(13, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota", "En Directo", "Rock", 1992, 318))
    bib.agregar(Cancion(70, "Ji Ji Ji (Remix)", "Patricio Rey y sus Redonditos de Ricota", "Remixes", "Rock", 2020, 300))
    bib.agregar(Cancion(16, "Gracias a la Vida", "Mercedes Sosa", "Hasta la Victoria", "Folk", 1971, 271))
    bib.agregar(Cancion(61, "Gracias a la Vida", "Violeta Parra", "Las Ultimas Composiciones", "Folk", 1966, 258))

    versiones_prueba = [
        (13, 12, "live"),
        (70, 13, "remix"),
        (16, 61, "cover"),
    ]

    print("Versiones de 12:", versiones_de(bib, versiones_prueba, 12))
    # [('Ji Ji Ji', 'live'), ('Ji Ji Ji (Remix)', 'remix')]

    print("Versiones de 61:", versiones_de(bib, versiones_prueba, 61))
    # [('Gracias a la Vida', 'cover')]

    print("Versiones de 70:", versiones_de(bib, versiones_prueba, 70))
    # []

# Teoría:
# - Caso base: ocurre cuando ninguna tupla en `versiones` tiene `version_de_id == cancion_id` (es decir, la canción no tiene versiones derivadas directas). En ese caso la función no realiza llamadas recursivas y retorna la lista vacia `[]`.
# - Secuencia de llamadas para `versiones_de(biblioteca, versiones, 12)` (suponiendo que la canción 70 es remix de la 13):
#   1. Llama a `versiones_de(..., 12)`: encuentra la versión directa `(13, 'live')` y hace una llamada recursiva para `cancion_id = 13`.
#   2. Llama a `versiones_de(..., 13)`: encuentra la versión directa `(70, 'remix')` y hace una llamada recursiva para `cancion_id = 70`.
#   3. Llama a `versiones_de(..., 70)`: alcanza el caso base (nadie es versión de 70) y devuelve `[]`.
#   4. Vuelve a `versiones_de(..., 13)`: concatena `[('Ji Ji Ji (Remix)', 'remix')] + []` y devuelve `[('Ji Ji Ji (Remix)', 'remix')]`.
#   5. Vuelve a `versiones_de(..., 12)`: concatena `[('Ji Ji Ji', 'live')] + [('Ji Ji Ji (Remix)', 'remix')]` y devuelve `[('Ji Ji Ji', 'live'), ('Ji Ji Ji (Remix)', 'remix')]`.