from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QLayout
import sys


class Job_seeker_app(QMainWindow):
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    job_seeker = Job_seeker_app()
    job_seeker.show()
    sys.exit(app.exec_())