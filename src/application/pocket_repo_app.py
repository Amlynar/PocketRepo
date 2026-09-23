
import sys
from injector import Injector

from core.app_module import AppModule
from framework.application.app import PYIApp
from framework.mvc.controller import PYIController
from framework.navigation.navigator import PYIRoute
from framework.style.theme import PYITheme
from navigation.routes import ProjectDetailsScreenRoute, ProjectListScreenRoute
from screens.project_details.project_details_controller import ProjectDetailsController
from screens.project_list.project_list_controller import ProjectListController


class PocketRepoApp(PYIApp):

    def __init__(self):
        super().__init__()
        self.injector = Injector(AppModule())


    def run(self):
        project_id = self.get_project_id()
        route = ProjectDetailsScreenRoute(project_id) if project_id else ProjectListScreenRoute()

        theme = self.injector.get(PYITheme)
        self.present_intial_route(route,theme)


    def map_route_to_controller(self, route: PYIRoute) -> PYIController:
        match route:
            case ProjectListScreenRoute():
                return self.injector.get(ProjectListController)
            case ProjectDetailsScreenRoute():
                project_details_controller = self.injector.get(ProjectDetailsController)
                project_details_controller.project_id = route.project_id
                return project_details_controller
            case _:
                raise ValueError(f"Unknown route: {self}")

    def get_project_id(self):
        for arg in sys.argv[1:]:
            if arg.startswith("project_id="):
                _, project_id = arg.split("=", 1)
                return project_id
                
        return None
