# Still in Progress

# Project: Data Warehouse (Udacity Project)

### Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to.

# Run the application

## (Optional) Create a Python environment: 
* For Python3 users: 
  * `pip install virtualenv`
  * `virtualenv venv_name`
  * `source path/to/venv_name activate`
* For Anaconda users: 
  * `conda create --name conda_env`
  * `conda activate conda_env`
  * `conda install pip`

## Install requirements
```pip install -r requirements.txt```


## Remarks:
Make sure to fill *dwh.cfg* with the corresponding parameters:

 Markup : *[CLUSTER]
  *HOST=<YOUR_AWS_REDSHIFT_ENDPOINT>
  *DB_NAME=<YOUR_AWS_REDSHIFT_CLUSTER_DATABASE>
  *DB_USER=<YOUR_AWS_DATABASE_USER>
  *DB_PASSWORD=<YOUR_AWS_DATABASE_PASSWORD>
  *DB_PORT=<YOUR_AWS_REDSHIFT_PORT>

 Markup : *[IAM_ROLE]
  *ARN=<IAM_ROLE_ARN> 

 Markup : *[S3]
  *LOG_DATA=s3://udacity-dend/log-data
  *LOG_JSONPATH=s3://udacity-dend/log_json_path.json
  *SONG_DATA=s3://udacity-dend/song-data/

 Markup : *[IAM_USER]
  *KEY=<YOUR_AWS_KEY>
  *SECRET=<YOUR_AWS_SECRET>

## Run:
1) ```python create_tables.py```
2) ```python etl.py```
