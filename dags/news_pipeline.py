from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'fakhri',
    'start_date': days_ago(1),
}

with DAG(dag_id="fake_news_pipeline", default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    scrape = BashOperator(
        task_id="scrape_news",
        bash_command="python /opt/airflow/scripts/scrape_news.py"
    )

    clean = BashOperator(
        task_id="clean_news",
        bash_command="python /opt/airflow/scripts/clean_news.py"
    )

    scrape >> clean
