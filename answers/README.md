 # Table of content:
 - [Answers: :snake: 1_my_first_airflow ](#item-one)
 - [Answers: :snake: 2_passing_parameters_between_dags ](#item-two)
 - [Answers: :snake: 3_job_using_macro ](#item-three)
 - [Answers: :snake: 4_passing_parameters_on_trigger ](#item-four)

 
<a id="item-one"></a>
# Answers: :snake: 1_my_first_airflow 

:white_check_mark: 1-What are the different tyepe of python documentation ?
- README
- Dag description
- function description
- Comments
- Logging

Get more information with real life example: [here](https://realpython.com/documenting-python-code/)

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
run_id=scheduled__2024-07-06T00:00:00+00:00/task_id=print_hello/attempt=1.log
[2024-07-07, 02:54:05 UTC] {local_task_job_runner.py:120} ▶ Pre task execution logs
[2024-07-07, 02:54:05 UTC] {1_my_first_airflow.py:16} INFO - Hello World!
[2024-07-07, 02:54:05 UTC] {python.py:237} INFO - Done. Returned value was: None
[2024-07-07, 02:54:05 UTC] {taskinstance.py:441} ▶ Post task execution logs
```

:white_check_mark: 5-Change the scheduling of the dag, and set it up to run every Monday at 6am UTC.

```
schedule_interval="0 6 * * 1"
```

Cron info [here](https://crontab.guru/every-monday)
Airflow scheduling [here](https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html)

:white_check_mark: 6-Turn the dag off, then trigger the Airflow job. 
Did it trigger the job ?

When triggering the job it automatically turn on the dag. You need to be careful to avoid clicking multiple times.


:white_check_mark: 7-Dependencies: Modify the following line, what is the difference ? (Hint you will have to go to the Graph tab)

Dependency is removed between the 2 tasks, they will run in parallel.

:white_check_mark: 8-Dag failure. 

When added in function `print_goodbye()`
```
print_hello = green - successful
print_goodbye = red - failed
```

When added in function `print_hello()`
```
print_hello = red - failed
print_goodbye = orange - upstream failed
```
The dependent task is not execute due to failure upstream.


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

:white_check_mark: 10-Many jobs appearing in Airflow that are not yours (like `example_bash_decorator`). Find the parameters that turn off the example dags in the configs.

```
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
```

<a id="item-two"></a>
# Answers: :snake: 2_passing_parameters_between_dags 

:white_check_mark: 1-What it the difference between `print` and `logging` ?

**Print:**

**Purpose**: Print is a simple function used for temporary output during development or debugging. It typically displays information directly to the console where you're running your program.
**Use Cases**:
Printing variable values or intermediate results to see how your code is behaving step-by-step.
Checking if a specific part of your code is executing as expected.
**Limitations**:
Print statements are not meant to be part of the final production code. They can clutter the output and make it harder to read.
Print statements don't offer any logging functionality, like recording timestamps or logging levels (e.g., error, warning, info).
Information printed might be lost or difficult to track after the program finishes execution.

**Logging:**

**Purpose:** Logging is a more robust and structured way to record information about your program's execution. It typically writes messages to log files or other destinations like databases.
**Use Cases:**
Recording important events or errors that occur during program execution for later analysis.
Tracking the performance of your program and identifying bottlenecks.
Auditing user actions and program behavior for troubleshooting or security purposes.
**Advantages:**
Logs are persistent and can be reviewed even after the program finishes running.
Logging libraries offer features like different logging levels (error, warning, info, debug) to categorize the importance of messages.
Logs can be formatted to include additional information like timestamps, thread names, and custom details.
Logs can be directed to different destinations based on their severity or purpose.

```
[2024-07-08, 4:20:07 UTC] {logging_mixin.py:188} INFO - Hello World!
[2024-07-08, 4:20:07 UTC] {2_passing_parameters_between_dags.py:17} INFO - Hello World!
```

:white_check_mark: 2-What is the difference when you use `logging.error` ?
```
[2024-07-08, 18:22:27 UTC] {2_passing_parameters_between_dags.py:16} ERROR - Hello World!
```
Using `logging.error` alone within an Airflow task doesn't necessarily cause the task to fail. Here's why:
- Logging vs Exceptions:  logging.error is primarily used for recording error messages during program execution. It doesn't inherently trigger task failures. Exceptions, on the other hand, are designed to signal errors that halt program execution.
- Airflow Task Operators:  Airflow tasks are typically implemented using operators like PythonOperator, BashOperator, etc. These operators capture the exit code of the underlying process (Python script, bash command, etc.) launched by the task.

:white_check_mark: 3-How do you combine string and a value in the logging ?
```
    logging.info(f"{string_to_log} Goodbye!")
```

f-string info and example: [here](https://builtin.com/data-science/python-f-string)

:white_check_mark: 4-Modify the code so `create_first_string` return a string and `final_string_log` log it.

You can use either Xcom or TaskFlow.

References: [Xcom link 1](https://marclamberti.com/blog/airflow-%20wh/), [Xcom link 2](https://ganguly-04.medium.com/using-xcoms-in-airflow-scenario-based-examples-with-code-2edcd6e10501), [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
```
def create_first_string(ti): # Modified
    """Create a first string and return it"""
    beginning_string = "Hello World!"
    ti.xcom_push(key="key_beginning_string", value=beginning_string) # New
    return beginning_string


def final_string_log(ti): # Modified
    """Add content to string and log it"""
    beginning_string = ti.xcom_pull(task_ids="create_first_string",key='key_beginning_string')  # New
    string_to_log = beginning_string + "Goodbye!"
    logging.info(string_to_log)

```



:white_check_mark: 5-Why do you need to break code into task in Airflow?

**Improved Modularity and Maintainability:**
- Smaller, focused tasks: Breaking down a large workflow into smaller, well-defined tasks makes your DAG easier to understand, maintain, and modify. You can focus on changing specific tasks without affecting the entire workflow.
- Reusability: Smaller tasks can be reused across different DAGs, promoting code reuse and reducing redundancy.

**Enhanced Control and Monitoring:**
- Independent execution: Tasks can be run independently, allowing for better parallelization and improved performance for large workflows.
- Granular monitoring: You can monitor the status and progress of individual tasks within the DAG, making it easier to identify and troubleshoot any issues.
- Task dependencies: Define clear dependencies between tasks, ensuring tasks are executed in the correct order and only when their prerequisites are met.

**Error Handling and Retries:**
- Isolate failures: If a task fails, it won't necessarily bring down the entire DAG. You can configure retries for individual tasks, allowing them to automatically recover from transient errors.
- Easier debugging: By isolating failures to specific tasks, it's easier to debug and fix the issue without needing to restart the entire workflow.

**Scalability and Performance:**
- Parallelization: Breaking down complex tasks allows for parallelizing some or all of the tasks in your DAG, leading to faster execution for large workflows.
- Distributed execution: Airflow can be configured to run tasks on different workers, further improving scalability for resource-intensive workflows.

Overall, breaking down a DAG into multiple tasks makes your Airflow workflows more manageable, maintainable, and scalable.

:white_check_mark: 6-Can I use it for a really large dataframe for example ?

It's generally not recommended to pass large amounts of data directly between tasks in Airflow using XComs (Airflow's built-in mechanism for sharing data between tasks). Here's why:

Limitations of XComs:
- Size limitations: XComs have a size limit (configurable, but typically in the megabyte range). Transferring large datasets can easily exceed this limit.
- Performance overhead: Serializing and deserializing large data objects for XCom storage can be slow and impact the performance of your DAG.
- Scalability issues: When dealing with large data volumes, Airflow workers might struggle to handle the XCom storage and retrieval.

:white_check_mark: 7-Is it better to save it locally in a file, for a dataframe with df.to_csv() ?

The file will be store in the Airflow machine, if you don't have access to the Airflow machine where the file is stored, then saving it locally won't work.
If you data is large and you need to break the dag into task, temporarly saving it to a cloud storage (S3, GCP storage) can be a solution.

Make sure to have regular cleaning to avoid cluttering, you can set up automatic deletion, or overwrite the file each time (depends on you need to keep the history).



<a id="item-three"></a>
# Answers: :snake: 3_job_using_macro 

:white_check_mark: 1-Open the [Macros Doc](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) and play with the variable, run the job and see what you get from the log. Print the logs below.

```
[2024-07-13, 07:23:06 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 2024-07-23T07:23:04.803334+00:00
```

```
[2024-07-13, 07:24:51 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 2024-07-23
```

```
[2024-07-13, 07:26:36 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 20240723T072635
```

ps: we will focus in this part around ts and ds, other varible specificity will not be covered.

:white_check_mark: 2-Change the scheduling to every 5 minutes, compare it with the run timestamp and understand how the `ts` variable behave. You can also change the scheduling to every 10 minutes and see if the behaviour you understood is correct.

```
[2024-07-23, 07:30:01 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 2024-07-23T07:25:00+00:00
```

```
[2024-07-23, 07:35:00 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 2024-07-23T07:30:00+00:00
```

```
[2024-07-23, 07:40:01 UTC] {3_macros_job.py:18} INFO - Hello World! 
        The macros is: 2024-07-23T07:35:00+00:00
```

`ts` provides a timestamp, it doesn't represent the exact start of the task's execution, you need to substract the scheduling frequency.

:white_check_mark: 3-Macros and dag failure: Add a line to make the dag fail, then fix the code and clear the dag (use `clear` instead of trigger). 

Is the macro variable the correct value you expected or it changed due to the failure ?

The macro is correct, the failure did not have an impact on the value.

:white_check_mark: 4-What is incremental load vs full load in the context of an ETL ?

**Full Load**

A full load in ETL (Extract, Transform, Load) involves loading the entire dataset from the source system into the target system. This is like copying all the files from one folder to another.
- **Pros**: Simple to implement, ensures data consistency.
- **Cons**: Resource-intensive, time-consuming, especially for large datasets.

**Incremental Load**

An incremental load only loads the changes that have occurred in the source data since the last load. It's like only copying the new or modified files from one folder to another.
- **Pros**: Faster, more efficient, reduces system load.
- **Cons**: Requires tracking changes in the source system, can be more complex to implement.


When to Use Which:

**Full Load**
- Initial data load into a new target system.
- When data volume is relatively small.
- When data changes infrequently.

**Incremental Load**:
- Large datasets with frequent updates.
- Real-time or near-real-time data processing.
- When data consistency is critical and you need to reflect changes quickly.


:white_check_mark: 5-Let's say that now the variable is used to run a sql query in a daily fashion and we use `ds` as a filtering variable. 

Code:
```
def string_with_macro(macro_variable):
    """Get the macro and print it
    """
    sql_to_execute = f"""
        SELECT 
            order_id
            , customer_id 
            , item_name
            , catalog_category
        FROM `events_production.order_created`
        WHERE events >= DATE('{macro_variable}')"""
    logging.info(sql_to_execute)
```


What is the difference between using `CURRENT_DATE()`, like in the following code ?

Code:
```
def string_with_macro(macro_variable):
    """Get the macro and print it
    """
    sql_to_execute = f"""
        SELECT 
            order_id
            , customer_id 
            , item_name
            , catalog_category
        FROM `events_production.order_created`
        WHERE events >= CURRENT_DATE()"""
    logging.info(sql_to_execute)
```

**Airflow Macros**: Airflow macros provide dynamic values that are evaluated at runtime, allowing you to create flexible and adaptable DAGs.

**SQL CURRENT_DATE()**: Returns the current date within the database at the time the SQL query is executed.

:white_check_mark: 6-Sql execution and failure: We have a ETL job running a sql query every day at 8am where data from yesterday is processed. 

The job fails and it take you hours to debug it, you finally find the error and push you code at 1am (next day). You rerun the task that failed. 

Use your understanding to fill the last line for each case below.

`ds`
```
2024-02-02 08:00:00: filtering events_ts >= 2024-02-01 successful
2024-02-03 08:00:00: filtering events_ts >= 2024-02-02 successful
2024-02-04 08:00:00: filtering events_ts >= 2024-02-03 successful
2024-02-05 08:00:00: filtering events_ts >= 2024-02-04 FAILED
2024-02-06 01:00:00: filtering events_ts >= 2024-02-04 successful
```

`CURRENT_DATE`
```
2024-02-02 08:00:00: filtering events_ts >= (2024-02-02 - 1 day) successful
2024-02-03 08:00:00: filtering events_ts >= (2024-02-03 - 1 day) successful
2024-02-04 08:00:00: filtering events_ts >= (2024-02-04 - 1 day) successful
2024-02-05 08:00:00: filtering events_ts >= (2024-02-05 - 1 day) FAILED
2024-02-06 01:00:00: filtering events_ts >= (2024-02-06 - 1 day) successful
```

`ds` -> events_ts >= 2024-02-04

`CURRENT_DATE` ->  filtering events_ts >= 2024-02-05

With Current data you will have process more data that you should. These data will be processed again at 8am when you normal scheduling gets trigger. If you did not take this into consideration when designing your ETL you can face duplicated data in your table. 


<a id="item-four"></a>
# Answers: :snake: 4_passing_parameters_on_trigger

:pencil2: 1-Trigger manually the job, then modify the following line and trigger manually the job again. 

```
dag = DAG(
    f"4_passing_parameters",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    params={
        "my_param": 6 # New
    }
)
````

You should be redirected to a new page, allowing you to specify a value.

Modify the value with an `integer` or a `string` and see what is displayed in the logs.

```
[2024-07-23, 08:37:00 UTC] {4_passing_parameters_on_trigger.py:18} INFO - Hello World! 
    Manual Trigerring with Params: {'my_param': 10}
```

You can not use a string, because the default value provided is `6`, the code induce that the type expected is an integer. Float do not work neither.

:pencil2: 2-Explicitly define the type of the variable and a default value.

```
    params={
        "int_param": Param(10, type="integer"),
        "string_param": Param(5, type="string")
    }
```

Logs
```
[2024-07-23, 08:50:02 UTC] {4_passing_parameters_on_trigger.py:18} INFO - Hello World! 
    Manual Trigerring with Params: {'int_param': 10, 'string_param': '5'}
```

```
[2024-07-23, 08:50:49 UTC] {4_passing_parameters_on_trigger.py:18} INFO - Hello World! 
    Manual Trigerring with Params: {'int_param': 1000, 'string_param': 'test'}
```

:pencil2: 3-For the integer parameter add a minimum and a maximum.

```
    params={
        "int_param": Param(10, type="integer", minimum=0, maximum=20),
        "string_param": Param(5, type="string")
    }
```

:pencil2: 4-Modify the code `string_with_params` function to grab the value directly.

```
def string_with_params(**context):
    """Get the macro and print it"""
    string_params = f"""Hello World! 
        Manual Trigerring with Params: {context["params"]}
        My int_param is <to_fill>
        My string_param is <to_fill>"""
    logging.info(string_params)
```

Code
```
def string_with_params(**context):
    """Get the macro and print it"""
    string_params = f"""Hello World! 
    Manual Trigerring with Params: {context["params"]}
    My int_param is {context["params"]["int_param"]}
    My string_param is {context["params"]["string_param"]}"""
    logging.info(string_params)
```

Logs
```
[2024-07-23, 08:54:29 UTC] {4_passing_parameters_on_trigger.py:20} INFO - Hello World! 
    Manual Trigerring with Params: {'int_param': 10, 'string_param': '5'}
    My int_param is 10
    My string_param is 5

```

:pencil2: 5-Build a code to run a sql, the filter should be conditional to a parameter. 

**daily_load**: normal behaviour, sql filter is build using the `ds` macro.

**backfill_date**: manual trigerring, sql filter is overwritten with the date provided.

```
def string_with_params(macro_variable, **context):
    if context["params"]["job_mode"] == "daily_run":
        date_filter = macro_variable
    elif context["params"]["job_mode"] == "backfill_run":
        date_filter = context["params"]["backfill_date"]

    sql_to_execute = f"""
        SELECT 
            order_id
            , customer_id 
            , item_name
            , catalog_category
        FROM `events_production.order_created`
        WHERE events >= DATE('{date_filter}')"""
    logging.info(sql_to_execute)


dag = DAG(
    f"4_passing_parameters",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    params={
        "job_mode": Param("daily_run", enum=["daily_run", "backfill_run"]),
        "backfill_date": Param(f"1999-01-01", type="string", format="date") # Only used when backfill is triggered
    }
)
```

Logs for `Daily Load`
```
[2024-07-23, 09:10:19 UTC] {4_passing_parameters_on_trigger.py:30} INFO - 
        SELECT 
            order_id
            , customer_id 
            , item_name
            , catalog_category
        FROM `events_production.order_created`
        WHERE events >= DATE('2024-07-23')
```

Logs for `Backfilling`
```
[2024-07-23, 09:11:13 UTC] {4_passing_parameters_on_trigger.py:30} INFO - 
        SELECT 
            order_id
            , customer_id 
            , item_name
            , catalog_category
        FROM `events_production.order_created`
        WHERE events >= DATE('2024-01-01')
```

:pencil2: 6-Do you see disaventages of doing this way ?

In the interface there is not way to see if it was a daily load or a backfill, you need to go to the logs to see it.

A date parameter is given but not used in the daily load, it can be source of confusion.