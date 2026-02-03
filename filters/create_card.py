from .get_filters import get_filters
from PyQt5.QtWidgets import QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from .delete_filters import delete_filter
from gui.style_filter_card import style_filter_card

def create_filters_card(text: str):
    card = QWidget()
    layout = QHBoxLayout()

    text_label = QLabel()
    text_label.setText(text)

    delete_button = QPushButton()
    delete_button.setText('Delete')
    delete_button.setCursor(Qt.PointingHandCursor)

    layout.addWidget(text_label)
    layout.addWidget(delete_button)

    #styles
    card.setStyleSheet(style_filter_card())

    card.setLayout(layout)
    return card