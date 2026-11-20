
from datetime import datetime


class SettingsModel:
    def __init__(self):
        self.framework_export_metadata: dict | None = None
        self.ca_certificate_downloaded_at: datetime | None = None
