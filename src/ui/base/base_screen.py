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
        print("Showing loading spinner...")
        self.spinner = ui.ActivityIndicator()
        print("ActivityIndicator created.")
        # Choose style: 'gray', 'white', or 'white_large'
        self.spinner.style = ui.ACTIVITY_INDICATOR_STYLE_WHITE_LARGE
        self.spinner.color = '#333333' # Dark gray spinner color
        print("set styles")
        # Ensure it stays on screen when initialized
        self.spinner.hides_when_stopped = True
        print("hides when stopped")
        # Add the spinner to this view hierarchy
        self.add_subview(self.spinner)
        print("added subview")
        # Start the spinning animation automatically
        self.spinner.start()
        print("Loading spinner shown.")

    def hide_loading_spinner(self):
        if self.spinner:
            self.spinner.stop()
            self.remove_subview(self.spinner)
            self.spinner = None

    def layout(self):
        if self.spinner:
            # Center the spinner in the view
            self.spinner.center = (self.width * 0.5, self.height * 0.5)