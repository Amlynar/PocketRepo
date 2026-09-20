
from common.models.project import Project


class ProjectDetailsModel:

    def __init__(self) -> None:
        self.project: Project | None = None
        