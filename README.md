# Apache-Airflow
Simple Apache Airflow - With Example

## How setup Apache Airflow - GCP Machine

### 1. Get a new machine or create a Virtual Environment

If new machine > Install pip and execute the below commands :
```sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip
export SLUGIFY_USES_TEXT_UNIDECODE=yes
```
### 2. Install Airflow

```
pip install apache-airflow
```
NOTE : Restarted the machine after installing

### 3. Create a Configuration file
```
export AIRFLOW_HOME=`pwd` airflow_home
```
### 4. Create Database

```
airflow initdb
```

### 5. Upload the script.py file to the machine

In the code, the tasks t1 and t2 are executed simultaneously.


If you want to execute t2 after t1 then add the below piece of code to the bottom of the python file.

```
t1.set_upstream(t2) #
```
### 6. Start Airflow Service
```
airflow webserver
```

### 7. Start Scheduler
```
airflow scheduler
```

## Completed
