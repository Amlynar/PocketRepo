
from framework.style.theme import PYITheme
import ui

class PYIScreenStyle:

    @staticmethod
    def fullscreen(screen: ui.View, theme: PYITheme):
        screen.background_color = theme.screen_background_color
        screen.flex = 'WH'