from injector import inject

from src.screens.project_list.project_list_controller import ProjectListController
from src.screens.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp:

    @inject
    def __init__(self, project_list_controller: ProjectListController, catalog_repo: CatalogRepository):
        self.project_list_controller = project_list_controller
        self.catalog_repo = catalog_repo

    def run(self):

        self.catalog_repo.load_catalog()
        self.project_list_controller.view.present("fullscreen")
            