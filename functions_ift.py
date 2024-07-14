import polars as pl
from io import StringIO
import requests

def download_files(table_name: str) -> pl.DataFrame:
    url = f"https://bit.ift.org.mx/descargas/datos/tabs/{table_name}.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"Error inesperado: {e}")
    
    response.encoding = 'utf-8'
    csv_string = StringIO(response.text)
    
    return pl.read_csv(csv_string)
    
def tweak_df(df: pl.DataFrame, columns_transformations: list, schema: dict) -> pl.DataFrame:
  # aplicación de funciones para el df
  # acepta lista de expresiones
  return df.with_columns(columns_transformations).cast(schema)

def dict_to_df(dict):
    return pl.from_dict(dict)
