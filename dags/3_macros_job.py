""" 
An example of job that use macros
[Macros Doc](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)
"""

from datetime import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def string_with_macro(macro_variable):
    """Get the macro and print it
    """
    string_macro = f"""Hello World! 
        The macros is: <to_replace>"""
    logging.info(string_macro)



dag = DAG(
    f"3_job_using_macro",
    schedule_interval="*/30 * * * *",
    start_date=datetime(2023, 4, 14),
    catchup=False
)

with dag:

    string_with_macro_op = PythonOperator(
        task_id='string_with_macro',
        python_callable=string_with_macro,
        op_kwargs={
            "macro_variable": "{{ ts }}"
        }
    )

# no dependency no need to put anything here