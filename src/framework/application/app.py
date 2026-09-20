
from framework.mvc.controller import PYIController
from framework.navigation.manager import PYINavigationManager
from framework.navigation.navigator import PYINavigationDelegate, PYIRoute
from framework.style.theme import PYITheme


class PYIApp:

    def __init__(self):
        self.navigation = PYINavigationDelegate()
        self.navigation.navigate = self.navigate
        
        self.navigation_manager: PYINavigationManager | None = None
        self.current_controller: PYIController | None = None

    def run(self) -> None:
        raise NotImplemented("PYI App run() not implemented")

    def map_route_to_controller(self, route: PYIRoute) -> PYIController:
        raise NotImplemented("PYIApp to_controller() not implemented")

    def present_intial_route(self, intial_route: PYIRoute, theme:PYITheme=PYITheme()):
        controller = self.get_and_decorate_controller(intial_route)
        self.navigation_manager = PYINavigationManager(intial_view=controller.view)
        self.navigation_manager.set_theme(theme)
        self.navigation_manager.present()
        self.current_controller = controller
        self.current_controller.on_screen_loaded()

    def navigate(self, route: PYIRoute):
        controller = self.get_and_decorate_controller(route)
        if self.navigation_manager and controller.view:
            self.navigation_manager.push_screen(controller.view)
            self.current_controller = controller
            controller.on_screen_loaded()


    def get_and_decorate_controller(self, route: PYIRoute) -> PYIController:
        controller = self.map_route_to_controller(route)
        if controller.view is None:
            raise NotImplemented(f"view is None for route {route}")
        controller.navigation = self.navigation
        return controller