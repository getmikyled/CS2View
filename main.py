import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from cs2_view_window import CS2ViewWindow


def main():
    app = QApplication(sys.argv)
    window = CS2ViewWindow()
    window.show()

    sys.exit(app.exec())

main()
    