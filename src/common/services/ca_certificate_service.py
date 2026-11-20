
from datetime import datetime
from pathlib import Path

import requests
from injector import inject

from common.infrastructure.file_manager import FileManager
from framework.network.home_lab_session import CA_BUNDLE_PATH


class CaCertificateDownloadError(Exception):
    pass


class CaCertificateService:

    CA_CERTIFICATE_URL = "http://ca.home.arpa/homelab-ca.crt"
    TIMEOUT_SECONDS = 15

    @inject
    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager

    def get_certificate_path(self) -> Path:
        # Single source of truth lives in framework so HomeLabSession and this service always agree.
        return Path(CA_BUNDLE_PATH)

    def download_ca_certificate(self):
        try:
            # Plain HTTP on purpose: the CA cert is what bootstraps TLS trust.
            response = requests.get(self.CA_CERTIFICATE_URL, timeout=self.TIMEOUT_SECONDS)
        except requests.exceptions.RequestException as e:
            raise CaCertificateDownloadError(f"Could not reach {self.CA_CERTIFICATE_URL}: {e}") from e

        if response.status_code != 200:
            raise CaCertificateDownloadError(
                f"Server returned HTTP {response.status_code} for {self.CA_CERTIFICATE_URL}"
            )
        if b"BEGIN CERTIFICATE" not in response.content:
            raise CaCertificateDownloadError("Response was not a PEM certificate; existing certificate left untouched.")

        path = self.get_certificate_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        # Write then rename so a failed write never destroys a previously good certificate.
        temp_path = path.with_name(path.name + ".tmp")
        temp_path.write_bytes(response.content)
        temp_path.replace(path)

    def get_downloaded_at(self) -> datetime | None:
        try:
            return datetime.fromtimestamp(self.get_certificate_path().stat().st_mtime)
        except OSError:
            return None
