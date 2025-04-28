from . import *
import os


class DemoLibrary:
    def __init__(self):
        self._parsed_demos = {}
        self._current_demo_data = None

    def upload_new_demo_file(self, file_path):
        """Upload and parse a new demo file into the library."""
        file_name = os.path.basename(file_path)
        parsed_demo = ParsedDemo(file_path)  # create a ParsedDemo
        self._parsed_demos[file_name] = parsed_demo  # store it directly
        self._current_demo_data = parsed_demo  # update current demo

    @property
    def current_demo_data(self):
        return self._current_demo_data

    @current_demo_data.setter
    def current_demo_data(self, value):
        self._current_demo_data = value

    def get_demo_data(self, file_path):
        """Returns parsed demo object given a file path."""
        file_name = os.path.basename(file_path)
        return self._parsed_demos.get(file_name)
    
    def __getitem__(self, file_name):
        """
        Allows access to parsed demos using the file name.
            Example: demo_library['demo.dem']
        """
        return self._parsed_demos.get(file_name)
