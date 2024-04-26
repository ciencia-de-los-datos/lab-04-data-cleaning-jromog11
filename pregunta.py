"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def convertir_a_formato_fecha(fecha):
    try:
        return pd.to_datetime(fecha, format="%d/%m/%Y")
    except:
        return pd.to_datetime(fecha, format="%Y/%m/%d")


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    df = df.copy()
    df = df.dropna()
    df = df.drop(columns=["Unnamed: 0"])
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["barrio"] = df["barrio"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["estrato"] = df["estrato"].astype(int)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(convertir_a_formato_fecha)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(
        r"[^\d.]", "", regex=True
    )
    df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df = df.drop_duplicates()

    return df
