from PyQt5.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QPushButton, QToolButton, QMenu, QAction
from PyQt5.QtGui import QIcon
from styles import CS2ViewStyles

class Toolbar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set toolbar styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(CS2ViewStyles.TOOLBAR_HEIGHT)

        # Create and set layout
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.padding = 5

        # Create menu button
        self.menu_button = QPushButton()
        self.menu_button.setObjectName('MenuButton')
        self.menu_button.setStyleSheet(CS2ViewStyles.TOOLBAR_STYLES)
        self.menu_button.setFixedSize(CS2ViewStyles.TOOLBAR_MENU_BUTTON_SIZE, CS2ViewStyles.TOOLBAR_MENU_BUTTON_SIZE)
        self.menu_button.setIcon(QIcon('icons/menu_icon.png'))
        self.menu_button.clicked.connect(self.__on_menu_button_clicked)

        # Add file menu to toolbar
        file_menu = self.__create_qmenu()
        file_button = self.__create_tool_button("File", file_menu)
        file_menu.addAction(QAction("Option 1", file_button))

        # Add help menu to toolbar
        help_menu = self.__create_qmenu()
        help_button = self.__create_tool_button("Help", help_menu)
        help_menu.addAction(QAction("Option 1", help_button))

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer.setStyleSheet(f'background-color: {CS2ViewStyles.PRIMARY_COLOR};')

        # Add all widgets to toolbar
        layout.addWidget(self.menu_button)
        layout.addWidget(file_button)
        layout.addWidget(help_button)
        layout.addWidget(spacer)

    def __create_qmenu(self):
        """ Creates a menu"""
        menu = QMenu()
        menu.setStyleSheet(CS2ViewStyles.TOOLBAR_STYLES)
        menu.setObjectName('ToolbarMenu')

        return menu

    def __create_tool_button(self, text, menu) -> QToolButton:
        """ Creates a tool button"""
        button = QToolButton()
        button.setObjectName('ToolbarButton')
        button.setStyleSheet(CS2ViewStyles.TOOLBAR_STYLES)
        button.setPopupMode(QToolButton.InstantPopup)
        button.setText(text)

        if menu is not None:
            button.setMenu(menu)

        return button

    def __on_menu_button_clicked(self):
        pass