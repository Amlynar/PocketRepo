

from src.framework.style.theme import PYITheme, PYIThemeBuilder


class PRTheme(PYITheme):

    def __init__(self):
        super().__init__()

class PRThemeBuilder(PYIThemeBuilder):

    def __init__(self):
        super().__init__()
        self.theme = PRTheme()

    def build(self) -> PRTheme:
        super().build()
        return self.theme
    