 # Table of content:
 - [Questions: :snake: 1_my_first_airflow ](#item-one)
 - [Questions: :snake: 2_passing_parameters_between_dags ](#item-two)
 - [Questions: :snake: 3_job_using_macro ](#item-three)
 


<a id="item-one"></a>
# Questions: :snake: 1_my_first_airflow 

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

<a id="item-two"></a>
# Questions: :snake: 2_passing_parameters_between_dags 

:pencil2: 1-What it the difference between `print` and `logging` ?

Compare the formatting in the logs
```
    beginning_string = "Hello World!"
    print(beginning_string)
    logging.info(beginning_string)
```

:pencil2: 2-What is the difference when you use `logging.error` ?
```
    beginning_string = "Hello World!"
    logging.error(beginning_string)
```

:pencil2: 3-How do you combine string and a value in the logging ?

How to simplify the line below in only 1 line:
```
    string_to_log = beginning_string + "Goodbye!"
    logging.info(string_to_log)
```

:pencil2: 4-Modify the code so `create_first_string` return a string and `final_string_log` log it.

You can use either Xcom or TaskFlow.

References: [Xcom link 1](https://marclamberti.com/blog/airflow-%20wh/), [Xcom link 2](https://ganguly-04.medium.com/using-xcoms-in-airflow-scenario-based-examples-with-code-2edcd6e10501), [TaskFlow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)

:pencil2: 5-Why do you need to break code into task in Airflow?

`1 dag with 1 big task vs 1 dag with multiple task` 

:pencil2: 6-Can I use it for a really large dataframe for example ?


:pencil2: 7-Is it better to save it locally in a file, for a dataframe with `df.to_csv()` ?



<a id="item-three"></a>
# Questions: :snake: 3_job_using_macro 

:pencil2: 1-Open the [Macros Doc](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) and play with the variable, run the job and see what you get from the log. 

Print the logs below.

ps: we will focus in this part around ts and ds, other varible specificity will not be covered.

:pencil2: 2-Change the scheduling to every 5 minutes, compare it with the run timestamp and understand how the `ts` variable behave. 

You can also change the scheduling to every 10 minutes and see if the behaviour you understood is correct.

:pencil2: 3-Macros and dag failure: Add a line to make the dag fail, then fix the code and clear the dag (use `clear` instead of trigger). 

Is the macro variable the correct value you expected or it changed due to the failure ?


:pencil2: 4-What is incremental load vs full load in the context of an ETL ?


:pencil2: 5-Let's say that now the variable is used to run a sql query in a daily fashion and we use `ds` as a filtering variable. 

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

:pencil2: 6-Sql execution and failure: We have a ETL job running a sql query every day at 8am where data from yesterday is processed. 

The job fails and it take you hours to debug it, you finally find the error and push you code at 1am (next day). You rerun the task that failed. 

Use your understanding to fill the last line for each case below.

`ds`
```
2024-02-02 08:00:00: filtering events_ts >= 2024-02-01 successful
2024-02-03 08:00:00: filtering events_ts >= 2024-02-02 successful
2024-02-04 08:00:00: filtering events_ts >= 2024-02-03 successful
2024-02-05 08:00:00: filtering events_ts >= 2024-02-04 FAILED
2024-02-06 01:00:00: <to fill - using rerun task not trigger>
```

`CURRENT_DATE`
```
2024-02-02 08:00:00: filtering events_ts >= (2024-02-02 - 1 day) successful
2024-02-03 08:00:00: filtering events_ts >= (2024-02-03 - 1 day) successful
2024-02-04 08:00:00: filtering events_ts >= (2024-02-04 - 1 day) successful
2024-02-05 08:00:00: filtering events_ts >= (2024-02-05 - 1 day) FAILED
2024-02-06 01:00:00: <to fill - using rerun task not trigger>
```


