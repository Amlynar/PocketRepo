
from collections.abc import Callable
from typing import Generic, TypeVar

from injector import Injector

from src.ui.base.base_controller import PRBaseController
from src.ui.project_list.project_list_controller import ProjectListController

T = TypeVar("T")
class PRNavigation(Generic[T]):
    def __init__(self):
        self.navigate: Callable[[T], None] | None = None
        
# Routes

class PRNavigationRoute: 

    def to_controller(self, injector: Injector) -> PRBaseController:
        match self:
            case ProjectListScreenRoute():
                return injector.get(ProjectListController)
            case _:
                raise ValueError(f"Unknown route: {self}")

class ProjectListScreenRoute(PRNavigationRoute): pass

