from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication,
                              QPushButton, QLabel, QFrame, QTabWidget, QLineEdit,
                              QCheckBox, QVBoxLayout, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QIcon
import sys


class Job_seeker_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self._create_widgets()
        self._initUI()
        self._set_layouts()

        
    def _create_widgets(self):
        #global thing
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        #main page widgets
        self.main_page = QWidget()#главній єкра с поиском и тд
        self.search_bar = QLineEdit()
        self.add_filter_button = QPushButton()
        self.delete_filter_button = QPushButton()
        self.filters_area = QScrollArea()
        self.search_job_button = QPushButton()
        self.work_ua_box = QCheckBox()
        self.robota_ua_box = QCheckBox()
        self.founded_jobs_area = QScrollArea()

        #saved jobs list widgets
        self.save_list_page = QWidget()#страница со списком сохраненіїх раьбот
        self.job_list_area = QScrollArea()

    def _initUI(self):

        #appearance of window

        self.setWindowTitle('Job Seeker')
        self.setWindowIcon(QIcon('images/programist.png'))

    def _set_layouts(self):
        pass
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    job_seeker = Job_seeker_app()
    job_seeker.show()
    sys.exit(app.exec_())