
from collections.abc import Callable

class PRNavigation:
    def __init__(self):
        self.navigate: Callable[[PRNavigationRoute], None] | None = None
        
# Routes

class PRNavigationRoute: pass

class ProjectListScreenRoute(PRNavigationRoute): pass

