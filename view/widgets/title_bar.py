from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QPoint

class TitleBar(QWidget):

    on_minimize_window_button_clicked = pyqtSignal()
    on_close_window_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.offset = QPoint()

        # Set title bar properties
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: #272727;")

        # Create title bar layout
        titleBarLayout = QHBoxLayout()
        self.setLayout(titleBarLayout)
        titleBarLayout.setContentsMargins(0, 0, 0, 0)
        titleBarLayout.setSpacing(0)
        titleBarLayout.padding = 0

        # Title label
        titleLabel = QLabel('<b><span style="color: #FF9946;">CS2</span>'
                            '<span style="color: #4CACFF;"> View</span></b>')
        titleLabel.setStyleSheet('padding-left: 8px')
        titleLabel.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        #titleLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer.setStyleSheet("background-color: #272727;")  # Match parent or desired color

        # Minimize Window Button
        minimizeWindowButton = QPushButton()
        minimizeWindowButton.setIcon(QIcon('icons/minimize_window_icon.png'))
        minimizeWindowButton.setStyleSheet('background: #272727')
        minimizeWindowButton.setFixedSize(40, 40)
        minimizeWindowButton.clicked.connect(self.on_minimize_window_button_clicked.emit)

        # Close Window Button
        closeWindowButton = QPushButton()
        closeWindowButton.setIcon(QIcon('icons/close_window_icon.png'))
        closeWindowButton.setStyleSheet('background: #272727')
        closeWindowButton.setFixedSize(40, 40)
        closeWindowButton.clicked.connect(self.on_close_window_button_clicked.emit)


        # Add all widgets to title bar
        titleBarLayout.addWidget(titleLabel)
        titleBarLayout.addWidget(spacer)
        titleBarLayout.addWidget(minimizeWindowButton)
        titleBarLayout.addWidget(closeWindowButton)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.window().move(event.globalPos() - self.offset)
