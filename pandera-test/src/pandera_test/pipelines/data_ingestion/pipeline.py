"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node
from .nodes import create_some_input, do_nothing_with_my_feature


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(create_some_input, inputs=None, outputs="some_input"),
            node(do_nothing_with_my_feature, inputs="some_input", outputs=None),
        ]
    )
