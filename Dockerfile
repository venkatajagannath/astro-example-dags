FROM quay.io/astronomer/astro-runtime:10.1.0
ADD scripts/s3_countries_transform_script.sh /usr/local/airflow/transform_script.sh
