""" 
Doc-string explaining was the job is doing
\n My first Airflow job
"""


from datetime import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_hello():
    """Logging hello world"""
    logging.info("Hello World!")


def print_goodbye():
    """Logging goodbye"""
    logging.info("Goodbye!")



dag = DAG(
    f"1_my_first_dag",
    schedule_interval="@daily",
    start_date=datetime(2024, 4, 14),
    catchup=False
)
dag.doc_md = __doc__

with dag:

    print_hello_op = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    print_goodbye_op = PythonOperator(
        task_id='print_goodbye',
        python_callable=print_goodbye
    )

print_hello_op >> print_goodbye_op

