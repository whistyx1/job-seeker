from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                              QPushButton, QLabel, QFrame, QTabWidget, QLineEdit,
                              QCheckBox, QVBoxLayout, QHBoxLayout, QScrollArea, QComboBox, QMessageBox)
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import Qt, QSize
import sys
from gui.main_page_styles import (style_add_filter_button, style_search_job_button,
                                   style_searchbar,style_site_label, style_main_page,
                                     style_checkbox, style_sqroll_area, style_region_label)
from gui.sqroll_area_gui import setup_sqroll_area
from filters.add_filters import add_filter
from filters.get_filters import get_filters
from parsing.robota_ua_parsing import RobotaUaParser
from parsing.work_ua_parsing import WorkUaParser
from jobs.create_job_card import create_job_card
from jobs.save_card import save_job_card
from jobs.delete_card import delete_card
from jobs.display_saved_jobs import display_saved_jobs
from create_jobs_file import get_jobs_from_file,save_jobs_into_file


class Job_seeker_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_filters = []
        self.saved_jobs = get_jobs_from_file()
        self._create_widgets()
        self._set_layouts()
        self._set_tabs()
        self._set_name_to_widgets()
        self._initUI()
        self._apply_styles()
        display_saved_jobs(self.saved_jobs, self.job_list_layout, self.on_delete_clicked)
    
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
        self.filter_container.setStyleSheet("""
            QWidget{
                background-color: transparent;
            }""")

        self.filter_layout = QVBoxLayout()
        self.filter_layout.setAlignment(Qt.AlignTop)

        self.empty_state_filters = setup_sqroll_area()
        self.filter_layout.addWidget(self.empty_state_filters)

        self.filter_container.setLayout(self.filter_layout)
        self.filters_area.setWidget(self.filter_container)

        self.search_job_button = QPushButton()
        self.search_job_button.clicked.connect(self._parse_job)
        self.site_picker_label = QLabel()
        self.work_ua_box = QCheckBox()
        self.robota_ua_box = QCheckBox()

        self.region_label = QLabel()
        self.region_combo = QComboBox()

        self.founded_jobs_area = QScrollArea()
        self.founded_jobs_area.setWidgetResizable(True)

        self.jobs_container = QWidget()
        self.jobs_container.setStyleSheet("""
            QWidget{
                background-color: transparent;
            }""")
        self.jobs_layout = QVBoxLayout()
        self.jobs_layout.setAlignment(Qt.AlignTop)
        self.empty_state_jobs = setup_sqroll_area()
        self.jobs_layout.addWidget(self.empty_state_jobs)

        self.jobs_container.setLayout(self.jobs_layout)
        self.founded_jobs_area.setWidget(self.jobs_container)

        #saved jobs list widgets
        self.save_list_page = QWidget()#страница со списком сохраненіїх раьбот
        self.job_list_area = QScrollArea()
        self.job_list_area.setWidgetResizable(True)
        
        self.job_list_container = QWidget()
        self.job_list_container.setStyleSheet('background-color: transparent;')
        self.job_list_layout = QVBoxLayout()
        self.job_list_layout.setAlignment(Qt.AlignTop)

        self.job_list_container.setLayout(self.job_list_layout)
        self.job_list_area.setWidget(self.job_list_container)

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

        #edit region label + box
        self.region_label.setText('Choose a region:')

        self.region_combo.addItem('Вся Україна', 'ukraine')
        self.region_combo.addItem('Харків', 'kharkiv')
        self.region_combo.addItem('Київ', 'kyiv')
        self.region_combo.addItem('Дніпро', 'dnipro')
        self.region_combo.addItem('Інше', 'other_countries')

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
        search_job_layout.addWidget(self.region_label)
        search_job_layout.addWidget(self.region_combo)
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

        #region label

        self.region_label.setStyleSheet(style_region_label())

    def enable_add_filter_func(self):
        add_filter(self.search_bar, self.filter_layout, self.empty_state_filters, self.active_filters)
    
    def display_jobs(self, jobs):

        for i in reversed(range(self.jobs_layout.count())):
            widget = self.jobs_layout.itemAt(i).widget()
            if widget and widget != self.empty_state_jobs:
                widget.deleteLater()

        if hasattr(self, 'empty_state_jobs'):
            self.empty_state_jobs.hide()
        
        for job in jobs:
            card = create_job_card(job, self.on_saved_clicked)
            self.jobs_layout.addWidget(card)
        
        self.search_job_button.setText('Find a Job')
        self.search_job_button.setEnabled(True)

        QMessageBox.information(self, 'Done!', f'I have found {len(jobs)} jobs')

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', 'Parsing error')

        self.search_job_button.setText('Find a Job')
        self.search_job_button.setEnabled(True)

    def _parse_job(self):
        filters = self.active_filters
        if not filters:
            QMessageBox.warning(None, 'error', 'You must apply some filters\nBefore searching a Job')
            return

        

        work_ua_selected = self.work_ua_box.isChecked()
        robota_ua_selected = self.robota_ua_box.isChecked()

        if not work_ua_selected and not robota_ua_selected:
            QMessageBox.warning(
                self, 
                'error', 
                'Choose at least one website for searching'
            )
            return

        region = self.region_combo.currentData()
        self.parsers = []

        if work_ua_selected:
            
            work_parser = WorkUaParser(
                filters=filters,
                region=region,
                max_pages=10
            )
            work_parser.jobs_found.connect(self.display_jobs)
            work_parser.error.connect(self.show_error)
            
            self.parsers.append(work_parser)
        if robota_ua_selected:
            QMessageBox.information(self, 'In development', 'Robota.ua is Temporarily unavailable\nMy sincere apologies')
            return

        self.search_job_button.setText('Searching...')
        self.search_job_button.setEnabled(False)

        for parser in self.parsers:
            parser.start()  

    def on_saved_clicked(self, job):
        saving = save_job_card(job, self.saved_jobs)

        if saving:
            self.refresh_saved_jobs_page()
            save_jobs_into_file(self.saved_jobs)
            QMessageBox.information(
                self, 
                'Saved!', 
                f'{job.title}" Added to Saved!'
            )
    
    def on_delete_clicked(self, job):
        deleting = delete_card(job, self.saved_jobs)

        if deleting:
            self.refresh_saved_jobs_page()
            save_jobs_into_file(self.saved_jobs)
            QMessageBox.information(
                self, 
                'Deleted', 
                f'{job.title}" Was Deleted from Saved'
            )
    
    def refresh_saved_jobs_page(self):
        display_saved_jobs(self.saved_jobs, self.job_list_layout, self.on_delete_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    job_seeker = Job_seeker_app()
    job_seeker.show()
    sys.exit(app.exec_())