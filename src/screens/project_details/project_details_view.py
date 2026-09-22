
from framework.style.style_label import PYILabelStyle
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
        
        # Position Title (Top)
        self.title_label.frame = (pad, pad, self.width - (pad * 2), 40)
        
        # Position Description (Below Title)
        desc_top = self.title_label.frame[1] + self.title_label.frame[3] + 8
        self.desc_label.frame = (pad, desc_top, self.width - (pad * 2), 50)

        btn_top = self.desc_label.frame[1] + self.desc_label.frame[3] + pad
        self.delete_btn.frame = (pad, btn_top, (self.width - pad) / 2, 20)
        self.install_btn.frame = ((self.width - pad) / 2, btn_top, (self.width - pad) / 2, 20)

        
        # Position TableView (Takes remaining space)
        table_top = self.install_btn.frame[1] + self.install_btn.frame[3] + pad
        table_height = self.height - table_top - pad
        self.table_view.frame = (pad, table_top, self.width - (pad * 2), table_height)

    def init_root_view(self, data_source):
        self.title_label = ui.Label()
        PYILabelStyle.normal(self.title_label, self.theme)
        self.title_label.text = ''
        # self.title_label.font = ('<system-bold>', 24)
        self.title_label.alignment = ui.ALIGN_CENTER
        # self.title_label.text_color = '#1c1c1e'
        
        self.desc_label = ui.Label()
        PYILabelStyle.normal(self.title_label, self.theme)
        self.desc_label.text = ''
        # self.desc_label.font = ('<system>', 14)
        self.desc_label.alignment = ui.ALIGN_CENTER
        # self.desc_label.text_color = '#3a3a3c'
        self.desc_label.number_of_lines = 0  # Allows multi-line wrapping

        self.delete_btn = ui.Button(title='Delete')
        self.delete_btn.action = data_source.delete_action
        # delete_btn.frame = (0, 0, half_width, 44)
        # delete_btn.background_color = '#ff3b30'
        # delete_btn.tint_color = 'white'
        # delete_btn.corner_radius = 5
        # delete_btn.flex = 'WBR'

        self.install_btn = ui.Button(title='Install')
        self.install_btn.action = data_source.install_action
        # install_btn.frame = (half_width + 10, 0, half_width, 44)
        # install_btn.background_color = '#34c759'
        # install_btn.tint_color = 'white'
        # install_btn.corner_radius = 5
        # install_btn.flex = 'WBL'
        
        # 3. TableView
        self.table_view = ui.TableView()
        PYITableViewStyle.normal(self.table_view, self.theme)
        self.table_view.flex = 'WH'
        self.table_view.data_source = data_source
        self.table_view.delegate = data_source
        # self.table_view.background_color = '#ffffff'
        # self.table_view.corner_radius = 8

        # scroll_view = ui.ScrollView()
        # scroll_view.flex = 'WH'
        for v in  (
            self.title_label,
            self.desc_label,
            self.table_view
        ):
            self.root_view.add_subview(v)
            # scroll_view.add_subview(v)
        # self.root_view.add_subview(scroll_view)

    def display_content(self):
        self.show_content(self.root_view)
        self.table_view.reload_data()