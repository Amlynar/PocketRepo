

from injector import inject

from common.repositories.catalog_repo import CatalogRepository
from framework.mvc.controller import PYIController
from screens.project_details.project_details_model import ProjectDetailsModel
from screens.project_details.project_details_view import ProjectDetailsView


class ProjectDetailsController(PYIController):

    @inject
    def __init__(self, model: ProjectDetailsModel, view: ProjectDetailsView, catalog_repository: CatalogRepository):
        super().__init__()
        self.model = model
        self.view = view
        self.catalog_repository = catalog_repository
        self.project_id: str | None = None

    def on_screen_loaded(self):
        if self.project_id is None:
            raise ValueError("project_id is None")
        # self.view.title_label.text = f"Project ID:{self.project_id}"
        # self.view.root_view.add_subview(self.view.title_label)

        
        self.view.show_content(self.view.root_view)
