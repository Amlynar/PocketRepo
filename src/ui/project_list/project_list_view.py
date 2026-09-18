from src.ui.base.base_screen import PRBaseScreen
from src.ui.project_list.project_list_model import ProjectListModel
import ui

class ProjectListView(PRBaseScreen):
    def __init__(self):
        super().__init__()
        
        self.model = ProjectListModel()
        self.table_view = ui.TableView()
        
        self.table_view.data_source = self
        self.table_view.delegate = self
        self.add_subview(self.table_view)

    def did_load(self):
        print("ProjectListView did load.")
        

    def update_ui(self, project_list_model: ProjectListModel):
        self.model = project_list_model
        self.table_view.reload_data()

    def tableview_number_of_rows(self, tableview, section):
        return len(self.model.projects)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell('subtitle')
        cell.text_label.text = self.model.projects[row].name
        return cell
    