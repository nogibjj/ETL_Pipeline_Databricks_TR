# Databricks ETL Pipeline Tools
[![CI](https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/actions/workflows/cicd.yml)

Tianji Rao

## Overview
In this project, we built a Databricks ETL pipeline tool that can extract data from a online resource (https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv) and use a toy dataframe to transform the data. The combined dataframe is loaded and data sink is also conducted. 

## Preparation 
1. Turn on the databricks cluster
2. Clone the Git repo to the databricks workspace
3. Create the workflow using the scripts in this repo
4. Write queries for data processing
5. Bulid a Pipeline and run it

## Workflow of the pipeline
<img width="742" alt="Screenshot 2023-11-13 at 10 01 11 PM" src="https://github.com/nogibjj/Complex-SQL-Query-tr/assets/104114843/3dbbff6b-24fd-4cba-a509-9291b5be88cd">

Here we have three blocks in this job pipeline. The first block `Extract` takes the `mylib/extract.py` to extract data from the online resource, the `Transform` task conduct the data transformation and data sink, then in the `Query_visualization` block, we can test the quereis and make one sample visualization. 

## Visualization
<img width="824" alt="Screenshot 2023-11-13 at 11 14 04 PM" src="https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/assets/104114843/db5b1a75-10fd-4ad4-aaf8-8ed60cb370aa">


## Format, lint, and test
- `make format`
- `make lint`
- `make test`

## Reference
- https://github.com/nogibjj/python-ruff-template
- https://docs.databricks.com/en/getting-started/data-pipeline-get-started.html
- https://learn.microsoft.com/en-us/azure/databricks/delta/
- https://learn.microsoft.com/en-us/training/paths/data-engineer-azure-databricks/
