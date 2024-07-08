# Answers: :snake: 1_my_first_airflow 

:white_check_mark: 1-What are the different tyepe of python documentation ?
- README
- Dag description
- function description
- Comments
- Logging

Get more information with real life example: here

https://realpython.com/documenting-python-code/

:white_check_mark: 2-What are the main components of an Airflow Dag ?

**Tasks**: These are the individual units of work that your workflow performs. Tasks can be anything from Python functions to calling external APIs or running shell commands. Each task has its own definition, which specifies what it does and how it should be executed.

**Dependencies**:  Airflow DAGs are directed acyclic graphs, meaning tasks can have dependencies on other tasks. This allows you to define the order in which tasks should be executed. For example, a task that analyzes data might depend on a task that extracts the data first.

**Operators**:  Operators are blueprints for how tasks are executed. Airflow provides a rich set of built-in operators for common tasks, such as BashOperator for running shell commands, PythonOperator for running Python functions, and many more. You can also create custom operators for specific needs.

**Schedule**:  A DAG defines how often it should be run. You can schedule a DAG to run on a specific date and time, at regular intervals (e.g., every hour, daily), or based on cron expressions for more complex scheduling needs.

**XComs** (XCom stands for "Execution Results"):  These are a way for tasks to share data with each other. Tasks can store their output data as XComs, which can then be accessed by other tasks in the DAG. This allows you to pass data between tasks and build complex workflows.

**Variables**: Airflow variables are a way to store and reuse configuration values within your DAGs. This allows you to keep sensitive information like API keys out of your code and manage them centrally.

:white_check_mark: 3-Navigate to the Airflow interface and find the embedded Airflow doc, tell me which part of the code is responsible for displaying it.

Top of the file: 
```
""" 
Doc-string explaining was the job is doing
\n My first Airflow job
"""
```

Middle of the file, after dag definition: 
```
dag.doc_md = __doc__
```

:white_check_mark: 4-Trigger the dag and navigate to the logs, find what was printed in the job. Show all the logs.

```
1e28794e2c6c
*** Found local files:
***   * /opt/airflow/logs/dag_id=1_my_first_dag/run_id=scheduled__2024-07-06T00:00:00+00:00/task_id=print_hello/attempt=1.log
[2024-07-07, 02:54:05 UTC] {local_task_job_runner.py:120} ▶ Pre task execution logs
[2024-07-07, 02:54:05 UTC] {1_my_first_airflow.py:16} INFO - Hello World!
[2024-07-07, 02:54:05 UTC] {python.py:237} INFO - Done. Returned value was: None
[2024-07-07, 02:54:05 UTC] {taskinstance.py:441} ▶ Post task execution logs
```

:white_check_mark: 5-Change the scheduling of the dag, and set it up to run every Monday at 6am UTC.

https://crontab.guru/every-monday

:white_check_mark: 6-Turn the dag off, then trigger the Airflow job. 
Did it trigger the job ?


:white_check_mark: 7-Dependencies: Modify the following line, what is the difference ? (Hint you will have to go to the Graph tab)


:white_check_mark: 8-Dag failure. 



:white_check_mark: 9-Naming convention, what it is and why it is useful ? 

In programming, a naming convention is a set of rules that define how you should name things like variables, functions, classes, and other elements in your code. These rules create a consistent and predictable way to structure your code, making it easier to understand for both you and other programmers.

Here's why naming conventions are important:

**Readability**: Consistent naming makes code easier to read and understand. Imagine if every variable had a random name! It would be like trying to follow a conversation where everyone uses nicknames you don't recognize.
**Maintainability**: When code is well-named, it's easier to modify and fix bugs later on. You (or someone else) can quickly grasp what a piece of code does by looking at the names used.
**Collaboration**: If multiple programmers are working on the same project, a shared naming convention ensures everyone is on the same page. It reduces confusion and makes collaboration smoother.
**Standard Practices**: Many programming languages and frameworks have their own recommended naming conventions. Following these conventions shows you understand best practices and makes your code more compatible with others' work.

Convention in the python file:
```
PythonOperator = <name_function>_op
task_id = <name_function>
python_callable = <name_function>
```
Exemple
```
PythonOperator = print_hello_op
task_id = print_hello
python_callable = print_hello
```

:white_check_mark: 10-Many jobs appearing in Airflow that are not yours (like `example_bash_decorator`). Find the parameters that turn off the example dags in the configs. (Hint: you may have to rebuild the image)

