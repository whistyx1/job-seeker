#styles to add filter button

def style_add_filter_button():
    return """QPushButton#add_filter_button{
        font-size: 35px;
        font-family: Calibri;
        background-color:hsl(131, 96%, 44%);
        color: white;
        border-radius: 15px;
        padding:5ps;
        border: none;
        }

        QPushButton#add_filter_button:hover{
            color: hsl(131, 96%, 44%);
            background-color: white;
        }
        QPushButton#add_filter_button:pressed {
            background-color: hsl(131, 100%, 27%);
            color:white;
        }
        """

#styles to search job button

def style_search_job_button():
    return """QPushButton#search_job_button{
        font-size: 35px;
        font-family: Calibri;
        background-color:hsl(4, 72%, 53%);
        color: white;
        border-radius: 15px;
        padding:5px;
        border: none;
        }
        QPushButton#search_job_button:hover{
            color: hsl(0, 70%, 63%);
            background-color: white;
        }
        QPushButton#search_job_button:pressed {
            background-color: hsl(0, 75%, 31%);
            color:white;
        }

    """

#styles to searchbar

def style_searchbar():
    return """QLineEdit{
        font-size: 20px;
        padding: 5px;
        background-color: hsl(204, 87%, 25%);
        color: hsl(204, 100%, 93%);
        border: none;
        border-radius: 5px;
    }
    """

#styles to label

def style_site_label():
    return """QLabel{
        font-size:25px;
        font-family: Calibri;
        font-weight: bold;
        color: hsl(203, 100%, 94%)

    }
    """

#style_main_page

def style_main_page():
    return """QTabWidget::pane{
        border: none;
        background-color: hsl(204, 73%, 56%)
    }
    QTabBar::tab{
        min-width: 120px;
        border-top-left-radius: 5px;
         border-top-right-radius: 5px;
        background-color: #053e63;
        color: white;
        font-size: 15px;
        font-family: Calibri;
        font-weight: bold;
        margin-right: 5px;
        margin-left: 5px;
        padding: 5px;
        
    }
    QTabBar::tab:selected {
        background-color: hsl(204, 68%, 81%);
        color: hsl(204, 83%, 7%)
    }
    QTabBar::tab:hover {
            background-color: hsl(204, 53%, 23%);
            color: white
            cursor: pointer;
        }
    """

#style to checkboxes

def style_checkbox():
    return """QCheckBox{
        font-size:25px;
        font-family: Calibri;
        font-weight: bold;
        color: hsl(203, 87%, 6%);
    }
    QCheckBox::indicator {
        width: 20px;
        height: 20px;
        border-radius: 5px;
        border: 2px solid white;
        background-color: hsl(261, 98%, 13%);
        }
    QCheckBox::indicator:checked {
        background-color: hsl(113, 100%, 50%);  
        border: 2px solid hsl(57, 90%, 49%);
        }
    """

#areas

def style_sqroll_area():
    return """QScrollArea{
        background-color: hsl(204, 73%, 56%);
        border: 1px solid hsl(252, 87%, 9%);
        border-radius: 5px;
    }
    """
