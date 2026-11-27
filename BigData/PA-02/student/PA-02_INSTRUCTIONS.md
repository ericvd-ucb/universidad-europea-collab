# PA-02 · Declara el contrato de ingesta antes de fiarte de la tabla

**Clase 2 · Unidad 2 — Ingesta, formatos, esquemas y fundamentos de pandas**

## Propósito

Un compañero te entrega una tabla y te dice «los datos están limpios, cárgalos y sigue». En esta actividad aprendes a **no aceptar una tabla porque haya cargado**, sino a aceptarla solo a través de **afirmaciones que se pueden comprobar**. Para cada afirmación decides:

- **PASS**: la evidencia disponible la respalda.
- **FAIL**: la evidencia disponible la contradice.
- **UNKNOWN**: **no es verificable con la evidencia de la que disponemos ahora**. No significa «no sé»: significa decir qué evidencia falta y qué la resolvería.

No limpias datos ni haces análisis. Tampoco es una práctica de sintaxis de pandas: el trabajo es decidir qué significa la tabla y comprobarlo.

La actividad usa a propósito una **evidencia limitada** (la tabla, el ReadMe del origen, la leyenda de símbolos y los totales publicados). El origen publica más documentación; no forma parte de este paquete.

## Conocimientos previos esperados

Solo lo visto en las clases 1 y 2: qué es el grain de una tabla, DataFrame y tipos de columna (`dtypes`), leer un CSV con `pd.read_csv` y sus opciones, contar valores ausentes, el contrato de verificación. **No hace falta recordar sintaxis**: las comprobaciones vienen escritas como fragmentos cortos que ejecutas y, si quieres, adaptas. Algunos usan funciones (`pd.to_datetime`, `.dt`, `pd.to_numeric`, `groupby().agg`, la opción `parse_dates`). Están marcados como **«código proporcionado — no se evalúa esta sintaxis»**: no tienes que escribirlos ni memorizarlos, pero sí **entender qué consigue el código, si su resultado es válido y qué significa**.

## Ficheros que se te entregan

| Ruta | Qué es |
|---|---|
| `student/PA-02_student.ipynb` | El notebook de trabajo (ábrelo desde la carpeta `student/`) |
| `data/international_airline_activity_2009-01_2025-11.csv` | La tabla |
| `data/totals_published.csv` | Totales publicados por año, para una reconciliación |
| `data/docs/ReadMe_sheet.md` | Hoja ReadMe del origen (copia literal) |
| `data/docs/symbols_legend.md` | Leyenda de símbolos del origen (copia literal) |
| `data/docs/DATASET_NOTICE.md` | Procedencia, atribución y qué se ha adaptado |

## Entorno

Python 3.14 y **pandas 3.0.6** (el entorno del curso). No necesitas Excel ni `openpyxl`. Si usas otra versión de pandas, algunos tipos y resultados pueden diferir y el notebook te avisará.


## Primera parte (en la clase)

1. Tu hipótesis de qué es una fila y de cuál es su clave.
2. Entre 4 y 6 afirmaciones del menú, con tu **predicción escrita antes** de ejecutar ninguna comprobación.
3. Para cada una, su comprobación ejecutada, tu veredicto (PASS, FAIL o UNKNOWN) y una evidencia (una cifra o un hecho). Al menos un UNKNOWN con una primera idea de qué evidencia lo resolvería.
4. Tus decisiones de lectura del fichero, implementadas y validadas.
5. Una defensa breve: qué demuestran los datos, qué demuestra la documentación y qué queda sin demostrar.

La **puesta en común** se hace en clase aunque no hayas terminado el código: lo importante es que hayas llegado a tus veredictos y a tu decisión de lectura.

## Segunda parte (≤ 20 minutos)

- Ampliar el contrato hasta 6 afirmaciones o más.
- Justificar **cada** UNKNOWN: qué evidencia lo resolvería.
- Anotar cuáles de tus veredictos cambian con tu lectura del fichero y por qué.
- Revisar la lista de verificación final.

## Entregable

El **mismo notebook**, completado, con la tabla final del contrato: afirmación · comprobación · resultado · evidencia, con **al menos 4 afirmaciones y al menos 1 UNKNOWN justificado**. Debe poder ejecutarse de principio a fin.

## Evidencia proporcionada y evidencia externa

- **Evidencia proporcionada**: el paquete (tabla, ReadMe, leyenda, totales) y lo que tú compruebas con código sobre él.
- **Evidencia externa**: cualquier otra cosa (documentación que encuentres, conocimiento propio, búsquedas, una IA).

Los veredictos se deciden con la evidencia proporcionada: **si no basta para establecer una afirmación, el veredicto es UNKNOWN**. No marques FAIL porque te parezca poco plausible, porque los datos sugieran una explicación, porque lo recuerdes o porque una IA lo afirme. Puedes usar evidencia externa y **no se penaliza por ser externa**, pero debes **identificarla** (fuente) en el campo `evidencia_externa`, separar lo que establece el paquete de lo que añade la externa y reconocer que tu conclusión depende de ella.

## Uso de IA

Puedes usar documentación externa y herramientas de IA para generar código, proponer hipótesis o explicarte una función. **La IA puede generar; tú sigues siendo responsable.**

## De qué sigues siendo responsable

- De **entender** cada línea que ejecutas, sea tuya o generada.
- De **comprobar** sobre esta tabla cualquier cosa que te sugiera una herramienta: una respuesta generada que no has comprobado no es evidencia proporcionada; si la usas, identifícala como evidencia externa.
- De que cada veredicto se apoye en **evidencia que has obtenido tú**.
- De **defender** tus decisiones: qué has leído como ausente y por qué, qué has dado por demostrado y qué no.
