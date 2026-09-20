from framework.mvc.screen import PYIScreen
from framework.style.style_table_view import PYITableViewStyle
from framework.style.theme import PYITheme
import ui
from injector import inject



class ProjectListView(PYIScreen):
    @inject
    def __init__(self, theme: PYITheme):
        super().__init__(theme=theme)

    def layout(self):
        super().layout()
        
    def init_root_view(self, data_source):
        self.table_view = ui.TableView()
        PYITableViewStyle.normal(self.table_view, self.theme)
        self.table_view.flex = 'WH'
        self.table_view.data_source = data_source
        self.table_view.delegate = data_source
        self.root_view.add_subview(self.table_view)
        