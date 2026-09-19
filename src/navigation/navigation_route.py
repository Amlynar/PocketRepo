
from collections.abc import Callable

from injector import Injector

from src.ui.base.base_controller import PRBaseController
from src.ui.project_list.project_list_controller import ProjectListController


class PRNavigation:
    def __init__(self):
        self.navigate: Callable[[PRNavigationRoute], None] | None = None
        
# Routes

class PRNavigationRoute: 

    def to_controller(self, injector: Injector) -> PRBaseController:
        match self:
            case ProjectListScreenRoute():
                return injector.get(ProjectListController)
            case _:
                raise ValueError(f"Unknown route: {self}")

class ProjectListScreenRoute(PRNavigationRoute): pass

