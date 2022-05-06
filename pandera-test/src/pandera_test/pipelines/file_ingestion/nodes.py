# Third-party
import pandas
import pandera

# Local
from .schemas import FILE_NAME_ROOT, FileNamesAndLabels, FilesIDsAndLabels


@pandera.check_io(
    file_names_and_labels=FileNamesAndLabels.to_schema(),
    out=FilesIDsAndLabels.to_schema(),
)
def convert_file_names_to_ID(
    file_names_and_labels: pandas.DataFrame,
) -> pandas.DataFrame:
    return (
        file_names_and_labels.assign(
            _id=lambda df: df[FileNamesAndLabels.file_name]
            .str.replace(FILE_NAME_ROOT, "")
            .astype(int)
        )
        .rename(columns={"_id": FilesIDsAndLabels.file_id})
        .drop(labels=[FileNamesAndLabels.file_name], axis="columns")
    )
