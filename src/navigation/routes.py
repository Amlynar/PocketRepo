
from framework.navigation.navigator import PYIRoute


class ProjectListScreenRoute(PYIRoute): pass

class ProjectDetailsScreenRoute(PYIRoute):
    def __init__(self, project_id: str) -> None:
        super().__init__()
        self.project_id = project_id
