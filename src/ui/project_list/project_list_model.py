
from common.models.project import Project


class ProjectListModel:
    def __init__(self):
        self.projects: list[Project] = []
