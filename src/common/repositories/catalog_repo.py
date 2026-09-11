import json
from typing import List
from injector import singleton

from src.common.models.project import Project

CATALOG_FILE_PATH = "./assets/catalog.json"

@singleton
class CatalogRepository:
    def __init__(self):
        self._catalogs: list[Project] = []

    def load_catalog(self) -> None:
        with open(CATALOG_FILE_PATH, 'r') as f:
            data = json.load(f)
            self._catalogs = [Project.from_dict(c) for c in data.get("projects", [])]

    def get_catalogs(self) -> list[Project]:
        return self._catalogs

    def project_exists(self, project_id: str) -> bool:
        return any(project.id == project_id for project in self._catalogs)

    def get_project_by_id(self, project_id: str) -> Project:
        for project in self._catalogs:
            if project.id == project_id:
                return project
        print(f"Project with ID '{project_id}' not found in the catalog.")
        raise ValueError(f"Project with ID '{project_id}' not found in the catalog.")
