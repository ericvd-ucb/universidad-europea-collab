# Procedencia, atribución y adaptación de los datos

**Datos:** *International Airline Activity* — Tabla 1 (*International Scheduled Air Transport*), de enero de 2009 a noviembre de 2025.

**Origen:** Bureau of Infrastructure and Transport Research Economics (BITRE).

**Fichero de origen:** `International_airline_activity_Table1_2009toCurrent_1125.xlsx` (libro de cinco hojas).

**Uso:** material aportado por el profesor para uso docente en esta asignatura.

## Qué es una adaptación y qué no

Este paquete contiene una **adaptación de formato** del libro de origen. Los valores no se han modificado: no se ha limpiado, imputado, eliminado ni reordenado nada.

| Fichero | Qué contiene | Cambios de formato |
|---|---|---|
| `international_airline_activity_2009-01_2025-11.csv` | Hoja *Data* del libro (columnas A a J; 21.588 filas más la cabecera) | CSV UTF-8, separador coma, una fila de cabecera. `Month` se escribe como texto `AAAA-MM-DD`; los números, como texto decimal; los `..` se conservan tal cual. |
| `totals_published.csv` | Valores de la tabla de totales por año de la hoja *Totals* (celdas A5:G22) | CSV; solo la tabla de totales. |
| `docs/ReadMe_sheet.md` | Hoja *ReadMe* | Copia literal en inglés original. |
| `docs/symbols_legend.md` | Sección `SYMBOLS AND OTHER USAGE` de la hoja *ExpNotes* | Copia literal en inglés original. |

No se incluyen otras hojas ni otras secciones del libro de origen.

## Integridad (SHA-256)

| Fichero | SHA-256 |
|---|---|
| `international_airline_activity_2009-01_2025-11.csv` | `020be36e95b40ca54031d82fe935d93a1c7f8a6623c3b6c3382d1989fd04562b` |
| `totals_published.csv` | `f8ef460681c0051b644b9c168f66ed043ed002f8c9f9739bafe50e2ee9d6ac86` |
