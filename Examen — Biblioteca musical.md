# Examen — Biblioteca musical

**Cátedra:** 00184 — Algoritmos y Estructuras de Datos  
**Cuatrimestre:** C2 2026  
**Tema:** Biblioteca musical  
**Lenguaje:** Python 3  
**Puntaje:** 100 puntos. La nota sobre 10 es `puntos / 10`. Se aprueba con 60 puntos.

Cada ejercicio pide una parte práctica (clases, objetos y funciones) y, al final, una pregunta teórica breve. Las excepciones de la consigna van dentro del ejercicio que las necesita: no hay un ejercicio aparte de excepciones.

Entregar un archivo por ejercicio: `ejercicio_01.py` … `ejercicio_10.py`. La respuesta teórica va al final de ese archivo, en comentarios.

## Condiciones

- Se pueden reutilizar las clases de un ejercicio anterior.
- La biblioteca (ejercicio 2) puede guardar las canciones en una `list` de Python.
- La playlist (ejercicio 4) usa `ListaEnlazada`. La pila y la cola se apoyan en esa lista.
- Búsqueda y ordenamiento se escriben a mano. `list.sort`, `sorted` y `bisect` no se toman como resolución de los ejercicios 7 y 8.
- Cada excepción es una clase propia que hereda de `Exception`, con un mensaje que explique el caso. Un `except:` sin tipo no cuenta.
- Los métodos devuelven un valor o lanzan la excepción. Avisar solo con `print` no reemplaza el `return` ni el `raise`.
- Se asume que las versiones no forman ciclos.

## Datos de prueba

| id | titulo | artista | album | genero | anio | duracion_seg |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | De Musica Ligera | Soda Stereo | Cancion Animal | Rock | 1990 | 213 |
| 12 | Jijiji | Patricio Rey y sus Redonditos de Ricota | Un Baion para el Ojo Idiota | Rock | 1988 | 316 |
| 13 | Ji Ji Ji | Patricio Rey y sus Redonditos de Ricota | En Directo | Rock | 1992 | 318 |
| 15 | Alfonsina y el mar | Mercedes Sosa | Mujeres Argentinas | Folklore | 1969 | 298 |
| 16 | Gracias a la Vida | Mercedes Sosa | Hasta la Victoria | Folklore | 1971 | 271 |
| 61 | Gracias a la Vida | Violeta Parra | Las Ultimas Composiciones | Folklore | 1966 | 258 |
| 62 | De Musica Ligera (Unplugged) | Soda Stereo | Comfort y Musica Para Volar | Rock | 1996 | 221 |
| 70 | Ji Ji Ji (Remix) | Patricio Rey y sus Redonditos de Ricota | Remixes | Rock | 2020 | 300 |

La canción 70 está solo en este examen, para que la cadena de versiones tenga dos niveles.

Versiones (`cancion_id` es una versión de `version_de_id`, con un tipo):

| cancion_id | version_de_id | tipo |
| --- | --- | --- |
| 13 | 12 | live |
| 16 | 61 | cover |
| 62 | 1 | live |
| 70 | 13 | remix |

## Puntaje

| Ej. | Qué cubre | Puntos |
| --- | --- | --- |
| 1 | Entidad: Canción | 8 |
| 2 | Catálogo: biblioteca | 8 |
| 3 | Relación recursiva: versiones | 12 |
| 4 | Colección lineal: playlist | 14 |
| 5 | Pila: historial de reproducción | 10 |
| 6 | Cola: up next | 10 |
| 7 | Búsqueda: título, artista, género | 10 |
| 8 | Ordenamiento: año y duración | 10 |
| 9 | Archivo de texto: `canciones.csv` | 9 |
| 10 | Archivo binario: registros de canción | 9 |
| | **Total** | **100** |

---

## Ejercicio 1 — Canción (8 pts)

Definir la clase `Cancion`.

Atributos: `id` (int), `titulo` (str), `artista` (str), `album` (str), `genero` (str), `anio` (int), `duracion_seg` (int).

Métodos:

- `duracion_mmss()` devuelve la duración como `m:ss`. `316` → `"5:16"`, `65` → `"1:05"`, `59` → `"0:59"`.
- `__str__` devuelve `#12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16`.
- `__eq__` compara por `id`.

**Teoría.** La duración se guarda en segundos enteros y `duracion_mmss` la calcula. Explicar en dos oraciones por qué conviene guardarla así y no en un string `"5:16"`.

---

## Ejercicio 2 — Biblioteca (8 pts)

Definir la clase `Biblioteca`, el catálogo de todas las canciones.

- `agregar(cancion)` incorpora una canción.
- `cantidad()` devuelve cuántas hay.
- `obtener(id)` devuelve la canción con ese `id`. Si no está, lanza `CancionNoEncontradaError`.
- `listar()` devuelve una lista de strings, uno por canción, usando `__str__`.
- `__iter__` permite recorrer las canciones con un `for`.

La playlist no vive en esta clase.

**Teoría.** En una o dos oraciones: qué guarda la biblioteca y qué guarda una playlist.

---

## Ejercicio 3 — Versiones (12 pts)

Implementar una función recursiva que lista las versiones derivadas de una canción (cover, live, remix), también las versiones de esas versiones:

```python
def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
```

`versiones` es una lista de tuplas `(cancion_id, version_de_id, tipo)`.

- Caso base: nadie es versión de esta canción. El resultado es la lista vacía.
- Si hay varias versiones directas, recorrerlas de menor a mayor `cancion_id`.
- Cada llamada recursiva trae lo derivado de esa versión. El resultado es preorden: primero la versión directa `(titulo, tipo)`, después lo que cuelga de ella.
- Si `cancion_id` no está en la biblioteca, lanzar `CancionNoEncontradaError`.

Con los datos de prueba, Jijiji (12) tiene el vivo Ji Ji Ji (13) y, debajo, el remix (70). Gracias a la Vida de Violeta Parra (61) tiene el cover de Mercedes Sosa (16).

**Teoría.** Escribir el caso base y la secuencia de llamadas de `versiones_de(..., 12)`, indicando qué lista devuelve cada llamada al volver.

---

## Ejercicio 4 — Playlist sobre lista enlazada (14 pts)

Implementar, con nodos propios:

```python
class Nodo:
    def __init__(self, dato, siguiente=None): ...

class ListaEnlazada:
    def esta_vacia(self) -> bool: ...
    def tamanio(self) -> int: ...
    def insertar_al_inicio(self, dato): ...
    def insertar_al_final(self, dato): ...
    def quitar_primero(self): ...
    def __iter__(self): ...
```

`quitar_primero` devuelve el dato que estaba al frente y lo saca de la lista. El iterador recorre desde el primero hasta el último y termina con `StopIteration` (o con `yield`).

Definir `Playlist`, que guarda canciones en una `ListaEnlazada`. No tiene tope de cantidad.

- `agregar(cancion)` la inserta al final.
- `quitar(id)` saca la canción con ese `id`. Si no está en la playlist, lanza `CancionNoEncontradaError`.
- `listar()` devuelve los `__str__` recorriendo el iterador de la lista.
- `duracion_total()` devuelve la suma de `duracion_seg` recorriendo el iterador. Playlist vacía: `0`.

**Teoría.** La lista solo guarda una referencia al primer nodo. ¿Cuántos nodos se recorren para insertar al final cuando ya hay `n` elementos?

---

## Ejercicio 5 — Historial de reproducción (10 pts)

Implementar `Pila` sobre `ListaEnlazada` (apilar y desapilar en el extremo del primer nodo):

- `apilar(dato)`
- `desapilar()` devuelve el tope. Si está vacía, lanza `PilaVaciaError`.
- `ver_tope()` devuelve el tope y lo deja en la pila. Si está vacía, lanza `PilaVaciaError`.
- `esta_vacia()`

Definir `HistorialReproduccion`, que usa una `Pila` de canciones:

- `registrar(cancion)` apila lo que acaba de sonar.
- `anterior()` desapila y devuelve la canción a la que se vuelve.
- `ultima()` devuelve la última canción reproducida, sin sacarla.

**Teoría.** Se registran, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `anterior()`? ¿Por qué?

---

## Ejercicio 6 — Cola de reproducción (10 pts)

Implementar `Cola` sobre `ListaEnlazada`:

- `encolar(dato)` agrega al final.
- `desencolar()` saca y devuelve el primero. Si está vacía, lanza `ColaVaciaError`.
- `ver_frente()` devuelve el primero y lo deja en la cola. Si está vacía, lanza `ColaVaciaError`.
- `esta_vacia()`

Definir `ColaReproduccion` (la cola “up next”), que usa una `Cola` de canciones:

- `encolar_cancion(cancion)`
- `siguiente()` devuelve la canción que toca ahora.
- `que_sigue()` devuelve la canción del frente, sin sacarla.

**Teoría.** Se encolan, en este orden, Jijiji, Alfonsina y el mar, y De Música Ligera. ¿Qué devuelve el primer `siguiente()`? ¿En qué se diferencia este orden del de la pila del ejercicio 5?

---

## Ejercicio 7 — Búsqueda (10 pts)

Las funciones reciben una `list` de `Cancion`. Se implementan a mano.

```python
def busqueda_lineal(canciones, campo, valor) -> list: ...
def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion: ...
```

- `busqueda_lineal`: `campo` es `"titulo"`, `"artista"` o `"genero"`. Devuelve todas las canciones cuyo campo es igual a `valor`, en el orden original. Si no hay ninguna, lista vacía. `"Rock"` y `"Soda Stereo"` tienen que poder buscarse por este camino.
- Binaria por `titulo`, sobre una lista ya ordenada alfabéticamente por `titulo`. Si el título no está, `CancionNoEncontradaError`. Si hubiera dos canciones con el mismo título, devuelve la primera que encuentre la búsqueda.

**Teoría.** ¿Por qué `busqueda_binaria_por_titulo` pide la lista ordenada por título? ¿Qué complejidad tiene sobre `n` canciones, y qué complejidad tiene la búsqueda lineal por artista?

---

## Ejercicio 8 — Ordenamiento (10 pts)

Ordenar in-place una `list` de `Cancion` y devolver esa misma lista. Dos algoritmos distintos, escritos a mano:

```python
def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""

def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor."""
```

Con los datos de prueba, el remix (2020) queda antes que el unplugged (1996) al ordenar por año, y De Música Ligera (213 s) queda antes que Jijiji (316 s) al ordenar por duración.

**Teoría.** Dar la complejidad de peor caso de cada algoritmo. ¿Cuál de los dos conserva el orden relativo de dos canciones con la misma clave?

---

## Ejercicio 9 — `canciones.csv` (9 pts)

Persistir la biblioteca en CSV, UTF-8, separador coma, con encabezado:

```text
id,titulo,artista,album,genero,anio,duracion_seg
```

```python
def guardar_canciones_csv(ruta, biblioteca): ...
def cargar_canciones_csv(ruta) -> Biblioteca: ...
```

`cargar_canciones_csv` rearma objetos `Cancion`. Lanza `ArchivoInvalidoError` si el archivo no existe, si el encabezado no es el pedido o si una fila tiene menos columnas.

Las versiones quedan fuera de este archivo.

**Teoría.** Para leer la canción de la fila 50, ¿hay que recorrer las filas anteriores? Explicar en una oración por qué, a partir de cómo está guardado el CSV.

---

## Ejercicio 10 — Registros binarios (9 pts)

Archivo binario de registros de longitud fija, con `struct` y formato estándar (`=`, sin padding de alineación).

Encabezado, 9 bytes: magia `4s` con `b"AYED"`, tema `1s` con `b"M"`, cantidad `I`.

Registro, 144 bytes:

| Campo | Formato |
| --- | --- |
| id | `I` |
| titulo | `40s` |
| artista | `40s` |
| album | `40s` |
| genero | `16s` |
| anio | `H` |
| duracion_seg | `H` |

Las cadenas van en UTF-8, recortadas al ancho y completadas con `\0`. Al leer, se corta en el primer `\0`. El artista más largo de los datos de prueba entra en 40 bytes.

```python
def guardar_binario(ruta, biblioteca): ...
def cargar_binario(ruta) -> Biblioteca: ...
def actualizar_registro(ruta, posicion, cancion): ...
```

`posicion` es 0-based. `actualizar_registro` escribe un solo registro en su lugar (`seek`) y no reescribe el resto del archivo. Lanza `ArchivoInvalidoError` si la magia no es `AYED`, si el tema no es `M`, si el archivo no cierra justo en `9 + cantidad * 144` bytes, o si `posicion` está fuera de rango.

**Teoría.** Escribir la fórmula del byte donde empieza el registro de posición `k`. Usar el tamaño del encabezado y el tamaño del registro.
