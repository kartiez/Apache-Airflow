import feedparser
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from textblob import TextBlob as tb
import re
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

def firstfunction():
    print('First function executed')

def secondfunction():
    print('Second function executed')

dag = DAG(
    'DAG1',
    default_args=default_args,
    description='Test DAG',
    schedule_interval=timedelta(minutes=1),
)

# YOUR FIRST TASK GOES HERE

t1 = PythonOperator(
    task_id='t1',
    depends_on_past=False,
    python_callable=firstfunction,
    #op_kwargs={ SPECIFY ARGUMENTS HERE },
    # retries=3,
    dag=dag,
)

# YOUR SECOND TASK GOES HERE

t2 = PythonOperator(
    task_id='t2',
    depends_on_past=False,
    python_callable=secondfunction,
    #op_kwargs={'SPECIFY ARGUMENTS HERE},
    # retries=3,
    dag=dag,
)
