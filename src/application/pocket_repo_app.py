from injector import Injector, inject

from src.screens.base.base_controller import PRBaseController
from src.navigation.navigation_route import PRNavigation, PRNavigationRoute, ProjectListScreenRoute
from src.navigation.navigation_manager import NavigationManager
from src.screens.project_list.project_list_controller import ProjectListController
from src.screens.project_list.project_list_view import ProjectListView
from src.common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp:

    def __init__(self):
        self.injector = Injector()

        self.navigation_manager = NavigationManager()
        self.navigation = PRNavigation()
        self.navigation.navigate = self.navigate

        self.current_controller = None

    def run(self):

        self.current_controller = self.get_and_decorate_controller(ProjectListScreenRoute())
        self.navigation_manager.setup_navigation(self.current_controller.view)
        self.navigation_manager.present()

        # self.navigation.navigate(ProjectListScreenRoute())
        # self.catalog_repo.load_catalog()
        # print(f"Loaded {len(self.catalog_repo.get_all_projects())} projects from catalog.")
        # self.project_list_controller.view.present("fullscreen")


    def navigate(self, route: PRNavigationRoute):
        controller = self.get_and_decorate_controller(route)
        self.navigation_manager.push_screen(controller.view)

    def get_and_decorate_controller(self, route: PRNavigationRoute) -> PRBaseController:
        self.current_controller = route.to_controller(self.injector)
        self.current_controller.navigation = self.navigation
        self.current_controller.on_screen_loaded()
        return self.current_controller


