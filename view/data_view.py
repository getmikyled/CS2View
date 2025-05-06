from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from .view import View
from .widgets.panels import ButtonPanel, TablePanel, ContentPanel
from .widgets.main import Shelf

class DataView(View):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Create shelf and shelf items toc hange between data sets
        self.data_shelf = Shelf()
        self.layout().addWidget(self.data_shelf)
        self.adr_stats_shelf_item = self.data_shelf.add_shelf_item(
            'ADR Stats',
            QIcon('icons/adr_icon.png'),
            'ADR Stats',
        )
        self.kast_stats_shelf_item = self.data_shelf.add_shelf_item(
            'KAST Stats',
            QIcon('icons/kast_icon.png'),
            'KAST Stats - Kills, Assists, Survives, Trades'
        )
        self.rating_stats_shelf_item = self.data_shelf.add_shelf_item(
            'Rating Stats',
            QIcon('icons/rating_icon.png'),
            'Rating Stats'
        )
        self.round_stats_shelf_item = self.data_shelf.add_shelf_item(
            'Round Stats',
            QIcon('icons/round_icon.png'),
            'Round Stats'
        )

        panel_container = QWidget(self)
        self.layout().addWidget(panel_container)
        panel_container.setLayout(QHBoxLayout())

        self.player_button_panel = ButtonPanel(width=200, expanding=False)
        panel_container.layout().addWidget(self.player_button_panel)

        self.content_panel = ContentPanel('Bruh')
        panel_container.layout().addWidget(self.content_panel)
        self.table_panel = TablePanel()
        self.content_panel.panel.layout().addWidget(self.table_panel)

    def add_player_buttons(self, players, all_players_func, t_func, ct_func, player_func):
        """Populates the player button panel with all the players"""
        # First add view all players button
        self.player_button_panel.create_button('All Players', all_players_func)
        self.player_button_panel.create_button('Terrorists', t_func)
        self.player_button_panel.create_button('Counter-Terrorists', ct_func)
        spacer = QWidget(self)
        spacer.setFixedHeight(10)
        self.player_button_panel.layout().addWidget(spacer)

        # Then add all players
        for player in players:
            self.player_button_panel.create_button(player, lambda checked=False, p=player: player_func(p))

    def clear_player_buttons(self):
        """
        Remove every button from the player_button_panel by clearing its layout.
        """
        layout = self.player_button_panel.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
