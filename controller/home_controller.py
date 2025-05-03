from .sub_controller import SubController

class HomeController(SubController):

    def __init__(self, model, view, parent_controller, widget_state=None):
        super().__init__(model, view, parent_controller, widget_state)

        # Upload demo file button callback
        self.view.upload_demo_file_widget_button.clicked.connect(
            lambda: self.set_widget(self.view.upload_demo_file_widget)
        )

        # Open recent demo file button callback
        self.view.open_recent_demo_file_widget_button.clicked.connect(
            lambda: self.set_widget(self.view.open_recent_file_widget)
        )

        # On upload file button clicked
        self.view.upload_file_button.button.clicked.connect(
            lambda: self.parent_controller.upload_new_demo_file(self.parent_controller.home_view.file_selector.line_edit.text())
        )

        '''
        Removed since menu button was removed
        # On view entered
        self.widget_state.on_entered_signal.connect(
            # Set menu button in tool bar to not visible
            lambda: self.parent_controller.window.toolbar.menu_button.setVisible(False)
        )

        # On view exited
        self.widget_state.on_exited_signal.connect(
            # Set menu button in tool bar to visible
            lambda: self.parent_controller.window.toolbar.menu_button.setVisible(True)
        )
        '''

    def set_widget(self, widget):
        self.view.substack.set_widget(widget)