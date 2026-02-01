
def style_add_filter_button():
    return """QPushButton#add_filter_button{
        font-size: 15px;
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
        }
        """