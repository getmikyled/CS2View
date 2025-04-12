from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from view import *
from view.widgets import TitleBar, Toolbar
from styles import CS2ViewStyles

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

        # Create Tool Bar
        self.tool_bar = Toolbar()
        layout.addWidget(self.tool_bar)

        # Create Widget Stack
        self.stack = QStackedWidget()
        self.stack.setObjectName("Stack")
        self.stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.stack.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.stack, stretch=1) # Add stack widget to central layout

        # Populate Widget Stack
        self.home = Home()
        self.stack.addWidget(self.home)
        self.stack.setStyleSheet(CS2ViewStyles.STACK_STYLES)
