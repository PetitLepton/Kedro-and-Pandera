# Third-party
import pandera

FILE_NAME_ROOT = "quartz_"


class FileNamesAndLabels(pandera.SchemaModel):
    file_name: pandera.typing.Series[str] = pandera.Field(str_startswith=FILE_NAME_ROOT)
    label: pandera.typing.Series[str] = pandera.Field(isin=["OK", "NOK"])

    @pandera.check("file_name")
    def check_ids(
        cls, series: pandera.typing.Series[str]
    ) -> pandera.typing.Series[bool]:
        """Check that each file name is of the form FILE_NAME_ROOTid."""
        return series.str.replace(FILE_NAME_ROOT, "").str.isdecimal()

    @pandera.check("file_name")
    def check_no_duplicates(cls, series: pandera.typing.Series[str]) -> bool:
        """Check that each file is only labeled once."""
        return len(series.drop_duplicates()) == len(series)


class FilesIDsAndLabels(pandera.SchemaModel):
    file_id: pandera.typing.Series[int]
    label: pandera.typing.Series[str] = pandera.Field(isin=["OK", "NOK"])
