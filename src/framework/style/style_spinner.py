
from framework.style.theme import PYITheme
import ui

class PYISpinnerStyle:

    @staticmethod
    def loading(spinner: ui.ActivityIndicator, theme: PYITheme):
        spinner.style = theme.spinner_style
        spinner.hides_when_stopped = True
        # loading_spinner.color = '#333333' # Dark gray spinner color
        # loading_spinner.alignment = ui.ALIGN_CENTER
        