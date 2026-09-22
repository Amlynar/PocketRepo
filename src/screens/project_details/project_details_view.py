
from framework.style.style_button import PYIButtonStyle
from framework.style.style_label import PYILabelStyle
from framework.style.style_spinner import PYISpinnerStyle
from framework.style.style_table_view import PYITableViewStyle
import ui
from injector import inject

from framework.mvc.screen import PYIScreen
from framework.style.theme import PYITheme


class ProjectDetailsView(PYIScreen):
    @inject
    def __init__(self, theme: PYITheme):
        super().__init__(theme=theme)
        self.theme = theme

    def layout(self):
        super().layout()

        pad = 16
        
        self.title_label.frame = (pad, pad, self.width - (pad * 2), 40)
        
        desc_top = self.title_label.frame[1] + self.title_label.frame[3] + 8
        self.desc_label.frame = (pad, desc_top, self.width - (pad * 2), 50)

        btn_top = self.desc_label.frame[1] + self.desc_label.frame[3] + pad

        self.delete_btn.frame = (pad, btn_top, (self.width - pad) / 2, 40)
        self.delete_spinner.center = self.delete_btn.center

        self.install_btn.frame = ((self.width - pad) / 2, btn_top, (self.width - pad) / 2, 40)
        self.install_spinner.center = self.install_btn.center

        # Position TableView (Takes remaining space)
        table_top = self.install_btn.frame[1] + self.install_btn.frame[3] + pad
        table_height = self.height - table_top - pad
        self.table_view.frame = (pad, table_top, self.width - (pad * 2), table_height)

    def init_root_view(self, data_source):
        self.title_label = ui.Label()
        PYILabelStyle.title(self.title_label, self.theme)
        self.title_label.flex = 'WH'
        self.title_label.text = ''
        self.title_label.alignment = ui.ALIGN_CENTER
        
        self.desc_label = ui.Label()
        PYILabelStyle.normal(self.title_label, self.theme)
        self.desc_label.flex = 'WH'
        self.desc_label.text = ''
        self.desc_label.alignment = ui.ALIGN_CENTER

        self.delete_btn = ui.Button(title='Delete')
        PYIButtonStyle.normal(self.delete_btn, self.theme)
        self.delete_btn.action = data_source.delete_action

        self.delete_spinner = ui.ActivityIndicator()
        PYISpinnerStyle.loading(self.delete_spinner, self.theme)

        self.install_btn = ui.Button(title='Install')
        PYIButtonStyle.normal(self.delete_btn, self.theme)
        self.install_btn.action = data_source.install_action

        self.install_spinner = ui.ActivityIndicator()
        PYISpinnerStyle.loading(self.install_spinner, self.theme)

        self.table_view = ui.TableView()
        PYITableViewStyle.normal(self.table_view, self.theme)
        self.table_view.flex = 'WH'
        self.table_view.data_source = data_source
        self.table_view.delegate = data_source


        for v in  (
            self.title_label,
            self.desc_label,
            self.table_view,
            self.delete_btn,
            self.delete_spinner,
            self.install_btn,
            self.install_spinner
        ):
            self.root_view.add_subview(v)

    def display_content(self):
        self.show_content(self.root_view)
        self.table_view.reload_data()
