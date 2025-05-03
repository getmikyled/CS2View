from PyQt5.QtWidgets import QPushButton, QTableWidgetItem

from styles import CS2ViewStyles
from .sub_controller import SubController
from PyQt5.QtCore import Qt

class HomeController(SubController):

    def __init__(self, model, view, parent_controller, widget_state=None):
        super().__init__(model, view, parent_controller, widget_state)

        # Upload demo file button callback
        self.view.upload_demo_file_widget_button.clicked.connect(
            lambda: self.set_widget(self.view.upload_demo_file_widget)
        )

        # Open recent demo file button callback
        self.view.open_recent_demo_file_widget_button.clicked.connect(
            self.on_open_recent_demo_file_widget_button_clicked
        )

        # On upload file button clicked
        self.view.upload_file_button.button.clicked.connect(
            lambda: self.parent_controller.upload_new_demo_file(self.parent_controller.home_view.file_selector.line_edit.text())
        )

        self.view.open_recent_file_table_panel.table.cellClicked.connect(self.on_recent_file_cell_clicked)

        self.refresh_recent_files()

        '''
        Removed since menu button was removed
        # On view entered
        self.widget_state.on_entered_signal.connect(
            # Set menu button in tool bar to not visible
            lambda: self.parent_controller.window.toolbar.menu_button.setVisible(False)
        )

        # On view exited
        self.widget_state.on_exited_signal.connect(
            # Set menu button in tool bar to visible
            lambda: self.parent_controller.window.toolbar.menu_button.setVisible(True)
        )
        '''

    def set_widget(self, widget):
        self.view.substack.set_widget(widget)

    def on_open_recent_demo_file_widget_button_clicked(self):
        self.set_widget(self.view.open_recent_file_widget)
        self.refresh_recent_files()

    def on_recent_file_cell_clicked(self, row, column):
        item = self.view.open_recent_file_table_panel.table.item(row, column)
        self.parent_controller.set_demo_file(self.parent_controller.get_demo_data(item.text()))

    def refresh_recent_files(self):

        # Clear table
        self.view.open_recent_file_table_panel.table.clear()
        self.view.open_recent_file_table_panel.table.setRowCount(len(self.model.parsed_demos))

        self.view.open_recent_file_table_panel.table.setColumnCount(1)
        self.view.open_recent_file_table_panel.table.setHorizontalHeaderLabels(['File Name'])

        for row in range(self.view.open_recent_file_table_panel.table.rowCount()):
            self.view.open_recent_file_table_panel.table.setRowHeight(row, 49)

        for column in range(self.view.open_recent_file_table_panel.table.columnCount()):
            self.view.open_recent_file_table_panel.table.setColumnWidth(column, 600)

        for i in range(len(self.model.parsed_demos)):
            parsed_demo = self.model.parsed_demos[list(self.model.parsed_demos.keys())[i]]

            item = QTableWidgetItem(parsed_demo.name)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

            self.view.open_recent_file_table_panel.table.setItem(i, 0, item)