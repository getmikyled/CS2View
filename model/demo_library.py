from . import *
import os

class DemoLibrary:

    _parsed_demos = None

    def __init__(self):
        """ Initializes demo library"""
        self._parsed_demos = {}
        pass

    def upload_new_demo_file(self, file_path):
        """Upload new demo file into the application's model in form of {file_name : parsed_demo}"""
        fileName = os.path.basename(file_path)
        self._parsed_demos[fileName] = ParsedDemo(file_path)

    def get_demo_data(self, file_path):
        """Returns demo file defined by file_name. Demo file must be parsed and in the library already.
        Note: At the moment, parameter is in file_path and is converted to name here, but is open to change for preference."""
        fileName = os.path.basename(file_path)
        return self._parsed_demos[fileName]