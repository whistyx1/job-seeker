from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                              QPushButton, QLabel, QFrame, QTabWidget, QLineEdit,
                              QCheckBox, QVBoxLayout, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt, QSize
import sys
from gui.main_page_styles import style_add_filter_button


class Job_seeker_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self._create_widgets()
        self._set_layouts()
        self._set_tabs()
        self._set_name_to_widgets()
        self._initUI()
        self._apply_styles()

        
    def _create_widgets(self):
        #global thing
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        #main page widgets
        self.main_page = QWidget()#главній єкра с поиском и тд
        self.search_bar = QLineEdit()
        self.add_filter_button = QPushButton()
        self.filters_area = QScrollArea()
        self.search_job_button = QPushButton()
        self.work_ua_box = QCheckBox()
        self.robota_ua_box = QCheckBox()
        self.founded_jobs_area = QScrollArea()

        #saved jobs list widgets
        self.save_list_page = QWidget()#страница со списком сохраненіїх раьбот
        self.job_list_area = QScrollArea()

    def _set_tabs(self):
        self.tabs.addTab(self.main_page, 'Main/Seeker')
        self.tabs.addTab(self.save_list_page, 'Saved Jobs List')

    def _initUI(self):

        #appearance of window

        self.setWindowTitle('Job Seeker')
        self.setWindowIcon(QIcon('images/programist.png'))

        #add text to widgets
        self.search_bar.setPlaceholderText('Type filters here:')

    def _set_layouts(self):
        
        #main page layout

        main_layout = QHBoxLayout()

        #left side/founded jobs

        left_side = QWidget()
        founded_job_lists_layout = QVBoxLayout()
        founded_job_lists_layout.addWidget(self.founded_jobs_area)
        left_side.setLayout(founded_job_lists_layout)

        #right side

        right_side = QWidget()
        search_job_layout = QVBoxLayout()
        search_job_layout.addWidget(self.search_bar)
        search_job_layout.addWidget(self.add_filter_button)
        search_job_layout.addWidget(self.filters_area)
        search_job_layout.addWidget(self.search_job_button)
        search_job_layout.addWidget(self.work_ua_box)
        search_job_layout.addWidget(self.robota_ua_box)
        right_side.setLayout(search_job_layout)

        main_layout.addWidget(left_side)
        main_layout.addWidget(right_side)

        #add layouts to main page

        self.main_page.setLayout(main_layout)

        #Jobs saved list page

        save_list_page_layout = QVBoxLayout()
        save_list_page_layout.addWidget(self.job_list_area)
        self.save_list_page.setLayout(save_list_page_layout)
    
    def _set_name_to_widgets(self):
        self.add_filter_button.setObjectName('add_filter_button')
        self.search_job_button.setObjectName('search_job_button')

    def _apply_styles(self):

        #add_filter_button

        self.add_filter_button.setStyleSheet(style_add_filter_button())
        self.add_filter_button.setCursor(Qt.PointingHandCursor)

        #search_job_button
        self.search_job_button.setCursor(Qt.PointingHandCursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    job_seeker = Job_seeker_app()
    job_seeker.show()
    sys.exit(app.exec_())