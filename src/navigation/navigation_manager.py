import ui

class NavigationManager:

    def __init__(self):
        self.root_view = None

    def push_screen(self, next_view: ui.View):
        if not self.root_view:
            self.setup_navigation(next_view)
        else:
            self.nav_view.push_view(next_view)
        
    def pop_screen(self):
        """Pops the top view off the stack (returns to the previous screen)."""
        self.nav_view.pop_view()
        
    def present(self, style='fullscreen'):
        """Displays the navigation container on screen."""
        self.nav_view.present(style)

    def setup_navigation(self, view: ui.View):
        self.root_view = view
        # self.root_view.name = "PocketRepo"
        # self.root_view.background_color = 'white'

        self.nav_view = ui.NavigationView(self.root_view)
        # self.nav_view.bar_tint_color = 'white'
        # self.nav_view.title_color = 'black'
        
