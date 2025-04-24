from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from styles import CS2ViewStyles

class Panel(QWidget):

    def __init__(self, parent=None, expanding=True, color=QColor(CS2ViewStyles.PRIMARY_COLOR)):
        super().__init__(parent)

        # Set properties/styles
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)

        if expanding:
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Create and set layout
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.layout().setContentsMargins(10, 10, 10, 10)
        self.layout().setSpacing(10)