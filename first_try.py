from airflow import DAG
from airflow.decorators import task
from dict import diccionario_datos
import functions_ift as f

with DAG(dag_id="prueba",schedule=None) as dag:
    @task
    def task_1():
        nombre = "TD_LINEAS_INTMOVIL_ITE_VA"
        prueba = f.download_files(nombre)
        return prueba 
    task_1()
