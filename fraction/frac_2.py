# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frac_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 228)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.input_second_number = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_second_number.setFont(font)
        self.input_second_number.setObjectName("input_second_number")
        self.gridLayout.addWidget(self.input_second_number, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.ravno = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ravno.setFont(font)
        self.ravno.setObjectName("ravno")
        self.gridLayout.addWidget(self.ravno, 0, 1, 3, 1, QtCore.Qt.AlignHCenter)
        self.input_number = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_number.setFont(font)
        self.input_number.setObjectName("input_number")
        self.gridLayout.addWidget(self.input_number, 0, 2, 3, 1, QtCore.Qt.AlignHCenter)
        self.input_first_number = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_first_number.setFont(font)
        self.input_first_number.setObjectName("input_first_number")
        self.gridLayout.addWidget(self.input_first_number, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.first_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.first_number.setFont(font)
        self.first_number.setObjectName("first_number")
        self.gridLayout.addWidget(self.first_number, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.second_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.second_number.setFont(font)
        self.second_number.setObjectName("second_number")
        self.gridLayout.addWidget(self.second_number, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.continue_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.continue_2.setFont(font)
        self.continue_2.setObjectName("continue_2")
        self.gridLayout_2.addWidget(self.continue_2, 2, 0, 1, 1)
        self.check = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.gridLayout_2.addWidget(self.check, 1, 0, 1, 1)
        self.otvet = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.otvet.setFont(font)
        self.otvet.setText("")
        self.otvet.setObjectName("otvet")
        self.gridLayout_2.addWidget(self.otvet, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ravno.setText(_translate("Form", "="))
        self.first_number.setText(_translate("Form", "1"))
        self.second_number.setText(_translate("Form", "3"))
        self.continue_2.setText(_translate("Form", "Продолжить дальше"))
        self.check.setText(_translate("Form", "Проверить"))
        self.otvet.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
