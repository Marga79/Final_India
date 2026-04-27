import pandas as pd



## 1. df_Rank_state:

def analisis_rapido1(df_Rank_state, n=5):
    
    """
    Funcion que proporciona un anális rápido del dataframe
    Parametros: 
    df_Rank_state
    n: numero de filas (por defecto 5)

    """
    print(f"Las {n} primeras filas son:")
    display(df_Rank_state.head(n))
    print("Información básica del dataframe:")
    display(df_Rank_state.info())

    print(f"El número de duplicados es:{df_Rank_state.duplicated().sum()}")
    display(df_Rank_state.isna().mean().round(2)*100)



def analisis_rapido1eda(df_Rank_state):
    """
    Funcion que muestra un resumen estadístico de las variables numéricas del dataframe y los valores únicos
    de la variable categórica "State".
    """
    print("=" * 50)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 50)
    display(df_Rank_state.describe().T.round(2))
    
    print("\n" + "=" * 50)
    print("VALORES ÚNICOS - STATE")
    print("=" * 50)
    cat_cols = df_Rank_state.select_dtypes(include="object").columns
    for col in cat_cols:
        print(f"\n {col} ({df_Rank_state[col].nunique()} únicos):")
        print(df_Rank_state[col].unique())


## 2. df_Rank_final2:

def analisis_rapido2(df_Rank_final2, n=5):
    
    """
    Funcion que proporciona un anális rápido del dataframe
    Parametros: 
    df_Rank_final2
    n: numero de filas (por defecto 5)

    """
    print(f"Las {n} primeras filas son:")
    display(df_Rank_final2.head(n))
    print("Información básica del dataframe:")
    display(df_Rank_final2.info())

    print(f"El número de duplicados es:{df_Rank_final2.duplicated().sum()}")
    display(df_Rank_final2.isna().mean().round(2)*100)


def analisis_rapido2eda(df_Rank_final2):
    """
    Funcion que muestra un resumen estadístico de las variables numéricas del dataframe y los valores únicos
    de las variables categóricas.
    """
    print("=" * 50)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("=" * 50)
    display(df_Rank_final2.describe().T.round(2))
    
    print("\n" + "=" * 50)
    print("VALORES ÚNICOS VARIABLES CATEGÓRICAS")
    print("=" * 50)
    cat_cols = df_Rank_final2.select_dtypes(include="object").columns
    for col in cat_cols:
        print(f"\n {col} ({df_Rank_final2[col].nunique()} únicos):")
        print(df_Rank_final2[col].unique())

## 3. df_Educ_clean:

def analisis_rapido3(df_Educ_clean, n=5):
    
    """
    Funcion que proporciona un anális rápido del dataframe
    Parametros: 
    df_Educ_clean
    n: numero de filas (por defecto 5)

    """
    print(f"Las {n} primeras filas son:")
    display(df_Educ_clean.head(n))
    print("Información básica del dataframe:")
    display(df_Educ_clean.info())

    print(f"El número de duplicados es:{df_Educ_clean.duplicated().sum()}")
    display(df_Educ_clean.isna().mean().round(2)*100)

# 4. df_merged:

def analisis_rapido4(df_merged, n=5):
    
    """
    Funcion que proporciona un anális rápido del dataframe
    Parametros: 
    df_merged
    n: numero de filas (por defecto 5)

    """
    print(f"Las {n} primeras filas son:")
    display(df_merged.head(n))
    print("Información básica del dataframe:")
    display(df_merged.info())

    print(f"El número de duplicados es:{df_merged.duplicated().sum()}")
    display(df_merged.isna().mean().round(2)*100)



def analisis_rapido4eda(df_merged):
    """
    Muestra un resumen estadístico estructurado en tres bloques:
    1. Indicadores de ranking
    2. Visión general educativa (illiterate vs literate)
    3. Desglose por niveles educativos
    """
    
    # --- Bloque 1: Indicadores de ranking ---
    cols_ranking = ['Score_mean', 'Rank_mean', 'TLR_mean', 'RPC_mean',
                    'GO_mean', 'OI_mean', 'PERCEPTION_mean', 'n_institutos']
    
    print("=" * 50)
    print("INDICADORES DE RANKING")
    print("=" * 50)
    display(df_merged[cols_ranking].describe().T.round(2))
    
    # --- Bloque 2: Visión general educativa ---
    cols_educ_resumen = [
        'illiterate_persons_rate',
        'literate_persons_rate'
    ]
    
    print("\n" + "=" * 50)
    print("VISIÓN GENERAL EDUCATIVA")
    print("=" * 50)
    display(df_merged[cols_educ_resumen].describe().T.round(4))
    
    # --- Bloque 3: Desglose por niveles educativos ---
    cols_educ_detalle = [
        'illiterate_persons_rate',
        'literate_w_o_education_level_persons_rate',
        'bellow_primary_persons_rate',
        'primary_persons_rate',
        'middle_persons_rate',
        'matric_secondary_persons_rate',
        'graduate_persons_rate'
    ]
    
    print("\n" + "=" * 50)
    print("DESGLOSE POR NIVELES EDUCATIVOS")
    print("=" * 50)
    display(df_merged[cols_educ_detalle].describe().T.round(4))


