from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from .panel import Panel

from styles import CS2ViewStyles


class ButtonPanel(Panel):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set widget properties
        self.setObjectName('ButtonPanel')

        # Set styles
        self.setStyleSheet(CS2ViewStyles.BUTTON_PANEL_STYLES)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(400)

    def create_button(self, text, onClickedFunc=None):
        '''Creates a new button of specified input and is added to the panel'''
        button = QPushButton(text)
        button.setObjectName('ButtonPanelButton')

        if onClickedFunc is not None:
            button.clicked.connect(onClickedFunc)

        self.layout.addWidget(button)