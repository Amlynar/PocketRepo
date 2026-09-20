
import ui
from injector import inject

from framework.mvc.screen import PYIScreen
from framework.style.theme import PYITheme


class ProjectDetailsView(PYIScreen):
    @inject
    def __init__(self, theme: PYITheme):
        super().__init__(theme=theme)


        self.title_label = ui.Label()
        self.title_label.text = ""
        self.title_label.flex = 'WH'


