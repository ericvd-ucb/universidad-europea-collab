# BigData: prácticas de Carlos Toledo

Prácticas de la asignatura de Carlos Toledo en el Máster en Big Data de la Universidad Europea de Madrid, publicadas aquí con su permiso.

## El enfoque

Estas prácticas no son ejercicios de programación. Casi todo el código viene escrito y está marcado como «código proporcionado, no se evalúa esta sintaxis». Lo que se evalúa es el **razonamiento sobre los datos**: qué representa una fila (el *grain*), qué afirma una tabla y qué no, qué resumen se puede combinar, qué comparación es válida y qué evidencia sostiene cada conclusión.

Todas siguen el mismo patrón:

- **Predecir antes de ejecutar.** El estudiante escribe su hipótesis o su declaración antes de ver ningún resultado, y después la contrasta.
- **Emitir un veredicto con evidencia.** Cada decisión se expresa con una etiqueta cerrada (por ejemplo PASS / FAIL / UNKNOWN, o ACCEPT / QUALIFY / RECOMPUTE / DO NOT COMPARE) y se defiende con una cifra, un hecho o una línea concreta de la documentación. «No se puede verificar con la evidencia disponible» es una respuesta legítima, siempre que se diga qué evidencia la resolvería.
- **Separar la evidencia proporcionada de la externa.** Lo que demuestran los datos y la documentación del paquete se distingue de lo que añaden una búsqueda, el conocimiento propio o una IA.
- **«La IA puede generar; tú sigues siendo responsable».** Se permite usar IA, pero el estudiante debe entender, comprobar y defender todo lo que entrega, y en varias prácticas tiene que auditar una propuesta hecha por un asistente.

Cada práctica incluye un fichero de instrucciones, un notebook de trabajo con comprobaciones automáticas (✔ / ✘) y una nota de procedencia de los datos (`DATASET_NOTICE.md`) con su origen, qué se ha adaptado y sus huellas SHA-256.

## Prácticas

| Práctica | Pregunta | Datos | Instrucciones | Google Colab |
|---|---|---|---|---|
| PA-02 | **Declara el contrato de ingesta antes de fiarte de la tabla.** Un compañero dice que los datos «están limpios». El estudiante formula afirmaciones comprobables sobre la tabla (qué es una fila, qué significa `..`, si los totales cuadran) y decide para cada una PASS, FAIL o UNKNOWN. | Actividad aérea internacional de Australia, 2009-2025 (BITRE) | [PA-02_INSTRUCTIONS.md](PA-02/student/PA-02_INSTRUCTIONS.md) | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/BigData/PA-02/student/PA-02_student.ipynb) |
| PA-04 | **¿Qué estado debe devolver cada partición?** Un compañero calcula el porcentaje de reseñas `fresh` en cada una de 24 particiones anuales y promedia los porcentajes. El estudiante decide qué resumen debe devolver cada partición para reconstruir bien la respuesta global y demuestra que el procesamiento por partes y la pasada única responden a la misma pregunta. | Reseñas de Rotten Tomatoes 2000-2023, en Parquet particionado por año (solo la columna `fresh` / `rotten`) | [PA-04_INSTRUCTIONS.md](PA-04/student/PA-04_INSTRUCTIONS.md) | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/BigData/PA-04/student/PA-04_student.ipynb) |
| PA-06 | **¿Es válida esta comparación?** Cinco afirmaciones de una dirección con la aritmética correcta. El estudiante decide si cada una se acepta, se matiza, se recalcula o no se debe comparar, y lo defiende citando la documentación del origen y comprobándolo sobre la tabla. | Los mismos datos de BITRE que PA-02, con un extracto de su documentación y cinco gráficos | [PA-06_INSTRUCTIONS.md](PA-06/student/PA-06_INSTRUCTIONS.md) | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/BigData/PA-06/student/PA-06_student.ipynb) |

PA-02 y PA-06 usan el mismo fichero de datos y funcionan bien en secuencia: primero se decide qué significa la tabla y después qué comparaciones admite. PA-04 trabaja con Polars y lectura perezosa (*lazy*) de Parquet; PA-02 y PA-06, con pandas.

## Entorno

Las prácticas están verificadas con Python 3.14, **pandas 3.0.6** y **Polars 1.44.2**, el entorno del curso. Cada notebook avisa si se ejecuta con otra versión. Se han probado también de principio a fin con pandas 2.2 y Polars 1.25 (versiones como las de Colab) y se ejecutan sin errores, aunque algún resultado puede diferir.

**Cambios añadidos para el repositorio** (el resto del material es el original del profesor):

- Cada notebook tiene una primera celda de código marcada «SOLO PARA GOOGLE COLAB» que descarga la carpeta `data/` de la práctica desde GitHub y se sitúa en `student/`, para que las rutas `../data/...` funcionen. En Jupyter o VS Code no hace nada.
- En PA-06, los cinco gráficos se enlazan desde GitHub en lugar de con una ruta relativa, para que también se vean en Colab.

## Datos y atribución

- **BITRE**, *International Airline Activity*, Tabla 1 (PA-02 y PA-06): Bureau of Infrastructure and Transport Research Economics, Gobierno de Australia. Adaptación de formato del libro original, sin cambiar valores.
- **Rotten Tomatoes** (PA-04): selección de una única columna (`reviewState`) y del año, sin textos, nombres ni puntuaciones. El fichero original no incluye autoría ni licencia.

Los detalles de cada conjunto están en los `DATASET_NOTICE.md` de cada práctica.
