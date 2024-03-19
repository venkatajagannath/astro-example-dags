from airflow.providers.amazon.aws.operators.eks import EksCreateClusterOperator
from airflow import DAG
from airflow.models.connection import Connection
from datetime import datetime
import os

# Define the AWS connection
conn = Connection(
    conn_id="aws_demo",
    conn_type="aws",
    extra={
        "config_kwargs": {
            "signature_version": "unsigned",
        },
    },
)

# Set the connection URI in the environment variable
env_key = f"AIRFLOW_CONN_{conn.conn_id.upper()}"
conn_uri = conn.get_uri()
os.environ[env_key] = conn_uri

# Define the DAG
with DAG(
    dag_id="eks_create_cluster_dag",
    schedule_interval=None,  # set to None if you want it to run only once
    start_date=datetime(2023, 1, 1),
    is_paused_upon_creation=False,
    catchup=False,
) as dag:
    
    # Create an instance of EksCreateClusterOperator
    create_cluster_task = EksCreateClusterOperator(
        task_id="create_eks_cluster",
        cluster_name="RayCluster",
        cluster_role_arn="",  # Fill in with your role ARN
        resources_vpc_config=None,  # Fill in with your VPC configuration
        create_cluster_kwargs=None,  # Optionally provide additional create_cluster arguments
        wait_for_completion=True,  # Set to False if you don't want to wait for the cluster creation to complete
        aws_conn_id=conn.conn_id,  # AWS connection ID
        region="us-east-1"  # Specify your desired region
    )
