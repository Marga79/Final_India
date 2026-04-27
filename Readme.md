**Análisis del Sistema Educativo y Universitario de India**

Proyecto de análisis de datos que combina un **EDA en Python** con un **Dashboard interactivo en Power BI**, con el objetivo de explorar la relación entre el nivel educativo de la población india y la calidad de sus instituciones universitarias según el ranking NIRF.

**Índice**

- Descripción
- Estructura del proyecto
- Datos
- Instalación y ejecución
- Notebooks
- Dashboard Power BI
- Principales conclusiones
- Autora
- Documentación adicional
 [Diccionario de términos](diccionario.md)

- **Descripción**

Este proyecto analiza dos dimensiones del sistema educativo indio:

- El **nivel educativo de la población** por estado, a partir del censo de 2011.
- El **rendimiento de las instituciones universitarias** entre 2021 y 2025, a partir de los rankings NIRF (_National Institutional Ranking Framework_).

La pregunta central del análisis es: ¿existe relación entre el nivel educativo de la población de un estado y la calidad de sus universidades?

- **Estructura del proyecto**

FINAL_INDIA/

├── data/
│   ├── output/                 # Datasets procesados listos para análisis
│   │   ├── df_Educ_clean.csv
│   │   ├── df_Educ_state.csv
│   │   ├── df_merged.csv
│   │   ├── df_Rank_final2.csv
│   │   └── df_Rank_state.csv
│   └── raw/                    # Datos originales sin procesar
│       ├── India_Education_Statistics.csv
│       ├── df_Rank_final.csv
│       ├── NIRF Ranking 2020.csv
│       ├── NIRF Ranking 2021.csv
│       ├── NIRF ranking 2022.csv
│       ├── NIRF Ranking 2023.csv
│       ├── NIRF Ranking 2024.csv
│       └── NIRF Ranking 2025.csv

├── notebook/
│   ├── 01 - Analisis_preliminar.ipynb
│   ├── 02 - Limpieza.ipynb
│   ├── 03 - EDA.ipynb
│   └── NIRF Ranking Completo.csv

├── src/
│   └── soporte.py              # Funciones auxiliares reutilizables

├── .gitattributes
├── README.md
└── diccionario.md              # Diccionario de términos añadido


- **Datos**

Los datos se han obtenido de <https://www.kaggle.com/> y corresponden a dos fuentes:

India_Education_Statistics.csv: Estadísticas de los niveles educativos de la India por estado y grupo de edad (correspondiente al censo de 2011)

NIRF Ranking Año.csv: clasificación NIRF (en español "Marco Nacional de Clasificación Institucional") de las 100 mejores instituciones universitarias de India durante los años 2020-2025. El ranking 2020 fue descartado durante el análisis preliminar por ser idéntico al de 2021.

- **Instalación y ejecución**

**Requisitos previos**

- Python 3.9 o superior
- Jupyter Notebook o JupyterLab

1\. Clonar el repositorio

git clone <https://github.com/Marga79/Final_India>

2\. Instalar dependencias

pip install -r requirements.txt

3\. Librerías utilizadas:

pandas

numpy

matplotlib

seaborn

**5\. Ejecutar los notebooks en orden**

jupyter notebook

Los notebooks se ejecutan en este orden:

1º) 01 - Analisis_preliminar.ipynb 🡪Carga, exploración inicial y detección de problemas.

2º) 02 - Limpieza.ipynb 🡪 Transformación, limpieza y fusión de datasets.

3º) 03 - EDA.ipynb 🡪 Análisis exploratorio completo y visualizaciones.

- 1. **Dashboard Power BI**

El archivo **Proyecto final_India.pbix** contiene dos páginas interactivas.

**Página 1 - Ranking NIRF**

Analiza el rendimiento y la evolución de las universidades usando df_Rank_final2.

Gráficos:

Top 10 universidades por score, evolución temporal de métricas TLR/RPC/GO, distribución del score y comparativa de universidades.

KPIs: Mejor universidad, Score promedio, Ranking promedio y Estado con mejor Score.

Filtrable por año (2021-2025).

**Página 2 - Educación & Calidad Universitaria por Estado**

Analiza el sistema educativo estatal y su relación con el rendimiento universitario, usando df_merged.

Gráficos de:

Tasa de alfabetización por estado, brecha de género en graduados por estado, score NIRF por estado y Diagrama de dispersión: alfabetización vs. calidad universitaria

KPIs: tasa media de alfabetización, tasa media de graduados, Score medio, Ranking medio y número de universidades con ranking.

**Requisitos**

Power BI Desktop (versión julio 2024 o posterior)

- 1. **Principales conclusiones**

**Ranking universitario**

- El **IIT Madras** lidera el ranking en 2025 con un score de 87.
- El score promedio nacional creció de 51,2 (2021) a 57,8 (2025), sin ningún año de retroceso.
- El RPC (investigación) aumentó un 22% en el periodo analizado.
- El sistema universitario de élite es muy estático: las mismas instituciones lideran año tras año.

**Nivel educativo de la población**

- **Kerala** encabeza la tasa de alfabetización estatal con un 80%, pero no destaca en graduados universitarios.
- Existe brecha de género en la graduación en todos los estados sin excepción.
- La adolescencia concentra el menor analfabetismo; la juventud, la mayor proporción de graduados.

**Relación entre educación y calidad universitaria**

- La correlación entre alfabetización poblacional y calidad universitaria es **débil**.
- Estados con alta alfabetización (Kerala) no necesariamente tienen universidades de élite.
- Estados con alto analfabetismo (Jharkhand, Uttar Pradesh) pueden albergar instituciones de primer nivel.
- El ranking NIRF responde más a políticas de investigación y concentración institucional que al nivel educativo del entorno.
  - **Autora**

Marga Boticario
