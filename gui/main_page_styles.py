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
        padding:5ps;
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
    }
    """

