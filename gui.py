from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QMainWindow, QPushButton
from PyQt6 import uic
from PyQt6.QtGui import QFont
import sys
start_date = "2022-01-28"
end_date = "2023-03-17"
wig20 = {
        "ASSECOPOL" : "ACP",
        "ALLEGRO" : "ALE",
        "ALIOR" : "ALR",
        "CDPROJEKT" : "CDR",
        "CYFRPLSAT" : "CPS",
        "DINOPL" : "DNP",
        "JSW" : "JSW.WA",
        "KGHM" : "KGH",
        "KRUK" : "KRU",
        "KETY" : "KTY",
        "LPP" : "LPP",
        "MBANK" : "MBK",
        "ORANGEPL" : "OPL",
        "PEPCO" : "PCO",
        "PEKAO" : "PEO",
        "PGE" : "PGE",
        "PKNORLEN" : "PKN",
        "PKOBP" : "PKO",
        "PZU" : "PZU",
        "SANPL" : "SPL"
    }

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/main_window1.ui', self)
        self.wig20_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.return_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        if self.stackedWidget.currentIndex() == 1:

            self.createButtons(wig20.keys())

    def createButtons(self, lista):
        buttons = [i for i in range(len(lista))]
        # Align buttons
        self.vbox.addStretch()
        self.vbox_r.addStretch()
        for index, item in enumerate(lista):
            buttons[index] = QPushButton(f"{item}")
            if index%2 == 0:
                self.vbox.addWidget(buttons[index])
            else:
                self.vbox_r.addWidget(buttons[index])
        # Align buttons 
        self.vbox.addStretch()
        self.vbox_r.addStretch()

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

make_gui()