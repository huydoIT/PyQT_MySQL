# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import getdata as cnt

class Form_MainWindow(object):
    def __init__(self, id):
        db = cnt.get_by_id(id)
        self.id = id
        self.b = db[0]
        self.n = db[1]
        print("Full name: %s || Balance = %s" % (db[1], db[0]))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbName = QtWidgets.QLabel(self.groupBox)
        self.lbName.setGeometry(QtCore.QRect(190, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbName.setFont(font)
        self.lbName.setObjectName("lbName")
        self.lbBal = QtWidgets.QLabel(self.groupBox)
        self.lbBal.setGeometry(QtCore.QRect(190, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.lbBal.setFont(font)
        self.lbBal.setObjectName("lbBal")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 451, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btInp = QtWidgets.QPushButton(self.groupBox_2)
        self.btInp.setGeometry(QtCore.QRect(90, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btInp.setFont(font)
        self.btInp.setObjectName("btInp")
        
        self.btInp.clicked.connect(self.btInp_click)
        
        self.btOut = QtWidgets.QPushButton(self.groupBox_2)
        self.btOut.setGeometry(QtCore.QRect(250, 20, 101, 41))
        
        self.btOut.clicked.connect(self.btOut_click)
       
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btOut.setFont(font)
        self.btOut.setObjectName("btOut")
        self.txtMoney = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMoney.setGeometry(QtCore.QRect(110, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtMoney.setFont(font)
        self.txtMoney.setObjectName("txtMoney")
        self.lbRs = QtWidgets.QLabel(self.groupBox_2)
        self.lbRs.setGeometry(QtCore.QRect(90, 140, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbRs.setFont(font)
        self.lbRs.setText("")
        self.lbRs.setObjectName("lbRs")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(326, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.label.setText(_translate("MainWindow", "Balance:"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.lbName.setText(_translate("MainWindow", self.n))
        self.lbBal.setText(_translate("MainWindow", str(self.b)))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.btInp.setText(_translate("MainWindow", "Input"))
        self.btOut.setText(_translate("MainWindow", "Output"))
        self.label_3.setText(_translate("MainWindow", "円"))
        self.label_4.setText(_translate("MainWindow", "Money"))

    def btInp_click(self):
        value = str(self.txtMoney.text())
        if value.isdigit():
            rs = int(value) + int(self.lbBal.text())
            if cnt.update_data((rs, self.id, )) == 0:
                print("Update success!")
                dt = cnt.get_by_id(self.id)   
                self.lbBal.setText(str(dt[0]))
                self.txtMoney.setText("")
            else:
                print("Update failed!")
        else:
            print("Input not accept.")
    
    def btOut_click(self):
        value = str(self.txtMoney.text())
        if value.isdigit():
            rs = int(value)*(-1) + int(self.lbBal.text())
            if cnt.update_data((rs, self.id, )) == 0:
                print("Update success!")
                dt = cnt.get_by_id(self.id)   
                self.lbBal.setText(str(dt[0]))
                self.txtMoney.setText("")
            else:
                print("Update failed!")
        else:
            print("Input not accept.")    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Form_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

