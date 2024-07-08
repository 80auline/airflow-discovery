 # Table of content:
 - [Questions: :snake: 1_my_first_airflow ](#item-one)
 - [Questions: :snake: 2_passing_parameters_between_dags ](#item-two)
 

 
<a id="item-one"></a>
## Questions: :snake: 1_my_first_airflow 

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
## Questions: :snake: 2_passing_parameters_between_dags 

:pencil2: 1-What it the difference between `print` and `logging` ?

:pencil2: 2-using logging add - error
Compare the formatting in the logs
```
    beginning_string = "Hello World!"
    print(beginning_string)
    logging.info(beginning_string)
```

what is the difference when you use `logging.error`?
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

:pencil2: 4-Modify the code so `create_first_string` return a string and `final_string_log` print it.

:pencil2: 5-Why do you need to break code into task in Airflow?

`1 dag with 1 big task vs 1 dag with multiple task` 

:pencil2: 6-Can I use it for a really large dataframe for example ?


:pencil2: 7-Is it better to save it locally in a file, for a dataframe with `df.to_csv()` ?







