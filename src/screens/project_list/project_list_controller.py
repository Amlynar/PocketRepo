from common.repositories.catalog_repo import CatalogRepository
from common.services.project_update_service import ProjectUpdateService
from framework.mvc.controller import PYIController
from framework.style.style_table_view_cell import PYITableViewCellStyle
from framework.style.theme import PYITheme
from navigation.routes import ProjectDetailsScreenRoute
from screens.project_list.project_list_model import ProjectListModel
from screens.project_list.project_list_view import ProjectListView
import ui
from injector import inject


class ProjectListController(PYIController):

    @inject
    def __init__(self, model: ProjectListModel, view: ProjectListView, theme: PYITheme, project_update_service: ProjectUpdateService, catalog_repository: CatalogRepository):
        super().__init__()
        self.model = model
        self.view = view
        self.theme = theme
        self.project_update_service = project_update_service
        self.catalog_repository = catalog_repository

        self.view.init_root_view(data_source=self)

        
    @ui.in_background
    def on_screen_loaded(self):
        if self.view is None:
            pass
    
        self.view.show_loading()
        try:
            self.model.projects = self.catalog_repository.fetch_all_projects()
            self.view.display_content()
        except Exception as _:
            self.view.show_error()
        
    def tableview_number_of_rows(self, tableview, section):
        return len(self.model.projects)
    
    def tableview_cell_for_row(self, tableview, section, row):
        project = self.model.projects[row]
        cell = ui.TableViewCell('default')
        PYITableViewCellStyle.navigation(cell, self.theme)
        cell.text_label.text = project.name
        return cell

    def tableview_did_select(self, tableview, section, row):
        project = self.model.projects[row]
        self.navigate(ProjectDetailsScreenRoute(project_id=project.id))
