""" 
An example of job that pass parameters on trigger
[Params Doc](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html)
"""

from datetime import datetime
import logging

from airflow import DAG
from airflow.models.param import Param
from airflow.operators.python_operator import PythonOperator


def string_with_params(**context):
    """Get the macro and print it"""
    string_params = f"""Hello World! 
    Manual Trigerring with Params: {context["params"]}"""
    logging.info(string_params)


dag = DAG(
    f"4_passing_parameters",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    params={

    }
)

with dag:

    string_with_params_op = PythonOperator(
        task_id='string_with_params',
        python_callable=string_with_params
    )

# no dependency no need to put anything here