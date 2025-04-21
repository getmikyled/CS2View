from PyQt5.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

from styles import CS2ViewStyles


class TitleBar(QWidget):

    on_minimize_window_button_clicked = pyqtSignal()
    on_close_window_button_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__offset = QPoint()

        # Set title bar styles
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(CS2ViewStyles.TITLE_BAR_HEIGHT)
        self.setStyleSheet(f"background-color: {CS2ViewStyles.PRIMARY_COLOR};")

        # Create title bar layout
        titleBarLayout = QHBoxLayout()
        self.setLayout(titleBarLayout)
        titleBarLayout.setContentsMargins(0, 0, 0, 0)
        titleBarLayout.setSpacing(0)
        titleBarLayout.padding = 0

        # Title label
        titleLabel = QLabel(f'<b><span style="color: {CS2ViewStyles.ACCENT_COLOR_1};">CS2</span>'
                            f'<span style="color: {CS2ViewStyles.ACCENT_COLOR_2};"> View</span></b>')
        titleLabel.setStyleSheet('padding-left: 8px')
        titleLabel.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        #titleLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer.setStyleSheet(f'background-color: {CS2ViewStyles.PRIMARY_COLOR};')

        # Minimize Window Button
        minimizeWindowButton = QPushButton()
        minimizeWindowButton.setIcon(QIcon('icons/minimize_window_icon.png'))
        minimizeWindowButton.setStyleSheet(f'background: {CS2ViewStyles.PRIMARY_COLOR}')
        minimizeWindowButton.setFixedSize(40, 40)
        minimizeWindowButton.clicked.connect(self.on_minimize_window_button_clicked.emit)

        # Close Window Button
        closeWindowButton = QPushButton()
        closeWindowButton.setIcon(QIcon('icons/close_window_icon.png'))
        closeWindowButton.setStyleSheet(f'background: {CS2ViewStyles.PRIMARY_COLOR}')
        closeWindowButton.setFixedSize(40, 40)
        closeWindowButton.clicked.connect(self.on_close_window_button_clicked.emit)


        # Add all widgets to title bar
        titleBarLayout.addWidget(titleLabel)
        titleBarLayout.addWidget(spacer)
        titleBarLayout.addWidget(minimizeWindowButton)
        titleBarLayout.addWidget(closeWindowButton)

    def mousePressEvent(self, event):
        """Fired when the left mouse button is pressed. Offset gets set to the event position."""
        if event.button() == Qt.LeftButton:
            self.__offset = event.pos()

    def mouseMoveEvent(self, event):
        """Fired when the mouse moves. Move the window if left-click on the title bar is held using the offset."""
        if event.buttons() == Qt.LeftButton:
            self.window().move(event.globalPos() - self.__offset)
