import ui
from injector import inject

from framework.mvc.controller import PYIController
from screens.project_list.project_list_model import ProjectListModel
from screens.project_list.project_list_view import ProjectListView, ProjectListItemProvider
from common.repositories.catalog_repo import CatalogRepository
from common.services.project_update_service import ProjectUpdateService
from navigation.routes import ProjectListScreenRoute
import time
class ProjectListController(PYIController):

    @inject
    def __init__(self, model: ProjectListModel, view: ProjectListView, item_provider: ProjectListItemProvider, project_update_service: ProjectUpdateService, catalog_repository: CatalogRepository):
        super().__init__()
        self.model = model
        self.view = view
        self.item_provider = item_provider
        self.project_update_service = project_update_service
        self.catalog_repository = catalog_repository

        self.view.init_root_view(data_source=self)

        
    @ui.in_background
    def on_screen_loaded(self):
        if self.view is None:
            raise ValueError("self.view should not be None")
        self.view.show_loading()
        time.sleep(3)
        self.catalog_repository.load_catalog()
        self.model.projects = self.catalog_repository.get_all_projects()
        self.view.display_content()
        
    def tableview_number_of_rows(self, tableview, section):
        return len(self.model.projects)
    
    def tableview_cell_for_row(self, tableview, section, row):
        project = self.model.projects[row]
        return self.item_provider.create(name=project.name)
