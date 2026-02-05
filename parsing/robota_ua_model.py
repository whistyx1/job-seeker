from dataclasses import dataclass

@dataclass
class Job:
    title: str
    company: str
    url: str
    data_added: str
    city: str
    salary:  str = ' '