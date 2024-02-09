from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QMainWindow, QPushButton
from PyQt6 import uic
from PyQt6.QtGui import QFont
import sys


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/main_window1.ui', self)
        self.wig20_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.return_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

def make_gui():
    app = QApplication(sys.argv)
    app.setFont(QFont("Modern", 20)) 
    window = MainScreen()  
    window.setFixedHeight(900)
    window.setFixedWidth(1440)
    app.setStyleSheet("""
    QPushButton{
                    color: black;
                    background-color: grey;
    }
    """)
    window.show()

    try:
        sys.exit(app.exec())
    except:
        print('exiting')

