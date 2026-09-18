import ui

class NavigationManager:

    def __init__(self):
        self.root_view = ui.View()
        self.root_view.name = "PocketRepo"
        self.root_view.background_color = 'white'

        self.nav_view = ui.NavigationView(self.root_view)

    def push_screen(self, next_view: ui.View):
        """Pushes a new ui.View onto the navigation stack."""
        self.nav_view.push_view(next_view)
        
    def pop_screen(self):
        """Pops the top view off the stack (returns to the previous screen)."""
        self.nav_view.pop_view()
        
    def present(self, style='fullscreen'):
        """Displays the navigation container on screen."""
        self.nav_view.present(style)
        
