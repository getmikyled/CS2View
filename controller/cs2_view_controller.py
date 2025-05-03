import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication

from view import DataView
from .home_controller import HomeController
from .data_controller import DataController
from cs2_view_window import CS2ViewWindow
from model import DemoLibrary
from view import HomeView

class CS2ViewController:

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        '''Set up singleton'''
        if cls._instance is None:
            cls._instance = super().__new__(*args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        '''Initializes the controller if it does not exist'''
        # Check if DemoLibrary has been initialized
        if not self._initialized:
            self._demo_library = DemoLibrary()

            # Start application
            QApplication.setStyle('Fusion')
            app = QApplication(sys.argv)
            self.window = CS2ViewWindow()

            self.window.toolbar.upload_new_file_action.triggered.connect(self.on_upload_new_file_action_triggered)
            self.window.toolbar.open_recent_file_action.triggered.connect(self.on_open_recent_file_action_triggered)
            self.window.toolbar.documentation_action.triggered.connect(self.on_documentation_action_triggered)

            # Set home and controller
            self.home_view = HomeView()
            home_widget_state = self.window.stack.addWidget(self.home_view)
            self.home_controller = HomeController(model=self._demo_library, view=self.home_view, parent_controller=self, widget_state=home_widget_state)

            # Set data view
            self.data_view = DataView()
            data_view_widget_state = self.window.stack.addWidget(self.data_view)
            self.data_controller = DataController(model=self._demo_library, view=self.data_view, parent_controller=self, widget_state=data_view_widget_state)

            self.window.set_widget(self.home_view)
            self.window.show()

            self._initialized = True

            sys.exit(app.exec())


    def upload_new_demo_file(self, file_path):
        self._demo_library.upload_new_demo_file(file_path)
        parsed_demo = self._demo_library.get_demo_data(file_path)
        self.data_controller.load_demo(parsed_demo)

        self.window.stack.set_widget(self.data_view)

    def set_demo_file(self, parsed_demo):
        self.data_controller.load_demo(parsed_demo)

        self.window.stack.set_widget(self.data_view)

    def get_demo_data(self, file_path):
        return self._demo_library.get_demo_data(file_path)

    def get_current_demo_data(self):
        return self._demo_library.current_demo_data

    def on_upload_new_file_action_triggered(self):
        self.window.set_widget(self.home_view)
        self.home_controller.set_widget(self.home_view.upload_demo_file_widget)

    def on_open_recent_file_action_triggered(self):
        self.window.set_widget(self.home_view)
        self.home_controller.set_widget(self.home_view.open_recent_file_widget)
        self.home_controller.refresh_recent_files()

    def on_documentation_action_triggered(self):
        url = QUrl('https://docs.google.com/document/d/1RAqIRo2O7rLT9-u1pLzBo7P7TmfK4t5fGA6AnJOGEME/edit?usp=sharing')
        QDesktopServices.openUrl(url)
