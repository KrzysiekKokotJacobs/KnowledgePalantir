from transforms.api import transform_df, Output
from pyspark.sql import types as T

@transform_df(
    Output("/Training Environment-574ad4/[Training] Sandbox Folders/KKokot/names_dataset")  #new dataset
)
def my_transform(ctx):
    json_data = [
        {"name": "John", "surname": "Doe"},
        {"name": "Jane", "surname": "Smith"},
        {"name": "Michael", "surname": "Johnson"}
    ]
    df = ctx.spark_session.createDataFrame(json_data)

    # The transform will automatically save the returned DataFrame
    return df