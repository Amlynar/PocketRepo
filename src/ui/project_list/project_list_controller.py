
from injector import inject

from src.ui.base.base_controller import PRBaseController
from src.ui.project_list.project_list_model import ProjectListModel
from src.ui.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository
from src.common.services.project_update_service import ProjectUpdateService


class ProjectListController(PRBaseController):

    @inject
    def __init__(self, project_update_service: ProjectUpdateService, catalog_repository: CatalogRepository):
        super().__init__()
        self.project_update_service = project_update_service
        self.catalog_repository = catalog_repository

        # self.catalog_repository.load_catalog()

        self.model = ProjectListModel()
        self.view = ProjectListView()

        # self.model.projects = self.catalog_repository.get_all_projects()
        # self.view.update_ui(self.model)

        

    def on_screen_loaded(self):
        self.view.show_loading_spinner()
