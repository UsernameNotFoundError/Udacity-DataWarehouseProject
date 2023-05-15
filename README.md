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
Make sure that the redshift clutser used is in the same region as your s3 buckets (in this case US-West-2 )
