from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import Qt

from styles import CS2ViewStyles


class BottomRightButton(QWidget):

    def __init__(self, parent=None, text=''):
        super().__init__(parent)

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignBottom | Qt.AlignRight)

        # Set styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setStyleSheet(CS2ViewStyles.FIELD_STYLES)

        # Add push button
        self.button = QPushButton(text)
        self.button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button.setFixedSize(200, CS2ViewStyles.FIELD_HEIGHT)
        self.layout().addWidget(self.button)