from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QPushButton, QFileDialog
from styles import CS2ViewStyles

class StringField(QWidget):

    def __init__(self, parent=None, text='Label'):
        super().__init__(parent)

        # Set layout
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout().padding = 0
        self.layout().setContentsMargins(0, 0, 0, 0)


        # Set styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(CS2ViewStyles.FIELD_HEIGHT + 10)
        self.setStyleSheet(CS2ViewStyles.FIELD_STYLES)

        # Add label
        self.label = QLabel(text)
        self.label.setFixedSize(200, CS2ViewStyles.FIELD_HEIGHT)
        self.layout().addWidget(self.label)

        # Add line edit
        self.line_edit = QLineEdit()
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line_edit.setFixedHeight(CS2ViewStyles.FIELD_HEIGHT)
        self.layout().addWidget(self.line_edit)
