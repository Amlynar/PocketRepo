
from framework.style.style_button import PYIButtonStyle
from framework.style.style_spinner import PYISpinnerStyle
import ui
from injector import inject

from framework.mvc.screen import PYIScreen
from framework.style.theme import PYITheme


class SettingsView(PYIScreen):
    @inject
    def __init__(self, theme: PYITheme):
        super().__init__(theme=theme)
        self.theme = theme

    def layout(self):
        super().layout()

        pad = 16

        self.export_framework_btn.frame = (pad, pad, self.width - (pad * 2), 40)
        self.export_framework_spinner.center = self.export_framework_btn.center

    def init_root_view(self, data_source):
        self.export_framework_btn = ui.Button(title='Export Framework')
        PYIButtonStyle.normal(self.export_framework_btn, self.theme)
        self.export_framework_btn.action = data_source.export_framework_action

        self.export_framework_spinner = ui.ActivityIndicator()
        PYISpinnerStyle.loading(self.export_framework_spinner, self.theme)

        for v in (
            self.export_framework_btn,
            self.export_framework_spinner
        ):
            self.root_view.add_subview(v)

    def display_content(self):
        self.show_content(self.root_view)
