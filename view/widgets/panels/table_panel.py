from styles import CS2ViewStyles
from .panel import Panel

from PyQt5.QtWidgets import QTableWidget

class TablePanel(Panel):

    def __init__(self, parent=None):
        super().__init__(parent, expanding=True)

        self.table = QTableWidget()
        self.layout().addWidget(self.table)
        self.table.setStyleSheet(CS2ViewStyles.TABLE_STYLES)