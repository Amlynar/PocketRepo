import ui

class NavigationManager:

    def __init__(self, intial_view: ui.View):
        self.root_view = intial_view

        self.nav_view = ui.NavigationView(self.root_view)
        self.nav_view.background_color = 'white'
        self.nav_view.flex = 'WH'

    def push_screen(self, next_view: ui.View):
        self.nav_view.push_view(next_view)
        
    def pop_screen(self):
        self.nav_view.pop_view()
        
    def present(self, style='fullscreen'):
        self.nav_view.present(style)
        
