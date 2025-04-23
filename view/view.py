from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

from styles import CS2ViewStyles

class View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)