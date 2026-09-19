
from abc import abstractmethod

from src.framework.navigation.navigator import PYINavigationDelegate, PYIRoute


class PYIController:

    def __init__(self):
        self.navigation: PYINavigationDelegate | None = None

    def navigate(self, route: PYIRoute):
        if self.navigation is not None and self.navigation.navigate is not None:
            self.navigation.navigate(route)

    @abstractmethod
    def on_screen_loaded(self):
        """
        Called when the screen is presented to ui.
        """
        pass
