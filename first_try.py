from airflow import DAG
from airflow.decorators import task

with DAG(dag_id="prueba",schedule=None) as dag:
    @task
    def task_1():
        return "esta es la primera prueba"
