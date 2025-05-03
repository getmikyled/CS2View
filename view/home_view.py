from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *

from .view import View
from .widgets.main import Header, StackedWidgetStateMachine
from .widgets.panels import ButtonPanel, Panel, ContentPanel
from .widgets.input import FileSelector, BottomRightButton

class HomeView(View):

    def __init__(self):
        super().__init__()

        # Create panel container
        panelContainer = QWidget()
        panelLayout = QHBoxLayout()
        panelContainer.setLayout(panelLayout)

        # Create Button panel
        self.button_panel = ButtonPanel()
        self.upload_demo_file_widget_button = self.button_panel.create_button("Upload New CS2 '.dem' File")
        self.open_recent_demo_file_widget_button = self.button_panel.create_button("Open Recent '.dem' File")

        # Create main panel
        self.main_panel = Panel()

        # Create stacked widget
        self.substack = StackedWidgetStateMachine()
        self.main_panel.layout().addWidget(self.substack)

        # Populate stacked widget
        self.empty_widget = QWidget()
        self.substack.addWidget(self.empty_widget)

        self.upload_demo_file_widget = self.__create_upload_demo_file_widget()
        self.substack.addWidget(self.upload_demo_file_widget)

        self.open_recent_file_widget = self.__create_open_recent_demo_file_widget()
        self.substack.addWidget(self.open_recent_file_widget)

        # Add widgets to layouts
        self.layout().addWidget(Header())
        self.layout().addWidget(panelContainer)
        panelLayout.addWidget(self.button_panel)
        panelLayout.addWidget(self.main_panel)

    def __create_upload_demo_file_widget(self) -> QWidget:
        '''Creates and returns the Upload Demo File Widget'''
        upload_demo_file_widget = ContentPanel("Upload New CS2 '.dem' File")

        self.file_selector = FileSelector(fileFilter="Demo Files (*.dem);;All Files (*)")
        upload_demo_file_widget.panel.layout().addWidget(self.file_selector)

        self.upload_file_button = BottomRightButton(text='Upload File')
        upload_demo_file_widget.panel.layout().addWidget(self.upload_file_button)

        return upload_demo_file_widget

    def __create_open_recent_demo_file_widget(self) -> QWidget:
        '''Creates and returns the Upload Demo File Widget'''
        open_recent_demo_file_widget = ContentPanel("Open Recent CS2 '.dem' File")

        return open_recent_demo_file_widget