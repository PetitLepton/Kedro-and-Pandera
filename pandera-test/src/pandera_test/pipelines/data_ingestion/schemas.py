# Third-party
import pandas
import pandera


class BoundedTimeSeries(pandera.SchemaModel):
    timestamp: pandera.typing.Series[pandas.Timestamp]
    temperature: pandera.typing.Series[float] = pandera.Field(
        in_range={"min_value": 10.0, "max_value": 120.0}
    )
