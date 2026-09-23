

from injector import inject
from common.services.project_delete_service import ProjectDeleteService
from common.services.project_update_service import ProjectUpdateService
from framework.alert.alert_dialog import PYIAlert
import ui

from common.repositories.catalog_repo import CatalogRepository, InvalidProjectIdError
from framework.mvc.controller import PYIController
from framework.style.style_table_view_cell import PYITableViewCellStyle
from framework.style.theme import PYITheme
from screens.project_details.project_details_model import ProjectDetailsModel
from screens.project_details.project_details_view import ProjectDetailsView


class ProjectDetailsController(PYIController):

    @inject
    def __init__(self, model: ProjectDetailsModel, view: ProjectDetailsView, theme: PYITheme, catalog_repository: CatalogRepository, project_delete_service: ProjectDeleteService, project_update_service: ProjectUpdateService):
        super().__init__()
        self.model = model
        self.view = view
        self.theme = theme
        self.catalog_repository = catalog_repository
        self.project_update_service = project_update_service
        self.project_delete_service = project_delete_service
        self.project_id: str | None = None

        self.view.init_root_view(data_source=self)

    @ui.in_background
    def on_screen_loaded(self):
        if self.project_id is None:
            PYIAlert.simple_alert(title="Error",message="View is None")
            return
        
        self.view.show_loading()
        try:
            project = self.catalog_repository.fetch_project(self.project_id)
            self.model.load_from_project(project)

            self.view.title_label.text = self.model.title
            self.view.desc_label.text = self.model.description
            self.view.display_content()
        except InvalidProjectIdError as e:
            self.view.show_error("Error", e.message)
        except Exception as _:
            self.view.show_error()

    def tableview_number_of_rows(self, tableview, section):
            return len(self.model.info_list)
        
    def tableview_cell_for_row(self, tableview, section, row):
        info_item = self.model.info_list[row]
        cell = ui.TableViewCell('default')
        PYITableViewCellStyle.navigation(cell, self.theme)
        cell.text_label.text = info_item[1]
        return cell

    @ui.in_background
    def delete_action(self, sender):
        if self.project_id is None:
            PYIAlert.simple_alert(title="Error",message="Project ID is None")
            return

        try:
            self.view.delete_spinner.start()
            self.project_delete_service.delete_project(self.project_id)
        except InvalidProjectIdError as _:
            PYIAlert.simple_alert(title="Error",message="Invalid Project ID")
        except Exception as _:
            PYIAlert.simple_alert(title="Error",message="Unable to delete.")
        finally:
            self.view.delete_spinner.stop()

    @ui.in_background
    def install_action(self, sender):
        if self.project_id is None:
            PYIAlert.simple_alert(title="Error",message="Project ID is None")
            return

        try:
            self.view.install_spinner.start()
            self.project_update_service.update_project(self.project_id)
        except InvalidProjectIdError as _:
            PYIAlert.simple_alert(title="Error",message="Invalid Project ID")
        except Exception as _:
            PYIAlert.simple_alert(title="Error",message="Unable to install.")
        finally:
            self.view.install_spinner.stop()

        