
from abc import abstractmethod


class PRBaseController:

    def __init__(self):
        self.navigation = None
        self.view = None

    @abstractmethod
    def on_screen_loaded(self):
        """
        Called when the screen is loaded.
        """
        pass
