from transforms.api import transform_df, Output
from pyspark.sql import types as T

@transform_df(
    Output("/Training Environment-574ad4/[Training] Sandbox Folders/KKokot/names_dataset")  #new dataset
)
def my_transform(ctx):

    data = [("John", "Doe"), ("Jane", "Smith"), ("Michael", "Johnson")]
    schema = T.StructType([
        T.StructField("name", T.StringType(), True),
        T.StructField("surname", T.StringType(), True)
    ])

    df = ctx.spark_session.createDataFrame(data, schema)

    # The transform will automatically save the returned DataFrame
    return df