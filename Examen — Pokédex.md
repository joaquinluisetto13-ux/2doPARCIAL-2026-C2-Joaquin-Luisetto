# Examen — Pokédex

**Cátedra:** 00184 — Algoritmos y Estructuras de Datos  
**Cuatrimestre:** C2 2026  
**Tema:** Pokédex  
**Lenguaje:** Python 3  
**Puntaje:** 100 puntos




Cada ejercicio corresponde a una fila del mapa del dominio de la consigna (sección 2). Las excepciones no tienen ejercicio propio: se implementan en el ejercicio donde el dominio las necesita.

## Condiciones

- Un archivo por ejercicio: `ejercicio_01.py` … `ejercicio_10.py`. Los ejercicios posteriores pueden importar los anteriores.
- La pregunta teórica se responde en el mismo archivo, en un comentario que empiece con `# TEORIA`.
- Biblioteca estándar de Python. En búsqueda y ordenamiento no se aceptan `sorted`, `list.sort` ni `bisect`.
- `Pila` y `Cola` se apoyan en `ListaEnlazada`. Un `list` de Python como almacenamiento de esos TAD no cumple el ejercicio.
- Cada excepción propia hereda de `Exception`. El mensaje puede ser breve. No se usa `except:` sin tipo.
- Las clases de un ejercicio se reutilizan en los siguientes. No hace falta redefinirlas.

## Datos de este examen

Pokédex:

| id | nombre | tipo1 | tipo2 | hp | ataque | defensa | velocidad | generacion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bulbasaur | Planta | Veneno | 45 | 49 | 49 | 45 | 1 |
| 2 | Ivysaur | Planta | Veneno | 60 | 62 | 63 | 60 | 1 |
| 3 | Venusaur | Planta | Veneno | 80 | 82 | 83 | 80 | 1 |
| 4 | Charmander | Fuego | | 39 | 52 | 43 | 65 | 1 |
| 5 | Charmeleon | Fuego | | 58 | 64 | 58 | 80 | 1 |
| 6 | Charizard | Fuego | Volador | 78 | 84 | 78 | 100 | 1 |
| 25 | Pikachu | Electrico | | 35 | 55 | 40 | 90 | 1 |
| 26 | Raichu | Electrico | | 60 | 90 | 55 | 110 | 1 |
| 133 | Eevee | Normal | | 55 | 55 | 50 | 55 | 1 |
| 134 | Vaporeon | Agua | | 130 | 65 | 60 | 65 | 1 |
| 135 | Jolteon | Electrico | | 65 | 65 | 60 | 130 | 1 |
| 136 | Flareon | Fuego | | 65 | 130 | 60 | 65 | 1 |

Evoluciones (`origen_id` evoluciona a `destino_id`):

| origen_id | destino_id |
| --- | --- |
| 1 | 2 |
| 2 | 3 |
| 4 | 5 |
| 5 | 6 |
| 25 | 26 |
| 133 | 134 |
| 133 | 135 |
| 133 | 136 |

## Dónde va cada excepción

| Excepción | Ejercicio |
| --- | --- |
| `PokemonNoEncontrado` | 2, 3 y 4 |
| `EquipoLlenoError` | 4 |
| `PilaVaciaError` | 5 |
| `ColaVaciaError` | 6 |
| `ArchivoInvalidoError` | 9 y 10 |

---

## Ejercicio 1 — Entidad del catálogo (8 pts)

Definir la clase `Pokemon`.

Constructor, en este orden: `id`, `nombre`, `tipo1`, `tipo2`, `hp`, `ataque`, `defensa`, `velocidad`, `generacion`. `tipo2` puede ser `""`.

- `__str__` devuelve `"#1 Bulbasaur (Planta/Veneno)"`. Si `tipo2` está vacío, `"#4 Charmander (Fuego)"`.
- `__eq__` es verdadero cuando el otro objeto es un `Pokemon` con el mismo `id`, aunque el resto de los atributos difiera.

### Pregunta teórica

¿Cuál atributo es la identidad del Pokémon y cuál es estado? ¿La identidad debería poder cambiar después de construido el objeto? Respondé sí o no, en una oración.

---

## Ejercicio 2 — Catálogo (8 pts)

Definir la clase `Pokedex` y la excepción `PokemonNoEncontrado`.

En este ejercicio el catálogo puede guardarse en un `list` de Python. A partir del ejercicio 4 la colección principal del dominio es una lista enlazada propia.

- `agregar(pokemon)`: si el `id` ya estaba, reemplaza ese objeto.
- `obtener(id)`: devuelve el `Pokemon`. Si no está, lanza `PokemonNoEncontrado`.
- `listar()`: devuelve los Pokémon en el orden en que quedaron cargados.
- `cantidad()`: devuelve cuántos hay.

### Pregunta teórica

`obtener` lanza una excepción cuando el id no está, en lugar de devolver `None`. ¿Qué gana quien llama al método? Una oración.

---

## Ejercicio 3 — Relación recursiva (12 pts)

Definir `descendientes(origen_id, pokedex, aristas)`.

`aristas` es una lista de pares `(origen_id, destino_id)`. La función devuelve la lista de ids alcanzables desde `origen_id`, sin incluirlo, en profundidad: cada destino se agrega y enseguida se expanden sus propios destinos, antes de pasar al siguiente hermano. El orden entre hermanos es el de la tabla.

- Caso base: el id no tiene destinos. El resultado de ese llamado es `[]`.
- `descendientes(1, ...)` devuelve `[2, 3]`.
- `descendientes(133, ...)` devuelve `[134, 135, 136]`.
- `descendientes(6, ...)` devuelve `[]`.
- Si `origen_id` no está en la Pokédex, o un destino de la tabla no está en la Pokédex, lanza `PokemonNoEncontrado`.

### Pregunta teórica

Escribí la traza de `descendientes(4)` con las aristas `(4, 5)` y `(5, 6)`. Alcanza con el argumento de cada llamado y el orden en que entran, hasta el caso base.

---

## Ejercicio 4 — Colección lineal principal (14 pts)

Definir `Nodo`, `ListaEnlazada` y `Equipo`.

`Nodo` guarda `dato` y `siguiente`. `siguiente` arranca en `None`.

`ListaEnlazada` se implementa con nodos. No usa un `list` para guardar los datos.

- `esta_vacia()`, `tamanio()`
- `insertar_al_final(dato)`, `insertar_al_inicio(dato)`
- `quitar_primero()`: saca el primer nodo y devuelve su dato. Pila y cola se apoyan en este método.
- `eliminar(id)`: quita el primer nodo cuyo `dato.id` sea `id`. Si no está, no cambia la lista y devuelve `False`. Si lo quita, devuelve `True`.
- `buscar(id)`: devuelve el dato o `None`.
- `__iter__`: un `for` recorre los datos en orden. Vale un generador con `yield` o una clase con `__next__` y `StopIteration`.

`Equipo` guarda los Pokémon en una `ListaEnlazada`. El máximo es 6.

- `agregar(pokemon)`: lo inserta al final. El séptimo intento lanza `EquipoLlenoError` y el equipo sigue con 6.
- `quitar(id)`: lo saca. Si ese id no está en el equipo, lanza `PokemonNoEncontrado`.
- `cantidad()`
- `__iter__` recorre el equipo usando el iterador de la lista enlazada.

### Pregunta teórica

Para borrar el último nodo hace falta conocer el penúltimo. En una lista enlazada simple, ¿dónde está guardada esa referencia? Una o dos oraciones.

---

## Ejercicio 5 — Pila (10 pts)

Definir `Pila` y `HistorialAcciones`.

`Pila` se implementa sobre `ListaEnlazada`.

- `apilar(dato)`, `desapilar()`, `ver_tope()`, `esta_vacia()`
- `desapilar` y `ver_tope` sobre una pila vacía lanzan `PilaVaciaError`.

`HistorialAcciones` usa una `Pila` de strings. Cada acción es un texto, por ejemplo `"agregar:25"`.

- `registrar(accion)`
- `deshacer()`: devuelve la última acción y la saca. Si no hay acciones, lanza `PilaVaciaError`.
- `ultima()`: devuelve la última acción sin sacarla. Si no hay, lanza `PilaVaciaError`.

### Pregunta teórica

Se apilan `"A"`, después `"B"`, después `"C"`. Se desapila una vez. ¿Qué queda en el tope? ¿Cómo se llama esta disciplina?

---

## Ejercicio 6 — Cola (10 pts)

Definir `Cola` y `ColaTurnos`.

`Cola` se implementa sobre `ListaEnlazada`.

- `encolar(dato)`, `desencolar()`, `ver_frente()`, `esta_vacia()`
- `desencolar` y `ver_frente` sobre una cola vacía lanzan `ColaVaciaError`.

`ColaTurnos` usa una `Cola` de `Pokemon`.

- `encolar(pokemon)`
- `siguiente()`: devuelve el Pokémon que espera hace más tiempo y lo saca. Si no hay nadie, lanza `ColaVaciaError`.
- `proximo()`: lo muestra sin sacarlo. Si no hay nadie, lanza `ColaVaciaError`.

### Pregunta teórica

Se encolan A, después B, después C. El primer `desencolar` devuelve A. ¿Por qué no devuelve C?

---

## Ejercicio 7 — Búsqueda (10 pts)

Definir `busqueda_lineal(pokemones, campo, valor)` y `busqueda_binaria(pokemones, campo, valor)`.

Reciben una lista de objetos `Pokemon` y devuelven objetos `Pokemon`. No convierten el catálogo a diccionarios.

`busqueda_lineal` devuelve la lista de coincidencias, en el orden recibido. Si no hay ninguna, devuelve `[]`.

- `campo == "nombre"`: igualdad con `nombre`.
- `campo == "tipo"`: coincide `tipo1` o `tipo2`.
- `campo == "nro"`: igualdad con `id`.

`busqueda_binaria` busca por igualdad y devuelve un `Pokemon` o `None`. El llamado es válido cuando la lista ya está ordenada de menor a mayor por `campo`. Implementar la búsqueda a la mitad, con corte explícito. No recorrer toda la lista.

`campo` en la binaria es `"nombre"` o `"nro"`.

### Pregunta teórica

La búsqueda binaria por nombre pide la lista ordenada por nombre. Si la lista está ordenada por ataque, ¿el resultado es confiable? Respondé sí o no, y por qué, en una oración.

---

## Ejercicio 8 — Ordenamiento (10 pts)

Definir `ordenar_seleccion(pokemones, campo, descendente)` y `ordenar_insercion(pokemones, campo, descendente)`.

Las dos modifican el orden de la lista y devuelven esa misma lista. `campo` es `"ataque"`, `"velocidad"` o `"nro"`. Con `descendente=False` el orden es de menor a mayor.

Tienen que poder usarse así:

- selección por `ataque`, descendente
- inserción por `velocidad`, ascendente

### Pregunta teórica

De los dos algoritmos, ¿cuál es estable? Definí estable en una oración.

---

## Ejercicio 9 — Archivo de texto (9 pts)

Definir `guardar_csv(ruta, pokedex)` y `cargar_csv(ruta)`.

El archivo es CSV con encabezado, codificación UTF-8 y separador coma. Columnas, en este orden: `id,nombre,tipo1,tipo2,hp,ataque,defensa,velocidad,generacion`.

- `guardar_csv` escribe todos los Pokémon de la Pokédex.
- `cargar_csv` devuelve una `Pokedex` con objetos `Pokemon`.
- Si el archivo no tiene encabezado, si una fila no tiene 9 columnas, o si un número no se puede convertir, lanza `ArchivoInvalidoError`.

### Pregunta teórica

Para leer el registro número 10 de este CSV, ¿hace falta leer los anteriores? Respondé sí o no, y decí si el acceso es secuencial o directo.

---

## Ejercicio 10 — Archivo binario (9 pts)

Definir `guardar_binario(ruta, pokedex)`, `cargar_binario(ruta)` y `actualizar_registro(ruta, posicion, pokemon)`.

Usar `struct` con formato estándar (`<`, sin padding). Las cadenas van en UTF-8, recortadas o rellenadas con `\0` al ancho del campo.

Encabezado, 9 bytes: `"<4scI"`

| Campo | Formato | Valor |
| --- | --- | --- |
| magia | `4s` | `b"AYED"` |
| tema | `c` | `b"P"` |
| cantidad | `I` | cantidad de Pokémon |

Registro, 56 bytes: `"<I20s12s12s4H"`

| Campo | Formato |
| --- | --- |
| id | `I` |
| nombre | `20s` |
| tipo1 | `12s` |
| tipo2 | `12s` |
| hp, ataque, defensa, velocidad | cuatro `H` |

`generacion` no se guarda en el binario de este examen. Al cargar, usar `generacion=1`.

`actualizar_registro` abre el archivo en lectura-escritura, se posiciona en el registro `posicion` (desde 0) y escribe solo ese registro. La cantidad del encabezado no cambia.

- Magia distinta de `b"AYED"`, archivo más corto que el encabezado, o `posicion` fuera de rango: `ArchivoInvalidoError`.

### Pregunta teórica

`actualizar_registro` cambia un Pokémon sin reescribir el archivo entero. ¿Qué dato del layout permite calcular el byte donde empieza ese registro?
