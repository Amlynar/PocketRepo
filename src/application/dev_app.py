from injector import inject

from common.repositories.catalog_repo import CatalogRepository
from common.services.project_update_service import ProjectUpdateService


class DevApp:

    @inject
    def __init__(self, project_update_service: ProjectUpdateService, catalog_repo: CatalogRepository):
        self.project_update_service = project_update_service
        self.catalog_repo = catalog_repo

    def run(self):
        print("Starting the PocketRepo DevApp application...")

        