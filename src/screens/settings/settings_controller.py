
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
    def __init__(self, model: SettingsModel, view: SettingsView, theme: PYITheme, framework_export_service: FrameworkExportService):
        super().__init__()
        self.model = model
        self.view = view
        self.theme = theme
        self.framework_export_service = framework_export_service

        self.view.init_root_view(data_source=self)

    def on_screen_loaded(self):
        self.view.display_content()

    @ui.in_background
    def export_framework_action(self, sender):
        try:
            self.view.export_framework_btn.hidden = True
            self.view.export_framework_spinner.start()
            self.framework_export_service.export_framework()
        except PermissionError as e:
            PYIAlert.simple_alert(title="Error", message=f"Permission denied while exporting framework: {e}")
        except OSError as e:
            PYIAlert.simple_alert(title="Error", message=f"I/O error while exporting framework: {e}")
        except Exception as e:
            PYIAlert.simple_alert(title="Error", message=f"Unable to export framework: {e}")
        finally:
            self.view.export_framework_spinner.stop()
            self.view.export_framework_btn.hidden = False
