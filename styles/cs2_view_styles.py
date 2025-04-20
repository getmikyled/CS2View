from PyQt5.QtCore import QRect


class CS2ViewStyles:

    # Window Size
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720

    # Colors
    PRIMARY_COLOR = '#272727'
    SECONDARY_COLOR = '#3C3C3C'
    HIGHLIGHT_COLOR = '#4B6262'

    # Text Colors
    FONT_COLOR = '#FFFFFF'
    ACCENT_COLOR_1 = '#FF9946'
    ACCENT_COLOR_2 = '#4CACFF'

    STACK_STYLES = f'''
        #Stack {{
            background-color: {PRIMARY_COLOR};
        }}
    '''

    # TITLE BAR
    TITLE_BAR_HEIGHT = 40

    HEADER_STYLES = f'''
    
        #HeaderLabel {{
            font-size: 50px;
        }}
        
        #DescriptionLabel {{
            color: {FONT_COLOR};
            font-size: 18px;
        }}
    '''

    TOOLBAR_HEIGHT = 25
    TOOLBAR_MENU_BUTTON_SIZE = TOOLBAR_HEIGHT
    TOOLBAR_STYLES = f'''
    
        #ToolbarMenu {{
            background-color: {PRIMARY_COLOR};
            color: {FONT_COLOR};
        }}
        
        #MenuButton {{
            margin: 0px 0px 0px 0px;
            background-color: {PRIMARY_COLOR};
        }}
        
        #ToolbarButton {{
                color: {FONT_COLOR};
                background-color: {PRIMARY_COLOR};    
                font-size: 18px;
        }}
            
        #ToolbarButton::menu-indicator {{
            image: none;
            width: 0px;
        }}
    '''

    BUTTON_PANEL_HEIGHT = '50px'

    BUTTON_PANEL_STYLES = f'''
    
        #ButtonPanelButton {{ 
            color: {FONT_COLOR};
            background-color: {SECONDARY_COLOR};
            height: {BUTTON_PANEL_HEIGHT};
            text-align: left;
            padding: 0px 0px 0px 10px;
        }}
            
        #ButtonPanelButton:hover, #ButtonPanelButton:disabled {{
            color: {FONT_COLOR};
            background-color: {HIGHLIGHT_COLOR};
            height: {BUTTON_PANEL_HEIGHT};
        }}
    '''

    MENU_WIDTH = 200;
    MENU_HEIGHT = 680;
    MENU_OUT_POSITION = QRect(-MENU_WIDTH, TITLE_BAR_HEIGHT + TOOLBAR_HEIGHT, MENU_WIDTH, WINDOW_HEIGHT - TITLE_BAR_HEIGHT - TOOLBAR_HEIGHT)
    MENU_IN_POSITION = QRect(0, TITLE_BAR_HEIGHT + TOOLBAR_HEIGHT, MENU_WIDTH, WINDOW_HEIGHT - TITLE_BAR_HEIGHT - TOOLBAR_HEIGHT)

    MENU_STYLES = f'''
        
        #PrimaryButton {{
            background-color: {PRIMARY_COLOR};
        }}
        
        #ButtonLabel {{
            color: {FONT_COLOR};
        }}
    '''

    PRIMARY_BUTTON_HEIGHT = 50

    CONTENT_PANEL_STYLES = f'''

        #TitleLabel {{
            color: {FONT_COLOR}
        }}
    '''

    FIELD_HEIGHT = 40
    FIELD_STYLES = f'''
    
        QLabel {{
            color: {FONT_COLOR};
            padding: 0 0 10px 0;
            margin: 0;
        }}
        
        QLineEdit {{
            background-color: {PRIMARY_COLOR};
            color: {FONT_COLOR};
            border: none;
            font-size: 18px;
            padding: 0 0 0px 0;
            margin: 0;
        }}
        
        QPushButton {{
            padding: 0px;
            margin: 0px;
            background-color: {PRIMARY_COLOR};
            color: {FONT_COLOR};
            padding: 0 0 0px 0;
            margin: 0;
        }}
        
        QPushButton::hover {{
            background-color: {HIGHLIGHT_COLOR};
        }}
    '''