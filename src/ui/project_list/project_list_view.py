import ui

from src.ui.base.base_screen import PRBaseScreen
from src.ui.project_list.project_list_model import ProjectListModel

class ProjectListView(PRBaseScreen):
    def __init__(self):
        super().__init__()
        self.root_view = None

    def layout(self):
        super().layout()
        # self.root_view.frame = (0, 0, self.width, self.height)
        
    def init_root_view(self, data_source):
        self.root_view = ui.View()
        self.root_view.background_color = "green"
        self.root_view.flex = 'WH'

        self.label = ui.Label()
        self.label.text = "Text Label"
        self.label.background_color = "black"
        self.label.text_color = "white"
        self.label.flex = "WH"
        self.label.alignment = 1
        self.root_view.add_subview(self.label)

        self.table_view = ui.TableView()
        # self.table_view.flex = 'WH'
        # self.table_view.data_source = data_source
        # self.table_view.delegate = data_source
        # self.root_view.add_subview(self.table_view)

    def display_content(self):
        self.show_content(self.root_view)
        self.table_view.reload_data()


class ProjectListItemProvider():
    def __init__(self):
        pass

    def create(self, name: str) -> ui.TableViewCell:
        cell = ui.TableViewCell('subtitle')
        cell.flex = 'WH'
        cell.text_label.text = name
        return cell
        