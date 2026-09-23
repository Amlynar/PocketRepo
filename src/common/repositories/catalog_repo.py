import json
from typing import Dict, List
from injector import singleton

from common.models.project import Project


CATALOG_FILE_PATH = "./assets/catalog.json"


@singleton
class CatalogRepository:
    def __init__(self):
        self._catalogs: Dict[str, Project] | None = None

    def fetch_all_projects(self) -> List[Project]:
        if self._catalogs is None:
            self.load_catalog()

        return list(self._catalogs.values())

    def fetch_project(self, project_id: str) -> Project:
        if self._catalogs is None:
            self.load_catalog()
        if project_id not in self._catalogs:
            raise InvalidProjectIdError(f"Project with ID '{project_id}' not found in the catalog.")
        return self._catalogs[project_id]

    def load_catalog(self) -> None:
        with open(CATALOG_FILE_PATH, 'r') as f:
            data = json.load(f)
            self._catalogs = {project.id: project for project in (Project.from_dict(c) for c in data.get("projects", []))}

    def get_all_projects(self) -> List[Project]:
        return list(self._catalogs.values())

class InvalidProjectIdError(Exception):
    def __init__(self, message="An error occurred") -> None:
        self.message = message
        super().__init__(self.message)
