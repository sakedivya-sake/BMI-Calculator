from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from bmiFE import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)

    def calculate(self):
        w = float(self.ui.lineEdit_2.text())
        h = float(self.ui.lineEdit.text())*0.3048
        bmi = w/(h**2)
        self.ui.lineEdit_3.setText(f"{bmi:.2f}")

        if bmi<18.5:
            status = "Underweight"
        elif 18.5<=bmi<25:
            status = "Normal Weight"
        elif 25<=bmi<30:
            status = "Pre Obesity"
        elif 30<=bmi<35:
            status = "Obesity Class 1"
        elif 35<=bmi<40:
            status = "Obesity Class 2"
        elif bmi>=40:
            status = "Obesity Class 3"
        self.ui.lineEdit_4.setText(status)

    def reset(self):
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def exit(self):
        sys.exit()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

