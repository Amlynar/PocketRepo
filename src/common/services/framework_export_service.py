
from pathlib import Path

from injector import inject

from common.infrastructure.file_manager import FileManager


class FrameworkExportService:

    @inject
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager

    def get_framework_source_directory(self) -> Path:
        # <src>/common/services/this_file.py -> <src>/framework
        return Path(__file__).resolve().parents[2] / "framework"

    def get_framework_export_directory(self) -> Path:
        return self.file_manager.get_documents_directory() / "site-packages-3" / "framework"

    def export_framework(self):
        self.file_manager.replace_directory(
            self.get_framework_source_directory(),
            self.get_framework_export_directory()
        )
