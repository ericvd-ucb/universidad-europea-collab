# PA-04 · ¿Qué estado debe devolver cada partición?

**Clase 4 · Unidad 2 — ETL y procesamiento escalable**

## Propósito

Una plataforma de datos de cine guarda las reseñas de críticos (2000–2023) en **24 particiones, una por año**, en Parquet. La pregunta del negocio es «¿qué proporción de **todas** las reseñas es `fresh`?». Se puede contestar con **una sola pasada** o procesando **cada partición por separado** (cada una devuelve un resumen pequeño y después se combinan los resúmenes). Un compañero ha hecho lo segundo calculando el porcentaje de `fresh` en cada partición y promediando los 24 porcentajes.

En esta actividad **no mides rendimiento ni memoria, no limpias fechas y no analizas las reseñas**: decides **qué debe devolver cada partición** para que la respuesta global se pueda **reconstruir correctamente** y **demuestras** que las dos formas de ejecutar contestan a la misma pregunta.

Python (Polars) es un instrumento para obtener evidencia. Lo que se trabaja es tu razonamiento sobre **qué resúmenes se pueden combinar**, **con qué peso cuenta cada partición** y **cómo se comprueba que dos planes de ejecución son equivalentes**.

## Conocimientos previos esperados

Lo visto hasta la clase 4: Parquet, particionado, lectura perezosa (*lazy*) con Polars, agregaciones por grupo y la comparación de resultados (enteros: exacta; decimales: con tolerancia). **No hace falta recordar sintaxis de Polars.** Casi todo el código viene escrito y está marcado como **«código proporcionado — no se evalúa esta sintaxis»**: no tienes que escribirlo ni memorizarlo, pero sí **entender qué consigue, qué devuelve cada partición y qué significa el resultado**. Escribes **valores, listas, frases cortas y una única expresión sencilla** (la combinación de tus resúmenes, en la parte 4).

## Ficheros que se te entregan

| Ruta | Qué es |
|---|---|
| `student/PA-04_student.ipynb` | El notebook de trabajo (ábrelo desde la carpeta `student/`); incluye un *glosario elaborado para esta actividad* (no es documentación original del conjunto de datos) |
| `data/rt_reviews_2000_2023/` | Las reseñas, en Parquet particionado por año (24 carpetas `year=AAAA`) |
| `data/DATASET_NOTICE.md` | Procedencia, qué se ha seleccionado y qué no se ha tocado |

## Entorno

Python 3.14 y **Polars 1.44.2** (el entorno del curso). Esta actividad se ha verificado con esa versión; con otras, algunos resultados pueden diferir y el notebook te avisará.


## Primera parte (25 minutos)

1. Tu **predicción** (¿coincidirá la cifra del compañero con la global?), tu declaración del **estado** que debe devolver cada partición y de **cómo vas a comparar**, escritas **antes** de ejecutar.
2. Las dos respuestas ejecutadas (la del compañero y la de una sola pasada) y la lectura de **qué pesa cada partición**.
3. Tu **combinación** de los 24 resúmenes (una expresión) y su **validación** frente a la pasada única.
4. Tu **explicación** de dos frases y tus dos cifras.

La **puesta en común** se hace en clase aunque no hayas terminado el código.

## Sgunda parte (20 minutos)

- La comprobación con **otra agrupación** de particiones (dos mitades).
- El **párrafo final** y la lista de verificación.
- (Opcional, no se entrega) una exploración con listas de años que elijas.

## Entregable

El **mismo notebook**, completado: tus declaraciones, tu expresión, tus cifras y tu explicación. Debe poder ejecutarse de principio a fin.

## Uso de IA y de documentación externa

Puedes usar documentación externa y herramientas de IA. **La IA puede generar; tú sigues siendo responsable** de entender, comprobar, poner a prueba y defender lo que entregas. Si tu conclusión depende de algo que no está en el notebook, indícalo y distingue qué demuestran tus datos de qué añade esa fuente.

## De qué sigues siendo responsable

- De **entender** cada línea que ejecutas, sea tuya o generada.
- De **comprobar** sobre estos datos cualquier cosa que te sugiera una herramienta.
- De que cada afirmación se apoye en **evidencia que has obtenido tú**, no solo en que el código se ejecute o en que dos cifras se parezcan.
- De **defender** por qué tu resultado responde a la pregunta global.
