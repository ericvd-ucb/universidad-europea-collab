# Procedencia y atribución de los datos

**Datos:** `rt_reviews_2000_2023/` — reseñas de críticos de cine del conjunto **Rotten Tomatoes** (`rotten_tomatoes_movie_reviews.csv`), aportado por el profesor para uso docente en esta asignatura.

**Procedencia:** según el inventario del proyecto, es el fichero `rotten_tomatoes_movie_reviews.csv` del material del profesor. El propio fichero no incluye autoría, licencia ni documentación; **no se afirma aquí nada más sobre su origen**. El **glosario del notebook (GLOSARIO ELABORADO PARA ESTA ACTIVIDAD) no es documentación original del conjunto de datos**.

**Adaptación (derivado preparado por el profesorado).** Estos datos son una **adaptación** del original:

1. **Selección de filas:** solo las reseñas con año **2000–2023** (24 particiones). El año es el de los **cuatro primeros caracteres** de la fecha de la reseña tal como figura en el original; **no se ha interpretado, corregido ni limpiado ninguna fecha**.
2. **Selección de columnas:** una sola columna del original, `reviewState`, con sus valores **sin modificar** (`fresh` / `rotten`), más el año como partición. **No se entrega** texto de reseñas, nombres, URL ni puntuaciones.
3. **Formato:** Parquet particionado por año (`year=AAAA/`).

No se ha modificado ningún valor, no se ha reordenado dentro de cada partición y no se ha eliminado ningún duplicado. Las reseñas con año anterior a 2000 **no forman parte** de esta actividad.

| | SHA-256 |
|---|---|
| Original `rotten_tomatoes_movie_reviews.csv` | `fce65e53761e807276a16a2f1409da13148450036518323b2b37202142cb322f` |
| Conjunto de los 24 ficheros de `rt_reviews_2000_2023/` (SHA-256 del texto «hash␣␣ruta», una línea por fichero, ordenadas por ruta) | `94b86a14a1a0e3b99581bd16cd19a1231cf1498a207c43e51786cbfb11d7af00` |

| Fichero | SHA-256 |
|---|---|
| `year=2000/00000000.parquet` | `f4d263e19d270012c7dac8e3ea5e202e265cfb6f2b74be03190f6af5fa5efad9` |
| `year=2001/00000000.parquet` | `9a45677923e6eaaf629e62f6a55b020effcb8dfa827a5ec8f5bdfd3c5b79753a` |
| `year=2002/00000000.parquet` | `4c2471d3219c4fa6fddce3d4103bde59cfce58ded2ad21d488005fec2fcb0052` |
| `year=2003/00000000.parquet` | `39d37cfa467df1689db7347094081fa7fb8d2ea0da8a3178d9639769b98a649d` |
| `year=2004/00000000.parquet` | `b20d91fc9461dac93eb0fb09dc873f12d1e630c5846e720c0b7fbe0b2f196955` |
| `year=2005/00000000.parquet` | `7a4d8dbab4ab99e75955fb76a7fe4f3bd08e018a64219374430ccd87dd5928e9` |
| `year=2006/00000000.parquet` | `4872e2e2365096e452442ebacc59dd6b270ff11310495cfb5943ec6d49212aa8` |
| `year=2007/00000000.parquet` | `f3b1e026e55dc227c930428a634c0f168f7969e6241d9126b779350aad05dac8` |
| `year=2008/00000000.parquet` | `88b4fae2e4b0f585f7c14cea79adea57009a89bac3835edc1efc247ff5be5e43` |
| `year=2009/00000000.parquet` | `29306af5dd45716f39707c91ac0ee5081af5938e6148603fc9f7e9683c3e3fc2` |
| `year=2010/00000000.parquet` | `5d26cdee8a2475b8210191fced4d4885aad7b85b0c5d5d6b20b46488b6769b5e` |
| `year=2011/00000000.parquet` | `4e9cdc0ef8b95b6feaf5d5d0c2cd0b6d46ba0571e6a2dccdc0c30325c8d4a3ef` |
| `year=2012/00000000.parquet` | `270ab6ab88889c752b68fae49647020f6bf5faf3bc2e933de31aedf77ceecc08` |
| `year=2013/00000000.parquet` | `587482b219e4333876c7887181ce34e04fab97a25d5eeaeaa0ca2c00074b28db` |
| `year=2014/00000000.parquet` | `68275d94f2d99e25b6f7df24f4fa6d2ca92466a1be2b0bbbded514c8004694c1` |
| `year=2015/00000000.parquet` | `3016e71a961654b8793be88dfb1f193b9045bdda8b648173f49d2956edfae712` |
| `year=2016/00000000.parquet` | `fd0c5abf843c6eb82770e0c075de6225423a6c0f79ba1340a9402271ce1318d3` |
| `year=2017/00000000.parquet` | `2a43bb31cff007b96c03c0dd38cd9655ab253266a41d2fec564b464e5bdf4ac2` |
| `year=2018/00000000.parquet` | `cbd8d23a6814ef94bc5a7846feede885ff4184b36d5caa4c87a954a93020c99e` |
| `year=2019/00000000.parquet` | `fe24239b948c855888d74d4ffcbc1071e08977bb6a5640b12521401f72ecfcc5` |
| `year=2020/00000000.parquet` | `d1943234a499a748a88dd9aa47c3857837823b4c45425673f0feb37a3cbfa2b6` |
| `year=2021/00000000.parquet` | `997d1c597531760c980f136b6d7707a1136ebbda15dcbe90499f44dfbdded2a0` |
| `year=2022/00000000.parquet` | `6b9de2d9b5a00defe354044c262dd21393fe2dc35c38b1f8f07562aef751f344` |
| `year=2023/00000000.parquet` | `41e79d0481334b92e7bbaf76a73bb40751029b56497e34cb9e86c0a6ebddda81` |
