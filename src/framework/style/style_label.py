
import ui
from framework.style.theme import PYITheme


class PYILabelStyle:

    @staticmethod
    def normal(label: ui.Label, theme: PYITheme):
        label.background_color = theme.view_background_color
        label.flex = 'WH'
