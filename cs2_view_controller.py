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

    def upload_new_demo_file(self, file_path):
        self._demo_library.upload_new_demo_file(file_path)

    def get_demo_data(self, file_path):
        return self._demo_library.get_demo_data(file_path)
