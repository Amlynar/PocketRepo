import ui

class PRBaseScreen(ui.View):
    def __init__(self):
        self.model = None
        self.view = None
        self.spinner = None
        self.background_color = 'white'
        self.flex = 'W+H' # Note: Use 'W+H' to allow the view to expand/fill parent containers
        # self.flex = 'LRTB'
        super().__init__()

    def show_loading_spinner(self):
        if self.spinner:
            return  # Spinner is already active
            
        self.spinner = ui.ActivityIndicator()
        
        # Choose style: 'gray', 'white', or 'white_large'
        # self.spinner.style = ui.ACTIVITY_INDICATOR_STYLE_WHITE_LARGE
        self.spinner.style = ui.ACTIVITY_INDICATOR_STYLE_GRAY
        self.spinner.color = '#333333' # Dark gray spinner color
        
        # FIX 1: Provide explicit dimensions for the spinner frame
        # self.spinner.width = 50
        # self.spinner.height = 50
        
        # Center it immediately on creation for the initial frame draw
        self.spinner.center = (self.width * 0.5, self.height * 0.5)
        
        self.spinner.hides_when_stopped = True
        
        self.add_subview(self.spinner)
        
        self.spinner.start()

    def hide_loading_spinner(self):
        if self.spinner:
            self.spinner.stop()
            self.remove_subview(self.spinner)
            self.spinner = None

    def layout(self):
        print("layout called")
        if self.spinner:
            self.spinner.center = (self.width * 0.5, self.height * 0.5)