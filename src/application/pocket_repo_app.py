from injector import Injector, inject

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

    def run(self):

        self.navigation_manager.present()

        self.navigation.navigate(ProjectListScreenRoute())
        # self.catalog_repo.load_catalog()
        # print(f"Loaded {len(self.catalog_repo.get_all_projects())} projects from catalog.")
        # self.project_list_controller.view.present("fullscreen")


    def navigate(self, route: PRNavigationRoute):
        # self.navigation_manager.navigate(route)
        controller = route.to_controller(self.injector)
        controller.navigation = self.navigation

        self.navigation_manager.push_screen(controller.view)


