from injector import Injector, inject, Module, provider, singleton, Injector

from framework.style.theme import PYITheme, PYIThemeBuilder
from framework.application.app import PYIApp
from navigation.routes import ProjectListScreenRoute
from framework.mvc.controller import PYIController
from framework.navigation.navigator import PYINavigationDelegate, PYIRoute
from framework.navigation.manager import PYINavigationManager
from screens.project_list.project_list_controller import ProjectListController
from screens.project_list.project_list_view import ProjectListView
from common.repositories.catalog_repo import CatalogRepository


class PocketRepoApp(PYIApp):

    def __init__(self):
        super().__init__()
        self.injector = Injector(AppModule())


    def run(self):
        theme = self.injector.get(PYITheme)
        self.present_intial_route(ProjectListScreenRoute(),theme)


    def map_route_to_controller(self, route: PYIRoute) -> PYIController:
        match route:
            case ProjectListScreenRoute():
                return self.injector.get(ProjectListController)
            case _:
                raise ValueError(f"Unknown route: {self}")

class AppModule(Module):

    @singleton
    @provider
    def provide_theme(self) -> PYITheme:
        return (
            PYIThemeBuilder()
            # .set_screen_background_color('red')
            .build()
        )