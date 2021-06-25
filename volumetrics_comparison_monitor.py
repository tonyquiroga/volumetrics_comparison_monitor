import modelop.monitors.volumetrics as volumetrics
import modelop.schema.infer as infer
import modelop.utils as utils

logger = utils.configure_logger()

MONITORING_PARAMETERS = {}

# modelop.init
def init(job_json):
    """A function to extract input schema from job JSON.
    Args:
        job_json (str): job JSON in a string format.
    """
    # Extract input schema from job JSON
    input_schema_definition = infer.extract_input_schema(job_json)

    logger.info("Input schema definition: %s", input_schema_definition)

    # Get monitoring parameters from schema
    global MONITORING_PARAMETERS
    MONITORING_PARAMETERS = infer.set_monitoring_parameters(
        schema_json=input_schema_definition, check_schema=True
    )


# modelop.metrics
def metrics(df_1, df_2):
    # Get identifier_columns from MONITORING_PARAMETERS
    identifier_columns = MONITORING_PARAMETERS["identifier_columns"]

    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)

    # Compare DataFrames on identifier_columns
    identifiers_comparison = volumetric_monitor.identifier_comparison(
        df_2, identifier_columns
    )

    count_comparison = volumetric_monitor.count_comparison(df_2)

    result = {
        # Top-level metrics
        "record_count_difference": count_comparison["values"][
            "record_count_difference"
        ],
        "identifiers_match": identifiers_comparison["values"]["identifiers_match"],
        # Complete test results
        "volumetrics": [count_comparison, identifiers_comparison],
    }
    yield result
