from framework.mvc.screen import PYIScreen
from framework.style.theme import PYITheme
import ui
from injector import inject



class ProjectListView(PYIScreen):
    @inject
    def __init__(self, theme: PYITheme):
        super().__init__()
        self.set_theme(theme)

    def layout(self):
        super().layout()
        # self.root_view.frame = (0, 0, self.width, self.height)
        
    def init_root_view(self, data_source):
        # self.root_view.background_color = "green"
        # self.root_view.flex = 'WH'

        # self.label = ui.Label()
        # self.label.text = "Text Label"
        # self.label.background_color = "black"
        # self.label.text_color = "white"
        # self.label.flex = "WH"
        # self.label.alignment = 1
        # self.root_view.add_subview(self.label)

        self.table_view = ui.TableView()
        self.table_view.flex = 'WH'
        self.table_view.background_color = self.theme.view_background_color
        self.table_view.data_source = data_source
        self.table_view.delegate = data_source
        self.root_view.add_subview(self.table_view)

    def display_content(self):
        self.show_content(self.root_view)
        self.table_view.reload_data()


class ProjectListItemProvider():
    @inject
    def __init__(self, theme: PYITheme):
        self.theme = theme

    def create(self, name: str) -> ui.TableViewCell:
        cell = ui.TableViewCell('subtitle')
        cell.background_color = self.theme.view_background_color
        cell.flex = 'WH'
        cell.text_label.text = name
        return cell
        