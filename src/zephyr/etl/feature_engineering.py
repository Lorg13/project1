from pyspark.sql import DataFrame
from pyspark.sql.functions import col, try_divide


def add_feature_columns(df: DataFrame) -> DataFrame:
    df_feat = df.withColumn(
        "energy_dance_ratio", try_divide(col("energy"), col("danceability"))
    )
    return df_feat
