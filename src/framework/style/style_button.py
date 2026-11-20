
import ui
from framework.style.theme import PYITheme


class PYIButtonStyle:

    @staticmethod
    def normal(button: ui.Label, theme: PYITheme):
        button.corner_radius = 5
        # self.delete_btn.background_color = '#ff3b30'
        # self.delete_btn.tint_color = 'white'

    @staticmethod
    def prominent(button: ui.Button, theme: PYITheme):
        button.corner_radius = 8
        button.background_color = theme.accent_color
        button.tint_color = 'white'
        button.font = ('<system-bold>', 16)
