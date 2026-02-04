def style_filter_card():
    return """
        QWidget{
        background-color:#21eb72;
        border-radius: 5px;
        border: 1px solid #061c0f;
        }
        QLabel{
            font-size: 25px;
            font-family: Calibri;
            color: #13291c;
            border:none;
        }QPushButton{
            font-size:20px;
            padding:5px;
            border-radius:10px;
            border:none;
            background-color:#ff0000;
            color: white;
        }QPushButton:hover {
            color: red;
            background-color: white;
        }
    """