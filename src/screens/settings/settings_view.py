
from framework.style.style_button import PYIButtonStyle
from framework.style.style_label import PYILabelStyle
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
        width = self.width - (pad * 2)
        button_height = 44

        # Each section: header, button (spinner overlaid), status caption.
        top = pad
        top = self._layout_section(
            top, pad, width, button_height,
            self.framework_header, self.export_framework_btn,
            self.export_framework_spinner, self.framework_status_label
        )
        self._layout_section(
            top + pad, pad, width, button_height,
            self.certificate_header, self.download_ca_certificate_btn,
            self.download_ca_certificate_spinner, self.certificate_status_label
        )

    def _layout_section(self, top, pad, width, button_height, header, button, spinner, status_label):
        header.frame = (pad, top, width, 20)
        button.frame = (pad, header.y + header.height + 6, width, button_height)
        spinner.center = button.center
        status_label.frame = (pad, button.y + button.height + 6, width, 36)
        return status_label.y + status_label.height

    def init_root_view(self, data_source):
        self.framework_header = self._make_section_header('FRAMEWORK')
        self.export_framework_btn = self._make_button('Export Framework', data_source.export_framework_action)
        self.export_framework_spinner = self._make_spinner()
        self.framework_status_label = self._make_caption()

        self.certificate_header = self._make_section_header('CERTIFICATES')
        self.download_ca_certificate_btn = self._make_button('Download CA Certificate', data_source.download_ca_certificate_action)
        self.download_ca_certificate_spinner = self._make_spinner()
        self.certificate_status_label = self._make_caption()

        for v in (
            self.framework_header,
            self.export_framework_btn,
            self.export_framework_spinner,
            self.framework_status_label,
            self.certificate_header,
            self.download_ca_certificate_btn,
            self.download_ca_certificate_spinner,
            self.certificate_status_label
        ):
            self.root_view.add_subview(v)

    def set_framework_status(self, text: str):
        self.framework_status_label.text = text

    def set_certificate_status(self, text: str):
        self.certificate_status_label.text = text

    def display_content(self):
        self.show_content(self.root_view)

    def _make_section_header(self, text):
        label = ui.Label()
        PYILabelStyle.section_header(label, self.theme)
        label.text = text
        return label

    def _make_caption(self):
        label = ui.Label()
        PYILabelStyle.caption(label, self.theme)
        return label

    def _make_button(self, title, action):
        button = ui.Button(title=title)
        PYIButtonStyle.prominent(button, self.theme)
        button.action = action
        return button

    def _make_spinner(self):
        spinner = ui.ActivityIndicator()
        PYISpinnerStyle.loading(spinner, self.theme)
        return spinner
