from src.ui.base.base_screen import PRBaseScreen
from src.ui.project_list.project_list_model import ProjectListModel
from src.ui.project_list.widget.project_list_content import ProjectListContent
import ui

class ProjectListView(PRBaseScreen):
    def __init__(self):
        super().__init__()
        self.source = None
        # self.model = ProjectListModel()

        

    def layout(self):
        super().layout()
        # self.table_view.frame = (0, 0, self.width, self.height)
        

    def display_content(self):
        self.content = ProjectListContent(data_source=self.source,delegate=self.source)
        self.show_content(self.content)
        self.content.table_view.reload_data()

        

    # def update_ui(self, project_list_model: ProjectListModel):
    #     self.model = project_list_model
    #     self.display_content()
    #     # is there a better way to do below?
    #     self.content.table_view.reload_data()

    # def tableview_number_of_rows(self, tableview, section):
    #     return len(self.model.projects)

    # def tableview_cell_for_row(self, tableview, section, row):
    #     cell = ui.TableViewCell('subtitle')
    #     cell.text_label.text = self.model.projects[row].name
    #     return cell
    