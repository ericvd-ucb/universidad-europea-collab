# FAS-XAI: cuadernos y artículos del Dr. Gabriel Marín Díaz

Materiales del Dr. Gabriel Marín Díaz (Departamento de Computación y Tecnología, Universidad Europea de Madrid; Facultad de Estadística, Universidad Complutense de Madrid). Usa mucho los cuadernos Jupyter en Computación Científica y publica sus artículos con código reproducible en Zenodo, dentro de la comunidad *FAS-XAI Code and Reproducible Research*.

Los cuadernos están alojados en Zenodo con licencia CC BY 4.0; aquí se enlazan sin copiarlos.

## Artículo

**FAS-XAI for Interpretable Stellar Population Discovery: Fuzzy Memberships, Explainable Artificial Intelligence, and Spatial Analysis of Hipparcos Data**
G. Marín Díaz. *AI* (MDPI), 7(11), 488, noviembre de 2026.
DOI: [10.3390/ai7110488](https://doi.org/10.3390/ai7110488)

Agrupa 49.273 estrellas del catálogo Hipparcos con *fuzzy C-means*, de modo que cada estrella puede pertenecer parcialmente a varios grupos, y explica los grupos con un modelo sustituto XGBoost y valores SHAP. Identifica cuatro poblaciones estelares; el índice de color, la magnitud absoluta y la distancia son las variables más influyentes.

## Cuadernos en Zenodo

### Python Exercises - EDA

Análisis exploratorio de datos científicos con Python: exoplanetas, Hipparcos-Gaia, meteoritos, terremotos y cráteres de Marte.
DOI: [10.5281/zenodo.21276917](https://doi.org/10.5281/zenodo.21276917)

| Cuaderno | Tema |
|---|---|
| `01 - Lectura - Hipparcos-Gaia v2.0.ipynb` | Lectura y exploración del catálogo Hipparcos-Gaia |
| `01 - Lectura - Meteoritos.ipynb` | Lectura y exploración de datos de meteoritos |
| `01 - Lectura Exoplanetas.ipynb` | Lectura de datos de exoplanetas |
| `Exoplanetas.ipynb` | Análisis de exoplanetas |
| `03 - Terremotos - Solución.ipynb` | Análisis de terremotos, con solución |
| `Mars - Craters.ipynb` | Cráteres de Marte |

### Interpretable Machine Learning - Diabetes

Implementación reproducible de aprendizaje automático interpretable para predecir diabetes: preprocesado, entrenamiento y explicación posterior de las predicciones, con una visualización HTML interactiva. Forma parte de la misma línea de investigación FAS-XAI.
DOI: [10.5281/zenodo.19107160](https://doi.org/10.5281/zenodo.19107160)

Nota: el registro de Zenodo contiene la visualización HTML (`InterpretableMLEthicompDiabetes.html`), no un archivo `.ipynb`.

## Relación con otros materiales del repositorio

Los cuadernos de meteoritos de la carpeta [Asteroids](../Asteroids/) trabajan con un conjunto de datos similar al de `01 - Lectura - Meteoritos.ipynb`.
