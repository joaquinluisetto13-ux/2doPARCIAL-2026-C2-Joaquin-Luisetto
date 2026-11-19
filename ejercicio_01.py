class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg

    def duracion_mmss(self) -> str:
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self) -> str:
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cancion):
            return False
        return self.id == other.id


if __name__ == "__main__":
    # Pruebas rápidas con los datos del enunciado
    c12 = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    c_test1 = Cancion(99, "Prueba 1", "Artista", "Album", "Rock", 2000, 65)
    c_test2 = Cancion(100, "Prueba 2", "Artista", "Album", "Rock", 2000, 59)

    print(c12)                  # #12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16
    print(c_test1.duracion_mmss())  # 1:05
    print(c_test2.duracion_mmss())  # 0:59
    print(c12 == Cancion(12, "Otro titulo", "Otro", "Otro", "Pop", 2020, 100))  # True

# Teoría:
# Guardar la duración como un entero en segundos permite realizar operaciones aritméticas (como sumar tiempos totales de una playlist) y comparaciones de ordenamiento de manera directa y eficiente sin tener que parsear texto.
# Además, evita inconsistencias de formato o errores de validación en los datos almacenados, delegando la representación visual ("m:ss") exclusivamente al momento de mostrarla.