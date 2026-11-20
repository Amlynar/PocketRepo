
from datetime import datetime, timezone

from common.services.ca_certificate_service import CaCertificateService
from common.services.framework_export_service import FrameworkExportService
from framework.alert.alert_dialog import PYIAlert
from framework.mvc.controller import PYIController
from framework.style.theme import PYITheme
from screens.settings.settings_model import SettingsModel
from screens.settings.settings_view import SettingsView
import ui
from injector import inject


class SettingsController(PYIController):

    @inject
    def __init__(self, model: SettingsModel, view: SettingsView, theme: PYITheme, framework_export_service: FrameworkExportService, ca_certificate_service: CaCertificateService):
        super().__init__()
        self.model = model
        self.view = view
        self.theme = theme
        self.framework_export_service = framework_export_service
        self.ca_certificate_service = ca_certificate_service

        self.view.init_root_view(data_source=self)

    def on_screen_loaded(self):
        self.refresh_status()
        self.view.display_content()

    @ui.in_background
    def export_framework_action(self, sender):
        self._run_async_action(
            button=self.view.export_framework_btn,
            spinner=self.view.export_framework_spinner,
            work=self.framework_export_service.export_framework,
            failure_message="Unable to export framework",
        )

    @ui.in_background
    def download_ca_certificate_action(self, sender):
        self._run_async_action(
            button=self.view.download_ca_certificate_btn,
            spinner=self.view.download_ca_certificate_spinner,
            work=self.ca_certificate_service.download_ca_certificate,
            failure_message="Unable to download CA certificate",
        )

    def _run_async_action(self, button, spinner, work, failure_message):
        try:
            button.hidden = True
            spinner.start()
            work()
            self.refresh_status()
        except PermissionError as e:
            PYIAlert.simple_alert(title="Error", message=f"{failure_message}: permission denied ({e})")
        except OSError as e:
            PYIAlert.simple_alert(title="Error", message=f"{failure_message}: I/O error ({e})")
        except Exception as e:
            PYIAlert.simple_alert(title="Error", message=f"{failure_message}: {e}")
        finally:
            spinner.stop()
            button.hidden = False

    def refresh_status(self):
        self.model.framework_export_metadata = self.framework_export_service.read_export_metadata()
        self.model.ca_certificate_downloaded_at = self.ca_certificate_service.get_downloaded_at()
        self.view.set_framework_status(self._framework_status_text())
        self.view.set_certificate_status(self._certificate_status_text())

    def _framework_status_text(self) -> str:
        metadata = self.model.framework_export_metadata
        if not metadata:
            return "Not exported yet."
        try:
            exported_at = datetime.strptime(metadata["exported_at"], "%Y-%m-%dT%H:%M:%SZ")
            when = exported_at.replace(tzinfo=timezone.utc).astimezone().strftime("%b %d, %Y %H:%M")
        except (ValueError, TypeError):
            when = str(metadata["exported_at"])
        return f"Framework exported: {when} (hash {metadata['content_hash'][:8]})"

    def _certificate_status_text(self) -> str:
        downloaded_at = self.model.ca_certificate_downloaded_at
        if not downloaded_at:
            return "Not downloaded yet."
        return f"Certificate downloaded: {downloaded_at.strftime('%b %d, %Y %H:%M')}"
