from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QFileDialog
from styles import CS2ViewStyles
from .string_field import StringField

class FileSelector(StringField):

    def __init__(self, parent=None, fileFilter='All Files (*)'):
        super().__init__(parent, 'Select File')

        self.file_filter = fileFilter

        # Browse file button
        self.browse_file_button = QPushButton()
        file_icon = QIcon('icons/folder_icon.png')
        self.browse_file_button.setIcon(file_icon)
        self.browse_file_button.setIconSize(QSize(CS2ViewStyles.FIELD_HEIGHT, CS2ViewStyles.FIELD_HEIGHT))
        self.browse_file_button.setFixedHeight(CS2ViewStyles.FIELD_HEIGHT)
        self.browse_file_button.clicked.connect(self.open_file_dialog)
        self.layout().addWidget(self.browse_file_button)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File", "", self.file_filter)
        if file_path:
            self.line_edit.setText(file_path)
