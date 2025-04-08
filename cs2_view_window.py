from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import *
from home_view import HomeView

class CS2ViewWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up window
        self.setGeometry(0, 0, 1080, 720)
        self.setWindowTitle("CS2 View")
        self.windowIcon = None

        self.setWindowFlags(Qt.FramelessWindowHint)

        # Create Widget Stack
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Populate Widget Stack
        self.home_view = HomeView()
        self.stack.addWidget(self.home_view)