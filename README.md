# Databricks ETL Pipeline Tools
[![CI](https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/actions/workflows/cicd.yml)

Tianji Rao

## Overview
In this project, we built a Databricks ETL pipeline tool that can extract data from a online resource (https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv) and use a toy dataframe to transform the data. The combined dataframe is loaded and data sink is also conducted.

## Video
[https://www.youtube.com/watch?v=4q1n-Twur48](https://youtu.be/ypI4cgsAVN8)

## Preparation 
1. Turn on the databricks cluster
2. Clone the Git repo to the databricks workspace
3. Create the workflow using the scripts in this repo
4. Write queries for data processing
5. Bulid a Pipeline and run it
6. Use Git push to auto trigger this pipeline

## Some components
1. `Data Extraction`: The extract operation defined in the provided Python script retrieves datasets from specified URLs (url and url2) using the Databricks REST API. The extracted data is then stored in Databricks FileStore with the file paths FILESTORE_PATH + "/alcohol.csv" and FILESTORE_PATH + "/toy.csv". The operation ensures the existence of the target directory, downloads the data from the URLs, and uploads it to the designated file paths in the Databricks FileStore.

2. `Transformation and Load`: The load function in the provided Python script utilizes PySpark to read CSV datasets (alcohol.csv and toy.csv) from the Databricks FileStore. It then adds a monotonically increasing ID column to each dataframe and writes the transformed data into Delta tables named "alcohol_delta" and "toy_delta" in the local SQLite3 database. The function returns a message indicating the completion of the loading process.

3. `Query`: In this project, we run some sample queries to draw certain data and also run a visualization on it, so that we can test the output of the data pipeline.

4. `DBFS`: DBFS (Databricks File System) is a distributed file system that is part of the Databricks Unified Analytics Platform. It provides a scalable and distributed file storage solution designed for big data processing in cloud environments.

5. `Data sink`: "data sink" typically refers to the destination where the transformed data is loaded or stored. In the project, the data sink is the local SQLite3 database. After the data is extracted, transformed, and assigned monotonically increasing IDs, it is loaded into Delta tables ("alcohol_delta" and "toy_delta") in the SQLite3 database. 

## Workflow of the pipeline
<img width="742" alt="Screenshot 2023-11-13 at 10 01 11 PM" src="https://github.com/nogibjj/Complex-SQL-Query-tr/assets/104114843/3dbbff6b-24fd-4cba-a509-9291b5be88cd">

Here we have three blocks in this job pipeline. The first block `Extract` takes the `mylib/extract.py` to extract data from the online resource, the `Transform` task conduct the data transformation and data sink, then in the `Query_visualization` block, we can test the quereis and make one sample visualization. 

## Visualization
<img width="824" alt="Screenshot 2023-11-13 at 11 14 04 PM" src="https://github.com/nogibjj/Data_ETL_Pipeline_Databricks_TR/assets/104114843/db5b1a75-10fd-4ad4-aaf8-8ed60cb370aa">


## Format, lint, and test
- `make format`
- `make lint`
- `make test`

## Conclusion 
In conclusion, this Databricks ETL pipeline project successfully demonstrates the process of extracting data from an online resource, transforming it using a toy dataframe, and then loading it into a data sink. The workflow is well-structured with clear stages, including extraction, transformation, and a final step for querying and visualization.

The integration of CI/CD (Continuous Integration/Continuous Deployment) using GitHub Actions ensures that the pipeline can be automatically triggered and validated whenever changes are made to the repository. This promotes code quality and reliability throughout the development lifecycle.

The use of Databricks clusters and the provided workflow scripts simplifies the deployment process. By following the preparation steps, users can easily set up the environment and execute the pipeline. The inclusion of make commands for formatting, linting, and testing enhances code maintainability and reliability.

## Recommandation
Documentation: Consider enhancing documentation to provide more detailed information on each step of the pipeline, making it easier for new users to understand and contribute to the project.

Error Handling: Implement robust error handling mechanisms within the pipeline to gracefully handle failures and provide meaningful error messages. This will aid in troubleshooting and debugging during the development and execution phases.

Parameterization: If applicable, consider parameterizing configurations, such as data source URLs or cluster configurations. This will make the pipeline more versatile and adaptable to different scenarios.

Logging: Integrate comprehensive logging to capture key information during pipeline execution. This will be valuable for monitoring, auditing, and diagnosing issues.

Security Considerations: Ensure that sensitive information, such as API keys or access credentials, is handled securely. Follow best practices for securing Databricks clusters and data sources.

Performance Optimization: Depending on the size of the dataset, consider optimizing the data processing steps for performance. This may involve tuning Databricks cluster configurations or optimizing the data transformation logic.

Scalability: Evaluate the scalability of the pipeline, especially if it needs to handle larger datasets in the future. Ensure that the pipeline design and configurations can scale effectively to meet growing demands.

Integration Testing: Extend the testing strategy to include integration tests that validate the end-to-end functionality of the pipeline. This will provide more confidence in the reliability of the entire system.

By addressing these recommendations, the ETL pipeline can be further improved in terms of robustness, flexibility, and scalability, making it a more reliable tool for data extraction, transformation, and loading in Databricks environments.

## Reference
- https://github.com/nogibjj/python-ruff-template
- https://docs.databricks.com/en/getting-started/data-pipeline-get-started.html
- https://learn.microsoft.com/en-us/azure/databricks/delta/
- https://learn.microsoft.com/en-us/training/paths/data-engineer-azure-databricks/
