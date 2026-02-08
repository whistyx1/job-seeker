import json
from parsing.robota_ua_model import Job
from pathlib import Path

file_path = Path('saved_jobs.json')

def save_jobs_into_file(jobs_list):
    data = []
    for job in jobs_list:
        data.append({
            'title': job.title,
            'company': job.company,
            'url': job.url,
            'data_added': job.data_added,
            'city': job.city,
            'salary':  job.salary,
        })
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f'Creating file error: {e}')

def get_jobs_from_file():
    if not file_path.exists():
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data =json.load(file)
        
        jobs_list = []
        for i in data:
            job = Job(
                title=i.get('title', ''),
                company=i.get('company', ''),
                url=i.get('url', ''),
                data_added=i.get('data_added', ''),
                city=i.get('city', ''),
                salary=i.get('salary', ''),
                )
            jobs_list.append(job)
        return jobs_list

    except Exception as e :
        print(f'Loading file error: {e}')
        return []