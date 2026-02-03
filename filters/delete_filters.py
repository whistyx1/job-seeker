def delete_filter(card, layout):
    layout.removeWidget(card)
    card.deleteLater()