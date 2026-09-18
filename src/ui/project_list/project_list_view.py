from src.ui.base.base_screen import PRBaseScreen
from src.ui.project_list.project_list_model import ProjectListModel
from src.ui.project_list.widget.project_list_content import ProjectListContent
import ui

class ProjectListView(PRBaseScreen):
    def __init__(self):
        super().__init__()
        self.source = None

    def layout(self):
        super().layout()
        # self.table_view.frame = (0, 0, self.width, self.height)
        

    def display_content(self):
        content = ProjectListContent(data_source=self.source,delegate=self.source)
        self.show_content(content)
        self.content.table_view.reload_data()
        
    