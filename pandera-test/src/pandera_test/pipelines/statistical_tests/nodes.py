"""This is a boilerplate pipeline 'statistical_tests' generated using Kedro
0.18.0."""

# Third-party
import numpy
import pandas
import pandera

# Local
from .schemas import Normalized


def create_some_input():
    return (
        pandas.DataFrame(data={"my_great_feature": numpy.random.random(size=10)})
        # Uncomment to pass the check
        .assign(
            my_great_feature=lambda df: (
                df["my_great_feature"] - df["my_great_feature"].mean()
            )
            / df["my_great_feature"].std()
        )
    )


@pandera.check_types
def do_nothing_with_my_feature(
    some_input: pandera.typing.DataFrame[Normalized],
) -> None:
    pass
