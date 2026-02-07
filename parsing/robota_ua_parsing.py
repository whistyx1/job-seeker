from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from .robota_ua_model import Job

class RobotaUaParser(QThread):
    jobs_found = pyqtSignal(list)
    progress = pyqtSignal(int, int)
    error = pyqtSignal(str)
    
    def __init__(self, filters, region, max_pages=10):
        super().__init__()
        self.filters = filters
        self.region = region
        self.max_pages = max_pages
    
    def run(self):
        try:
            jobs = self._parse()
            self.jobs_found.emit(jobs)
        except Exception as e:
            self.error.emit(str(e))
    
    def _parse(self):
        jobs_list = []
        seen_links = set()

        total = len(self.filters) * self.max_pages
        current = 0
        
        for filter_word in self.filters:
            for page in range(1, self.max_pages + 1):
                url=f'https://robota.ua/zapros/{filter_word}/{self.region}/params;page={page}'
                print(f'Parsing: {url}')
                try:
                    res = requests.get(url, timeout=10)
                    print(res.text[:1000]) 
                    res.raise_for_status()
                except requests.RequestException as e:
                    print(f"Error fetching {url}: {e}")
                    current += 1
                    self.progress.emit(current, total)
                    continue
                
                soup = BeautifulSoup(res.text, 'lxml')
                jobs = soup.find_all('a', class_='santa--mb-20 ng-star-inserted')

                print(f"Found {len(jobs)} jobs on page {page}")

                for job in jobs:
                    #title
                    title_tag = job.find('h2', class_='santa-typo-h3')
                    if not title_tag:
                        continue
                    title = title_tag.get_text(strip=True)

                    #company

                    company_tag = job.find('span', class_='santa-mr-20')
                    company = company_tag.get_text(strip=True) if company_tag else ''

                    #url

                    url_tag = job.get('href', '')
                    if not url_tag:
                        continue
                    job_url = url_tag.get('href', '')
                    if job_url and not job_url.startswith('http'):
                        job_url = 'https://robota.ua' + job_url
                    
                    #data

                    data_tag = job.find('h2', class_='santa-typo-secondary')
                    data_added = data_tag.get_text(strip=True) if data_tag else ''


                    #city+salary

                    spans = job.find_all('span', class_='ng-tns-c104-140 ng-trigger')

                    salary = ''
                    city = ''

                    for span in spans:
                        text = span.get_text(strip=True)
    
                        if '₴' in text or '$' in text or '—' in text:
                            salary = text
                        else:
                            city = text

                    if job_url in seen_links:
                        continue

                    seen_links.add(job_url)

                    job_obj = Job(
                        title=title,
                        company=company,
                        url=job_url,
                        city=city,
                        data_added=data_added,
                        salary=salary
                    )
                    
                    jobs_list.append(job_obj)
                current += 1
                self.progress.emit(current, total)
        
        return jobs_list
