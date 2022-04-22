from controllers.templates.list_controller_template import ListControllerTemplate


class SimpleListController(ListControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)
