"""Project pipelines."""
from pandera_test.pipelines import (
    create_data_ingestion_pipeline,
    create_file_ingestion_pipeline,
    create_statistical_tests_pipeline,
)

# Built-in
from typing import Dict

# Third-party
from kedro.pipeline import Pipeline, pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    file_ingestion_pipeline = create_file_ingestion_pipeline()
    data_ingestion_pipeline = create_data_ingestion_pipeline()
    statistical_tests_pipeline = create_statistical_tests_pipeline()

    return {
        "__default__": pipeline([]),
        "file_ingestion": file_ingestion_pipeline,
        "data_ingestion": data_ingestion_pipeline,
        "statistical_tests": statistical_tests_pipeline,
    }
