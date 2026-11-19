import struct
from pathlib import Path
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "=4s1sI"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  # 9 bytes

FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      # 144 bytes

MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"M"


def _codificar_texto(texto: str, ancho: int) -> bytes:
    """Codifica un string a UTF-8, lo recorta al ancho en bytes y rellena con \\0."""
    raw = texto.encode("utf-8")[:ancho]
    return raw.ljust(ancho, b"\x00")


def _decodificar_texto(raw: bytes) -> str:
    """Corta en el primer \\0 y decodifica como UTF-8."""
    corte = raw.split(b"\x00", 1)[0]
    return corte.decode("utf-8")


def _empaquetar_cancion(cancion: Cancion) -> bytes:
    return struct.pack(
        FORMATO_REGISTRO,
        cancion.id,
        _codificar_texto(cancion.titulo, 40),
        _codificar_texto(cancion.artista, 40),
        _codificar_texto(cancion.album, 40),
        _codificar_texto(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg,
    )


def _desempaquetar_cancion(datos: bytes) -> Cancion:
    cid, tit_b, art_b, alb_b, gen_b, anio, duracion = struct.unpack(FORMATO_REGISTRO, datos)
    return Cancion(
        id=cid,
        titulo=_decodificar_texto(tit_b),
        artista=_decodificar_texto(art_b),
        album=_decodificar_texto(alb_b),
        genero=_decodificar_texto(gen_b),
        anio=anio,
        duracion_seg=duracion,
    )


def _validar_y_leer_encabezado(archivo, tamanio_archivo: int) -> int:
    """Valida magia, tema y tamaño total del archivo. Devuelve la cantidad de registros."""
    if tamanio_archivo < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es demasiado corto para contener un encabezado válido.")

    archivo.seek(0)
    encabezado_bytes = archivo.read(TAM_ENCABEZADO)
    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado_bytes)

    if magia != MAGIA_ESPERADA:
        raise ArchivoInvalidoError(f"Magia inválida: se esperaba {MAGIA_ESPERADA!r} y se recibió {magia!r}.")
    if tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError(f"Tema inválido: se esperaba {TEMA_ESPERADO!r} y se recibió {tema!r}.")

    tamanio_esperado = TAM_ENCABEZADO + cantidad * TAM_REGISTRO
    if tamanio_archivo != tamanio_esperado:
        raise ArchivoInvalidoError(
            f"Tamaño de archivo inválido: se esperaban {tamanio_esperado} bytes y hay {tamanio_archivo}."
        )

    return cantidad


def guardar_binario(ruta, biblioteca: Biblioteca) -> None:
    """Guarda todas las canciones de la biblioteca en un archivo binario de registros fijos."""
    path = Path(ruta)
    cantidad = biblioteca.cantidad()
    with open(path, mode="wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA_ESPERADA, TEMA_ESPERADO, cantidad))
        for cancion in biblioteca:
            archivo.write(_empaquetar_cancion(cancion))


def cargar_binario(ruta) -> Biblioteca:
    """Lee un archivo binario válido y devuelve una Biblioteca con los objetos Cancion."""
    path = Path(ruta)
    if not path.is_file():
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe o no es un archivo válido.")

    tamanio_archivo = path.stat().st_size
    biblioteca = Biblioteca()

    with open(path, mode="rb") as archivo:
        cantidad = _validar_y_leer_encabezado(archivo, tamanio_archivo)
        for _ in range(cantidad):
            registro_bytes = archivo.read(TAM_REGISTRO)
            biblioteca.agregar(_desempaquetar_cancion(registro_bytes))

    return biblioteca


def actualizar_registro(ruta, posicion: int, cancion: Cancion) -> None:
    """Sobrescribe el registro en `posicion` (0-based) usando seek sin reescribir el resto."""
    path = Path(ruta)
    if not path.is_file():
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe o no es un archivo válido.")

    tamanio_archivo = path.stat().st_size
    with open(path, mode="r+b") as archivo:
        cantidad = _validar_y_leer_encabezado(archivo, tamanio_archivo)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                f"Posición {posicion} fuera de rango para un archivo con {cantidad} registros."
            )

        offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO
        archivo.seek(offset)
        archivo.write(_empaquetar_cancion(cancion))


if __name__ == "__main__":
    bib = Biblioteca()
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213)
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    bib.agregar(c1)
    bib.agregar(c12)

    ruta_bin = Path("biblioteca_test.bin")
    guardar_binario(ruta_bin, bib)

    # Actualizamos la posición 1 (Jijiji -> Ji Ji Ji)
    c13 = Cancion(13, "Ji Ji Ji", "Patricio Rey y sus Redonditos de Ricota", "En Directo", "Rock", 1992, 318)
    actualizar_registro(ruta_bin, 1, c13)

    bib_leida = cargar_binario(ruta_bin)
    print("Biblioteca tras actualizar posición 1:", bib_leida.listar())

    if ruta_bin.exists():
        ruta_bin.unlink()

# Teoría:
# El byte donde empieza el registro de posición `k` (0-based) se calcula con la fórmula:
# offset(k) = TAM_ENCABEZADO + k * TAM_REGISTRO = 9 + k * 144
# Esto permite acceder directamente al registro en tiempo constante O(1) mediante `seek` sin necesidad de leer los registros anteriores.