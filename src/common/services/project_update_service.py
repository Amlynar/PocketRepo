
from injector import inject

from common.infrastructure.file_downloader import FileDownloader
from common.infrastructure.file_manager import FileManager
from common.repositories.catalog_repo import CatalogRepository


class ProjectUpdateService:

    @inject
    def __init__(self, file_manager: FileManager, file_downloader: FileDownloader, catalog_repo: CatalogRepository):
        self.file_manager = file_manager
        self.file_downloader = file_downloader
        self.catalog_repo = catalog_repo


    def update_project(self, project_id: str):
        exists = self.catalog_repo.project_exists(project_id)
        if not exists:
            raise ValueError(f"Project with ID '{project_id}' does not exist in the catalog.")

        project = self.catalog_repo.get_project_by_id(project_id)
        github_url = project.source.url
        zip_file_name = f"{project.destination}_temp.zip"
        extract_path = self.file_manager.get_project_directory(project_directory_name=project.destination)

        self.file_manager.delete_directory(extract_path)
        self.file_downloader.download(github_url, zip_file_name)
        self.file_manager.extract_zip_file(zip_file_name, extract_path)
        self.file_manager.delete_file(zip_file_name)
