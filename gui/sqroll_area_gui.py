from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def setup_sqroll_area():

    container = QWidget()
    layout = QVBoxLayout()

    empty_label = QLabel()
    empty_label.setPixmap(QPixmap('/images/empty_cloud.jpg').scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    empty_label.setAlignment(Qt.AlignCenter)

    empty_text = QLabel()
    empty_text.setText('Its empty now\nAdd filters and search a Job!')
    empty_text.setStyleSheet("""
        QLabel{
            font-size: 20px;
            color: #8ff1f2;
            font-family: Calibri;
            font-style: italic;
        }
        """)
    
    layout.addWidget(empty_label)
    layout.addWidget(empty_text)
    layout.setAlignment(Qt.AlignCenter)

    container.setLayout(layout)

    return container