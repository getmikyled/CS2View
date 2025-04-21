import os

class ParsedDemo:

    name = ''
    path = ''

    ''' INSERT WHATEVER YOUR PARSED DEMO STUFF GOT HERE'''
    def __init__(self, file_path):
        self.name = os.path.basename(file_path)
        self.path = file_path
