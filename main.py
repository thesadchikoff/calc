from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(450, 740)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.insert = QtWidgets.QLabel(self.centralwidget)
        self.insert.setGeometry(QtCore.QRect(0, 0, 500, 60))
        self.insert.setMinimumSize(QtCore.QSize(500, 60))
        self.insert.setMaximumSize(QtCore.QSize(500, 60))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.insert.setFont(font)
        self.insert.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255)")
        self.insert.setObjectName("insert")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(20, 570, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ravno.setGeometry(QtCore.QRect(170, 570, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ravno.setFont(font)
        self.btn_ravno.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 208, 64);")
        self.btn_ravno.setObjectName("btn_ravno")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(320, 570, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(133, 255, 141);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(20, 440, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(20, 310, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_4.setObjectName("btn_4")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(20, 180, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(170, 180, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(320, 180, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_3.setObjectName("btn_3")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(320, 310, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(320, 440, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(170, 440, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(170, 310, 110, 110))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(209, 207, 255);\n"
"")
        self.btn_5.setObjectName("btn_5")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(10, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(255, 208, 64);\n"
"border-radius: 20px;")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(120, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 208, 64);\n"
"border-radius: 20px;")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_umnojit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnojit.setGeometry(QtCore.QRect(230, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_umnojit.setFont(font)
        self.btn_umnojit.setStyleSheet("background-color: rgb(255, 208, 64);\n"
"border-radius: 20px;\n"
"")
        self.btn_umnojit.setObjectName("btn_umnojit")
        self.btn_delenie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delenie.setGeometry(QtCore.QRect(340, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delenie.setFont(font)
        self.btn_delenie.setStyleSheet("background-color: rgb(255, 208, 64);\n"
"border-radius: 20px;")
        self.btn_delenie.setObjectName("btn_delenie")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        
        self.add_functions()


        self.is_equal = False


        

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Калькулятор"))
        self.insert.setText(_translate("mainWindow", "0"))
        self.btn_zero.setText(_translate("mainWindow", "0"))
        self.btn_ravno.setText(_translate("mainWindow", "="))
        self.btn_clear.setText(_translate("mainWindow", "C"))
        self.btn_7.setText(_translate("mainWindow", "7"))
        self.btn_4.setText(_translate("mainWindow", "4"))
        self.btn_1.setText(_translate("mainWindow", "1"))
        self.btn_2.setText(_translate("mainWindow", "2"))
        self.btn_3.setText(_translate("mainWindow", "3"))
        self.btn_6.setText(_translate("mainWindow", "6"))
        self.btn_9.setText(_translate("mainWindow", "9"))
        self.btn_8.setText(_translate("mainWindow", "8"))
        self.btn_5.setText(_translate("mainWindow", "5"))
        self.btn_plus.setText(_translate("mainWindow", "+"))
        self.btn_minus.setText(_translate("mainWindow", "-"))
        self.btn_umnojit.setText(_translate("mainWindow", "*"))
        self.btn_delenie.setText(_translate("mainWindow", "/"))


    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_delenie.clicked.connect(lambda: self.write_number(self.btn_delenie.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_umnojit.clicked.connect(lambda: self.write_number(self.btn_umnojit.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))

        self.btn_ravno.clicked.connect(self.results)


    def write_number(self, number):
        if self.insert.text() == '0' or self.is_equal:
            self.insert.setText(number)
            self.is_equal = False
        else:
            self.insert.setText(self.insert.text() + number)


    def results(self):
        if not self.is_equal:
            res = eval(self.insert.text())
            self.insert.setText("Результат: " + str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset|QMessageBox.Ok|QMessageBox.Cancel)

            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Повторно выполнить данное действие невозможно")
            error.setDetailedText("Ошибка вычисления.\nНеобходимо указать числа до конечного вычисления")

            error.buttonClicked.connect(self.popup_action)
            error.exec_()


    def popup_action(self, btn):
        if btn.text() == "Ok":
            self.is_equal = False
            print("Ok")
        elif btn.text() == "Reset":
            self.insert.setText("")
            self.is_equal = False
        elif btn.text() == "Cancel":
            self.insert.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())