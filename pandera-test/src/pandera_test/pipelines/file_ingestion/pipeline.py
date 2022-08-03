"""This is a boilerplate pipeline 'file_ingestion' generated using Kedro
0.18.0."""

# Built-in
from typing import Any

# Third-party
from kedro.pipeline import Pipeline, node

# Local
from .nodes import convert_file_names_to_ID


def create_pipeline(**kwargs: Any) -> Pipeline:
    return Pipeline(
        [
            node(
                convert_file_names_to_ID,
                inputs="file_names_and_labels",
                outputs="file_ids_and_labels",
            )
        ]
    )
