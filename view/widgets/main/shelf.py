
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from styles import CS2ViewStyles


class Shelf(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set properties/styles
        self.setObjectName('Shelf')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(CS2ViewStyles.SHELF_HEIGHT)
        self.setStyleSheet(CS2ViewStyles.SHELF_STYLES)

        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CS2ViewStyles.PRIMARY_COLOR))
        self.setPalette(palette)


        # Create layout
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().setSpacing(5)

        self.shelf_items = []


    def add_shelf_item(self, name, qicon, tooltip=None):
        """Creates a shelf item and adds it to the shelf. Returns the ShelfItem"""
        shelf_item = ShelfItem(name, qicon, tooltip)
        self.shelf_items.append(shelf_item)
        self.layout().addWidget(shelf_item)

        return shelf_item


class ShelfItem(QPushButton):
    def __init__(self, name, qicon, tooltip=None):
        super().__init__()

        self.setStyleSheet(CS2ViewStyles.SHELF_STYLES)
        self.setFixedSize(CS2ViewStyles.SHELF_ITEM_SIZE, CS2ViewStyles.SHELF_ITEM_SIZE)

        self.name = name
        self.setToolTip(tooltip)
        self.setIcon(qicon)

