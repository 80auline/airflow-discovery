# Questions: 1_my_first_airflow 

:pencil2: 1-What are the different tyepe of python documentation ?

:pencil2: 2-What are the main components of an Airflow Dag ?

:pencil2: 3-Navigate to the Airflow interface and find the embedded Airflow doc, tell me which part of the code is responsible for displaying it.

:pencil2: 4-Trigger the dag and navigate to the logs, find what was printed in the job. Show all the logs.

:pencil2: 5-Change the scheduling of the dag, and set it up to run every Monday at 6am UTC.

:pencil2: 6-Turn the dag off, then trigger the Airflow job. 
Did it trigger the job ?


:pencil2: 7-Dependencies: Modify the following line, what is the difference ? (Hint you will have to go to the Graph tab)

Replace 
```
print_hello_op >> print_goodbye_op
``` 

With
```
print_hello_op
``` 
Is the task `print_goodbye_op` still executed ?

Remove the line completely, are both tasks still executed ?


:pencil2: 8-Dag failure. Change the following line

Replace
```
def print_goodbye():
    """Logging goodbye"""
    logging.info("Goodbye!")
```
With
```
def print_goodbye():
    """Logging goodbye"""
    print(a)
    logging.info("Goodbye!")
```
Give me the state of each task and the error message.

Move the `print(a)` to the `print_hello` with chaining activated.
After triggering the job, give me the state of each task. 

:pencil2: 9-Naming convention, what it is and why it is useful ? 

Look at the `PythonOperator`, can you deduct a naming convention from these 2 examples, what is it ?

Play and modify the `Operator name`, `task_id` and the `python_callable` to fully understand what each of them refer to.


:pencil2: 10-Many jobs appearing in Airflow that are not yours (like `example_bash_decorator`). Find the parameters that turn off the example dags in the configs. (Hint: you may have to rebuild the image)

