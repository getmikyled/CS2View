from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from styles import CS2ViewStyles

class Panel(QWidget):

    def __init__(self, parent=None, expanding=True):
        super().__init__(parent)

        # Set properties/styles
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CS2ViewStyles.PRIMARY_COLOR))
        self.setPalette(palette)

        if expanding:
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Create and set layout
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)