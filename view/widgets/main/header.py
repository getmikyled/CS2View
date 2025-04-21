from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout

from styles import CS2ViewStyles


class Header(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(125)
        self.setStyleSheet(CS2ViewStyles.HEADER_STYLES)

        # Set up the layout
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignTop)

        # Header Label
        headerLabel = QLabel(f'<b><span style="color: {CS2ViewStyles.ACCENT_COLOR_1};">CS2</span>'
                            f'<span style="color: {CS2ViewStyles.ACCENT_COLOR_2};"> View</span></b>')
        headerLabel.setObjectName('HeaderLabel')

        # Description Label
        descriptionLabel = QLabel('Analyze Your CS2 Matches')
        descriptionLabel.setObjectName('DescriptionLabel')

        # Add all widgets to layout
        layout.addWidget(headerLabel)
        layout.addWidget(descriptionLabel)