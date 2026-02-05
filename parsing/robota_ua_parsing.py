from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from robota_ua_model import Job

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
        
        for filter_word in self.filters:
            for page in range(1, self.max_pages + 1):

                try:
                    res = requests.get(url, timeout=10)
                    res.raise_for_status()  # Викине помилку якщо 404, 500 і т.д.
                except requests.RequestException as e:
                    print(f"Error fetching {url}: {e}")
                    continue
                res = requests.get(url=f'https://robota.ua/zapros/{filter_word}/{self.region}/params;page={page}')
                soup = BeautifulSoup(res.text, 'lxml')
                jobs = soup.find_all('div', class_='santa--mb-20')

                for job in jobs:
                    title = job.find('h2', class_='santa-typo-h3').get_text(strip=True)
                    company = job.find('span', class_='santa-mr-20').get_text(strip=True)
                    url = job.find('a', class_='card').get('href')
                    if url and not url.startswith('http'):
                        url = 'https://robota.ua' + url
                    data_added = job.find('div', class_='santa-typo-secondary').get_text(strip=True)
                    spans = job.find_all('span', class_='ng-tns-c104-140 ng-trigger')

                    salary = ''
                    city = ''

                    for span in spans:
                        text = span.get_text(strip=True)
    
                        if '₴' in text or '$' in text or '—' in text:
                            salary = text
                        else:
                            city = text

                    job_obj = Job(
                        title=title,
                        company=company,
                        url=url,
                        city=city,
                        data_added=data_added,
                        salary=salary
                    )

                    if url not in seen_links:
                        seen_links.add(url)
                        jobs_list.append(job_obj)
        
        return jobs_list
