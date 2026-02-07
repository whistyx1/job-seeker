from .create_card import create_filters_card
from .get_filters import get_filters
from .delete_filters import delete_filter
from PyQt5.QtWidgets import QMessageBox, QPushButton    
from functools import partial

def add_filter(searchbar, layout, empty_state_widget, active_filters_list):
    filters = get_filters(searchbar)

    if not filters:
        QMessageBox.warning(None, 'error', 'An Empty Bar can not be a Filter\nTry again')
        return

    if empty_state_widget:
        empty_state_widget.hide()
    
    for filter_text in filters:
        if filter_text in active_filters_list:
            continue

        active_filters_list.append(filter_text)

    
        card = create_filters_card(filter_text)
        delete_button = card.findChild(QPushButton)
        if delete_button:
            delete_button.clicked.connect(partial(delete_filter, card, layout, empty_state_widget, active_filters_list, filter_text))

        layout.addWidget(card)
    
    searchbar.clear()