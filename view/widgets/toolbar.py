from PyQt5.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QToolButton, QMenu, QAction
from styles import CS2ViewStyles

class Toolbar(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set toolbar styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(20)

        # Create and set layout
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.padding = 5

        # Add file menu to toolbar
        file_menu = self.__create_menu()
        file_button = self.__create_tool_button("File", file_menu)
        file_menu.addAction(QAction("Option 1", file_button))

        # Add help menu to toolbar
        help_menu = self.__create_menu()
        help_button = self.__create_tool_button("Help", help_menu)
        help_menu.addAction(QAction("Option 1", help_button))

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer.setStyleSheet(f'background-color: {CS2ViewStyles.PRIMARY_COLOR};')

        # Add all widgets to toolbar
        layout.addWidget(file_button)
        layout.addWidget(help_button)
        layout.addWidget(spacer)

    def __create_menu(self):
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