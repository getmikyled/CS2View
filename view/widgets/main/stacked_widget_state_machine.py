from PyQt5.QtWidgets import QStackedWidget, QSizePolicy
from PyQt5.QtCore import pyqtSignal, QObject


class StackedWidgetStateMachine(QStackedWidget):

    stacked_widget_states = dict()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def addWidget(self, widget):
        super().addWidget(widget)

        # Create widget state and add it to dictionary
        widgetState = StackedWidgetState(widget)
        self.stacked_widget_states[widget] = widgetState

        return widgetState

    def set_widget(self, newWidget):
        prevWidget = self.currentWidget()
        self.setCurrentWidget(newWidget)

        # Exit current widget
        self.stacked_widget_states[prevWidget].on_exited_signal.emit()

        # Enter new widget
        self.stacked_widget_states[newWidget].on_entered_signal.emit()

class StackedWidgetState(QObject):

    on_entered_signal = pyqtSignal()
    on_exited_signal = pyqtSignal()

    def __init__(self, widget):
        super().__init__()

        self.widget = widget