from injector import Injector, inject

from src.framework.application.app import PYIApp
from src.navigation.routes import ProjectListScreenRoute
from src.framework.mvc.controller import PYIController
from src.framework.navigation.navigator import PYINavigationDelegate, PYIRoute
from src.framework.navigation.manager import PYINavigationManager
from src.ui.project_list.project_list_controller import ProjectListController
from src.ui.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp(PYIApp):

    def __init__(self):
        super().__init__()
        self.injector = Injector()


    def run(self):
        self.present_intial_route(ProjectListScreenRoute())


    def map_route_to_controller(self, route: PYIRoute) -> PYIController:
        match route:
            case ProjectListScreenRoute():
                return self.injector.get(ProjectListController)
            case _:
                raise ValueError(f"Unknown route: {self}")

