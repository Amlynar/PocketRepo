import ui

class ProjectListContent(ui.View):

    def __init__(self, data_source=None, delegate=None):
        self.table_view = ui.TableView()
                
        self.table_view.data_source = data_source
        self.table_view.delegate = delegate
        self.add_subview(self.table_view)
