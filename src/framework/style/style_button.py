import ui
from framework.style.theme import PYITheme


class PYIButtonStyle:

    @staticmethod
    def normal(button: ui.Label, theme: PYITheme):
        button.corner_radius = 5
        # self.delete_btn.background_color = '#ff3b30'
        # self.delete_btn.tint_color = 'white'