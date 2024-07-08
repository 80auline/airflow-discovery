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
```""" 
Doc-string explaining was the job is doing
\n My first Airflow job
"""
```

Middle of the file, after dag definition: 
```
dag.doc_md = __doc__
```

:white_check_mark: 4-Trigger the dag and navigate to the logs, find what was printed in the job. Show all the logs.



:white_check_mark: 5-Change the scheduling of the dag, and set it up to run every Monday at 6am UTC.

:white_check_mark: 6-Turn the dag off, then trigger the Airflow job. 
Did it trigger the job ?


:white_check_mark: 7-Dependencies: Modify the following line, what is the difference ? (Hint you will have to go to the Graph tab)


:white_check_mark: 8-Dag failure. Change the following line



:white_check_mark: 9-Naming convention, what it is and why it is useful ? 



:white_check_mark: 10-Many jobs appearing in Airflow that are not yours (like `example_bash_decorator`). Find the parameters that turn off the example dags in the configs. (Hint: you may have to rebuild the image)

