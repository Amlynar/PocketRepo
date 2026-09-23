
from common.models.project import Project
from typing import List, Tuple

class ProjectDetailsModel:

    def __init__(self):
        self.title: str = ""
        self.description: str = ""
        self.info_list: list[tuple[str, str]] = []


    def load_from_project(self, project: Project):
        self.title = project.name
        self.description = project.description

        self.info_list = [
            ("ID", project.id),
            ("Destination", project.destination),
            ("URL", project.source.url)
        ]
