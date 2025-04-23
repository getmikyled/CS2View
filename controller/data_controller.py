from .sub_controller import SubController

class DataController(SubController):

    def __init__(self, model, view, parent_controller, widget_state):
        super().__init__(model, view, parent_controller, widget_state)