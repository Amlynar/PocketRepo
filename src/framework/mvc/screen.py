
from framework.style.style_label import PYILabelStyle
from framework.style.style_screen import PYIScreenStyle
from framework.style.style_spinner import PYISpinnerStyle
from framework.style.style_view import PYIViewStyle
from framework.style.theme import PYITheme
import ui


class PYIScreen(ui.View):
    def __init__(self, theme: PYITheme):
        self.theme = theme
        PYIScreenStyle.fullscreen(self,self.theme)

        self.root_view: ui.View = ui.View()
        PYIViewStyle.clear(self.root_view, self.theme)
        self.root_view.flex = 'WH'

        self.loading_spinner = None
        self.content = None
        self.error = None

        super().__init__()

    def layout(self):
        if self.loading_spinner:
            self.loading_spinner.center = (self.width * 0.5, self.height * 0.5)
        if self.content:
            self.content.frame = (0, 0, self.width, self.height)
        if self.error:
            self.error.frame = (0, 0, self.width, self.height)

            pad = 16
                    
            self.error_title_label.frame = (pad, pad, self.width - (pad * 2), 40)

            desc_top = self.error_title_label.frame[1] + self.error_title_label.frame[3] + 8
            self.error_desc_label.frame = (pad, desc_top, self.width - (pad * 2), 50)

    def show_loading(self):
        if self.loading_spinner:
            return
        self.hide_all_displayed()
            
        self.loading_spinner = ui.ActivityIndicator()
        PYISpinnerStyle.loading(self.loading_spinner, self.theme)
        self.loading_spinner.center = (self.width * 0.5, self.height * 0.5)
        
        self.add_subview(self.loading_spinner)
        self.loading_spinner.start()

    def hide_loading(self):
        if self.loading_spinner:
            self.loading_spinner.stop()
            self.remove_subview(self.loading_spinner)
            self.loading_spinner = None

    def show_error(self, title="Error", message="Something went wrong."):
        if self.error:
            return
        self.hide_all_displayed()

        self.error_title_label = ui.Label()
        PYILabelStyle.title(self.error_title_label, self.theme)
        self.error_title_label.flex = 'WH'
        self.error_title_label.text = title
        self.error_title_label.alignment = ui.ALIGN_CENTER
        
        self.error_desc_label = ui.Label()
        PYILabelStyle.normal(self.error_desc_label, self.theme)
        self.error_desc_label.flex = 'WH'
        self.error_desc_label.text = message
        self.error_desc_label.alignment = ui.ALIGN_CENTER

        self.error = ui.View()
        PYIViewStyle.clear(self.error, self.theme)
        self.error.flex = 'WH'
        for v in (
            self.error_title_label,
            self.error_desc_label
        ):
            self.error.add_subview(v)
        self.add_subview(self.error)

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
