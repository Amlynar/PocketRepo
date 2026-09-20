
from framework.style.theme import PYITheme
import ui

class PYITableViewCellStyle:

    @staticmethod
    def subtitle(cell: ui.TableViewCell, theme: PYITheme):
        cell.background_color = theme.view_background_color
        cell.flex = 'WH'
