"""
query and viz file
"""

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt


# sample query
def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    spark = SparkSession.builder.appName("Query").getOrCreate()
    query = (
            "SELECT t1.country, t1.beer_servings, t1.spirit_servings, "
            "t1.wine_servings, t1.total_litres_of_pure_alcohol, t1.id, "
            "COUNT(*) as total_rows "
            "FROM toy_delta t1 "
            "INNER JOIN alcohol_delta t2 ON t1.id = t2.id "
            "GROUP BY t1.country, t1.beer_servings, t1.spirit_servings, "
            "t1.wine_servings, t1.total_litres_of_pure_alcohol, t1.id "
            "ORDER BY t1.id DESC;"
    )
    query_result = spark.sql(query)
    return query_result


# sample viz for project
def viz():
    query = query_transform()
    count = query.count()
    if count > 0:
        print(f"Data validation passed. {count} rows available.")
    else:
        print("No data available. Please investigate.")
    plt.figure(figsize=(15, 8))  # Adjusted figure size
    query.select("beer_servings", "t1.beer_servings").toPandas().boxplot(
    )
    plt.xlabel("Alcohol")
    plt.ylabel("Beer")
    plt.suptitle("")
    plt.title("Beer servings")
    # Adjust the rotation and spacing of x-axis labels
    plt.xticks(rotation=30, ha="right")  # ha='right' aligns the labels to the right
    plt.tight_layout()  # Ensures proper spacing
    plt.show()


if __name__ == "__main__":
    query_transform()
    viz()