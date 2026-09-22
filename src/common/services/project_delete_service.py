
from injector import inject

from common.infrastructure.file_downloader import FileDownloader
from common.infrastructure.file_manager import FileManager
from common.repositories.catalog_repo import CatalogRepository


class ProjectDeleteService:

    @inject
    def __init__(self, file_manager: FileManager, catalog_repo: CatalogRepository):
        self.file_manager = file_manager
        self.catalog_repo = catalog_repo


    def delete_project(self, project_id: str):
        project = self.catalog_repo.fetch_project(project_id)
        extract_path = self.file_manager.get_project_directory(project_directory_name=project.destination)

        self.file_manager.delete_directory(extract_path)
