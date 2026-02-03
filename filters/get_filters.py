def get_filters(widget):
    filters_list = []

    text = widget.text()

    if text:
        filters_list.append(text)

    return filters_list