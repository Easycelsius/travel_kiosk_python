# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QDialog

print("subpage")

class Ui_Dialog(QDialog):
    # def __init__(self):
    #     super(Ui_Dialog, self).__init__()
    #     Dialog = QtWidgets.QDialog()
    #     Dialog.setupUi(Dialog)
    #     Dialog.setStyleSheet(open('style.css').read())
    #     print("6")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 402)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "?????? ?????? ??????"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "?????????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "????????????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "?????????"))
        self.label.setText(_translate("Dialog", "?????? ??????"))
        self.lineEdit_2.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "????????????"))
        self.pushButton_2.setText(_translate("Dialog", "????????????"))
        self.comboBox.setItemText(0, _translate("Dialog", "????????????"))
        self.comboBox.setItemText(1, _translate("Dialog", "??????"))

    def showModel(self):
        print("??????")
        return super().exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setStyleSheet(open('style.css').read())
    Dialog.show()
    sys.exit(app.exec_())