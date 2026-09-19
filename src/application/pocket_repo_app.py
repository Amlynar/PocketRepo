from injector import Injector, inject

from src.framework.mvc.controller import PYIController
from src.framework.navigation.navigator import PYINavigationDelegate, PYIRoute, ProjectListScreenRoute
from src.framework.navigation.manager import PYINavigationManager
from src.ui.project_list.project_list_controller import ProjectListController
from src.ui.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp:

    def __init__(self):
        self.injector = Injector()

        self.navigation = PYINavigationDelegate()
        self.navigation.navigate = self.navigate

        self.current_controller = None

    def run(self):

        self.current_controller = self.get_and_decorate_controller(ProjectListScreenRoute())
        self.navigation_manager = PYINavigationManager(intial_view=self.current_controller.view)
        self.navigation_manager.present()
        self.current_controller.on_screen_loaded()

    def navigate(self, route: PYIRoute):
        controller = self.get_and_decorate_controller(route)
        self.navigation_manager.push_screen(controller.view)
        self.current_controller.on_screen_loaded()

    def get_and_decorate_controller(self, route: PYIRoute) -> PYIController:
        self.current_controller = self.to_controller(self.injector,route)
        self.current_controller.navigation = self.navigation
        return self.current_controller

    def to_controller(self, injector: Injector, route: PYIRoute) -> PYIController:
        match route:
            case ProjectListScreenRoute():
                return injector.get(ProjectListController)
            case _:
                raise ValueError(f"Unknown route: {self}")
