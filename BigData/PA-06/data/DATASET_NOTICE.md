# Procedencia, atribución y adaptación de los datos

**Datos:** *International Airline Activity* — Tabla 1 (*International Scheduled Air Transport*), de enero de 2009 a noviembre de 2025.

**Origen:** Bureau of Infrastructure and Transport Research Economics (BITRE).

**Fichero de origen:** `International_airline_activity_Table1_2009toCurrent_1125.xlsx` (libro de cinco hojas).

**Uso:** material aportado por el profesor para uso docente en esta asignatura. No se afirma aquí nada más sobre su licencia.

## Qué es una adaptación y qué no

Este paquete contiene **adaptaciones de formato y selecciones** del libro de origen preparadas por el profesorado. Los valores no se han modificado: no se ha limpiado, imputado, eliminado ni reordenado nada.

| Fichero | Qué contiene | Qué se ha hecho |
|---|---|---|
| `international_airline_activity_2009-01_2025-11.csv` | Hoja *Data* del libro (columnas A a J; 21.588 filas más la cabecera) | CSV UTF-8, separador coma, una fila de cabecera. `Month` se escribe como texto `AAAA-MM-DD`; los números, como texto decimal; los `..` se conservan tal cual. Es **el mismo fichero**, byte a byte, que el de la actividad PA-02. |
| `docs/EXTRACTO_DOCUMENTACION.md` | **Selección** de celdas de las hojas *ReadMe*, *ExpNotes*, *Data Issues*, *Totals* y *Data* | Copia **literal en el inglés original** de cada celda seleccionada (sin sus espacios iniciales y finales), con un ID por bloque. La introducción y las etiquetas «Hoja / celdas» son nuestras. **No se incluye todo el libro**: de *ExpNotes* solo los párrafos que se indican y los símbolos. |
| `figuras/afirmacion_1.png` … `afirmacion_5.png` | Cinco gráficos | **Generados por el profesorado** a partir de la tabla de este mismo paquete (sin anotaciones ni marcas añadidas), con matplotlib 3.11.2 (herramienta de preparación; no es necesaria para trabajar). |

El **glosario del notebook** (GLOSARIO ELABORADO PARA ESTA ACTIVIDAD) **no es documentación original del conjunto de datos**. No se incluyen otras hojas ni otras secciones del libro de origen.

## Integridad (SHA-256)

| Fichero | SHA-256 |
|---|---|
| Libro de origen `International_airline_activity_Table1_2009toCurrent_1125.xlsx` | `b2a501d3f9857ee5b8c1341496ed38e165f7f5fd29d8ff4c967709fab0e7472a` |
| `international_airline_activity_2009-01_2025-11.csv` | `020be36e95b40ca54031d82fe935d93a1c7f8a6623c3b6c3382d1989fd04562b` |
| `docs/EXTRACTO_DOCUMENTACION.md` | `4e8a757cca4ace8d23af40aff43aa3d4ad19c5034e77b3aac241e4c8d366f610` |
| `figuras/afirmacion_1.png` | `ac1110116fff9c16c1d474b5fa5704bbe66b70bf1188b04f9c5969f94117b0b0` |
| `figuras/afirmacion_2.png` | `b0eb59f1264b9ef61eb5ea1f12ea1d569bc4016e2624b49e40a5fd1ad75df42d` |
| `figuras/afirmacion_3.png` | `9d325000b63205829afd45e22450f4dbae163dd5879141f1eabba6ecb2c74200` |
| `figuras/afirmacion_4.png` | `526138dbdd14f3d54ce19c0d7ac11922a9368a98f614881268d168da72b4cc03` |
| `figuras/afirmacion_5.png` | `068a500240f9daf4c4813380ba7f6cc70d1c7d5661d651057a8b513beb0f5a59` |
