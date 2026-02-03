def get_filters(widget):

    text = widget.text().strip()

    if not text:
        return []
    
    if ',' in text:
        filters = text.split(',')
    else:
        filters = text.split()
    
    return [f.strip() for f in filters if f.strip()]