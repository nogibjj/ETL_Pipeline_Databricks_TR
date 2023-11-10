"""
Transforms and Loads data into the local SQLite3 database
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset = "dbfs:/FileStore/mini_project11/alcohol.csv",
         dataset2 = "dbfs:/FileStore/mini_project11/toy.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    
    alcohol_df = spark.read.csv(dataset2, header=True, inferSchema=True)
    toy_df = spark.read.csv(dataset, header=True, inferSchema=True)
    
    alcohol_df = alcohol_df.withColumn("id", monotonically_increasing_id())
    toy_df = toy_df.withColumn("id", monotonically_increasing_id())
    
    alcohol_df.write.format("delta").mode("overwrite").saveAsTable("alcohol_delta")
    toy_df.write.format("delta").mode("overwrite").saveAsTable("toy_delta")

    return "Finish loading"

if __name__ == "__main__":
    load()