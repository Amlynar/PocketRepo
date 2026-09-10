import json
from typing import List

from src.common.models.project import Project

CATALOG_FILE_PATH = "./assets/catalog.json"

class CatalogRepository:
    def __init__(self):
        self._catalogs: list[Project] = []

    def load_catalog(self) -> None:
        with open(CATALOG_FILE_PATH, 'r') as f:
            data = json.load(f)
            self._catalogs = [Project.from_dict(c) for c in data.get("projects", [])]

    def get_catalogs(self) -> list[Project]:
        return self._catalogs
