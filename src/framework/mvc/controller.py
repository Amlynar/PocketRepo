
from abc import abstractmethod


class PYIController:

    def __init__(self):
        self.navigation = None

    @abstractmethod
    def on_screen_loaded(self):
        """
        Called when the screen is presented to ui.
        """
        pass
