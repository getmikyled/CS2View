from distutils.command.upload import upload

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *

from styles import CS2ViewStyles
from .widgets import Header, ButtonPanel, Panel, StackedWidgetStateMachine, ContentPanel, FileSelector, StringField, \
    BottomRightButton


class Home(QWidget):

    def __init__(self):
        super().__init__()

        # Set widget properties
        self.setObjectName('Page')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(10, 10, 10, 10)

        # Set styles
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CS2ViewStyles.SECONDARY_COLOR))
        self.setPalette(palette)

        # Create and set layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        # Create panel container
        panelContainer = QWidget()
        panelLayout = QHBoxLayout()
        panelContainer.setLayout(panelLayout)

        # Create Button panel
        self.button_panel = ButtonPanel()
        self.button_panel.create_button("Upload New CS2 '.demo' File", lambda: self.stacked_widget_state_machine.set_widget(self.upload_demo_file_widget))
        self.button_panel.create_button("Open Recent '.demo' File", lambda: self.stacked_widget_state_machine.set_widget(self.open_recent_demo_file_widget))

        # Create main panel
        self.main_panel = Panel()

        # Create stacked widget
        self.stacked_widget_state_machine = StackedWidgetStateMachine()
        self.main_panel.layout().addWidget(self.stacked_widget_state_machine)

        # Populate stacked widget
        self.empty_widget = QWidget()
        self.stacked_widget_state_machine.addWidget(self.empty_widget)
        self.upload_demo_file_widget = self.__create_upload_demo_file_widget()
        self.stacked_widget_state_machine.addWidget(self.upload_demo_file_widget)
        self.open_recent_demo_file_widget = self.__create_open_recent_demo_file_widget()
        self.stacked_widget_state_machine.addWidget(self.open_recent_demo_file_widget)

        # Add widgets to layouts
        self.layout().addWidget(Header())
        self.layout().addWidget(panelContainer)
        panelLayout.addWidget(self.button_panel)
        panelLayout.addWidget(self.main_panel)

    def __create_upload_demo_file_widget(self) -> QWidget:
        '''Creates and returns the Upload Demo File Widget'''
        upload_demo_file_widget = ContentPanel("Upload New CS2 '.demo' File")

        self.file_selector = FileSelector()
        upload_demo_file_widget.panel.layout().addWidget(self.file_selector)

        self.match_name = StringField(text='Match Name')
        upload_demo_file_widget.panel.layout().addWidget(self.match_name)

        self.upload_file_button = BottomRightButton(text='Upload File')
        upload_demo_file_widget.panel.layout().addWidget(self.upload_file_button)

        return upload_demo_file_widget

    def __create_open_recent_demo_file_widget(self) -> QWidget:
        '''Creates and returns the Upload Demo File Widget'''
        open_recent_demo_file_widget = ContentPanel("Open Recent CS2 '.demo' File")

        return open_recent_demo_file_widget

    def get_file_path_from_selector(self):
        return self.file_selector.line_edit.text()