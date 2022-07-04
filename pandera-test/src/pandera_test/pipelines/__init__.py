# Local
from .data_ingestion import create_pipeline as create_data_ingestion_pipeline
from .file_ingestion import create_pipeline as create_file_ingestion_pipeline
from .statistical_tests import create_pipeline as create_statistical_tests_pipeline

__all__ = [
    "create_file_ingestion_pipeline",
    "create_data_ingestion_pipeline",
    "create_statistical_tests_pipeline",
]
