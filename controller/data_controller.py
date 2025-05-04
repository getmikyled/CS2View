from .sub_controller import SubController
from model.parsed_demo import ParsedDemo
from PyQt5.QtWidgets import QTableWidgetItem
import polars as pl

class DataController(SubController):

    def __init__(self, model, view, parent_controller, widget_state):
        super().__init__(model, view, parent_controller, widget_state)
        demo = None
        self.current_table = ''
        self.current_player = None
        self.current_side = None

        # Set up table
        self.view.table_panel.table.setRowCount(10)
        self.view.table_panel.table.setColumnCount(5)
        self.view.table_panel.table.setHorizontalHeaderLabels(['Player', 'Kills', 'Assists', 'Suicides', 'Trades'])

        for row in range(self.view.table_panel.table.rowCount()):
            self.view.table_panel.table.setRowHeight(row, 49)

        for column in range(self.view.table_panel.table.columnCount()):
            self.view.table_panel.table.setColumnWidth(column, 152)

        # To clear tabl
        # self.view.table_panel.table.clear()
    def load_demo(self, parsed_demo, player_name=None, side=None):
        self.fill_table(parsed_demo.get_adr, player_name=player_name, side=side, table_key='adr')
        
        self.parsed_demo = parsed_demo
        self.current_table = 'adr'
        self.current_player = None
        self.current_side = None
        
        self.view.clear_player_buttons()
        
        player_list = parsed_demo.get_all_players(single_list=True)
        self.view.add_player_buttons(
            player_list,
            self.on_all_players_button_clicked,
            self.on_terrorists_button_clicked,
            self.on_counter_terrorists_button_clicked,
            self.on_player_button_clicked
        )
        
        print(self.current_table)
        
    def load_adr(self, parsed_demo, player_name=None, side=None):
        self.fill_table(parsed_demo.get_adr, player_name=player_name, side=side, table_key='adr')
        
    def load_kast(self, parsed_demo, player_name=None, side=None):
        self.fill_table(parsed_demo.get_kast, player_name=player_name, side=side, table_key='kast')
        
    def load_rating(self, parsed_demo, player_name=None, side=None):
        self.fill_table(parsed_demo.get_rating, player_name=player_name, side=side, table_key='rating')
        
    def load_rounds(self, parsed_demo):
        tbl = self.view.table_panel.table
        tbl.clearContents()
        
        data = parsed_demo.get_round_stats()
        
                # Set rows/cols/headers
        n_rows, n_cols = data.shape
        tbl.setRowCount(n_rows)
        tbl.setColumnCount(n_cols)
        tbl.setHorizontalHeaderLabels(data.columns)
        self.adjust_table()

        # Fill cells
        for i, row in enumerate(data.rows()):
            for j, val in enumerate(row):
                tbl.setItem(i, j, QTableWidgetItem(str(val)))

        self.current_table = 'rounds'
        
        
    def fill_table(self, func, *, player_name=None, side=None, table_key=None):
        '''
        Fills the table with data from the given function, filters by player name and side if provided
        '''
        parsed_demo = func.__self__

        # Clear only the cell contents, not the entire widget/layout
        tbl = self.view.table_panel.table
        tbl.clearContents()

        data = func(player_name=player_name, side=side)

        # Set rows/cols/headers
        n_rows, n_cols = data.shape
        tbl.setRowCount(n_rows)
        tbl.setColumnCount(n_cols)
        tbl.setHorizontalHeaderLabels(data.columns)
        self.adjust_table()

        # Fill cells
        for i, row in enumerate(data.rows()):
            for j, val in enumerate(row):
                tbl.setItem(i, j, QTableWidgetItem(str(val)))

        self.current_table = table_key
    
    def adjust_table(self):
        # Adjust table size so its readable
        for row in range(self.view.table_panel.table.rowCount()):
            self.view.table_panel.table.setRowHeight(row, 30)

        for column in range(self.view.table_panel.table.columnCount()):
            self.view.table_panel.table.setColumnWidth(column, 152)

    def on_terrorists_button_clicked(self):
        if self.current_side == 't':
            self.current_side = None
        else:
            self.current_side = 't'
        self.refresh_current_view()

    def on_counter_terrorists_button_clicked(self):
        if self.current_side == 'ct':
            self.current_side = None
        else:     
            self.current_side = 'ct'
        self.refresh_current_view()

    def on_all_players_button_clicked(self):
        self.current_player = None
        self.refresh_current_view()

    def on_adr_stats_button_clicked(self):
        pass
    
    def on_kast_stats_button_clicked(self):
        pass
    
    def on_rating_stats_button_clicked(self):
        pass
    
    def on_round_stats_button_clicked(self):
        pass

    def on_player_button_clicked(self, player):
        if self.current_player == player:
            self.current_player = None
        else:
            self.current_player = player    
        self.refresh_current_view()
            
    def refresh_current_view(self):
        pd = self.parsed_demo
        kwargs = {
            'player_name': self.current_player,
            'side':        self.current_side,
        }
        if self.current_table == 'adr':
            self.load_adr(pd, **kwargs)
        elif self.current_table == 'kast':
            self.load_kast(pd, **kwargs)
        elif self.current_table == 'rating':
            self.load_rating(pd, **kwargs)
        elif self.current_table == 'rounds':
            self.load_rounds(pd)   # no filtering needed for rounds
