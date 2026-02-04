from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                              QPushButton, QLabel, QFrame, QTabWidget, QLineEdit,
                              QCheckBox, QVBoxLayout, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt, QSize
import sys
from gui.main_page_styles import (style_add_filter_button, style_search_job_button,
                                   style_searchbar,style_site_label, style_main_page,
                                     style_checkbox, style_sqroll_area)
from gui.sqroll_area_gui import setup_sqroll_area
from filters.add_filters import add_filter
from filters.get_filters import get_filters


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
        self.add_filter_button.clicked.connect(self.enable_add_filter_func)
        self.filters_area = QScrollArea()
        self.filters_area.setWidgetResizable(True)

        self.filter_container = QWidget()
        self.filter_layout = QVBoxLayout()
        self.filter_layout.setAlignment(Qt.AlignTop)

        self.empty_state_filters = setup_sqroll_area()
        self.filter_layout.addWidget(self.empty_state_filters)

        self.filter_container.setLayout(self.filter_layout)
        self.filters_area.setWidget(self.filter_container)

        self.search_job_button = QPushButton()
        self.site_picker_label = QLabel()
        self.work_ua_box = QCheckBox()
        self.robota_ua_box = QCheckBox()

        self.founded_jobs_area = QScrollArea()
        self.founded_jobs_area.setWidgetResizable(True)

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
        self.setMinimumSize(1000, 600)

        #add text to widgets
        self.search_bar.setPlaceholderText('Type filters here(e. g. docker, python, c):')
        self.add_filter_button.setText('Add a Filter')
        self.search_job_button.setText('Find a Job')
        self.site_picker_label.setText('Pick a website to search:')

        #setup checkboxes

        self.work_ua_box.setText('Work.ua')
        self.robota_ua_box.setText('Robota.ua')

        #set icons to checkboxes

        self.work_ua_box.setIcon(QIcon('images/work_ua_logo.png'))
        self.work_ua_box.setIconSize(QSize(30, 60))
        self.robota_ua_box.setIcon(QIcon('images/robota_ua_logo.png'))
        self.robota_ua_box.setIconSize(QSize(30, 60))

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
        search_job_layout.addWidget(self.site_picker_label)
        search_job_layout.addWidget(self.work_ua_box)
        search_job_layout.addWidget(self.robota_ua_box)
        search_job_layout.addWidget(self.search_job_button)
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

        #main page
        self.tabs.setStyleSheet(style_main_page())

        #add_filter_button

        self.add_filter_button.setStyleSheet(style_add_filter_button())
        self.add_filter_button.setCursor(Qt.PointingHandCursor)

        #search_job_button

        self.search_job_button.setStyleSheet(style_search_job_button())
        self.search_job_button.setCursor(Qt.PointingHandCursor)

        #searchbar

        self.search_bar.setStyleSheet(style_searchbar())
        self.search_bar.setCursor(Qt.IBeamCursor)

        #label
        self.site_picker_label.setStyleSheet(style_site_label())

        #checkboxes

        self.work_ua_box.setStyleSheet(style_checkbox())
        self.robota_ua_box.setStyleSheet(style_checkbox())

        self.work_ua_box.setCursor(Qt.PointingHandCursor)
        self.robota_ua_box.setCursor(Qt.PointingHandCursor)

        #sqrollaareas

        self.filters_area.setStyleSheet(style_sqroll_area())
        self.founded_jobs_area.setStyleSheet(style_sqroll_area())
        self.job_list_area.setStyleSheet(style_sqroll_area())

    def enable_add_filter_func(self):
        add_filter(self.search_bar, self.filter_layout, self.empty_state_filters)
    
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    job_seeker = Job_seeker_app()
    job_seeker.show()
    sys.exit(app.exec_())