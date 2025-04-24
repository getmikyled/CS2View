from .sub_controller import SubController

class DataController(SubController):

    def __init__(self, model, view, parent_controller, widget_state):
        super().__init__(model, view, parent_controller, widget_state)

        self.view.add_player_buttons(['bruh', 'no', 'dude'], self.on_all_players_button_clicked, self.on_player_button_clicked)

        # Set up table
        self.view.table_panel.table.setRowCount(10)
        self.view.table_panel.table.setColumnCount(5)
        self.view.table_panel.table.setHorizontalHeaderLabels(['Player', 'Kills', 'Assists', 'Suicides', 'Trades'])

        for row in range(self.view.table_panel.table.rowCount()):
            self.view.table_panel.table.setRowHeight(row, 49)

        for column in range(self.view.table_panel.table.columnCount()):
            self.view.table_panel.table.setColumnWidth(column, 152)

        # To clear table
        # self.view.table_panel.table.clear()

    def on_all_players_button_clicked(self):
        print('on_all_players_button_clicked')

    def on_player_button_clicked(self, player):
        print(f'on_player_button_clicked - {player}')