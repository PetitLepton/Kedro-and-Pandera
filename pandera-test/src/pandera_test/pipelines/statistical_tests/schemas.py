# Third-party
import pandera


class Normalized(pandera.SchemaModel):
    my_great_feature: pandera.typing.Series[float]

    @pandera.check("my_great_feature")
    def check_zero_mean(cls, series: pandera.typing.Series[float]) -> bool:
        return abs(series.mean()) < 1.0e-15

    @pandera.check("my_great_feature")
    def check_unit_std(cls, series: pandera.typing.Series[float]) -> bool:
        return abs(series.std() - 1.0) < 1.0e-15
