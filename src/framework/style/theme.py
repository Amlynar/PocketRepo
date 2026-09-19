import ui

class PYITheme:

    def __init__(self):
        self.screen_background_color = 'white'
        self.navigation_bar_background_color = 'blue'
        self.spinner_style = ui.ACTIVITY_INDICATOR_STYLE_GRAY

class PYIThemeBuilder:

    def __init__(self):
        self.theme = PYITheme()

    def set_background_color(self, color):
        self.theme.screen_background_color = color
        return self

    def set_navigation_bar_background_color(self, color):
        self.theme.navigation_bar_background_color = color
        return self

    def set_spinner_style(self, style):
        self.theme.spinner_style = style
        return self
    