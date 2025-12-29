from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when


def clean_data(df: DataFrame) -> DataFrame:
    df_clean = (
        df.dropDuplicates()
        .filter(col("danceability").isNotNull())
        .filter(col("energy").isNotNull())
    )

    numeric_cols = ["danceability", "energy"]

    for c in numeric_cols:
        df_clean = df_clean.withColumn(
            c,
            when(
                col(c).rlike(r"^[-+]?\d*\.?\d+(e[-+]?\d+)?$"), col(c).cast("double")
            ).otherwise(None),
        )

    return df_clean
