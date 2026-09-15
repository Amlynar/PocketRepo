import ui

class PRBaseScreen(ui.View):
    def __init__(self):
        self.model = None
        self.view = None
        self.background_color = 'white'
        self.flex = 'LRTB'
        super().__init__()
