# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonalAssistantUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 526)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblFriday = QtWidgets.QLabel(self.centralwidget)
        self.lblFriday.setGeometry(QtCore.QRect(0, 10, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(13)
        self.lblFriday.setFont(font)
        self.lblFriday.setStyleSheet("color: rgb(255, 0, 0)")
        self.lblFriday.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFriday.setObjectName("lblFriday")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 381, 411))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background:rgb(255, 255, 255)")
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(150, 470, 101, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0)")
        self.btnStart.setObjectName("btnStart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Assistant"))
        self.lblFriday.setText(_translate("MainWindow", "F.R.I.D.A.Y"))
        self.btnStart.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
