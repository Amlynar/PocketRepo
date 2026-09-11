from injector import inject

from src.common.services.project_update_service import ProjectUpdateService
from src.common.repositories.catalog_repo import CatalogRepository


class DevApp:

    @inject
    def __init__(self, project_update_service: ProjectUpdateService, catalog_repo: CatalogRepository):
        self.project_update_service = project_update_service
        self.catalog_repo = catalog_repo

    def run(self):
        print("Starting the PocketRepo DevApp application...")

        self.catalog_repo.load_catalog()
        projects = self.catalog_repo.get_catalogs()
        print("Catalogs loaded:")
        for project in projects:
            print(f"- {project.name} (ID: {project.id})")
        print("Updating project 'draft_locke'...")
        project = self.catalog_repo.get_project_by_id("draft_locke")
        self.project_update_service.update_project(project.id)

        print(f"Project '{project.name}' has been updated successfully.")

        