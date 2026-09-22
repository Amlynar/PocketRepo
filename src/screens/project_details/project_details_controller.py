

from injector import inject
import ui

from common.repositories.catalog_repo import CatalogRepository
from framework.mvc.controller import PYIController
from framework.style.style_table_view_cell import PYITableViewCellStyle
from framework.style.theme import PYITheme
from screens.project_details.project_details_model import ProjectDetailsModel
from screens.project_details.project_details_view import ProjectDetailsView


class ProjectDetailsController(PYIController):

    @inject
    def __init__(self, model: ProjectDetailsModel, view: ProjectDetailsView, theme: PYITheme, catalog_repository: CatalogRepository):
        super().__init__()
        self.model = model
        self.view = view
        self.theme = theme
        self.catalog_repository = catalog_repository
        self.project_id: str | None = None

        self.view.init_root_view(data_source=self)

    def on_screen_loaded(self):
        if self.project_id is None:
            raise ValueError("project_id is None")
        # self.view.title_label.text = f"Project ID:{self.project_id}"
        # self.view.root_view.add_subview(self.view.title_label)


        self.view.show_content(self.view.root_view)

    def tableview_number_of_rows(self, tableview, section):
            return 10
        
    def tableview_cell_for_row(self, tableview, section, row):
        # project = self.model.projects[row]
        cell = ui.TableViewCell('default')
        PYITableViewCellStyle.navigation(cell, self.theme)
        cell.text_label.text = "Some test item"
        return cell