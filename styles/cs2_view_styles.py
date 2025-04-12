
class CS2ViewStyles:

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

    HEADER_STYLES = f'''
    
        #HeaderLabel {{
            font-size: 50px;
        }}
        
        #DescriptionLabel {{
            color: {FONT_COLOR};
            font-size: 18px;
        }}
    '''

    TOOLBAR_STYLES = f'''
    
        #ToolbarMenu {{
            background-color: {PRIMARY_COLOR};
            color: {FONT_COLOR};
        }}
        
        #ToolbarButton {{
                color: {FONT_COLOR};
                background-color: {PRIMARY_COLOR};    
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
        }}
            
        #ButtonPanelButton:hover, #ButtonPanelButton:disabled {{
            color: {FONT_COLOR};
            background-color: {HIGHLIGHT_COLOR};
            height: {BUTTON_PANEL_HEIGHT};
        }}
    '''
