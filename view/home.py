from PyQt5.QtWidgets import *

class Home(QWidget):

    def __init__(self):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_container = self.create_main_container()
        self.main_layout.addWidget(self.main_container)

    def create_main_container(self) -> QWidget:
        # Main Container Widget
        mainContainer = QWidget()
        mainContainer.setStyleSheet("background-color: #3C3C3C;")

        mainLayout = QVBoxLayout(mainContainer)

        return mainContainer
