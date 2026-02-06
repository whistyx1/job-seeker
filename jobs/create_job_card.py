from PyQt5.QtWidgets import (QLabel, QFrame, QVBoxLayout,
                              QPushButton, QHBoxLayout,
                             )
from PyQt5.QtCore import Qt
import webbrowser

def open_url(url):
    webbrowser.open(url)

def create_job_card(job):
    card = QFrame()
    card.setObjectName('job-card')

    main_layout = QVBoxLayout()

    #layout for data and title
    top_layout = QHBoxLayout()

    title = QLabel(job.title)
    title.setObjectName('job-title')
    title.setWordWrap(True)
    title.setStyleSheet("""
        QLabel#job-title{
            font-size: 15px;
            color: #36060e;           
        }
    """)
    top_layout.addWidget(title)

    if job.data_added:
        date = QLabel(f'Added {job.data_added}')
        date.setObjectName("job-date-added")
        date.setObjectName("""
            QLabel#job-date-added{
            font-size: 15px;
            color: #36060e;
            font-style: italic;
            }
        """)
        top_layout.addWidget(date)
    
    main_layout.addLayout(top_layout)

    #company + city

    info = QLabel(f" {job.company}  {job.city}")
    info.setObjectName("job-info")
    info.setStyleSheet("""
        QLabel#job-info {
            font-size: 15px;
            color: #36060e;
            margin-top: 5px;
        }
    """)
    main_layout.addWidget(info)

    #salary

    if job.salary:
        salary = QLabel(f"Salary: {job.salary}")
        salary.setObjectName("job-salary")
        salary.setStyleSheet("""
            QLabel#job-salary {
                font-size: 15px;
                color: #36060e;
                font-weight: bold;
                margin-top: 5px;
            }
        """)
        main_layout.addWidget(salary)

    #buttons

    buttons_layout = QHBoxLayout()

    open_button = QPushButton('Open')
    open_button.setObjectName("open-button")
    open_button.setCursor(Qt.PointingHandCursor)
    open_button.setStyleSheet("""
        QPushButton#open-button {
            background-color: #5FB8A3;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 15px;
            font-weight: bold;
        }
        QPushButton#open-button:hover {
            background-color: #7DD3C0;
        }
    """)
    
    open_button.clicked.connect(lambda: open_url(job.url))

    save_button = QPushButton('Save')
    save_button.setObjectName("save-button")
    save_button.setMaximumWidth(40)
    save_button.setCursor(Qt.PointingHandCursor)
    save_button.setStyleSheet("""
        QPushButton#save-button {
            background-color: #FFC107;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px;
            font-size: 16px;
        }
        QPushButton#save-button:hover {
            background-color: #FFD54F;
        }
    """)
    buttons_layout.addWidget(open_button)
    buttons_layout.addWidget(save_button)
    buttons_layout.addStretch()

    main_layout.addLayout(buttons_layout)

    card.setLayout(main_layout)

    card.setStyleSheet("""
        QFrame#jobCard {
            background-color: white;
            border: 2px solid #5FB8A3;
            border-radius: 12px;
            padding: 15px;
            margin: 5px;
        }
        QFrame#jobCard:hover {
            border: 2px solid #7DD3C0;
            background-color: #F0F9F7;
        }
    """)

    return card