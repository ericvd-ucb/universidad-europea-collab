# PA-06 · ¿Es válida esta comparación?

**Clase 5 · Unidad 3 — Calidad de datos y análisis exploratorio**

## Propósito

La dirección de una aerolínea consultora presenta **cinco afirmaciones** sobre el tráfico aéreo internacional de Australia (BITRE, enero de 2009 – noviembre de 2025). **En las cinco, la aritmética es correcta**: cada cifra sale de la tabla. Tu trabajo no es repetir el cálculo, sino decidir **si cada afirmación puede mantenerse tal como está**, eligiendo **una de cuatro etiquetas** (`ACCEPT`, `QUALIFY`, `RECOMPUTE`, `DO NOT COMPARE`) y defendiéndola con **una línea concreta de la documentación** del libro de origen y con una comprobación sobre la tabla.

En esta actividad **no predices, no descompones series, no buscas causas, no mides significación estadística y no necesitas saber de aviación** más allá del glosario del notebook. Python (pandas) es un instrumento para obtener evidencia; lo que se trabaja es **cómo se produjo cada serie** y **si lo documentado afecta a lo que se compara**.

## Conocimientos previos esperados

Lo visto hasta la clase 5: granularidad de una tabla (qué es una fila), calidad de datos, exploración con tablas y gráficos, y lectura de documentación. **No hace falta recordar sintaxis de pandas.** Casi todo el código viene escrito y está marcado como **«código proporcionado — no se evalúa esta sintaxis»**: no tienes que escribirlo ni memorizarlo, pero sí **entender qué consigue, si el resultado es válido y qué significa**. Escribes **etiquetas, identificadores de la documentación, palabras, meses, listas y frases cortas**.

## Ficheros que se te entregan

| Ruta | Qué es |
|---|---|
| `student/PA-06_student.ipynb` | El notebook de trabajo (ábrelo desde la carpeta `student/`); incluye un *glosario elaborado para esta actividad* (no es documentación original del conjunto de datos) |
| `data/international_airline_activity_2009-01_2025-11.csv` | La tabla: una fila por mes × aerolínea × país del puerto |
| `data/figuras/afirmacion_1.png` … `afirmacion_5.png` | Un gráfico por afirmación |
| `data/docs/EXTRACTO_DOCUMENTACION.md` | Extracto de la documentación del libro de origen: copia literal en inglés, con un ID por bloque (≈ 3 páginas) |
| `data/DATASET_NOTICE.md` | Procedencia, qué se ha seleccionado y qué no se ha tocado |

## Entorno

Python 3.14 y **pandas 3.0.6** (el entorno del curso). Esta actividad se ha verificado con esa versión; con otras, algunos resultados pueden diferir y el notebook te avisará. Los gráficos son imágenes ya generadas: no necesitas ninguna librería de dibujo.

## Tiempo

**Núcleo de clase: ≈ 27 minutos** (partes 0 a 6 y la puesta en común). Es una referencia de diseño, no una medición.

## Qué debe estar hecho al terminar la clase

1. Tu **primera impresión** de cada afirmación (solo con cifra y gráfico), escrita **antes** de leer la documentación.
2. El **mes** en el que ves cambiar cada serie (o «ninguno»).
3. Tu **decisión** sobre cada afirmación: etiqueta, línea(s) de la documentación en las que te apoyas, unidad a la que se refiere esa línea y una frase de defensa. Tu lectura de la columna `Year`.
4. Las **recomputaciones** que tu decisión exija (una regla de unión de nombres; una lista de meses comparables) y su comprobación.
5. Tu **balance**: una frase.

La **puesta en común** se hace en clase aunque no hayas terminado el código.

## Qué puedes terminar en casa (≤ 20 minutos)

- Una frase por afirmación: **qué cambiaría tu respuesta**.
- La **auditoría de una propuesta** hecha por un asistente de IA.
- Un **memo** de 5 a 8 líneas sobre la afirmación más difícil.
- (Opcional, no se entrega) una comprobación de fechas.

## Entregable

El **mismo notebook**, completado: tus declaraciones, tus citas, tus defensas, tus recomputaciones y tu memo. Debe poder ejecutarse de principio a fin.

## Uso de IA y de documentación externa

Puedes usar documentación externa y herramientas de IA. **La IA puede generar; tú sigues siendo responsable** de entender, comprobar, poner a prueba y defender lo que entregas. Si tu conclusión depende de algo que **no está** en el extracto ni en la tabla, indícalo y distingue qué demuestran tus datos de qué añade esa fuente. En la parte 7 tendrás que auditar una propuesta de un asistente.

## De qué sigues siendo responsable

- De **entender** cada línea que ejecutas, sea tuya o generada.
- De que cada etiqueta se apoye en **evidencia que has leído y comprobado tú**, no solo en que el código se ejecute o en que el gráfico parezca claro.
- De **no inventar** correcciones, factores ni fechas que la documentación no da.
- De **defender** por qué cada afirmación se mantiene, se acota, se recalcula o no se compara.
