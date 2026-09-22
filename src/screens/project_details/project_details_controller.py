

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

    @ui.in_background
    def on_screen_loaded(self):
        if self.project_id is None:
            raise ValueError("project_id is None")
        # self.view.title_label.text = f"Project ID:{self.project_id}"
        # self.view.root_view.add_subview(self.view.title_label)
        self.view.show_loading()

        project = self.catalog_repository.get_project_by_id(self.project_id)
        self.model.load_from_project(project)

        self.view.title_label.name = self.model.title
        self.view.desc_label.name = self.model.description
        self.view.display_content()

    def tableview_number_of_rows(self, tableview, section):
            return len(self.model.info_list)
        
    def tableview_cell_for_row(self, tableview, section, row):
        info_item = self.model.info_list[row]
        cell = ui.TableViewCell('default')
        PYITableViewCellStyle.navigation(cell, self.theme)
        cell.text_label.text = info_item[row][1]
        return cell
        