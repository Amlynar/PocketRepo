import ui

from src.ui.base.base_screen import PRBaseScreen
from src.ui.project_list.project_list_model import ProjectListModel

class ProjectListView(PRBaseScreen):
    def __init__(self):
        super().__init__()
        self.root_view = None

    def layout(self):
        super().layout()
        self.table_view.frame = (0, 0, self.width, self.height)
        
    def init_root_view(self, data_source):
        self.root_view = ui.View()

        self.table_view = ui.TableView()                        
        self.table_view.data_source = data_source
        self.table_view.delegate = data_source

        self.root_view.add_subview(self.table_view)

    def init_table_cell(self, name: str) -> ui.TableViewCell:
        cell = ui.TableViewCell('subtitle')
        cell.text_label.text = name
        return cell

    def display_content(self):
        self.show_content(self.root_view)
        self.table_view.reload_data()



class ProjectListItem(ui.TableViewCell):
    def __init__(self, name: str):
        super().__init__('subtitle')
        self.cell.text_label.text = name
        