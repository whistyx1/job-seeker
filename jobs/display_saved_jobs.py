from .create_saved_job_card import create_saved_job_card

def display_saved_jobs(saved_jobs_list, layout, remove_callback):
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.deleteLater()
        
    for job in saved_jobs_list:
        card = create_saved_job_card(job, remove_callback)
        layout.addWidget(card)
    

        