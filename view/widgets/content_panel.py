from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from styles import CS2ViewStyles
from view.widgets import Panel

class ContentPanel(QWidget):

    def __init__(self, title, parent=None):
        super().__init__(parent)

        # Set style sheets
        self.setStyleSheet(CS2ViewStyles.CONTENT_PANEL_STYLES)

        # Set layout
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(10)

        # Add content title text
        content_title_label = QLabel(title)
        content_title_label.setObjectName('TitleLabel')
        content_title_label.setAlignment(Qt.AlignLeft)
        self.layout().addWidget(content_title_label)

        # Add content panel
        self.panel = Panel(color=QColor(CS2ViewStyles.SECONDARY_COLOR))
        self.layout().addWidget(self.panel)