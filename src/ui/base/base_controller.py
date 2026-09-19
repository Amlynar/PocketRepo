
from abc import abstractmethod
from typing import Generic, TypeVar

from src.navigation.navigation_route import PRNavigation

T = TypeVar("T")
class PRBaseController(Generic[T]):

    def __init__(self):
        self.navigation: PRNavigation[T] | None = None

    @abstractmethod
    def on_screen_loaded(self):
        """
        Called when the screen is presented to ui.
        """
        pass

    def navigate(self, route: T):
        self.navigation.navigate(route)
