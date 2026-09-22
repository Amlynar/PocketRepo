
import ui
from framework.style.theme import PYITheme


class PYILabelStyle:

    @staticmethod
    def normal(label: ui.Label, theme: PYITheme):
        label.background_color = theme.view_background_color
        label.number_of_lines = 0

    @staticmethod
    def title(label: ui.Label, theme: PYITheme):
        label.background_color = theme.view_background_color
        label.font = ('<system-bold>', 24)
