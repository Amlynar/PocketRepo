import ui

class PYITheme:

    def __init__(self):
        self.background_color_primary = 'white'
        self.spinner_style = ui.ACTIVITY_INDICATOR_STYLE_GRAY

class PYIThemeBuilder:

    def __init__(self):
        self.theme = PYITheme()

    def set_background_color_primary(self, color):
        self.theme.background_color_primary = color
        return self

    def set_spinner_style(self, style):
        self.theme.spinner_style = style
        return self
    