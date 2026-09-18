import ui
from injector import inject

from src.ui.base.base_controller import PRBaseController
from src.ui.project_list.project_list_model import ProjectListModel
from src.ui.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository
from src.common.services.project_update_service import ProjectUpdateService

class ProjectListController(PRBaseController):

    @inject
    def __init__(self, model: ProjectListModel, view: ProjectListView, project_update_service: ProjectUpdateService, catalog_repository: CatalogRepository):
        super().__init__()
        self.model = model
        self.view = view
        self.project_update_service = project_update_service
        self.catalog_repository = catalog_repository

        self.source = ui.ListDataSource(self.model.projects)
        self.view.source = self.source


        
    @ui.in_background
    def on_screen_loaded(self):
        self.view.show_loading()
        self.catalog_repository.load_catalog()
        self.model.projects = self.catalog_repository.get_all_projects()
        self.view.display_content()
        
    def tableview_number_of_rows(self, tableview, section):
        return len(self.model.projects)
    
    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell('subtitle')
        cell.text_label.text = self.model.projects[row].name
        return cell
