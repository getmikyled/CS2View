from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from pages import *
from CS2ViewWidgets import *

class CS2ViewWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up window
        self.setGeometry(300, 300, 1080, 720)
        self.setWindowTitle("CS2 View")
        self.windowIcon = None

        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set up central widget and layout
        central = QWidget()
        central.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central.setContentsMargins(0, 0, 0, 0)
        layout = QVBoxLayout(central)
        central.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setCentralWidget(central)

        # Create Title Bar
        self.title_bar = TitleBar()
        self.title_bar.on_minimize_window_button_clicked.connect(self.showMinimized) # self.showMinimized binded
        self.title_bar.on_close_window_button_clicked.connect(self.close) # self.close binded
        layout.addWidget(self.title_bar) # Add title bar widget to central layout

        # Create Widget Stack
        self.stack = QStackedWidget()
        self.stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.stack, stretch=1) # Add stack widget to central layout

        # Populate Widget Stack
        self.home = Home()
        self.stack.addWidget(self.home)