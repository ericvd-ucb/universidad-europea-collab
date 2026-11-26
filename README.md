# universidad-europea-collab

Ensayos y ejemplos para la colaboración con la Universidad Europea de Madrid.

## Carpetas y cuadernos

### [Asteroids](Asteroids/)

Actividades de análisis de datos de meteoritos para Computación Científica I, con versiones para estudiantes y profesorado.

| Cuaderno | Descripción | Google Colab |
|---|---|---|
| [meteoritos_alumnos.ipynb](Asteroids/meteoritos_alumnos.ipynb) | Actividades y retos con Python estándar, sin pandas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Asteroids/meteoritos_alumnos.ipynb) |
| [meteoritos_profesor.ipynb](Asteroids/meteoritos_profesor.ipynb) | Versión para el profesorado con soluciones propuestas, sin pandas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Asteroids/meteoritos_profesor.ipynb) |
| [meteoritos_pandas_alumnos.ipynb](Asteroids/meteoritos_pandas_alumnos.ipynb) | Actividades y retos de análisis de meteoritos con pandas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Asteroids/meteoritos_pandas_alumnos.ipynb) |
| [meteoritos_pandas_profesor.ipynb](Asteroids/meteoritos_pandas_profesor.ipynb) | Versión con pandas para el profesorado, con soluciones propuestas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Asteroids/meteoritos_pandas_profesor.ipynb) |

### [Economia](Economia/)

Análisis de la economía española y europea con datos de Eurostat. La carpeta `ig-imagenes` contiene las imágenes de referencia utilizadas en el cuaderno sobre los mandatos.

| Cuaderno | Descripción | Google Colab |
|---|---|---|
| [eurostat_gdp_comparison.ipynb](Economia/eurostat_gdp_comparison.ipynb) | Compara el PIB, el crecimiento y el PIB per cápita de economías europeas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Economia/eurostat_gdp_comparison.ipynb) |
| [spain_economy_by_term.ipynb](Economia/spain_economy_by_term.ipynb) | Reproduce y contrasta una comparación de indicadores económicos por mandato presidencial en España. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Economia/spain_economy_by_term.ipynb) |
| [spain_economy_by_term_step_by_step.ipynb](Economia/spain_economy_by_term_step_by_step.ipynb) | Versión paso a paso del cuaderno anterior: el mismo análisis con código más sencillo, una pequeña tarea por celda y funciones cortas. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Economia/spain_economy_by_term_step_by_step.ipynb) |
| [spain_vibecession.ipynb](Economia/spain_vibecession.ipynb) | Explora la relación entre confianza del consumidor e indicadores económicos en España y la zona euro. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Economia/spain_vibecession.ipynb) |

### [FAS-XAI](FAS-XAI/)

Cuadernos y artículos reproducibles del Dr. Gabriel Marín Díaz (Computación Científica): análisis exploratorio de datos científicos (exoplanetas, Hipparcos-Gaia, meteoritos, terremotos, cráteres de Marte) e inteligencia artificial explicable. Los cuadernos están alojados en Zenodo; la carpeta contiene una ficha con los enlaces.

| Recurso | Descripción | Enlace |
|---|---|---|
| FAS-XAI for Interpretable Stellar Population Discovery | Artículo en *AI* (MDPI, 2026): agrupamiento difuso, XAI y análisis espacial de datos de Hipparcos. | [DOI 10.3390/ai7110488](https://doi.org/10.3390/ai7110488) |
| Python Exercises - EDA | Seis cuadernos de análisis exploratorio: exoplanetas, Hipparcos-Gaia, meteoritos, terremotos y cráteres de Marte. | [Zenodo](https://doi.org/10.5281/zenodo.21276917) |
| Interpretable Machine Learning - Diabetes | Aprendizaje automático interpretable para predecir diabetes, con visualización HTML interactiva. | [Zenodo](https://doi.org/10.5281/zenodo.19107160) |

### [Fisica](Fisica/)

Apuntes interactivos de Física del Estado Sólido del Dr. José Manuel López López. La carpeta `images` contiene las figuras que usa el cuaderno.

| Cuaderno | Descripción | Google Colab |
|---|---|---|
| [Estructura_Cristalina.ipynb](Fisica/Estructura_Cristalina.ipynb) | Unidad 1: estructura cristalina y enlace atómico. Redes de Bravais, estructuras SC, BCC, FCC, HCP y diamante, índices de Miller, defectos y tipos de enlace, con cálculos y ejercicios en Python. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Fisica/Estructura_Cristalina.ipynb) |

### [Metales](Metales/)

Modelos matemáticos del mecanizado de metales (torneado, fresado, taladrado y vida de la herramienta), basados en las fórmulas del *Metal Cutting Training Handbook* de Sandvik Coromant. La carpeta `metal-cutting-models` contiene el paquete de Python `metalcutting` que usan los ejercicios, junto con sus pruebas y la versión con soluciones.

| Cuaderno | Descripción | Google Colab |
|---|---|---|
| [metal_cutting_demo.ipynb](Metales/metal_cutting_demo.ipynb) | Demostración paso a paso de una operación de torneado: velocidad de corte, rpm, avance, tiempo de mecanizado, caudal de viruta, espesor de viruta y fuerza específica de corte. Solo usa Python estándar. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Metales/metal_cutting_demo.ipynb) |
| [metal_cutting_exercises.ipynb](Metales/metal_cutting_exercises.ipynb) | Ejercicios de torneado, fresado, taladrado, vida de la herramienta y un caso final de planificación, con celdas `check()` que comprueban cada respuesta (tolerancia del 1 %). Usa el paquete `metalcutting`; en Colab, la primera celda lo descarga automáticamente. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Metales/metal_cutting_exercises.ipynb) |

### [Taller-IA](Taller-IA/)

Materiales del taller "Jupyter in Teaching: Building with AI" para profesorado STEAM (26 de noviembre de 2026): hoja de prompts, guía de programación en directo, cuaderno de inicio y diapositivas sobre proyectos con datos abiertos.

| Cuaderno | Descripción | Google Colab |
|---|---|---|
| [live-coding-starter.ipynb](Taller-IA/live-coding-starter.ipynb) | Diez cosas sencillas en Python, de una calculadora a una tabla y un gráfico. | [Abrir en Colab](https://colab.research.google.com/github/ericvd-ucb/universidad-europea-collab/blob/main/Taller-IA/live-coding-starter.ipynb) |

Los enlaces de Colab abren la versión de la rama `main` en GitHub; los cambios locales deben publicarse para que aparezcan allí.
