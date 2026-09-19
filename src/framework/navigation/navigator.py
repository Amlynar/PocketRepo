
from collections.abc import Callable

class PYINavigationDelegate:
    def __init__(self):
        self.navigate: Callable[[PYIRoute], None] | None = None
        
# Routes

class PYIRoute: pass
