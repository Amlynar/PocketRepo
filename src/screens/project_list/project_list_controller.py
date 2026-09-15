
from injector import inject

from src.screens.project_list.project_list_model import ProjectListModel
from src.screens.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository
from src.common.services.project_update_service import ProjectUpdateService


class ProjectListController:

    @inject
    def __init__(self, project_update_service: ProjectUpdateService, catalog_repository: CatalogRepository):
        self.project_update_service = project_update_service
        self.catalog_repository = catalog_repository

        self.model = ProjectListModel()
        self.view = ProjectListView()

        self.model.projects = self.catalog_repository.get_all_projects()
        self.view.update_ui(self.model)
