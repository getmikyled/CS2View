from PyQt5.QtWidgets import *
import sys

class HomeView(QWidget):

    def __init__(self):
        super().__init__()

        # Add label
        text = QLabel(self)
        text.setText("HELLO")
