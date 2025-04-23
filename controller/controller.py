
class Controller:

    def __init__(self, model, view, parent_controller=None):

        # Cache model and view
        self.model = model
        self.view = view