def delete_card(job, saved_jobs_list):
    if job in saved_jobs_list:
        saved_jobs_list.remove(job)
        return True
    
    return False