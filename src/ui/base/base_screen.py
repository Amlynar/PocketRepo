import ui

class PRBaseScreen(ui.View):
    def __init__(self):
        self.loading_spinner = None
        self.content = None
        self.error = None
        self.background_color = 'blue'
        self.flex = 'WH'
        super().__init__()

    def layout(self):
        if self.loading_spinner:
            self.loading_spinner.center = (self.width * 0.5, self.height * 0.5)
        if self.content:
            self.content.frame = (0, 0, self.width, self.height)
        if self.error:
            self.error.frame (0, 0, self.width, self.height)

    def show_loading(self):
        if self.loading_spinner:
            return
        self.hide_all_displayed()
            
        self.loading_spinner = ui.ActivityIndicator()
        self.loading_spinner.style = ui.ACTIVITY_INDICATOR_STYLE_GRAY
        self.loading_spinner.color = '#333333' # Dark gray spinner color
        self.loading_spinner.center = (self.width * 0.5, self.height * 0.5)
        # self.loading_spinner.alignment = ui.ALIGN_CENTER
        self.loading_spinner.hides_when_stopped = True
        
        self.add_subview(self.loading_spinner)
        self.loading_spinner.start()

    def hide_loading(self):
        if self.loading_spinner:
            self.loading_spinner.stop()
            self.remove_subview(self.loading_spinner)
            self.loading_spinner = None

    def show_error(self):
        if self.error:
            return
        self.hide_all_displayed()
        # TODO Implement full screen error state

    def hide_error(self):
        if self.error:
            self.remove_view(self.error)
            self.error = None

    def show_content(self, view: ui.View):
        if self.content:
            return
        self.hide_all_displayed()
        self.content = view
        self.add_subview(self.content)

    def hide_content(self):
        if self.content:
            self.remove_subview(self.content)
            self.content = None

    def hide_all_displayed(self):
        if self.loading_spinner:
            self.hide_loading()
        if self.content:
            self.hide_content()
        if self.error:
            self.hide_error()
