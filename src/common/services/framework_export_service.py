
import json
from datetime import datetime, timezone
from pathlib import Path

from injector import inject

from common.infrastructure.file_manager import FileManager


class FrameworkExportService:

    METADATA_FILE_NAME = ".pocketrepo-meta.json"

    @inject
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager

    def get_framework_source_directory(self) -> Path:
        # <src>/common/services/this_file.py -> <src>/framework
        return Path(__file__).resolve().parents[2] / "framework"

    def get_framework_export_directory(self) -> Path:
        return self.file_manager.get_documents_directory() / "site-packages-3" / "framework"

    def get_metadata_path(self) -> Path:
        return self.get_framework_export_directory() / self.METADATA_FILE_NAME

    def export_framework(self):
        source = self.get_framework_source_directory()
        content_hash = self.file_manager.hash_directory(source)
        self.file_manager.replace_directory(source, self.get_framework_export_directory())
        self._write_metadata(content_hash)

    def read_export_metadata(self) -> dict | None:
        """Returns {"exported_at", "content_hash"}, or None if never exported / unreadable."""
        try:
            data = json.loads(self.get_metadata_path().read_text(encoding="utf-8"))
            return {"exported_at": data["exported_at"], "content_hash": data["content_hash"]}
        except (OSError, ValueError, KeyError, TypeError):
            return None

    def _write_metadata(self, content_hash: str):
        metadata = {
            "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "content_hash": content_hash,
        }
        self.get_metadata_path().write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
