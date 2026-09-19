

from src.framework.navigation.navigator import PYINavigationDelegate, PYIRoute


class PYIController():

    def __init__(self):
        self.navigation: PYINavigationDelegate | None = None
        self.view: PYIController | None

    def navigate(self, route: PYIRoute):
        if self.navigation and self.navigation.navigate:
            self.navigation.navigate(route)

    def on_screen_loaded(self):
        """
        Called when the screen is presented to ui.
        """
        pass
