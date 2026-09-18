import ui

class PRBaseScreen(ui.View):
    def __init__(self):
        self.model = None
        self.view = None
        self.spinner = None
        self.background_color = 'white'
        self.flex = 'LRTB'
        super().__init__()

    def show_loading_spinner(self):
        self.spinner = ui.ActivityIndicator()
        
        # Choose style: 'gray', 'white', or 'white_large'
        self.spinner.style = ui.ACTIVITY_INDICATOR_STYLE_WHITE_LARGE
        self.spinner.color = '#333333' # Dark gray spinner color
        
        # Ensure it stays on screen when initialized
        self.spinner.hides_when_stopped = True
        
        # Add the spinner to this view hierarchy
        self.add_subview(self.spinner)
        
        # Start the spinning animation automatically
        self.spinner.start()

    def hide_loading_spinner(self):
        if self.spinner:
            self.spinner.stop()
            self.remove_subview(self.spinner)
            self.spinner = None

    def layout(self):
        super().layout()
        if self.spinner:
            # Center the spinner in the view
            self.spinner.center = (self.width * 0.5, self.height * 0.5)