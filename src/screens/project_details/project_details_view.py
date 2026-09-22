
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

        self.title_label = ui.Label()
        PYILabelStyle.normal(self.title_label, self.theme)
        self.title_label.text = 'My Title'
        # self.title_label.font = ('<system-bold>', 24)
        self.title_label.alignment = ui.ALIGN_CENTER
        # self.title_label.text_color = '#1c1c1e'
        
        self.desc_label = ui.Label()
        self.desc_label.text = 'This dashboard displays your upcoming tasks. Select an item below to view more detailed insights or to complete it.'
        # self.desc_label.font = ('<system>', 14)
        self.desc_label.alignment = ui.ALIGN_CENTER
        # self.desc_label.text_color = '#3a3a3c'
        self.desc_label.number_of_lines = 0  # Allows multi-line wrapping
        
        # 3. TableView
        self.table_view = ui.TableView()
        PYITableViewStyle.normal(self.table_view, self.theme)
        # self.table_view.background_color = '#ffffff'
        # self.table_view.corner_radius = 8

        for v in  (
            self.title_label,
            self.desc_label,
            self.table_view
        ):
            self.root_view.add_subview(self.table_view)


    def layout(self):
        super().layout()

        pad = 16
        
        # Position Title (Top)
        self.title_label.frame = (pad, pad, self.width - (pad * 2), 40)
        
        # Position Description (Below Title)
        desc_top = self.title_label.frame[1] + self.title_label.frame[3] + 8
        self.desc_label.frame = (pad, desc_top, self.width - (pad * 2), 50)
        
        # Position TableView (Takes remaining space)
        table_top = self.desc_label.frame[1] + self.desc_label.frame[3] + pad
        table_height = self.height - table_top - pad
        self.table_view.frame = (pad, table_top, self.width - (pad * 2), table_height)
