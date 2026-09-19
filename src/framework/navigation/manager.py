from src.framework.style.theme import PYITheme
import ui

class PYINavigationManager:

    def __init__(self, intial_view: ui.View):
        self.root_view = intial_view

        self.nav_view = ui.NavigationView(self.root_view)
        self.nav_view.flex = 'WH'
        self.set_theme(PYITheme())

    def set_theme(self, theme: PYITheme):
        self.theme = theme
        self.nav_view.background_color = self.theme.navigation_bar_background_color

    def push_screen(self, next_view: ui.View):
        self.nav_view.push_view(next_view)
        
    def pop_screen(self):
        self.nav_view.pop_view()
        
    def present(self, style='fullscreen'):
        self.nav_view.present(style)
        
