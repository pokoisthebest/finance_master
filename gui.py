from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt6 import uic
from PyQt6.QtGui import QFont
import sys
import plots
import historical_data as hd

# start_date = "2022-01-28"
# end_date = "2023-03-17"
wig20 = hd.get_file_list()
wig20 = [filename.replace('.csv','') for filename in wig20]


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/main_window1.ui', self)
        self.wig20_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.return_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.company_windows = {}  # Store references to CompanyWindow instances
        if self.stackedWidget.currentIndex() == 1:
            self.createButtons(wig20)  

    def createButtons(self, lista):
        buttons = [QPushButton(f"{item}") for item in lista]
        # Align buttons
        self.vbox.addStretch()
        self.vbox_r.addStretch()
        for index, button in enumerate(buttons):
            company = lista[index]
            if index % 2 == 0:
                self.vbox.addWidget(button)
            else:
                self.vbox_r.addWidget(button)
            button.clicked.connect(lambda checked, company=company: self.show_company(company))
        # Align buttons
        self.vbox.addStretch()
        self.vbox_r.addStretch()

    def show_company(self, company_name):
        if company_name not in self.company_windows:
            self.company_windows[company_name] = plots.PlotlyViewer(company_name)
        self.company_windows[company_name].show()

app = QApplication(sys.argv)
app.setFont(QFont("Modern", 20))
window = MainScreen()
window.setFixedHeight(900)
window.setFixedWidth(1440)
app.setStyleSheet("""
QWidget{
    background-color: #0D1B2A;
    color: #E0E1DD;
}
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
