"""This is a boilerplate pipeline 'data_ingestion' generated using Kedro
0.18.0."""
# Third-party
import pandas
import pandera

# Local
from .schemas import BoundedTimeSeries


def create_some_input():
    N = 10
    return pandas.DataFrame(
        data={
            "timestamp": pandas.date_range(start="1970-01-01", freq="1h", periods=N),
            "temperature": (N - 1) * [28.0] + [128.0],
        }
    )


def do_nothing_with_my_feature(
    some_input: pandas.DataFrame,
) -> None:
    try:
        _ = BoundedTimeSeries.validate(some_input)
    except pandera.errors.SchemaError as e:
        # Send an email through the notifier?
        failure_indexes = e.failure_cases["index"].values
        print(some_input.loc[failure_indexes, :])
        # raise e
    pass
