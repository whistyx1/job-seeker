from .create_card import create_filters_card
from .get_filters import get_filters
from .delete_filters import delete_filter
from PyQt5.QtWidgets import QMessageBox, QPushButton    

def add_filter(searchbar, layout):
    filters = get_filters(searchbar)

    if not filters:
        QMessageBox.warning(None, title='error', text='An Empty Bar can not be a Filter\nTry again')
        return
    else:
        for text in filters:
            card = create_filters_card(text)

            delete_button = card.findChild(QPushButton)
            delete_button.clicked.connect(lambda checked: delete_filter(card, layout))

            layout.addWidget(card)
    
    searchbar.clear()