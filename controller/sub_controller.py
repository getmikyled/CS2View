from .controller import Controller

class SubController(Controller):

    def __init__(self, model, view, parent_controller, widget_state=None):
        super().__init__(model, view)

        self.parent_controller = parent_controller
        self.widget_state = widget_state