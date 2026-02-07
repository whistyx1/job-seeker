from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from .robota_ua_model import Job

class WorkUaParser(QThread):
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
                if self.region and self.region != 'ukraine':
                    url=f'https://www.work.ua/jobs-{self.region}-{filter_word}/?page={page}'
                else:
                    url = f'https://www.work.ua/jobs-{filter_word}/?page={page}'
                print(f'Parsing: {url}')
                try:
                    res = requests.get(url, timeout=10)
                    res.raise_for_status()
                    res.encoding = 'utf-8'
                except requests.RequestException as e:
                    print(f"Error fetching {url}: {e}")
                    current += 1
                    self.progress.emit(current, total)
                    continue
                
                soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')

                test1 = soup.find_all('div', {'class': 'card'})
                test2 = soup.find_all('div', class_='card card-hover')
                test3 = soup.find_all('div', class_='job-link')

                print(f"Selector test:")
                print(f"  class='card': {len(test1)}")
                print(f"  class='card card-hover': {len(test2)}")  
                print(f"  class='job-link': {len(test3)}")

                print(f"HTML length: {len(res.text)}")
                print(f"Title: {soup.title.string if soup.title else 'No title'}")
                jobs = soup.find_all('div', class_='card')

                print(f"Found {len(jobs)} jobs on page {page}")

                for job in jobs:
                    #title
                    title_tag = job.find('h2', class_='my-0')
                    if not title_tag:
                        continue
                    title_link = title_tag.find('a')
                    if not title_link:
                        continue

                    title = title_link.get_text(strip=True)

                    #url

                    job_url = title_link.get('href', '')
                    if job_url and not job_url.startswith('http'):
                        job_url = 'https://work.ua' + job_url

                    if job_url in seen_links:
                        continue

                    seen_links.add(job_url)
                    
                    #data

                    data_added = ''
                    time_tag = job.find('time')
                    if time_tag:
                        data_added = time_tag.get_text(strip=True)

                    #company+salary 
                    company = ''
                    salary = ''
                    strong_spans = job.find_all('span', class_='strong-600')
                    
                    for span in strong_spans:
                        text = span.get_text(strip=True)
                        if 'грн' in text or '₴' in text or '$' in text:
                            salary = text
                        elif not company:
                            company = text
                    
                    #city

                    city = ''
                    info_div = job.find('div', class_='mt-xs')
                    if info_div:
                        text = info_div.get_text()
                        for city_name in ['Київ', 'Харків', 'Дніпро', 'Одеса', 'Львів']:
                            if city_name in text:
                                city = city_name
                                break

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
