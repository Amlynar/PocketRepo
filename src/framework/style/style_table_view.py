
from framework.style.theme import PYITheme
import ui


class PYITableViewStyle:

    @staticmethod
    def normal(table_view: ui.TableView, theme: PYITheme):
        table_view.background_color = theme.view_background_color
        