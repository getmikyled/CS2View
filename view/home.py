from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from styles import CS2ViewStyles
from .widgets import Header, ButtonPanel, Panel

class Home(QWidget):

    def __init__(self):
        super().__init__()

        # Set widget properties
        self.setObjectName('Page')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(10, 10, 10, 10)

        # Set styles
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CS2ViewStyles.SECONDARY_COLOR))
        self.setPalette(palette)

        # Create and set layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create panel container
        panelContainer = QWidget()
        panelLayout = QHBoxLayout()
        panelContainer.setLayout(panelLayout)

        # Create Button panel
        self.button_panel = ButtonPanel()
        self.button_panel.create_button("Upload New CS2 '.demo' File")
        self.button_panel.create_button("Open Recent '.demo' File")
        self.button_panel.create_button("Compare Two CS2 '.demo' File")

        # NOTE: TO BE REPLACED W/ STACK WIDGET
        self.other_panel = Panel()

        # Add widgets to layouts
        layout.addWidget(Header())
        layout.addWidget(panelContainer)
        panelLayout.addWidget(self.button_panel)
        panelLayout.addWidget(self.other_panel)