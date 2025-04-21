from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPalette, QColor, QPixmap
from styles import CS2ViewStyles

class SlidingMenu(QWidget):

    SLIDE_DURATION = 500
    is_visible = False

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName('MenuContainer')
        self.setAutoFillBackground(True)

        # Set background
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(CS2ViewStyles.PRIMARY_COLOR))
        self.setPalette(palette)

        # Set initial properties
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(CS2ViewStyles.MENU_WIDTH, CS2ViewStyles.MENU_HEIGHT)

        # Set up layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        # Set up buttons
        self.home_button = self.__create_primary_button('Home', 'icons/home_icon.png')
        layout.addWidget(self.home_button)
        self.database_button = self.__create_primary_button('Stats', 'icons/stats_icon.png')
        layout.addWidget(self.database_button)


    def __create_primary_button(self, text, icon_path):
        ''''''
        # Create the button and layout
        button = QPushButton()
        button.setObjectName('PrimaryButton')
        button.setStyleSheet(CS2ViewStyles.MENU_STYLES)
        button.setFixedHeight(CS2ViewStyles.PRIMARY_BUTTON_HEIGHT)
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        button.setLayout(layout)

        # Add the icon to the layout
        iconLabel = QLabel()
        iconLabel.setPixmap(QPixmap(icon_path).scaled(25, 25, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(iconLabel)

        # Add the text to the layout
        textLabel = QLabel(text)
        textLabel.setObjectName('ButtonLabel')
        textLabel.setAlignment(Qt.AlignLeft)
        layout.addWidget(textLabel)

        return button

    def __create_secondary_button(self, text):
        button = QPushButton(text)

        return button

    def trigger_slide_animation(self):
        '''Slide the menu in or out depending on current status'''
        if not self.is_visible:
            self.__play_slide_in_animation()
        else:
            self.__play_slide_out_animation()

        self.is_visible = not self.is_visible

    def __play_slide_in_animation(self):
        '''Play the slide in animation on the sliding menu'''
        self.anim = QPropertyAnimation(self, b'geometry')
        self.anim.setDuration(self.SLIDE_DURATION)
        self.anim.setStartValue(CS2ViewStyles.MENU_OUT_POSITION)
        self.anim.setEndValue(CS2ViewStyles.MENU_IN_POSITION)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
        self.anim.DeleteWhenStopped = True
        pass

    def __play_slide_out_animation(self):
        '''Play the slide in animation on the sliding menu'''
        self.anim = QPropertyAnimation(self, b'geometry')
        self.anim.setDuration(self.SLIDE_DURATION)
        self.anim.setStartValue(CS2ViewStyles.MENU_IN_POSITION)
        self.anim.setEndValue(CS2ViewStyles.MENU_OUT_POSITION)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
        self.anim.DeleteWhenStopped = True
        pass