import sys

from PyQt5.QtWidgets import QApplication

from cs2_view_window import CS2ViewWindow
from model import ParsedDemo, DemoLibrary

class CS2ViewController:

    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(*args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        # Check if DemoLibrary has been initialized
        if not self._initialized:
            self._demo_library = DemoLibrary()
        self._initialized = True

    def initialize_app(self):
        app = QApplication(sys.argv)
        self.window = CS2ViewWindow()

        # Register home callbacks
        self.window.home.upload_file_button.button.connect(lambda: self.upload_new_demo_file(self.window.home.file_selector.line_edit))

        self.window.setWidget(self.window.home)
        self.window.show()



        sys.exit(app.exec())

    def upload_new_demo_file(self, file_path):
        self._demo_library.upload_new_demo_file(file_path)

        self.window.stack.set_widget(self.window.data_view)

    def get_demo_data(self, file_path):
        return self._demo_library.get_demo_data(file_path)

    def get_current_demo_data(self):
        return self._demo_library.current_demo_data

