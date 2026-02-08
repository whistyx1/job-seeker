from PyQt5.QtWidgets import (QLabel, QFrame, QVBoxLayout,
                              QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt
import webbrowser
from .delete_card import delete_card

def open_url(url):
    webbrowser.open(url)

def create_saved_job_card(job, remove_callback):
    card = QFrame()
    card.setObjectName('job-card')

    main_layout = QVBoxLayout()

    # Layout for date and title
    top_layout = QHBoxLayout()

    title = QLabel(job.title)
    title.setObjectName('job-title')
    title.setWordWrap(True)
    title.setStyleSheet("""
        QLabel#job-title {
            font-size: 15px;
            color: #36060e; 
            font-weight: bold; 
            border: none;         
        }
    """)
    top_layout.addWidget(title)

    if job.data_added:
        date = QLabel(f'Added {job.data_added}')
        date.setObjectName("job-date-added")
        date.setStyleSheet("""
            QLabel#job-date-added {
                border: none; 
                font-size: 12px;
                color: #999;
                font-style: italic;
            }
        """)
        top_layout.addWidget(date, alignment=Qt.AlignRight | Qt.AlignTop)
    
    main_layout.addLayout(top_layout)

    # Company + city
    info = QLabel(f"🏢 {job.company} • 📍 {job.city}")
    info.setObjectName("job-info")
    info.setStyleSheet("""
        QLabel#job-info {
            font-size: 14px;
            color: #5A5A5A;
            margin-top: 5px;
            border: none; 
        }
    """)
    main_layout.addWidget(info)

    # Salary
    if job.salary:
        salary = QLabel(f"💰 {job.salary}")
        salary.setObjectName("job-salary")
        salary.setStyleSheet("""
            QLabel#job-salary {
                font-size: 14px;
                color: #5FB8A3;
                font-weight: bold;
                margin-top: 5px;
                border: none; 
            }
        """)
        main_layout.addWidget(salary)

    # Buttons
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
            font-size: 14px;
        }
        QPushButton#open-button:hover {
            background-color: #7DD3C0;
        }
    """)
    open_button.clicked.connect(lambda: open_url(job.url))

    delete_button = QPushButton('Delete')
    delete_button.setObjectName("delete-button")
    delete_button.setMinimumWidth(80)
    delete_button.setCursor(Qt.PointingHandCursor)
    delete_button.setStyleSheet("""
        QPushButton#delete-button{
            background-color: #ff0015;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 15px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton#delete-button:hover{
            background-color: #9e0814;
        }
    """)
    delete_button.clicked.connect(lambda: remove_callback(job))
    
    buttons_layout.addWidget(open_button)
    buttons_layout.addWidget(delete_button)
    buttons_layout.addStretch()

    main_layout.addLayout(buttons_layout)

    card.setLayout(main_layout)

    card.setStyleSheet("""
        QFrame#job-card {
            background-color: #f7faff;
            border: 2px solid #5FB8A3;
            border-radius: 12px;
            padding: 15px;
            margin: 5px;
        }
        QFrame#job-card:hover {
            border: 2px solid #7DD3C0;
            background-color: #F0F9F7;
        }
    """)

    card.mousePressEvent = lambda event: open_url(job.url)
    card.setCursor(Qt.PointingHandCursor)
    
    return card