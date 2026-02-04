from .create_card import create_filters_card
from .get_filters import get_filters
from .delete_filters import delete_filter
from PyQt5.QtWidgets import QMessageBox, QPushButton    
from functools import partial

def add_filter(searchbar, layout, empty_state_widget):
    filters = get_filters(searchbar)

    if not filters:
        QMessageBox.warning(None, 'error', 'An Empty Bar can not be a Filter\nTry again')
        return

    if empty_state_widget:
        empty_state_widget.hide()

    
    for text in filters:
        card = create_filters_card(text)
        delete_button = card.findChild(QPushButton)
        if delete_button:
            delete_button.clicked.connect(partial(delete_filter, card, layout, empty_state_widget))

        layout.addWidget(card)
    
    searchbar.clear()