from datetime import timedelta
from google.protobuf.duration_pb2 import Duration
import pandas as pd
import yaml

from feast import (
    Entity,
    FeatureService,
    Feature,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
    SnowflakeSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64

project_name = yaml.safe_load(open("feature_store.yaml"))["project"]


# Declaring an entity for the dataset
# patient = Entity(
#     name="patient_id", 
#     value_type=Int64, 
#     description="The ID of the patient")
patient = Entity(name="patient_id", join_keys=["patient_id"])

# Declaring the source of the first set of features
# f_source1 = FileSource(
#     path=r"C:\feast\breast_cancer\data\data_df1.parquet",
#     event_timestamp_column="event_timestamp"
# )

f_source1 = SnowflakeSource(database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
                            table="DF1_BREAST_CANCER",
                            timestamp_field="event_timestamp")

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="mean_radius", dtype=Float32),
        Field(name="mean_texture", dtype=Float32),
        Field(name="mean_perimeter", dtype=Float32),
        Field(name="mean_area", dtype=Float32),
        Field(name="mean_smoothness", dtype=Float32)
        ],    
    source=f_source1
)

# Declaring the source of the second set of features
# f_source2 = FileSource(
#     path=r"C:\feast\breast_cancer\data\data_df2.parquet",
#     event_timestamp_column="event_timestamp"
# )
f_source2 = SnowflakeSource(database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
                            table="DF2_BREAST_CANCER",
                            timestamp_field="event_timestamp")

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="mean_compactness", dtype=Float32),
        Field(name="mean_concavity", dtype=Float32),
        Field(name="mean_concave_points", dtype=Float32),
        Field(name="mean_symmetry", dtype=Float32),
        Field(name="mean_fractal_dimension", dtype=Float32)
        ],    
    source=f_source2
)

# Declaring the source of the third set of features
# f_source3 = FileSource(
#     path=r"C:\feast\breast_cancer\data\data_df3.parquet",
#     event_timestamp_column="event_timestamp"
# )
f_source3 = SnowflakeSource(database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
                            table="DF3_BREAST_CANCER",
                            timestamp_field="event_timestamp")

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="radius_error", dtype=Float32),
        Field(name="texture_error", dtype=Float32),
        Field(name="perimeter_error", dtype=Float32),
        Field(name="area_error", dtype=Float32),
        Field(name="smoothness_error", dtype=Float32),
        Field(name="compactness_error", dtype=Float32),
        Field(name="concavity_error", dtype=Float32)
        ],    
    source=f_source3
)

# Declaring the source of the fourth set of features
# f_source4 = FileSource(
#     path=r"C:\feast\breast_cancer\data\data_df4.parquet",
#     event_timestamp_column="event_timestamp"
# )
f_source4 = SnowflakeSource(database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
                            table="DF4_BREAST_CANCER",
                            timestamp_field="event_timestamp")

# Defining the fourth set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(days=1),
    entities=[patient],
    schema=[
        Field(name="concave_points_error", dtype=Float32),
        Field(name="symmetry_error", dtype=Float32),
        Field(name="fractal_dimension_error", dtype=Float32),
        Field(name="worst_radius", dtype=Float32),
        Field(name="worst_texture", dtype=Float32),
        Field(name="worst_perimeter", dtype=Float32),
        Field(name="worst_area", dtype=Float32),
        Field(name="worst_smoothness", dtype=Float32),
        Field(name="worst_compactness", dtype=Float32),
        Field(name="worst_concavity", dtype=Float32),
        Field(name="worst_concave_points", dtype=Float32),
        Field(name="worst_symmetry", dtype=Float32),
        Field(name="worst_fractal_dimension", dtype=Float32),        
        ],    
    source=f_source4
)

# Declaring the source of the targets
# target_source = FileSource(
#     path=r"C:\feast\breast_cancer\data\target_df.parquet", 
#     created_timestamp_column="event_timestamp"
# )
target_source = SnowflakeSource(database=yaml.safe_load(open("feature_store.yaml"))["offline_store"]["database"],
                                table="TARGET_BREAST_CANCER",
                                timestamp_field="event_timestamp")

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=[patient],
    ttl=timedelta(days=1),
    schema=[
        Field(name="target", dtype=Int64)        
        ],    
    source=target_source
)