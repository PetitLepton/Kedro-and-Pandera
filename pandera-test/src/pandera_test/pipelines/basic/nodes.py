# Third-party
import pandera

# Local
from .schemas import FILE_NAME_ROOT, FileNamesAndLabels, FilesIDsAndLabels


@pandera.check_types
def convert_file_names_to_ID(
    file_names_and_labels: pandera.typing.DataFrame[FileNamesAndLabels],
) -> pandera.typing.DataFrame[FilesIDsAndLabels]:
    return (
        file_names_and_labels.assign(
            _id=lambda df: df[FileNamesAndLabels.file_name]
            .str.replace(FILE_NAME_ROOT, "")
            .astype(int)
        )
        .rename(columns={"_id": FilesIDsAndLabels.file_id})
        .drop(labels=[FileNamesAndLabels.file_name], axis="columns")
    )
