import csv
from pathlib import Path
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    """Excepción lanzada cuando el archivo CSV no existe, tiene encabezado erróneo o filas incompletas."""
    pass


ENCABEZADO_ESPERADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta, biblioteca: Biblioteca) -> None:
    """Guarda todas las canciones de la biblioteca en un archivo CSV UTF-8 con encabezado."""
    path = Path(ruta)
    with open(path, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO_ESPERADO)
        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg,
            ])


def cargar_canciones_csv(ruta) -> Biblioteca:
    """Carga un archivo CSV UTF-8 y devuelve una nueva Biblioteca con los objetos Cancion."""
    path = Path(ruta)
    if not path.is_file():
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe o no es un archivo válido.")

    biblioteca = Biblioteca()
    with open(path, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo, delimiter=",")

        encabezado = next(lector, None)
        if encabezado != ENCABEZADO_ESPERADO:
            raise ArchivoInvalidoError(
                f"Encabezado inválido. Se esperaba {ENCABEZADO_ESPERADO} y se recibió {encabezado}."
            )

        for num_fila, fila in enumerate(lector, start=2):
            if not fila:
                continue  # Ignora líneas completamente vacías al final del archivo
            if len(fila) < len(ENCABEZADO_ESPERADO):
                raise ArchivoInvalidoError(
                    f"La fila {num_fila} tiene menos columnas de las esperadas ({len(fila)} de {len(ENCABEZADO_ESPERADO)})."
                )
            try:
                cancion = Cancion(
                    id=int(fila[0]),
                    titulo=fila[1],
                    artista=fila[2],
                    album=fila[3],
                    genero=fila[4],
                    anio=int(fila[5]),
                    duracion_seg=int(fila[6]),
                )
            except ValueError as e:
                raise ArchivoInvalidoError(f"Error de formato numérico en la fila {num_fila}: {e}")

            biblioteca.agregar(cancion)

    return biblioteca


if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    bib.agregar(Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316))

    ruta_prueba = Path("canciones_test.csv")
    guardar_canciones_csv(ruta_prueba, bib)

    bib_cargada = cargar_canciones_csv(ruta_prueba)
    print("Canciones cargadas:", bib_cargada.listar())

    # Limpieza del archivo temporal de prueba
    if ruta_prueba.exists():
        ruta_prueba.unlink()

# Teoría:
# Sí, hay que recorrer todas las filas anteriores porque un archivo CSV es un archivo de texto secuencial con registros de longitud variable separados por saltos de línea, por lo que no permite calcular un desplazamiento directo en bytes para saltar a la fila 50 sin leer y contar los saltos de línea previos.