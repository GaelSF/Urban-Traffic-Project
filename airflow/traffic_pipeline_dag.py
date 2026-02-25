from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="traffic_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    simulate = BashOperator(
        task_id="simulate",
        bash_command="python -m src.simulation.traffic_simulation"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python -m src.transformation.transform_data"
    )

    load = BashOperator(
        task_id="load_to_db",
        bash_command="python -m src.ingestion.load_to_db"
    )

    simulate >> transform >> load