
from injector import Module, provider, singleton

from framework.style.theme import PYITheme, PYIThemeBuilder


class AppModule(Module):

    @singleton
    @provider
    def provide_theme(self) -> PYITheme:
        return (
            PYIThemeBuilder()
            # .set_screen_background_color('red')
            .set_navigation_bar_background_color('red')
            .build()
        )
    