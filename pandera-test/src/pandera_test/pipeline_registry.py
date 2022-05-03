"""Project pipelines."""
from pandera_test.pipelines import create_basic_pipeline

# Built-in
from typing import Dict

# Third-party
from kedro.pipeline import Pipeline, pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    basic_pipeline = create_basic_pipeline()

    return {"__default__": pipeline([]), "basic": basic_pipeline}
