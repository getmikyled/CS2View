from tokenize import String

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QPushButton, QFileDialog
from styles import CS2ViewStyles
from view.widgets import StringField

class FileSelector(StringField):

    def __init__(self, parent=None):
        super().__init__(parent, 'Select File')

        # Browse file button
        self.browse_file_button = QPushButton()
        file_icon = QIcon('icons/folder_icon.png')
        self.browse_file_button.setIcon(file_icon)
        self.browse_file_button.setIconSize(QSize(CS2ViewStyles.FIELD_HEIGHT, CS2ViewStyles.FIELD_HEIGHT))
        self.browse_file_button.setFixedHeight(CS2ViewStyles.FIELD_HEIGHT)
        self.browse_file_button.clicked.connect(self.open_file_dialog)
        self.layout().addWidget(self.browse_file_button)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "Demo Files (*.demo);;All Files (*)")
        if file_path:
            self.line_edit.setText(file_path)
