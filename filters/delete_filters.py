def delete_filter(card, layout, empty_state_widget):
    layout.removeWidget(card)
    card.hide()
    card.deleteLater()

    has_cards = False
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget and widget != empty_state_widget and widget.isVisible():
            has_cards = True
            break

    if not has_cards:
        if empty_state_widget:
            empty_state_widget.show()