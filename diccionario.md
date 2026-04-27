**Diccionario de datos**

Descripción detallada de las variables de los datasets utilizados en el proyecto.

**Índice**

- India_Education_Statistics.csv
- NIRF Ranking Año.csv 🡪 df_Rank_final.csv

**Descripción:**

- **India_Education_Statistics.csv:** Estadísticas educativas de India por unidad administrativa (estado, distrito, tehsil) y grupo de edad, extraídas del censo de 2011. En este proyecto se trabaja únicamente a nivel estado (Area Name), filtrando por registros de tipo Total (excluyendo la división Rural/Urbano).

**Table Name**: Identificador de tabla. Presenta únicamente el valor C2308. Eliminada en la limpieza.

**State Code**: indica el código numérico del estado. Eliminada en la limpieza.

**District Code**: indica el código numérico del distrito. Eliminada en la limpieza.

**Tehsil Code**: indica el código Tehsil, similar a un código postal. Eliminada en la limpieza.

**Area Name**: indica el nombre del estado. Variable principal de agrupación.

**Total/ Rural/ Urban**: indica si la zona del estado es Rural, Urban o Total. Se conservan únicamente los registros Total.

**Age-group**: indica la edad. La etiqueta "All ages" es un agregado del total y se elimina en la limpieza.

**Total - Persons**: indica el total de personas en la unidad administrativa.

**Total - Males**: indica el total de hombres en la unidad administrativa.

**Total - Females**: indica el total de mujeres en la unidad administrativa.

**Illiterate - Persons**: indica el número de personas totales analfabetas.

**Illiterate - Males**: indica el número de hombres analfabetos.

**Illiterate - Females**: indica el número de mujeres analfabetas.

**Literate - Persons**: indica el total de personas alfabetizadas.

**Literate - Males**: indica el total de hombres alfabetizados.

**Literate - Females**: indica el número total de mujeres alfabetizadas.

**Educational level - Literate without educational level - Persons**: indica el total de personas alfabetizadas sin nivel educativo formal.

**Educational level - Literate without educational level - Males**: indica el total de hombres alfabetizados sin nivel educativo formal.

**Educational level - Literate without educational level - Females**: indica el total de mujeres alfabetizadas sin nivel educativo formal.

**Educational level - Below primary - Persons**: indica el total de personas que no han completado la educación primaria.

**Educational level - Below primary - Males**: indica el total de hombres que no han completado la educación primaria.

**Educational level - Below primary - Females**: indica el total de mujeres que no han completado la educación primaria.

**Educational level - Primary - Persons**: indica el total de personas con educación primaria o básica.

**Educational level - Primary - Males**: indica el total de hombres con educación primaria o básica.

**Educational level - Primary - Females**: indica el total de mujeres con educación primaria o básica.

**Educational level - Middle - Persons**: indica el total de personas con educación secundaria básica.

**Educational level - Middle - Males**: indica el total de hombres con educación secundaria básica.

**Educational level - Middle - Females**: indica el total de mujeres con educación secundaria básica.

**Educational level - Matric/Secondary - Persons**: indica el total de personas con educación secundaria completa.

**Educational level - Matric/Secondary - Males**: indica el total de hombres con educación secundaria completa.

**Educational level - Matric/Secondary - Females**: indica el total de mujeres con educación secundaria completa.

**Educational level - Higher secondary/Intermediate/Pre-University/Senior secondary - Persons**: indica el total de personas con estudios preuniversitarios, o de bachillerato.

**Educational level - Higher secondary/Intermediate/Pre-University/Senior secondary - Males**: indica el total de hombres con estudios preuniversitarios, o de bachillerato.

**Educational level - Higher secondary/Intermediate/Pre-University/Senior secondary - Females**: indica el total de mujeres con estudios preuniversitarios, o de bachillerato.

**Educational level - Non-technical diploma or certificate not equal to degree - Persons**: indica el total de personas con estudios posteriores a secundaria, pero no universitarios.

**Educational level - Non-technical diploma or certificate not equal to degree - Males**: indica el total de hombres con estudios posteriores a secundaria, pero no universitarios.

**Educational level - Non-technical diploma or certificate not equal to degree - Females**: indica el total de mujeres con estudios posteriores a secundaria, pero no universitarios.

**Educational level - Technical diploma or certificate not equal to degree - Persons**: indica el total de personas con diploma técnico o certificado que no equivale a un título universitario.

**Educational level - Technical diploma or certificate not equal to degree - Males**: indica el total de hombres con diploma técnico o certificado que no equivale a un título universitario.

**Educational level - Technical diploma or certificate not equal to degree - Females**: indica el total de mujeres con diploma técnico o certificado que no equivale a un título universitario.

**Educational level - Graduate & above - Persons**: indica el total de personas con título universitario completo.

**Educational level - Graduate & above - Males**: indica el total de hombres con título universitario completo.

**Educational level - Graduate & above - Females**: indica el total de mujeres con título universitario completo.

**Educational level - Unclassified - Persons**: indica el total de personas totales no clasificadas.

**Educational level - Unclassified - Males**: indica el total de hombres no clasificados.

**Educational level - Unclassified - Females**: indica el total de mujeres no clasificadas.

- Datos oficiales del **_National Institutional Ranking Framework_** (Marco Nacional de Clasificación Institucional), publicados anualmente por el Ministerio de Educación del Gobierno de India. Recogen las 100 mejores instituciones de educación superior del país. Se dispone de rankings para los años 2021, 2022, 2023, 2024 y 2025 (el ranking 2020 fue descartado por ser idéntico al de 2021).

Los seis archivos presentan estructura y variables idénticas. Durante la limpieza se fusionan en un único dataset (df_Rank_final2) añadiendo la variable Año.

Las variables del conjunto de datos del **NIRF** son:

**Institute ID**: identificador único de la institución.

**Institute Name**: Nombre oficial de la universidad o institución de educación superior.

**TLR (Enseñanza, Aprendizaje y Recursos)**: Puntuación que representa la calidad del profesorado, la capacidad estudiantil, las instalaciones y el entorno académico.

**RPC (Investigación y Práctica Profesional)**: Puntuación que refleja las publicaciones de investigación, las patentes y el impacto en la práctica profesional.

**GO (Resultados de Graduación)**: Puntuación basada en la colocación de los estudiantes, los estudios superiores y el rendimiento académico.

**OI (Difusión e Inclusión)**: Puntuación que mide la diversidad, la representación regional, el equilibrio de género y la inclusión.

**PERCEPTION**: Puntuación de reputación derivada de colegas académicos y empleadores.

**City**: Ciudad donde se ubica la institución.

**State**: Estado o territorio de la Unión de la India de la institución.

**Score**: Puntuación general ponderada del NIRF, calculada utilizando todos los parámetros.

**Rank**: Clasificación nacional final asignada a la institución para ese año.

**Año**: Año del ranking. Variable añadida durante la fusión de los datasets. Valores: 2021-2025.
