# Questions: 1_my_first_airflow 

:pencil2: 1-What is the python type of Documentation ?

:pencil2: 2-What are the main components of a Airflow Dag ?

3-Navigate to Airflow interface and find the embedded Airflow doc, tell me which part of the code is responsible for displaying it.

4-Trigger the dag and navigate to the logs, find what was printed in the job. Show all the logs.

5-Change the scheduling of the dag, and set it up to run every Monday of the week at 6am UTC.

6-Turn the dag off, then trigger the Airflow job. 
Did is got triggered ?

7-Dag failure. Change the following line
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
Give me the state of each task and ind the error message and paste it here.

Move the `print(a)` to the print_hello with chaining activated.
After triggering the job give me the state of each task. 

7-Naming convention, what it is and why it is useful ? 
Look at the PythonOperator, can you deduct a naming convention from this 2 examples, what it is ?

Play and modify the Operator name, task_id and the python_callable to fully understand what each of them refer too


8-Dependecencies: Modify the following line, what is the difference ? (Hint you will have to go to the Graph tab)

Replace 
```
print_hello_op >> print_goodbye_op
``` 

With
```
print_hello_op
``` 
Is the task `print_goodbye_op` still executed ?

Remove the line completley, is the dag still executed ?

9-Many job appearing in Airflow that are not yours. Find the parameters that turn off the example dags in the configs. (Hint: you may have to rebuild the image)

