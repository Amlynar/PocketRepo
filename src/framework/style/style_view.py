
from framework.style.theme import PYITheme
import ui


class PYIViewStyle:

    @staticmethod
    def clear(view: ui.View, theme: PYITheme):
        view.background_color = theme.view_background_color
        