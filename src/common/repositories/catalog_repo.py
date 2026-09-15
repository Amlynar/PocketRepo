import json
from typing import Dict, List
from injector import singleton

from src.common.models.project import Project


CATALOG_FILE_PATH = "./assets/catalog.json"


@singleton
class CatalogRepository:
    def __init__(self):
        self._catalogs: Dict[str, Project] = {}

    def load_catalog(self) -> None:
        with open(CATALOG_FILE_PATH, 'r') as f:
            data = json.load(f)
            self._catalogs = {project.id: project for project in (Project.from_dict(c) for c in data.get("projects", []))}

    def get_all_projects(self) -> List[Project]:
        return list(self._catalogs.values())

    def project_exists(self, project_id: str) -> bool:
        return project_id in self._catalogs

    def get_project_by_id(self, project_id: str) -> Project:
        if project_id not in self._catalogs:
            print(f"Project with ID '{project_id}' not found in the catalog.")
            raise ValueError(f"Project with ID '{project_id}' not found in the catalog.")
        return self._catalogs[project_id]
