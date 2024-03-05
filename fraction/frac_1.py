from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 400)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fourth_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fourth_number.setFont(font)
        self.fourth_number.setText("")
        self.fourth_number.setObjectName("fourth_number")
        self.gridLayout.addWidget(self.fourth_number, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.input_second_number = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_second_number.setFont(font)
        self.input_second_number.setObjectName("input_second_number")
        self.gridLayout.addWidget(self.input_second_number, 2, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.input_first_number = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.input_first_number.setFont(font)
        self.input_first_number.setObjectName("input_first_number")
        self.gridLayout.addWidget(self.input_first_number, 0, 4, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.check = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check.setFont(font)
        self.check.setObjectName("check")
        self.gridLayout.addWidget(self.check, 3, 0, 1, 5)
        self.continue_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.continue_2.setFont(font)
        self.continue_2.setObjectName("continue_2")
        self.gridLayout.addWidget(self.continue_2, 4, 0, 1, 5)
        self.second_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.second_number.setFont(font)
        self.second_number.setText("")
        self.second_number.setObjectName("second_number")
        self.gridLayout.addWidget(self.second_number, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ravno = QtWidgets.QLabel(Form)
        self.ravno.setObjectName("ravno")
        self.gridLayout.addWidget(self.ravno, 1, 3, 1, 1)
        self.sign = QtWidgets.QLabel(Form)
        self.sign.setObjectName("sign")
        self.gridLayout.addWidget(self.sign, 1, 1, 1, 1)
        self.first_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.first_number.setFont(font)
        self.first_number.setText("")
        self.first_number.setObjectName("first_number")
        self.gridLayout.addWidget(self.first_number, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.firth_number = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.firth_number.setFont(font)
        self.firth_number.setText("")
        self.firth_number.setObjectName("firth_number")
        self.gridLayout.addWidget(self.firth_number, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.skip = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.skip.setFont(font)
        self.skip.setObjectName("skip")
        self.gridLayout.addWidget(self.skip, 5, 0, 1, 5)
        self.otvet = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.otvet.setFont(font)
        self.otvet.setText("")
        self.otvet.setObjectName("otvet")
        self.gridLayout.addWidget(self.otvet, 6, 0, 1, 5, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fourth_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.input_second_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.input_first_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.check.setText(_translate("Form", "Проверить"))
        self.continue_2.setText(_translate("Form", "Продолжить дальше"))
        self.second_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.ravno.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">=</span></p></body></html>"))
        self.sign.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">-</span></p></body></html>"))
        self.first_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.firth_number.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.skip.setText(_translate("Form", "Пропустить задание"))
        self.otvet.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
