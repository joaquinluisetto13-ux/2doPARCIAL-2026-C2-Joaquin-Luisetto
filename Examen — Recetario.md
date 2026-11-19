# Examen — Recetario

**Cátedra:** 00184 — Algoritmos y Estructuras de Datos  
**Cuatrimestre:** C2 2026  
**Tema:** Recetario  
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

Recetas:

| id | nombre | tiempo_min | dificultad | categoria |
| --- | --- | --- | --- | --- |
| 1 | Chimichurri | 15 | baja | salsa |
| 2 | Salsa criolla | 20 | baja | salsa |
| 3 | Sofrito | 25 | baja | base |
| 5 | Masa de empanadas | 90 | media | base |
| 9 | Asado | 180 | media | principal |
| 10 | Empanadas de carne | 150 | media | principal |
| 12 | Locro | 150 | alta | principal |

Sub-recetas (`receta_id` usa `subreceta_id`):

| receta_id | subreceta_id |
| --- | --- |
| 9 | 1 |
| 9 | 2 |
| 10 | 3 |
| 10 | 5 |
| 12 | 3 |

Ingredientes:

| receta_id | nombre | cantidad | unidad |
| --- | --- | --- | --- |
| 1 | perejil | 50 | g |
| 1 | ajo | 4 | dientes |
| 2 | tomate | 3 | u |
| 2 | cebolla | 1 | u |
| 3 | cebolla | 2 | u |
| 3 | ajo | 2 | dientes |
| 5 | harina | 500 | g |
| 5 | agua | 150 | ml |
| 9 | vacio | 1200 | g |
| 9 | chorizo | 4 | u |
| 10 | carne picada | 500 | g |
| 12 | maiz blanco | 300 | g |

La dificultad se ordena `baja` < `media` < `alta`.

Los días del menú son exactamente estas cadenas: `lunes`, `martes`, `miercoles`, `jueves`, `viernes`, `sabado`, `domingo`.

## Dónde va cada excepción

| Excepción | Ejercicio |
| --- | --- |
| `RecetaNoEncontrada` | 2 y 4 |
| `SubrecetaFaltanteError` | 3 |
| `IngredienteFaltanteError` | 3 |
| `PilaVaciaError` | 5 |
| `ColaVaciaError` | 6 |
| `ArchivoInvalidoError` | 9 y 10 |

---

## Ejercicio 1 — Entidad del catálogo (8 pts)

Definir la clase `Receta`.

Constructor, en este orden: `id`, `nombre`, `tiempo_min`, `dificultad`, `categoria`.

- `__str__` devuelve `"#9 Asado — 180 min, media, principal"`.
- `__eq__` es verdadero cuando el otro objeto es una `Receta` con el mismo `id`, aunque el resto de los atributos difiera.

### Pregunta teórica

¿Cuál atributo es la identidad de la receta y cuál es estado? ¿La identidad debería poder cambiar después de construido el objeto? Respondé sí o no, en una oración.

---

## Ejercicio 2 — Catálogo (8 pts)

Definir la clase `LibroRecetas` y la excepción `RecetaNoEncontrada`.

En este ejercicio el libro puede guardarse en un `list` de Python. A partir del ejercicio 4 la colección principal del dominio es una lista enlazada propia.

- `agregar(receta)`: si el `id` ya estaba, reemplaza ese objeto.
- `obtener(id)`: devuelve la `Receta`. Si no está, lanza `RecetaNoEncontrada`.
- `listar()`: devuelve las recetas en el orden en que quedaron cargadas.
- `cantidad()`: devuelve cuántas hay.

### Pregunta teórica

`obtener` lanza una excepción cuando el id no está, en lugar de devolver `None`. ¿Qué gana quien llama al método? Una oración.

---

## Ejercicio 3 — Relación recursiva (12 pts)

Definir `ingredientes_totales(receta_id, libro, subrecetas, ingredientes)`.

- `subrecetas` es una lista de pares `(receta_id, subreceta_id)`.
- `ingredientes` es una lista de tuplas `(receta_id, nombre, cantidad, unidad)`.
- La función devuelve una lista de tuplas `(nombre, cantidad, unidad)`.

Orden: primero los ingredientes propios de la receta, en el orden de la tabla; después, cada sub-receta en el orden de la tabla, con el mismo criterio, antes de pasar a la sub-receta hermana.

Con los datos de este examen, `ingredientes_totales(9, ...)` devuelve:

1. `("vacio", 1200, "g")`
2. `("chorizo", 4, "u")`
3. `("perejil", 50, "g")`
4. `("ajo", 4, "dientes")`
5. `("tomate", 3, "u")`
6. `("cebolla", 1, "u")`

- Caso base: la receta no tiene sub-recetas. Se devuelven solo sus ingredientes (puede ser una lista vacía).
- Si `receta_id` no está en el libro, lanza `RecetaNoEncontrada`.
- Si un `subreceta_id` no está en el libro, lanza `SubrecetaFaltanteError`.
- Si una fila de ingredientes de una receta que se está expandiendo tiene el nombre vacío, lanza `IngredienteFaltanteError`.

### Pregunta teórica

Escribí la traza de `ingredientes_totales(9)` con los datos del enunciado. Alcanza con el `receta_id` de cada llamado y el orden en que entran, hasta el caso base.

---

## Ejercicio 4 — Colección lineal principal (14 pts)

Definir `Nodo`, `ListaEnlazada` y `MenuSemanal`.

`Nodo` guarda `dato` y `siguiente`. `siguiente` arranca en `None`.

`ListaEnlazada` se implementa con nodos. No usa un `list` para guardar los datos.

- `esta_vacia()`, `tamanio()`
- `insertar_al_final(dato)`, `insertar_al_inicio(dato)`
- `quitar_primero()`: saca el primer nodo y devuelve su dato. Pila y cola se apoyan en este método.
- `eliminar_donde(condicion)`: `condicion` es una función de un argumento. Quita el primer nodo cuyo dato la cumple. Si ninguno la cumple, no cambia la lista y devuelve `False`. Si lo quita, devuelve `True`.
- `__iter__`: un `for` recorre los datos en orden. Vale un generador con `yield` o una clase con `__next__` y `StopIteration`.

`MenuSemanal` guarda pares `(dia, receta)` en una `ListaEnlazada`.

- `agregar(dia, receta)`: si ese día ya tenía una receta, la reemplaza. Si `dia` no es uno de los siete nombres, lanza `ValueError`.
- `quitar(dia)`: saca la receta de ese día. Si ese día no tiene receta, lanza `RecetaNoEncontrada`.
- `receta_de(dia)`: devuelve la `Receta`. Si el día no tiene, lanza `RecetaNoEncontrada`.
- `__iter__` recorre los pares `(dia, receta)` en el orden en que se agregaron, usando el iterador de la lista enlazada.

### Pregunta teórica

Para borrar el último nodo hace falta conocer el penúltimo. En una lista enlazada simple, ¿dónde está guardada esa referencia? Una o dos oraciones.

---

## Ejercicio 5 — Pila (10 pts)

Definir `Pila` y `HistorialCocinado`.

`Pila` se implementa sobre `ListaEnlazada`.

- `apilar(dato)`, `desapilar()`, `ver_tope()`, `esta_vacia()`
- `desapilar` y `ver_tope` sobre una pila vacía lanzan `PilaVaciaError`.

`HistorialCocinado` usa una `Pila` de `Receta`.

- `cocinar(receta)`: apila la receta.
- `deshacer()`: devuelve la última receta cocinada y la saca. Si no hay ninguna, lanza `PilaVaciaError`.
- `ultima()`: devuelve la última sin sacarla. Si no hay, lanza `PilaVaciaError`.

### Pregunta teórica

Se apilan `"A"`, después `"B"`, después `"C"`. Se desapila una vez. ¿Qué queda en el tope? ¿Cómo se llama esta disciplina?

---

## Ejercicio 6 — Cola (10 pts)

Definir `Cola` y `ColaPreparacion`.

`Cola` se implementa sobre `ListaEnlazada`.

- `encolar(dato)`, `desencolar()`, `ver_frente()`, `esta_vacia()`
- `desencolar` y `ver_frente` sobre una cola vacía lanzan `ColaVaciaError`.

`ColaPreparacion` usa una `Cola` de `Receta`.

- `encolar(receta)`
- `siguiente()`: devuelve la receta que entró primero y la saca. Si no hay ninguna, lanza `ColaVaciaError`.
- `proxima()`: la muestra sin sacarla. Si no hay ninguna, lanza `ColaVaciaError`.

### Pregunta teórica

Se encolan A, después B, después C. El primer `desencolar` devuelve A. ¿Por qué no devuelve C?

---

## Ejercicio 7 — Búsqueda (10 pts)

Definir `busqueda_lineal(recetas, ingredientes, campo, valor)` y `busqueda_binaria(recetas, campo, valor)`.

Reciben y devuelven objetos `Receta`. No convierten el libro a diccionarios.

`ingredientes` es la lista de tuplas `(receta_id, nombre, cantidad, unidad)`.

`busqueda_lineal` devuelve la lista de coincidencias, en el orden de `recetas`. Si no hay ninguna, devuelve `[]`.

- `campo == "nombre"`: igualdad con `nombre`.
- `campo == "categoria"`: igualdad con `categoria`.
- `campo == "ingrediente"`: la receta tiene una fila de ingredientes con ese `nombre`.

`busqueda_binaria` busca por `campo == "nombre"` y devuelve una `Receta` o `None`. El llamado es válido cuando `recetas` ya está ordenada de menor a mayor por nombre. Implementar la búsqueda a la mitad, con corte explícito. No recorrer toda la lista.

### Pregunta teórica

La búsqueda binaria por nombre pide la lista ordenada por nombre. Si la lista está ordenada por tiempo, ¿el resultado es confiable? Respondé sí o no, y por qué, en una oración.

---

## Ejercicio 8 — Ordenamiento (10 pts)

Definir `ordenar_seleccion(recetas, campo, descendente)` y `ordenar_insercion(recetas, campo, descendente)`.

Las dos modifican el orden de la lista y devuelven esa misma lista. `campo` es `"tiempo"` o `"dificultad"`. Con `descendente=False` el orden es de menor a mayor. Para dificultad el orden es `baja` < `media` < `alta`.

Tienen que poder usarse así:

- selección por `tiempo`, ascendente
- inserción por `dificultad`, ascendente

### Pregunta teórica

De los dos algoritmos, ¿cuál es estable? Definí estable en una oración.

---

## Ejercicio 9 — Archivo de texto (9 pts)

Definir estas cuatro funciones:

- `guardar_recetas_csv(ruta, libro)`
- `cargar_recetas_csv(ruta)` → `LibroRecetas`
- `guardar_ingredientes_csv(ruta, ingredientes)`
- `cargar_ingredientes_csv(ruta)` → lista de tuplas `(receta_id, nombre, cantidad, unidad)`

CSV con encabezado, UTF-8, separador coma.

Recetas: `id,nombre,tiempo_min,dificultad,categoria`.

Ingredientes: `receta_id,nombre,cantidad,unidad`.

Si un archivo no tiene encabezado, si una fila no tiene la cantidad de columnas de su tabla, o si un número no se puede convertir, lanza `ArchivoInvalidoError`.

### Pregunta teórica

Para leer el registro número 10 de `recetas.csv`, ¿hace falta leer los anteriores? Respondé sí o no, y decí si el acceso es secuencial o directo.

---

## Ejercicio 10 — Archivo binario (9 pts)

Definir `guardar_binario(ruta, libro)`, `cargar_binario(ruta)` y `actualizar_registro(ruta, posicion, receta)`.

Usar `struct` con formato estándar (`<`, sin padding). Las cadenas van en UTF-8, recortadas o rellenadas con `\0` al ancho del campo.

Encabezado, 9 bytes: `"<4scI"`

| Campo | Formato | Valor |
| --- | --- | --- |
| magia | `4s` | `b"AYED"` |
| tema | `c` | `b"R"` |
| cantidad | `I` | cantidad de recetas |

Registro, 62 bytes: `"<I32sH8s16s"`

| Campo | Formato |
| --- | --- |
| id | `I` |
| nombre | `32s` |
| tiempo_min | `H` |
| dificultad | `8s` |
| categoria | `16s` |

Los ingredientes no entran en este binario.

`actualizar_registro` abre el archivo en lectura-escritura, se posiciona en el registro `posicion` (desde 0) y escribe solo ese registro. La cantidad del encabezado no cambia.

- Magia distinta de `b"AYED"`, archivo más corto que el encabezado, o `posicion` fuera de rango: `ArchivoInvalidoError`.

### Pregunta teórica

`actualizar_registro` cambia una receta sin reescribir el archivo entero. ¿Qué dato del layout permite calcular el byte donde empieza ese registro?
