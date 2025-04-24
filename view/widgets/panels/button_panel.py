from PyQt5.QtWidgets import QPushButton, QSizePolicy
from view.widgets.panels.panel import Panel

from styles import CS2ViewStyles

class ButtonPanel(Panel):

    def __init__(self, parent=None, width=400, expanding=True):
        super().__init__(parent=parent, expanding=expanding)

        # Set widget properties
        self.setObjectName('ButtonPanel')

        # Set styles
        self.setStyleSheet(CS2ViewStyles.BUTTON_PANEL_STYLES)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(width)

    def create_button(self, text, on_clicked_func=None):
        '''Creates a new button of specified input and is added to the panel'''
        button = QPushButton(text)
        button.setObjectName('ButtonPanelButton')

        if on_clicked_func is not None:
            button.clicked.connect(on_clicked_func)

        self.layout().addWidget(button)

        return button