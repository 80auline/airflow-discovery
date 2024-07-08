""" 
An example of job that pass content between one task to another
https://marclamberti.com/blog/airflow-xcom/
"""

from datetime import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def create_first_string():
    """Create a first string and return it"""
    beginning_string = "Hello World!"
    #TODO: return the beginning_string


def final_string_log():
    """Add content to string and log it"""
    #TODO: Retrieve the value from previous task in beginning_string
    string_to_log = beginning_string + "Goodbye!"
    logging.info(string_to_log)


dag = DAG(
    f"2_passing_data_between_tasks",
    schedule_interval="0 9 * * 1",
    start_date=datetime(2024, 1, 1),
    catchup=False
)
dag.doc_md = __doc__

with dag:

    create_first_string_op = PythonOperator(
        task_id='create_first_string',
        python_callable=create_first_string
    )

    final_string_log_op = PythonOperator(
        task_id='final_string_log',
        python_callable=final_string_log
    )

create_first_string_op >> final_string_log_op
