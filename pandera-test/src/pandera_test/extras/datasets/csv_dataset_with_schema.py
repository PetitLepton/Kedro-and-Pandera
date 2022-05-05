# Built-in
from typing import Any, Dict, Optional

# Third-party
import pandas
from kedro.extras.datasets.pandas import CSVDataSet
from pandera.io import _deserialize_schema


class CSVDataSetWithSchema(CSVDataSet):
    def __init__(
        self,
        filepath: str,
        yaml_schema: Optional[Dict[str, Any]] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(filepath, *args, **kwargs)
        self.yaml_schema = yaml_schema

    @property
    def schema(self):
        return _deserialize_schema(self.yaml_schema)

    def _load(self) -> pandas.DataFrame:
        _loaded = super()._load()
        self.schema.validate(_loaded)
        return _loaded
