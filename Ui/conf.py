# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\configuracion.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_primera_vez(object):
    def setupUi(self, primera_vez):
        primera_vez.setObjectName("primera_vez")
        primera_vez.resize(360, 190)
        primera_vez.setMinimumSize(QtCore.QSize(360, 190))
        primera_vez.setMaximumSize(QtCore.QSize(360, 190))
        self.Inf = QtWidgets.QPlainTextEdit(primera_vez)
        self.Inf.setGeometry(QtCore.QRect(9, 9, 342, 69))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Inf.setFont(font)
        self.Inf.setAutoFillBackground(False)
        self.Inf.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.Inf.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Inf.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Inf.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Inf.setReadOnly(True)
        self.Inf.setObjectName("Inf")
        self.msje_error = QtWidgets.QLabel(primera_vez)
        self.msje_error.setGeometry(QtCore.QRect(9, 70, 342, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.msje_error.setFont(font)
        self.msje_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.msje_error.setText("")
        self.msje_error.setObjectName("msje_error")
        self.mail_tag = QtWidgets.QLabel(primera_vez)
        self.mail_tag.setGeometry(QtCore.QRect(10, 90, 61, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mail_tag.setFont(font)
        self.mail_tag.setObjectName("mail_tag")
        self.mail = QtWidgets.QLineEdit(primera_vez)
        self.mail.setGeometry(QtCore.QRect(94, 90, 251, 20))
        self.mail.setDragEnabled(False)
        self.mail.setClearButtonEnabled(True)
        self.mail.setObjectName("mail")
        self.pass_tag = QtWidgets.QLabel(primera_vez)
        self.pass_tag.setGeometry(QtCore.QRect(9, 120, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_tag.setFont(font)
        self.pass_tag.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.pass_tag.setObjectName("pass_tag")
        self.password = QtWidgets.QLineEdit(primera_vez)
        self.password.setGeometry(QtCore.QRect(94, 120, 251, 20))
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setDragEnabled(False)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.aceptar = QtWidgets.QPushButton(primera_vez)
        self.aceptar.setGeometry(QtCore.QRect(100, 158, 151, 23))
        self.aceptar.setObjectName("aceptar")

        self.retranslateUi(primera_vez)
        QtCore.QMetaObject.connectSlotsByName(primera_vez)

    def retranslateUi(self, primera_vez):
        _translate = QtCore.QCoreApplication.translate
        primera_vez.setWindowTitle(_translate("primera_vez", "Configuración"))
        self.Inf.setPlainText(_translate("primera_vez", "Hemos notado que esta es tu primera vez utilizando MCMail. Para comenzar por favor ingresa con tu cuenta de Gmail o Hotmail."))
        self.mail_tag.setText(_translate("primera_vez", "E-mail:"))
        self.mail.setPlaceholderText(_translate("primera_vez", "ejemplo@mail.com"))
        self.pass_tag.setText(_translate("primera_vez", "Contraseña:"))
        self.password.setPlaceholderText(_translate("primera_vez", "Contraseña"))
        self.aceptar.setText(_translate("primera_vez", "Aceptar"))
