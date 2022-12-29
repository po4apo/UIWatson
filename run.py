import subprocess

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtCore
import sys


class MainWindow(QMainWindow): # главное окно
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Watson v.0.0001")
        self.resize(220, 80)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.start_btn = QPushButton('Start project', self)
        self.start_btn.move(10, 10)
        self.stop_btn = QPushButton('Stop project', self)
        self.stop_btn.move(110, 10)
        self.status = QLabel('Status', self)
        self.status.setGeometry(10, 30, 300, 30)
        self.status.setWordWrap(True)
        self.out = QLabel('Out', self)
        self.out.setGeometry(10, 60, 300, 50)
        self.out.setWordWrap(True)
        self.start_btn.clicked.connect(self.start_project)
        self.stop_btn.clicked.connect(self.stop_project)


    def start_project(self):
        out = subprocess.run(['watson', 'start', 'work', '+RE-906'], capture_output=True)
        self.out.setText(f'{str(out.stderr)}\n{str(out.stdout)}')
        self.status.setText("Project started")
        self.status.setStyleSheet("color: green")

    def stop_project(self):
        out = subprocess.run(['watson', 'stop'], capture_output=True)
        self.out.setText(f'{str(out.stderr)}\n{str(out.stdout)}')
        self.status.setText("Project stopped")
        self.status.setStyleSheet("color: red")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())