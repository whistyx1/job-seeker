from PyQt5.QtWidgets import QMessageBox
from .display_saved_jobs import display_saved_jobs

def save_job_card(job, job_list):
    if job.url in [j.url for j in job_list]:
        QMessageBox.warning(
            'Already exist', 
            'You have already saved this job'
        )
        return
    
    job_list.append(job)

    return True