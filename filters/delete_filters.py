def delete_filter(card, layout, empty_state_widget):
    layout.removeWidget(card)
    card.deleteLater()

    if layout.count() == 0:
        empty_state_widget.show()