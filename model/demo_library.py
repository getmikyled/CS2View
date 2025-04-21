from . import *
import os

class DemoLibrary:

    _parsed_demos = None
    _current_demo_data = None

    def __init__(self):
        """ Initializes demo library"""
        self._parsed_demos = {}
        self.current_demo_data = None
        pass

    def upload_new_demo_file(self, file_path):
        """Upload new demo file into the application's model in form of {file_name : parsed_demo}"""
        file_name = os.path.basename(file_path)
        self.current_demo_data = ParsedDemo(file_path)
        self._parsed_demos[file_name] = self.current_demo_data

    @property
    def current_demo_data(self):
        return self._current_demo_data

    @current_demo_data.setter
    def current_demo_data(self, value):
        self._current_demo_data = value

    def get_demo_data(self, file_path):
        """Returns demo file defined by file_name. Demo file must be parsed and in the library already.
        Note: At the moment, parameter is in file_path and is converted to name here, but is open to change for preference."""
        file_name = os.path.basename(file_path)
        return self._parsed_demos[file_name]